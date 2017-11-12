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

    self.scenario = {
      'Dole': [
        Move(id=0, dir=EMoveDir.Right),
        Move(id=0, dir=EMoveDir.Down)
      ],
      'Chiquita': [
        Move(id=0, dir=EMoveDir.Left),
        Fire(id=0, dir=EFireDir.Up)
      ]
    }


  def decide(self):
    print('decide')
    # if len(self.scenario[self.my_side]) > 0:
      # self.send_command(self.scenario[self.my_side].pop(0))

    # random moves
    my_bananas = self.world.bananas[self.my_side]
    for banana in my_bananas:
      if banana.status != EBananaStatus.Alive:
        continue
      # else
      x = banana.position % self.world.width
      y = banana.position // self.world.height
      if self.world.board[y][x] == ECell.Box:
        self.send_command(Enter(id=banana.id))
      else:
        if banana.laser_count > 0:
          self.send_command(Fire(id=banana.id, dir=EFireDir(random.randint(0, 7))))
        else:
          self.send_command(Move(id=banana.id, dir=EMoveDir(random.randint(0, 3))))
