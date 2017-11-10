# -*- coding: utf-8 -*-

# python imports
import random
from  time import time
import json
# chillin imports

from chillin_server import TurnbasedGameHandler
from chillin_server.gui.canvas_elements import ScaleType,Color

# project imports
from ks.models import World,ECell,EDir,Agent,PowerUp,PowerUpType
from ks.commands import Move, Turn, Fire


class GameHandler(TurnbasedGameHandler):

    def on_recv_command(self, side_name, agent_name, command_type, command):
        print('command: %s %s' % (side_name, command_type ))
        # command can be fire , turn or move
        self.commands[(side_name,command.id)] = ((side_name, command),time())


    def on_initialize(self):
        print('initialize')
        self.sides = self.sides.keys()
        self.world = World()
        self.world.powerups = []
        self.img = []
        self.__deleted_power_ups_img =[]
        self.__deleted_agents_imgs = []
        self.commands = {}
        self.exited_agents = {self.sides[0]: [], self.sides[1]: []}
        self.killed_agents = {self.sides[0]: [], self.sides[1]: []}
        self.world.agents = []
        map_file = open((self.config['map']), "r").read()
        map_json = json.loads(map_file)
        map_rows = map_json['map']
        self.powerup_appearence_time = map_json['apearance_time']
        self.cycle_limitation = map_json['game_cycles_num']
        self.agents_dir_row = map_json['dirs']
        self.world.scores = {self.sides[0]: 0, self.sides[1]: 0}
        self.world.exit_score = json.loads(map_file)['exit_score']
        self.commands = {}

        self.world.board = [[ECell.EMPTY for _ in range(len(map_rows))] for _ in range(len(map_rows))]
        self.cell_size = self.canvas.height / len(self.world.board[0])
        counter = 0
        agent_count = 0
        dirs = {
            'u': EDir.UP,
            'd': EDir.DOWN,
            'r': EDir.RIGHT,
            'l': EDir.LEFT
        }
        for y, row in enumerate(map_rows):
            for x, col in enumerate(row):
                if col == "g":
                    self.world.board[y][x] = ECell.GATE
                elif col == "b":
                    self.world.board[y][x] = ECell.BLOCK

                elif col == "2" or col == "1":
                    a = Agent()
                    self.world.agents.append(a)
                    self.world.agents[agent_count].position = counter
                    if col == "1":
                        self.world.agents[agent_count].side_name = self.sides[1]
                    else:
                        self.world.agents[agent_count].side_name = self.sides[0]
                    self.world.agents[agent_count].id = agent_count
                    self.world.agents[agent_count].laser_count = map_json['laser_count']
                    self.world.agents[agent_count].laser_range = map_json['laser_range']
                    self.world.agents[agent_count].health = map_json['health']
                    self.world.agents[agent_count].max_health = map_json['health']
                    self.world.agents[agent_count].laser_max_count = map_json['laser_max_count']
                    self.world.agents[agent_count].death_score = map_json['death_score']
                    self.world.agents[agent_count].direction = dirs[self.agents_dir_row[agent_count]]
                    agent_count  +=1
                counter += 1
        print "laser range" + self.world.agents[1].laser_count.__str__()

    def on_initialize_gui(self):
        print('initialize gui')
        self.img_coefficent = 0.2
        self.canvas.resize_canvas(self.canvas.width,self.canvas.height)
        background_ref = self.canvas.create_image('Background', 0, 0)
        self.canvas.edit_image(background_ref, scale_type=ScaleType.ScaleX, scale_value=self.canvas.width)
        self.canvas.edit_image(background_ref, scale_type=ScaleType.ScaleY, scale_value=self.canvas.height)
        cell_imgs_dict = {
            ECell.BLOCK:'Block',
            ECell.GATE:'Gate',
            ECell.EMPTY:'Empty'
        }
        self.cell_imgs= [[None for _ in range(len(self.world.board[0]))] for _ in range(len(self.world.board[0]))]
        for y in range(len(self.world.board[0])):
            for x in range(len(self.world.board[0])):
                self.cell_imgs[y][x] = self.canvas.create_image(cell_imgs_dict[self.world.board[y][x]], x=x * self.cell_size +  self.cell_size /2 ,  y=y * self.cell_size  +  self.cell_size / 2,center_origin=True)
                self.canvas.edit_image(self.cell_imgs[y][x], scale_type=ScaleType.ScaleY, scale_value=self.cell_size * self.img_coefficent )
                self.canvas.edit_image(self.cell_imgs[y][x], scale_type=ScaleType.ScaleX, scale_value=self.cell_size * self.img_coefficent )

        for i in range(len(self.world.agents)):
            self.img.append(self.canvas.create_image('Agent_team_'+ self.world.agents[i].side_name.__str__(),
                                                     x=self.cell_size*self._position_to_xy(self.world.agents[i].position)[0] + self.cell_size/ 2,
                                                     y=self.cell_size*self._position_to_xy(self.world.agents[i].position)[1] + self.cell_size/ 2,
                                                     angle=self._convert_to_angle(self.world.agents[i].direction), center_origin=True))
            self.canvas.edit_image(self.img[i], scale_type=ScaleType.ScaleY, scale_value=self.cell_size * self.img_coefficent ,
                                   angle=self._convert_to_angle(self.world.agents[i].direction), center_origin=True)
            self.canvas.edit_image(self.img[i], scale_type=ScaleType.ScaleX, scale_value=self.cell_size * self.img_coefficent ,
                               angle=self._convert_to_angle(self.world.agents[i].direction), center_origin=True)


        self.canvas.apply_actions()


    def on_process_cycle(self):
        print('process: %s ----------------' % self.current_cycle)

        #generate power ups
        self._generate_power_up()

        self.myCommands = [c[0] for  c in sorted(self.commands.values(),key=lambda x: x[1])]

        for side_name, command in self.myCommands:
            if command.name() == Fire.name():
                self._shoot(self.world.agents[command.id])

            if  command.name() == Move.name():
                if self.world.agents[command.id] in self.world.agents:
                    print "yesss"
                    self.world.agents[command.id] = self._move(self.world.agents[command.id])
                if self.world.agents[command.id] in self.world.agents:
                    has_powerup = self._has_power_up(self.world.agents[command.id].position)
                    if has_powerup != False:
                        if self._has_power_up(self.world.agents[command.id].position) == PowerUpType.HEAL_PACK:
                            print "healpack"
                            if self.world.agents[command.id].health + 1 !=self.world.agents[command.id].max_health:
                                self.world.agents[command.id].health +=1
                        if self._has_power_up(self.world.agents[command.id].position) == PowerUpType.LASER:
                            print "laser"
                            if self.world.agents[command.id].laser_count + 1 != self.world.agents[command.id].laser_max_count:
                                self.world.agents[command.id].laser_count += 1

            if command.name() == Turn.name():
                self.world.agents[command.id] = self._turn(self.world.agents[command.id],command.clockwise)

            self._power_up_life()
            print "agent life" + command.id.__str__() + " : "+self.world.agents[command.id].health.__str__()
            print "agent laser count" + command.id.__str__() + " : " + self.world.agents[command.id].laser_count.__str__()
            self.changed_blocks =  self._change_blocks()
            #end of game
        #self._end()




    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.world)


    def on_update_gui(self):
        power_up_dict = {
            PowerUpType.HEAL_PACK: "laser",
            PowerUpType.LASER: "healpack"

        }
        print('update gui')

        self.powerup_imgs = []

        # apply block changes
        """
         self.canvas.edit_image(self.cell_imgs[self.changed_blocks[2]][self.changed_blocks[3]], x = self.changed_blocks[0]*self.img_coefficent + self.img_coefficent / 2,
                               y=self.changed_blocks[1] * self.img_coefficent + self.img_coefficent / 2 )
        self.canvas.edit_image(self.cell_imgs[self.changed_blocks[0]][self.changed_blocks[1]],
                               x=self.changed_blocks[2] * self.img_coefficent + self.img_coefficent / 2,
                               y=self.changed_blocks[3] * self.img_coefficent + self.img_coefficent / 2)

        """

        for side_name, command in self.myCommands:
            if command.name() == Move.name():
                if  self.world.agents[command.id] in self.world.agents:
                    #apply move
                    pos = self._position_to_xy(self.world.agents[command.id].position)
                    self.canvas.edit_image(ref=self.img[command.id], x=pos[0]*self.cell_size + self.cell_size /2,
                                           y=pos[1]*self.cell_size +self.cell_size /2)

            if command.name() == Turn.name():

                #apply turn
                angle = self._convert_to_angle(self.world.agents[command.id].direction)
                self.canvas.edit_image(ref=self.img[command.id],angle=angle)

            if command.name() == Fire.name():

                #apply  fire
                dir = self.world.agents[command.id].direction
                laser = self.canvas.create_image("Fire", x=self._position_to_xy(self.world.agents[command.id].position)[0]*self.cell_size,
                                        y=self._position_to_xy(self.world.agents[command.id].position)[1]*self.cell_size ,center_origin=False)
                if dir == EDir.RIGHT:
                    self.canvas.edit_image(laser, scale_type=ScaleType.ScaleX,
                                          scale_value=self.cell_size*self.img_coefficent * self.world.agents[command.id].laser_range )
                    self.canvas.edit_image(laser, scale_type=ScaleType.ScaleY,
                                          scale_value=self.cell_size * self.img_coefficent )
                if dir == EDir.LEFT:
                    self.canvas.edit_image(laser, scale_type=ScaleType.ScaleX,
                                          scale_value=self.cell_size * self.img_coefficent * self.world.agents[
                                              command.id].laser_range ,angle=180)
                    self.canvas.edit_image(laser, scale_type=ScaleType.ScaleY,
                                          scale_value=self.cell_size * self.img_coefficent )

                if dir == EDir.UP:
                    self.canvas.edit_image(laser, scale_type=ScaleType.ScaleX,
                                          scale_value=self.cell_size * self.img_coefficent , angle=270)
                    self.canvas.edit_image(laser, scale_type=ScaleType.ScaleY,
                                          scale_value=self.cell_size * self.img_coefficent * self.world.agents[command.id].laser_range , angle=270)

                if dir == EDir.DOWN:
                    self.canvas.edit_image(laser, scale_type=ScaleType.ScaleX,
                                          scale_value=self.cell_size * self.img_coefficent ,angle=90)
                    self.canvas.edit_image(laser, scale_type=ScaleType.ScaleY,
                                          scale_value=self.cell_size * self.img_coefficent * self.world.agents[
                                              command.id].laser_range , angle=90)
                self.canvas.apply_actions()
                self.canvas.delete_element(laser)
             #draw power ups
        for i in  range(len(self.world.powerups)):
            pos = self._position_to_xy(self.world.powerups[i].position)
            self.powerup_imgs.append(self.canvas.create_image(power_up_dict[self.world.powerups[i].type].__str__()+"_powerup",x=pos[0] * self.cell_size + self.cell_size /2,y=pos[1] * self.cell_size +  self.cell_size /2 ,center_origin=True))
            self.canvas.edit_image(self.powerup_imgs[i],scale_type=ScaleType.ScaleX, scale_value=self.cell_size * self.img_coefficent )
            self.canvas.edit_image(self.powerup_imgs[i], scale_type=ScaleType.ScaleY, scale_value=self.cell_size * self.img_coefficent )
        #delete agents images
        for side in self.sides:
            for agent in self.exited_agents[side]:
                if self.img[self.world.agents.index(agent)] in  self.img:
                    self.canvas.delete_element()
            for agent in self.killed_agents[side]:
                if self.img[self.world.agents.index(agent)] in  self.img:
                    self.canvas.delete_element()
        self.commands = {}
        self.canvas.apply_actions()


    def _convert_to_direction(self, angle):

        dirs = {
            0: EDir.DOWN,
            1: EDir.LEFT,
            2: EDir.UP,
            3: EDir.RIGHT

        }
        return dirs[angle/90]


    def _convert_to_angle(self, direction):
        dirs = {
            EDir.DOWN: 0,
            EDir.LEFT: 90,
            EDir.UP: 180,
            EDir.RIGHT: 270

        }
        return dirs[direction]


    def _position_to_xy(self, position):

        x = position % len(self.world.board[0])
        y = position / len(self.world.board[0])
        # its square
        return [x, y]


    def _xy_to_position(self, x, y):

        return (len(self.world.board[0]) * y )+ x


    def _move(self, agent):

        pos = self._position_to_xy(agent.position)
        x = pos[0]
        y = pos[1]
        if self.world.board[y][x] == ECell.GATE:
            agent = self._exit_from_gate(agent)
        else:
            if agent.direction == EDir.RIGHT and x < len(self.world.board[0])- 1:
                if self.world.board[y][x + 1] != ECell.BLOCK:
                    if self._has_agent(agent.position+1) == False:
                        agent.position += 1

            elif agent.direction == EDir.LEFT and x >0:
                if self.world.board[y][x - 1] != ECell.BLOCK:
                    if self._has_agent(agent.position - 1) == False:
                        agent.position -= 1

            elif agent.direction == EDir.UP and y >0 :
                if self.world.board[y - 1][x] != ECell.BLOCK:
                    if self._has_agent(agent.position - len(self.world.board[0])) == False:
                        agent.position -= len(self.world.board[0])

            elif agent.direction == EDir.DOWN and y < len(self.world.board[0])-1:
                if self.world.board[y + 1][x] != ECell.BLOCK:
                    if self._has_agent(agent.position + len(self.world.board[0])) == False:
                        agent.position += len(self.world.board[0])

        return agent


    def _turn(self,agent,clockwise):
        dirs = {
            EDir.DOWN: 0,
            EDir.LEFT: 1,
            EDir.UP: 2,
            EDir.RIGHT: 3

        }
        if clockwise:
            agent.direction = self._convert_to_direction((dirs[agent.direction] * 90 + 90) % 360)
        else:
            agent.direction = self._convert_to_direction((dirs[agent.direction] * 90 - 90) % 360)

        return agent

    def _generate_power_up(self):
        
        type ={
            0: PowerUpType.LASER,
            1: PowerUpType.HEAL_PACK
        }

        powerUp_num_rand = self._rand(len(self.world.agents))
        for i in range(powerUp_num_rand):
            while True:
                x_rnd = self._rand(len(self.world.board[0]) - 1)
                y_rnd = self._rand(len(self.world.board[0]) - 1)
                if self.world.board[y_rnd][x_rnd] == ECell.EMPTY:
                    if self._has_agent(self._xy_to_position(x_rnd, y_rnd)) == False:
                        if self._has_power_up(self._xy_to_position(x_rnd, y_rnd)) == False:
                            break

            power_up = PowerUp()
            power_up.type = type[self._rand(1)]
            power_up.position = self._xy_to_position(x_rnd,y_rnd)
            power_up.apearance_time = self.powerup_appearence_time
            self.world.powerups.append(power_up)

    def _rand(self, n):
        random.seed(time())
        return random.randint(0, n)


    def _power_up_life(self):
        for powerup in self.world.powerups:
            powerup.apearance_time -=1
            if powerup.apearance_time == 0:
                self.__deleted_power_ups_img.append(self.powerup_imgs[self.world.powerups.index(powerup)])
                print ("deleted power up  = " + powerup.position.__str__())
                self.world.powerups.pop(self.world.powerups.index(powerup))



    def _has_power_up(self,position):

        for i in range(len(self.world.powerups)):
            if self.world.powerups[i].position == position:
                return self.world.powerups[i].type
        return False


    def _has_agent(self,position):

        for i in range(len(self.world.agents)):
            if position == self.world.agents[i].position:
                return [True,self.world.agents[i]]
        return False


    def _shoot(self,agent):


        if agent.direction == EDir.RIGHT:
            for x in range(agent.laser_range):
                if (agent.position + x+1) % len(self.world.board[0]) >= len(self.world.board[0])-1:
                    break
                if self._has_agent(agent.position+x+1) != False:
                    if agent.side_name !=self._has_agent(agent.position+x+1)[1].side_name:
                        self._kill(self._has_agent(agent.position+x+1)[1])
                        self.world.scores[agent.side_name] += agent.death_score
                        break
        elif agent.direction == EDir.LEFT:
            for x in range(agent.laser_range):
                if agent.position - (x+1) % len(self.world.board[0]) <= 0:
                    break
                if self._has_agent(agent.position-(x+1)) != False:
                    if agent.side_name !=  self._has_agent(agent.position-(x+1))[1].side_name:
                        self._kill(self._has_agent(agent.position-(x+1))[1])
                        self.world.scores[agent.side_name] += agent.death_score
                        break
        elif agent.direction == EDir.UP:
            for y in range(agent.laser_range):
                if agent.position-(y+1)*len(self.world.board[0]) <= 0:
                    break
                if self._has_agent(agent.position-(y + 1) * len(self.world.board[0])) != False :
                    if agent.side_name !=  self._has_agent(agent.position - (y + 1) * len(self.world.board[0]))[1].side_name:
                        self._kill(self._has_agent(agent.position - (y + 1) * len(self.world.board[0]))[1])
                        self.world.scores[agent.side_name] += agent.death_score
                        break

        elif agent.direction == EDir.DOWN:

            for y in range(agent.laser_range):
                if agent.position + (y+1) * len(self.world.board[0]) >= len(self.world.board[0]) * len(self.world.board[0]) :
                    break
                if self._has_agent(agent.position + (y + 1) * len(self.world.board[0])) != False:
                    if agent.side_name !=  self._has_agent(agent.position + (y + 1) * len(self.world.board[0]))[1].side_name:
                        self._kill(self._has_agent(agent.position + (y + 1) * len(self.world.board[0]))[1])
                        self.world.scores[agent.side_name] += agent.death_score
                        break


    def _chk_agent_end(self):

       first_side = 0
       second_side = 0
       for i in  range(len(self.world.agents)):
           if self.world.agents[i].side_name == self.sides[0]:
               first_side += 1
           else:
               second_side += 1
       if first_side == 0:
           return self.sides[0]
       elif second_side == 0:
           return self.sides[1]
       else:
           return False


    def _kill(self,agent):

        if self.world.agents[self.world.agents.index(agent)].health == 0:
            self.killed_agents[agent.side_name].append(agent)
            self._delete_agent(agent)

        else:
            self.world.agents[self.world.agents.index(agent)].health -= 1



    def _delete_agent(self,agent):

        self.world.agents.pop(self.world.agents.index(agent))


    def _exit_from_gate(self,agent):

        pos = self._position_to_xy(agent.position)
        if agent.direction == EDir.RIGHT:
            if pos[0] == len(self.world.board[0]):
                self.world.scores[agent.side_name] += self.world.exit_score
                self.exited_agents[agent.side_name].append(agent)
                self._delete_agent(agent)
        elif agent.direction == EDir.LEFT:
            if pos[0] == 0:
                self.world.scores[agent.side_name] += self.world.exit_score
                self.exited_agents[agent.side_name].append(agent)
                print "exited agent" + self.exited_agents.__str__()
                self._delete_agent(agent)
        elif agent.direction == EDir.UP:
            if pos[1] == 0:
                self.world.scores[agent.side_name] += self.world.exit_score
                self.exited_agents[agent.side_name].append(agent)
                self._delete_agent(agent)
        else:
            if pos[1] == len(self.world.board[0]):
                self.world.scores[agent.side_name] += self.world.exit_score
                self.exited_agents[agent.side_name].append(agent)
                print "exited agent" + self.exited_agents.__str__()
                self._delete_agent(agent)
        return agent


    def _end(self):

        s0 = self.sides[0]
        s1 = self.sides[1]
        if self.current_cycle >= self.cycle_limitation:
            self.end_game(max(self.world.scores[s0],self.world.scores[s1]))
        else:
            if len(self.killed_agents[s0]) == len(self.agents_dir_row) / 2 or len(self.exited_agents[s1]) == len(self.agents_dir_row) / 2:
                self.end_game(s1)

            elif len(self.killed_agents[s1]) == len(self.agents_dir_row) / 2 or len(self.exited_agents[s0]) == len(self.agents_dir_row) / 2:
                self.end_game(s0)


    def _change_blocks(self):

        while True:
            x_rnd_s =self._rand(len(self.world.board[0]) - 1)
            y_rnd_s = self._rand(len(self.world.board[0]) - 1)
            if self.world.board[y_rnd_s][x_rnd_s] == ECell.BLOCK:
                break
        print "y rand s" + y_rnd_s.__str__()
        print "x rand s" + x_rnd_s.__str__()
        while True:
            x_rnd_d = self._rand(len(self.world.board[0]) - 1)
            y_rnd_d = self._rand(len(self.world.board[0]) - 1)
            if self.world.board[y_rnd_d][x_rnd_d] == ECell.EMPTY:
                if self._has_agent(self._xy_to_position(x_rnd_d, y_rnd_d)) == False:
                    if self._has_power_up(self._xy_to_position(x_rnd_d, y_rnd_d)) == False:
                        break

        print "y rand d" + y_rnd_d.__str__()
        print "x rand d" + x_rnd_d.__str__()

        self.world.board[y_rnd_s][x_rnd_s] = ECell.EMPTY
        self.world.board[y_rnd_d][x_rnd_d] = ECell.BLOCK
        print self.world.board
        return [x_rnd_s, y_rnd_s, x_rnd_d, y_rnd_d]