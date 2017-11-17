# -*- coding: utf-8 -*-

# python imports
from __future__ import division
import random
import json
import math

# chillin imports
from chillin_server import TurnbasedGameHandler
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ks.models import World, Banana, PowerUp, ECell, EBananaStatus, EPowerUpType
from ks.commands import Move, Enter, Fire, EFireDir, EMoveDir


# GLOBALS
BOARD_WIDTH = 0
BOARD_HEIGHT = 0


class GameHandler(TurnbasedGameHandler):

  def on_recv_command(self, side_name, agent_name, command_type, command):
    if None in command.__dict__.values():
        print('None in command: %s(%i) %s' % (side_name, command.id, command_type))
        return

    print('command: %s(%i) %s' % (side_name, command.id, command_type))
    if command.id not in self.commands[side_name]:
      self.commands[side_name][command.id] = command


  def on_initialize(self):
    print('initialize')

    # Read map file
    self.map_config = json.loads(open((self.config['map']), "r").read())
    board = self.map_config['board']

    # fill GLOBALS
    global BOARD_WIDTH, BOARD_HEIGHT
    BOARD_WIDTH = len(board[0])
    BOARD_HEIGHT = len(board)

    # Initialize World
    self.world = World()
    self.world.width = BOARD_WIDTH
    self.world.height = BOARD_HEIGHT
    self.world.scores = {side: 0 for side in self.sides}
    self.world.board = [[ECell.Empty for _ in range(self.world.width)] for _ in range(self.world.height)]
    self.world.bananas = {side: [] for side in self.sides}
    self.world.powerups = []
    self.world.enter_score = self.map_config['enter_score']
    self.powerup_emmiters = [] # powerup emitters position
    # Create World board
    for y in range(self.world.height):
      for x in range(self.world.width):
        if board[y][x] == 't': # Tree
          self.world.board[y][x] = ECell.Tree
        elif board[y][x] == 'b': # Box
          self.world.board[y][x] = ECell.Box
        elif board[y][x] == 'p': # PowerUp Emitter
          self.world.board[y][x] = ECell.PowerUpEmitter
          self.powerup_emmiters.append(Pos(x=x, y=y).position)
    # Create Bananas
    for side in self.sides:
      for banana in self.map_config['bananas'][side]:
        new_banana = Banana()
        new_banana.id = len(self.world.bananas[side])
        new_banana.status = EBananaStatus.Alive
        new_banana.position = banana['position']
        new_banana.health = self.map_config['init_health']
        new_banana.max_health = self.map_config['max_health']
        new_banana.laser_count = self.map_config['init_laser_count']
        new_banana.max_laser_count = self.map_config['max_laser_count']
        new_banana.laser_range = self.map_config['init_laser_range']
        new_banana.laser_damage = self.map_config['init_laser_damage']
        new_banana.curr_reload = 0
        new_banana.reload_time = self.map_config['init_reload_time']
        new_banana.death_score = self.map_config['death_score']

        self.world.bananas[side].append(new_banana)

    # Variables
    self.commands = {side: {} for side in self.sides}
    self.lasers_ref = []

    self.scale_factor = self.canvas.width / (self.world.width * self.config['cell_size'])
    self.scale_percent = math.floor(self.scale_factor * 100)
    self.cell_size = math.floor(self.config['cell_size'] * self.scale_factor)

    self.fire_dirs = {
      EFireDir.Up.name:        Pos(x=0, y=-1),
      EFireDir.UpRight.name:   Pos(x=1, y=-1),
      EFireDir.Right.name:     Pos(x=1, y=0),
      EFireDir.RightDown.name: Pos(x=1, y=1),
      EFireDir.Down.name:      Pos(x=0, y=1),
      EFireDir.DownLeft.name:  Pos(x=-1, y=1),
      EFireDir.Left.name:      Pos(x=-1, y=0),
      EFireDir.LeftUp.name:    Pos(x=-1, y=-1)
    }
    self.fire_angle = {
      EFireDir.Up.name:        -90,
      EFireDir.UpRight.name:   -135,
      EFireDir.Right.name:     180,
      EFireDir.RightDown.name: 135,
      EFireDir.Down.name:      90,
      EFireDir.DownLeft.name:  45,
      EFireDir.Left.name:      0,
      EFireDir.LeftUp.name:    -45
    }

    self.move_dirs = {
      EMoveDir.Up.name:        Pos(x=0, y=-1),
      EMoveDir.Right.name:     Pos(x=1, y=0),
      EMoveDir.Down.name:      Pos(x=0, y=1),
      EMoveDir.Left.name:      Pos(x=-1, y=0)
    }
    self.move_angle = {
      EMoveDir.Up.name:        -90,
      EMoveDir.Right.name:     180,
      EMoveDir.Down.name:      90,
      EMoveDir.Left.name:      0
    }


  def on_initialize_gui(self):
    print('initialize gui')

    # Draw background
    background_ref = self.canvas.create_image('Background', 0, 0)
    self.canvas.edit_image(background_ref, scale_type=ScaleType.ScaleX, scale_value=self.world.width * self.scale_percent)
    self.canvas.edit_image(background_ref, scale_type=ScaleType.ScaleY, scale_value=self.world.height * self.scale_percent)

    # Draw Board
    for y in range(self.world.height):
      for x in range(self.world.width):
        cell = self.world.board[y][x]
        if cell == ECell.Tree: # Tree
          self.canvas.create_image('Tree', x * self.cell_size, y * self.cell_size, scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
        elif cell == ECell.Box: # Box
          self.canvas.create_image('Box', x * self.cell_size, y * self.cell_size, scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
        elif cell == ECell.PowerUpEmitter: # PowerUp Emitter
          self.canvas.create_image('PowerUpEmitter', x * self.cell_size, y * self.cell_size, scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)

    # Draw Bananas
    for side in self.sides:
      img_name = side
      for banana in self.world.bananas[side]:
        pos = Pos(position=banana.position)
        canvas_pos = self._get_canvas_position(pos.x, pos.y, center_origin=True)
        banana.img_ref = self.canvas.create_image(img_name, canvas_pos['x'], canvas_pos['y'], center_origin=True, scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)

    # Apply actions
    self.canvas.apply_actions()


  def on_process_cycle(self):
    print('cycle %i' % (self.current_cycle,))

    # init variables
    laser_cells = {side: [] for side in self.sides} # Cells that in emitted lasers in this cycle
    new_positions = {side: {} for side in self.sides}
    enters = {side: [] for side in self.sides}
    new_dirs = {side: {} for side in self.sides}

    # Remove previous lasers
    for laser_ref in self.lasers_ref:
      self.canvas.delete_element(laser_ref)

    # Check reloads
    for side in self.sides:
      for banana in self.world.bananas[side]:
        if banana.status != EBananaStatus.Alive:
          continue

        if banana.curr_reload > 0:
          banana.curr_reload -= 1

          if banana.curr_reload == 0:
            self._change_ammo(banana, 1)

    # Check powerups
    ended_powerups = []
    for powerup in self.world.powerups:
      powerup.apearance_time -= 1

      if powerup.apearance_time == 0:
        ended_powerups.append(powerup)
        self.canvas.delete_element(powerup.img_ref)
    # remove ended powerups
    for powerup in ended_powerups:
      self.world.powerups.remove(powerup)

    # Read Commands
    for side in self.commands:
      for id in self.commands[side]:
        banana = self.world.bananas[side][id]

        # Check is alive
        if self.world.bananas[side][id].status != EBananaStatus.Alive:
          continue

        command = self.commands[side][id]
        if command.name() == Move.name():
          new_position = Pos(position=banana.position) + self.move_dirs[command.dir.name]
          if self.world.board[new_position.y][new_position.x] != ECell.Tree:
            # Check no ones there
            is_empty = True
            for check_side in self.sides:
              for check_banana in self.world.bananas[check_side]:
                if check_banana.status == EBananaStatus.Alive and check_banana.position == new_position.position:
                  is_empty = False
                  break
              if not is_empty:
                break

            if is_empty:
              new_positions[side][id] = new_position.position
              new_dirs[side][id] = command.dir
        elif command.name() == Enter.name():
          pos = Pos(position=banana.position)
          if self.world.board[pos.y][pos.x] == ECell.Box:
            enters[side].append(banana) # Later check is alive after lasers?
        elif command.name() == Fire.name():
          # Check has ammo
          if banana.laser_count == 0:
            continue

          self._change_ammo(banana, -1)

          # Emit laser
          fire_dir = self.fire_dirs[command.dir.name]
          laser_start_pos = Pos(position=banana.position)
          laser_end_pos = Pos(position=banana.position)
          # Go until reach tree or max range
          for _ in range(banana.laser_range):
            laser_end_pos += fire_dir
            if self.world.board[laser_end_pos.y][laser_end_pos.x] == ECell.Tree:
              break
            # else
            laser_cells[side].append((laser_end_pos.position, banana.laser_damage))

            reach_banana = False
            for check_side in self.sides:
              for check_banana in self.world.bananas[check_side]:
                if not self.map_config['friendly_fire'] and side == check_side:
                  break
                if laser_end_pos.position == check_banana.position:
                  reach_banana = True
              if reach_banana:
                break
            if reach_banana:
              break


          # Draw Laser
          laser_center = {
            'x': math.floor(((laser_start_pos.x + laser_end_pos.x) / 2) * self.cell_size + self.cell_size / 2),
            'y': math.floor(((laser_start_pos.y + laser_end_pos.y) / 2) * self.cell_size + self.cell_size / 2)
          }
          laser_length = math.sqrt((((laser_start_pos.x - laser_end_pos.x) * self.cell_size) ** 2) + (((laser_start_pos.y - laser_end_pos.y) * self.cell_size) ** 2))
          laser_ref = self.canvas.create_image('Laser', laser_center['x'], laser_center['y'],
                      center_origin=True, angle=self.fire_angle[command.dir.name],
                      scale_type=ScaleType.ScaleX, scale_value=math.floor(laser_length * 100 / self.config['cell_size']))
          self.lasers_ref.append(laser_ref)
          # Rotate player
          self.canvas.edit_image(banana.img_ref, angle=self.fire_angle[command.dir.name])

    # Dealing Damages
    for side in laser_cells:
      for position_damage in laser_cells[side]:
        position, damage = position_damage
        for b_side in self.sides:
          # Check friendly fire
          if not self.map_config['friendly_fire'] and b_side == side:
            continue

          for banana in self.world.bananas[b_side]:
            if banana.status != EBananaStatus.Alive:
              continue

            if banana.position == position: # Hit
              self._change_health(banana, -damage)
              if banana.status == EBananaStatus.Dead:
                self._update_score(side, banana.death_score)

    # Check new positions
    for side in self.sides:
      for id in new_positions[side]:
        banana = self.world.bananas[side][id]

        if banana.status != EBananaStatus.Alive:
          continue

        can_move = True
        for side2 in self.sides:
          for id2 in new_positions[side2]:
            if side == side2 and id == id2:
              continue

            if new_positions[side][id] == new_positions[side2][id2]:
              can_move = False
              break
          if not can_move:
            break

        if can_move:
          banana.position = new_positions[side][id]
          # Update canvas
          pos = Pos(position=banana.position)
          canvas_pos = self._get_canvas_position(pos.x, pos.y, center_origin=True)
          self.canvas.edit_image(banana.img_ref, canvas_pos['x'], canvas_pos['y'], angle=self.move_angle[new_dirs[side][id].name])

    # Check Enters
    for side in self.sides:
      for banana in enters[side]:
        if banana.status == EBananaStatus.Alive:
          self._update_score(side, self.world.enter_score)
          self._enter(banana)

    # Check end game
    end_game = False
    if self.current_cycle >= self.map_config['max_cycles']:
      end_game = True
    else:
      for side in self.sides:
        for banana in self.world.bananas[side]:
          if banana.status == EBananaStatus.Alive:
            break
        else:
          end_game = True
          break

    if end_game:
      winner = ''
      if self.world.scores['Dole'] > self.world.scores['Chiquita']:
        winner = 'Dole'
      elif self.world.scores['Chiquita'] > self.world.scores['Dole']:
        winner = 'Chiquita'
      self.end_game(winner_sidename=winner, details={
        'Scores': {
          'Dole': str(self.world.scores['Dole']),
          'Chiquita': str(self.world.scores['Chiquita'])
        }
      })

    # Generate Powerups
    if self.current_cycle % self.map_config['powerup_creation_offset'] == 0:
      for position in self.powerup_emmiters:
        if random.uniform(0.0, 1.0) < self.map_config['powerup_emit_chance']:
          new_powerup = PowerUp()
          new_powerup.type = EPowerUpType(random.randint(0, len(EPowerUpType) - 1))
          new_powerup.position = position
          new_powerup.apearance_time = self.map_config['powerup_apearance_time']
          new_powerup.value = 1
          # Draw
          pos = Pos(position=position)
          new_powerup.img_ref = self.canvas.create_image('PowerUp' + new_powerup.type.name, pos.x * self.cell_size, pos.y * self.cell_size, scale_type=ScaleType.ScaleToWidth, scale_value=self.cell_size)
          # Add to world
          self.world.powerups.append(new_powerup)

    # Check for pickup
    picked_powerups = []
    for side in self.sides:
      for banana in self.world.bananas[side]:
        if banana.status != EBananaStatus.Alive:
          continue

        for powerup in self.world.powerups:
          if powerup.position == banana.position:
            if self._pickup_powerup(banana, powerup):
              picked_powerups.append(powerup)
    # remove picked powerups
    for powerup in picked_powerups:
      self.world.powerups.remove(powerup)

    # Reset commands object
    self.commands = {side: {} for side in self.sides}


  def on_update_clients(self):
    print('update clients')
    self.send_snapshot(self.world)


  def on_update_gui(self):
    print('update gui')

    # move bananas to front
    for side in self.sides:
      for banana in self.world.bananas[side]:
        self.canvas.bring_to_front(banana.img_ref)

    # Apply actions
    self.canvas.apply_actions()


  def _get_canvas_position(self, x, y, center_origin=False):
    addition = self.cell_size // 2 if center_origin else 0
    return {
      'x': x * self.cell_size + addition,
      'y': y * self.cell_size + addition
    }


  def _change_ammo(self, banana, ammo):
    banana.laser_count += ammo
    if ammo < 0:
      if banana.curr_reload == 0:
        banana.curr_reload = banana.reload_time

    if banana.laser_count < 0:
      banana.laser_count = 0
    elif banana.laser_count >= banana.max_laser_count:
      banana.laser_count = banana.max_laser_count # fix laser_count > max_laser_count
      banana.curr_reload = 0 # stop reloading


  def _change_health(self, banana, health):
    banana.health += health

    if banana.health <= 0:
      banana.health = 0 # fix health < 0
      banana.status = EBananaStatus.Dead # Update status
      self.canvas.delete_element(banana.img_ref) # Remove banana sprite
    elif banana.health > banana.max_health:
      banana.health = banana.max_health


  def _enter(self, banana):
    banana.status = EBananaStatus.InBox # Update status
    self.canvas.delete_element(banana.img_ref) # Remove banana sprite


  def _update_score(self, side, score):
    self.world.scores[side] += score


  def _pickup_powerup(self, banana, powerup):
    picked = False

    if powerup.type == EPowerUpType.Ammo:
      if banana.laser_count < banana.max_laser_count:
        self._change_ammo(banana, powerup.value)
        picked = True
    elif powerup.type == EPowerUpType.Heal:
      if banana.health < banana.max_health:
        self._change_health(banana, powerup.value)
        picked = True

    if picked:
      self.canvas.delete_element(powerup.img_ref)
      return True
    return False



class Pos(object):
  x = 0
  y = 0
  position = 0


  def __init__(self, x=None, y=None, position=None):
    if position is not None:
      self.position = position
      self._position_to_xy()
    else:
      self.x = x
      self.y = y
      self._xy_to_position()


  def _position_to_xy(self):
    self.x = self.position % BOARD_WIDTH
    self.y = self.position // BOARD_HEIGHT


  def _xy_to_position(self):
    self.position = (self.y * BOARD_WIDTH) + self.x


  def __add__(self, other):
    return Pos(x=self.x + other.x, y=self.y + other.y)
