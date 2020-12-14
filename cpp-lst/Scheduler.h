#include <utility>

//
// Created by tristan on 09/01/19.
//

#ifndef ORDONANCEUR_SCHEDULER_H
#define ORDONANCEUR_SCHEDULER_H


#include <deque>

#include "Task.h"

class Scheduler {

private:
    int currentTime = 0;
    std::deque<Task> tasks;

public:
    explicit Scheduler(std::deque<Task> tasks) : tasks(std::move(tasks)) {}
//    Task* nextTask();
    void run();

};


#endif //ORDONANCEUR_SCHEDULER_H
