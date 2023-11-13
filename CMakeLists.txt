cmake_minimum_required(VERSION 3.8)
project(leaky_node)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2_ros REQUIRED)

add_executable(leaky_node leaky_node.cpp)
add_executable(tf2_leaky_node tf2_leaky_node.cpp)

ament_target_dependencies(leaky_node "rclcpp")
ament_target_dependencies(tf2_leaky_node "rclcpp" "tf2_ros")

install(TARGETS tf2_leaky_node leaky_node DESTINATION lib/${PROJECT_NAME})
ament_package()
