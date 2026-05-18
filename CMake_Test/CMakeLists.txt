cmake_minimum_required(VERSION 3.19)

project(Test)

set(CMAKE_CXX_STANDARD 14)

add_subdirectory(common)

add_subdirectory(modules)

add_executable(test main.cpp)

target_include_directories(test PUBLIC  ${CMAKE_CURRENT_SOURCE_DIR}/common/kalman/include   ${OpenCV_INCLUDE_DIRS})

target_link_libraries(test math A1 A2 M1 M2 ${OpenCV_LIBS})
