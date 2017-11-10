# -*- coding: utf-8 -*-

# python imports
import random
from ks.models import World,ECell,EDir,Agent,PowerUp,PowerUpType
# chillin imports
from chillin_client import TurnbasedAI

# project imports
from ks.models import World
from ks.commands import Move, Turn, Fire
from random import randint

class AI(TurnbasedAI):

    def __init__(self, world):
        super(AI, self).__init__(world)


    def decide(self):
        print('decide')
        for id in range(len(self.world.agents)):
            #if self.world.agents[id].side_name == self.my_side:
             #   print "dir" + self.world.agents[id].direction.__str__()
              #  self.send_command(Move(id=id))
              #  if self.world.agents[id].position%len(self.world.board[0]) == len(self.world.board[0])-1 and self.world.agents[id].direction == EDir.RIGHT:
               #     if self.world.board[self.world.agents[id].position / len(self.world.board[0])][
                #              self.world.agents[id].position % len(self.world.board[0])] == ECell.GATE:
                 #       self.send_command(Move(id=id))
                  #  else:
                   #     self.send_command(Turn(id=id ,clockwise=True))
            if id  == 0:
                self.send_command(Move(id=id))
            else:
                self.send_command(Move(id=id))

