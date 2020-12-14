#include <utility>

//
// Created by tristan on 09/01/19.
//

#ifndef ORDONANCEUR_TASK_H
#define ORDONANCEUR_TASK_H

#include <string>

class Task {

private:
    int deadline;
    int computeTime;

public:
    std::string name;
    Task(int deadline, int computeTime, std::string name):
        deadline(deadline), computeTime(computeTime), name(std::move(name)) {}
    void execute();
    int getSlackTime(int currentTime) const;
    bool isOver() const;
};


#endif //ORDONANCEUR_TASK_H
