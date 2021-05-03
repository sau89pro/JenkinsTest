cmake_minimum_required(VERSION 2.8)

project(JenkinsTest)

set(SRC main.cpp test/test.cpp)

add_executable(jenkins_test ${SRC})

install(TARGETS jenkins_test)
