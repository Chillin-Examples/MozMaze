# -*- coding: utf-8 -*-

# python imports
import random

# project imports
from ks.commands import Move, Enter, Fire, EMoveDir, EFireDir
from ks.models import ECell, EPowerUpType, EBananaStatus


ai = None

CELL_EMPTY = ECell.Empty
CELL_BOX = ECell.Box
CELL_TREE = ECell.Tree
CELL_POWERUP_EMITTER = ECell.PowerUpEmitter

POWERUP_AMMO = EPowerUpType.Ammo
POWERUP_HEAL = EPowerUpType.Heal

BANANA_STATUS_ALIVE = EBananaStatus.Alive
BANANA_STATUS_INBOX = EBananaStatus.InBox
BANANA_STATUS_DEAD = EBananaStatus.Dead


MOVE_DIR_UP = EMoveDir.Up
MOVE_DIR_RIGHT = EMoveDir.Right
MOVE_DIR_DOWN = EMoveDir.Down
MOVE_DIR_LEFT = EMoveDir.Left

FIRE_DIR_UP = EFireDir.Up
FIRE_DIR_UPRIGHT = EFireDir.UpRight
FIRE_DIR_RIGHT = EFireDir.Right
FIRE_DIR_RIGHTDOWN = EFireDir.RightDown
FIRE_DIR_DOWN = EFireDir.Down
FIRE_DIR_DOWNLEFT = EFireDir.DownLeft
FIRE_DIR_LEFT = EFireDir.Left
FIRE_DIR_LEFTUP = EFireDir.LeftUp



def initialize(width, height, scores, board, bananas, powerups, enter_score, my_side, other_side):
    pass


def decide(width, height, scores, board, bananas, powerups, enter_score, my_side, other_side):
    my_bananas = bananas[my_side]
    for banana in my_bananas:
        if banana.status == BANANA_STATUS_ALIVE:
            row = banana.position // width
            column = banana.position % width

            if board[row][column] == CELL_BOX: # enter
                enter(banana.id)
                print('%i %s' % (banana.id, 'Enter'))
            else:

                if banana.laser_count > 0: # fire
                    fire(banana.id, random.choice([
                        FIRE_DIR_UP,
                        FIRE_DIR_UPRIGHT,
                        FIRE_DIR_RIGHT,
                        FIRE_DIR_RIGHTDOWN,
                        FIRE_DIR_DOWN,
                        FIRE_DIR_DOWNLEFT,
                        FIRE_DIR_LEFT,
                        FIRE_DIR_LEFTUP
                    ]))
                    print('%i %s' % (banana.id, 'Fire'))

                else: # move
                    move(banana.id, random.choice([
                        MOVE_DIR_UP,
                        MOVE_DIR_RIGHT,
                        MOVE_DIR_DOWN,
                        MOVE_DIR_LEFT
                    ]))
                    print('%i %s' % (banana.id, 'Move'))



def move(banana_id, dir):
    ai.send_command(Move(id=banana_id, dir=dir))


def enter(banana_id):
    ai.send_command(Enter(id=banana_id))


def fire(banana_id, dir):
    ai.send_command(Fire(id=banana_id, dir=dir))
