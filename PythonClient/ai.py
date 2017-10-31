# -*- coding: utf-8 -*-

# python imports
import random

# chillin imports
from chillin_client import TurnbasedAI

# project imports
from ks.models import World
from ks.commands import Move, Turn, Fire


class AI(TurnbasedAI):

    def __init__(self, world):
        super(AI, self).__init__(world)


    def decide(self):
        print('decide')
