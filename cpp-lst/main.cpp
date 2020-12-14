#include <iostream>
#include <deque>

#include "Task.h"
#include "Scheduler.h"

int main() {

    std::deque<Task> tasks = {
            Task(10, 5, "test1"),
            Task(21, 3, "test2"),
            Task(6, 1, "test3")
    };
    Scheduler scheduler = Scheduler(tasks);
    scheduler.run();

    return 0;
}

