cmake_minimum_required(VERSION 2.8.3)
project(ublox_logger)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package()
include_directories(
  ${catkin_INCLUDE_DIRS}
)
