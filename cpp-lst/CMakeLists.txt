cmake_minimum_required(VERSION 3.13)
project(ordonanceur)

set(CMAKE_CXX_STANDARD 14)

add_executable(ordonanceur main.cpp Task.cpp Task.h Scheduler.cpp Scheduler.h)