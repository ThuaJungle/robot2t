cmake_minimum_required(VERSION 3.5)
project(robot2t)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # set(ament_cmake_copyright_FOUND TRUE)
  # set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# ==========================================================
# PHẦN QUAN TRỌNG: Cài đặt các thư mục tài nguyên
# ==========================================================

# Chỉ liệt kê các thư mục ĐÃ TỒN TẠI. 
# Hiện tại bạn mới có 'launch' và 'description'.
# Sau này nếu tạo thêm folder 'config' hay 'worlds' thì thêm tên vào đây.
install(
  DIRECTORY config launch description meshes maps scripts/arduino_bridge.py worlds 
  DESTINATION share/${PROJECT_NAME}
)

# ==========================================================
# Lệnh kết thúc (Chỉ được có 1 dòng này ở cuối file)
# ==========================================================
ament_package()
