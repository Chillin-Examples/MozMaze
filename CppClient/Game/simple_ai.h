#ifndef SIMPLE_AI_H
#define SIMPLE_AI_H

#include <iostream>
#include <vector>

#include "ks/models.h"
#include "ks/commands.h"

using namespace std;
using namespace ks::models;
using namespace ks::commands;

class AI;


namespace simple_ai {

AI *ai;

const int CELL_EMPTY = ECell::Empty;
const int CELL_BOX = ECell::Box;
const int CELL_TREE = ECell::Tree;
const int CELL_POWERUP_EMITTER = ECell::PowerUpEmitter;

const int POWERUP_AMMO = EPowerUpType::Ammo;
const int POWERUP_HEAL = EPowerUpType::Heal;

const int BANANA_STATUS_ALIVE = EBananaStatus::Alive;
const int BANANA_STATUS_INBOX = EBananaStatus::InBox;
const int BANANA_STATUS_DEAD = EBananaStatus::Dead;


const int MOVE_DIR_UP = EMoveDir::MUp;
const int MOVE_DIR_RIGHT = EMoveDir::MRight;
const int MOVE_DIR_DOWN = EMoveDir::MDown;
const int MOVE_DIR_LEFT = EMoveDir::MLeft;

const int FIRE_DIR_UP = EFireDir::FUp;
const int FIRE_DIR_UPRIGHT = EFireDir::FUpRight;
const int FIRE_DIR_RIGHT = EFireDir::FRight;
const int FIRE_DIR_RIGHTDOWN = EFireDir::FRightDown;
const int FIRE_DIR_DOWN = EFireDir::FDown;
const int FIRE_DIR_DOWNLEFT = EFireDir::FDownLeft;
const int FIRE_DIR_LEFT = EFireDir::FLeft;
const int FIRE_DIR_LEFTUP = EFireDir::FLeftUp;


void move(int bananaId, int dir)
{
    Move move;
    move.id(bananaId);
    move.dir((EMoveDir) dir);
    ai->sendCommand(&move);
}

void enter(int bananaId)
{
    Enter enter;
    enter.id(bananaId);
    ai->sendCommand(&enter);
}

void fire(int bananaId, int dir)
{
    Fire fire;
    fire.id(bananaId);
    fire.dir((EFireDir) dir);
    ai->sendCommand(&fire);
}


void initialize(
    int width, int height, int myScore, int otherScore, int **board,
    Banana myBananas[], int myBananasCount, Banana otherBananas[], int otherBananasCount,
    PowerUp powerups[], int powerupsCount, int enter_score,
    string mySide, string otherSide, int currentCycle, float cycleDuration)
{
}


void decide(
    int width, int height, int myScore, int otherScore, int **board,
    Banana myBananas[], int myBananasCount, Banana otherBananas[], int otherBananasCount,
    PowerUp powerups[], int powerupsCount, int enter_score,
    string mySide, string otherSide, int currentCycle, float cycleDuration)
{
    for (int i= 0; i < myBananasCount; i++)
        if (myBananas[i].status() == BANANA_STATUS_ALIVE)
        {
            Banana banana = myBananas[i];
            int row = banana.position() / width;
            int column = banana.position() % width;

            if (board[row][column] == CELL_BOX) // enter
            {
                enter(banana.id());
                cout << banana.id() << " " << "Enter" << endl;
            }
            else
            {
                if (banana.laser_count() > 0) // fire
                {
                    fire(banana.id(), FIRE_DIR_UPRIGHT);
                    cout << banana.id() << " " << "Fire" << endl;
                }
                else // move
                {
                    move(banana.id(), MOVE_DIR_DOWN);
                    cout << banana.id() << " " << "Move" << endl;
                }
            }
        }
}

}

#endif // SIMPLE_AI_H
