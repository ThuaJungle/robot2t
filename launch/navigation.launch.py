#File: navigation.launch.py 
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'robot2t'
    pkg_share = get_package_share_directory(package_name)

    # Đường dẫn file map và params
    map_file = os.path.join(pkg_share, 'maps', 'my_map.yaml')
    params_file = os.path.join(pkg_share, 'config', 'nav2_params.yaml')

    # Gọi file launch chuẩn của nav2_bringup
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('nav2_bringup'), 'launch', 'bringup_launch.py'
        )]),
        launch_arguments={
            'map': map_file,
            'params_file': params_file,
            'use_sim_time': 'false',
            'autostart': 'true' # Tự động kích hoạt (Lifecycle)
        }.items()
    )

    return LaunchDescription([
        nav2_launch
    ])