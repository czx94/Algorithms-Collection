cmake_minimum_required(VERSION 2.8)

project(sort)

set(CMAKE_BUILD_TYPE "Debug")

add_executable(quick_sort QuickSort.cpp)
add_executable(bubble_sort BubbleSort.cpp)

