# -*- coding: utf-8 -*-

# chillin imports
from chillin_client import TurnbasedAI

# project imports
import simple_ai
from ks.models import World


class AI(TurnbasedAI):

    def __init__(self, world):
        super(AI, self).__init__(world)
        simple_ai.ai = self


    def initialize(self):
        world = self.world
        print('My side: %s' % (self.my_side,))
        simple_ai.initialize(world.width, world.height, world.scores[self.my_side], world.scores[self.other_side],
                             world.board, world.bananas[self.my_side], world.bananas[self.other_side],
                             world.powerups, world.enter_score, self.my_side, self.other_side,
                             self.current_cycle, self.cycle_duration)


    def decide(self):
        world = self.world
        simple_ai.decide(world.width, world.height, world.scores[self.my_side], world.scores[self.other_side],
                         world.board, world.bananas[self.my_side], world.bananas[self.other_side],
                         world.powerups, world.enter_score, self.my_side, self.other_side,
                         self.current_cycle, self.cycle_duration)
