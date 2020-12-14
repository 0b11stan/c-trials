//
// Created by tristan on 09/01/19.
//

#include <cstdio>
#include "Task.h"

void Task::execute() {
    printf("run %s\n", name.c_str());
    computeTime--;
}


int Task::getSlackTime(int currentTime) const {
    return ( deadline - currentTime ) - computeTime;
}

bool Task::isOver() const {
    return computeTime == 0;
}
