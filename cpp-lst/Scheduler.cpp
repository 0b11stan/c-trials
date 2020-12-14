//
// Created by tristan on 09/01/19.
//

#include "Scheduler.h"

void Scheduler::run() {
    while (! tasks.empty()) {
        auto task = this->tasks.begin();
        auto lowestSlackTimeTask = task;

        while (task != this->tasks.end()) {

            if (task->isOver()) {
                task = tasks.erase(task);
            }
            else {
                int lowestSlackTime = lowestSlackTimeTask->getSlackTime(currentTime);
                int slackTime = task->getSlackTime(currentTime);

                if (lowestSlackTime > slackTime) lowestSlackTimeTask = task;

                task++;
            }
        }

        lowestSlackTimeTask->execute();

        currentTime++;
    }
}
