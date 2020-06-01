cmake_minimum_required(VERSION 3.0.2)
project(menguiin_bot)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  nav_msgs
  roscpp
  rospy
  sensor_msgs
  std_msgs
)

add_message_files(FILES Angle.msg Distance.msg Velocity.msg)
generate_messages(DEPENDENCIES std_msgs)

catkin_package(
#  INCLUDE_DIRS include
  LIBRARIES menguiin_bot
CATKIN_DEPENDS roscpp sensor_msgs std_msgs message_runtime
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(project1 src/project1.cpp)
add_dependencies(project1 ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(project1
  ${catkin_LIBRARIES}
)

add_executable(input_value src/input_value.cpp)
add_dependencies(input_value ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(input_value
  ${catkin_LIBRARIES}
)