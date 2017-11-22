# -*- coding: utf-8 -*-

# python imports
import random

# chillin imports
from chillin_client import TurnbasedAI

# project imports
from ks.commands import Move, Enter, Fire, EMoveDir, EFireDir
from ks.models import World, EBananaStatus, ECell


class AI(TurnbasedAI):

  def __init__(self, world):
    super(AI, self).__init__(world)

    # self.scenario = {
    #   'Dole': [
    #     Move(id=0, dir=EMoveDir.Right),
    #     Move(id=0, dir=EMoveDir.Down)
    #   ],
    #   'Chiquita': [
    #     Move(id=0, dir=EMoveDir.Left),
    #     Fire(id=0, dir=EFireDir.Up)
    #   ]
    # }


  def decide(self):
    print('-------------- decide --------------')
    # if len(self.scenario[self.my_side]) > 0:
      # self.send_command(self.scenario[self.my_side].pop(0))

    # random moves
    my_bananas = self.world.bananas[self.my_side]
    for banana in my_bananas:
      if banana.status != EBananaStatus.Alive:
        continue
      # else
      x, y = self._position_to_xy(banana.position)
      if self.world.board[y][x] == ECell.Box:
        self.send_command(Enter(id=banana.id))
        print('%i %s' % (banana.id, 'Enter'))
      else:
        if banana.laser_count > 0:
          self.send_command(Fire(id=banana.id, dir=EFireDir(random.randint(0, 7))))
          print('%i %s' % (banana.id, 'Fire'))
        else:
          valid_dirs = []
          move_dirs = {
            EMoveDir.Up:    banana.position - self.world.width,
            EMoveDir.Right: banana.position + 1,
            EMoveDir.Down:  banana.position + self.world.width,
            EMoveDir.Left:  banana.position - 1
          }
          for dir in move_dirs:
            x, y = self._position_to_xy(move_dirs[dir])
            if self.world.board[y][x] != ECell.Tree:
              valid_dirs.append(dir)

          self.send_command(Move(id=banana.id, dir=EMoveDir(valid_dirs[random.randint(0, len(valid_dirs) - 1)])))
          print('%i %s' % (banana.id, 'Move'))


  def _position_to_xy(self, position):
    x = position % self.world.width
    y = position // self.world.width
    return (x, y)
