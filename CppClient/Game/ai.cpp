#include "ai.h"

#include <ctime>
#include <vector>
#include <iostream>

using namespace std;
using namespace koala::chillin::client;
using namespace ks::models;
using namespace ks::commands;


AI::AI(World *world): TurnbasedAI<World*>(world)
{
    srand(time(0));
}

void AI::initialize()
{
}

void AI::decide()
{
}

int AI::getRandInt(int start, int end)
{
    return (random() % (end - start + 1)) + start;
}
