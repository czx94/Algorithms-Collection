cmake_minimum_required(VERSION 2.8)

project(DataStructure)

set(CMAKE_BUILD_TYPE "Debug")

add_executable(linkedlist LinkedList.cpp)
add_executable(queue Queue.cpp)
add_executable(stack Stack.cpp)

