import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command # <--- Thêm Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

# Không cần import xacro ở đây nữa

def generate_launch_description():

    # 1. Kiểm tra xem có dùng giờ giả lập không
    use_sim_time = LaunchConfiguration('use_sim_time')

    # 2. Lấy đường dẫn file Xacro
    pkg_path = os.path.join(get_package_share_directory('robot2t'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')
    
    # 3. Xử lý file Xacro bằng lệnh Command (Cách chuẩn ROS 2)
    # Thay vì xacro.process_file, ta dùng Command để gọi lệnh xacro từ terminal ảo
    robot_description_config = Command(['xacro ', xacro_file])
    
    # 4. Tạo node Robot State Publisher
    params = {'robot_description': robot_description_config, 'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),

        node_robot_state_publisher
    ])