cmake_minimum_required(VERSION 3.5)
project(cmd_vel_mux)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake_ros REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rcl_interfaces REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(rcpputils REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(include)

# Nodelet library
add_library(${PROJECT_NAME} SHARED src/cmd_vel_mux.cpp)
ament_target_dependencies(${PROJECT_NAME}
  geometry_msgs
  rcl_interfaces
  rclcpp
  rclcpp_components
  rcpputils
  std_msgs
)

rclcpp_components_register_node(${PROJECT_NAME}
  PLUGIN "cmd_vel_mux::CmdVelMux"
  EXECUTABLE cmd_vel_mux_node)

add_executable(default_cmd_vel_publisher
  src/default_vel_pub.cpp
)

ament_target_dependencies(default_cmd_vel_publisher
  geometry_msgs
  rclcpp
)

install(TARGETS
  default_cmd_vel_publisher
  DESTINATION lib/${PROJECT_NAME}
)

install(TARGETS ${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
)

install(DIRECTORY config launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
