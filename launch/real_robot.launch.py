import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'robot2t'

    # 1. Chạy Robot State Publisher (Để công bố TF của xe)
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
        )]), 
        launch_arguments={'use_sim_time': 'false'}.items() # Quan trọng: false
    )

    # 2. Chạy Lidar Driver (Ví dụ YDLidar X3)
    # Bạn cần cài driver trước: sudo apt install ros-jazzy-ydlidar-ros2-driver (hoặc build từ source)
    # Nếu dùng hãng khác (RPLidar), thay đổi node tương ứng
    lidar_node = Node(
        package='ydlidar_ros2_driver',
        executable='ydlidar_ros2_driver_node',
        name='ydlidar_ros2_driver_node',
        output='screen',
        parameters=[{
            'port': '/dev/ttyUSB1', # Kiểm tra cổng thật trên Pi
            'frame_id': 'laser_frame',
            'baudrate': 115200,
            'angle_min': -3.14,
            'angle_max': 3.14,
            'range_min': 0.1,
            'range_max': 12.0,
            'frequency': 10.0
        }]
    )

    # 3. Chạy Arduino Bridge (Node Python tự viết)
    # Node này thay thế plugin Gazebo: Nhận cmd_vel -> Gửi Serial -> Đọc Encoder -> Gửi Odom
    arduino_node = Node(
        package='robot2t',
        executable='arduino_bridge.py', # Đảm bảo đã chmod +x và khai báo trong setup.py
        output='screen',
        parameters=[{'use_sim_time': False}]
    )

    return LaunchDescription([
        rsp,
        lidar_node,
        arduino_node
    ])