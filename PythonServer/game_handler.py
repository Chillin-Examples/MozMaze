# -*- coding: utf-8 -*-

# python imports
import random

# chillin imports
from chillin_server import TurnbasedGameHandler
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ks.models import World
from ks.commands import Move, Turn, Fire


class GameHandler(TurnbasedGameHandler):

    def on_recv_command(self, side_name, agent_name, command_type, command):
        print('command: %s %s' % (side_name, command_type, ))


    def on_initialize(self):
        print('initialize')
        self.world = World()


    def on_initialize_gui(self):
        print('initialize gui')


    def on_process_cycle(self):
        print('process: %s' % (self.current_cycle))


    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.world)


    def on_update_gui(self):
        print('update gui')
