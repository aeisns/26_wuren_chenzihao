cmake_minimum_required(VERSION 3.8)
project(map_to_visualize)
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
find_package(rclcpp REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(fsd_common_msgs REQUIRED)

add_executable(map_vis src/map.cpp)
ament_target_dependencies(map_vis rclcpp visualization_msgs fsd_common_msgs)

install(TARGETS map_vis DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()

