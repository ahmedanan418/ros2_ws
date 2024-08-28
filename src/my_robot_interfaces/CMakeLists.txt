cmake_minimum_required(VERSION 3.8)
project(my_robot_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
#####Add this everytime#####
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME} #Add every .msg or .srv here
  "msg/HardwareStatus.msg"
  "msg/LedStateArray.msg"
  "srv/ComputeRectangleArea.srv"
  ############################


)


#Add this line
ament_export_dependencies(rosidl_default_runtime)

ament_package()
