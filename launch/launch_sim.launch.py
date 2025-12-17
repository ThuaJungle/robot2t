<<<<<<< HEAD
#File: launch_sim.launch.py
=======
>>>>>>> 895e434610b068c9ee05b7b7b49194167d756d06
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
<<<<<<< HEAD
    package_name = 'robot2t'

    pkg_share = get_package_share_directory(package_name)

    #Cau hinh file world 
    world_file_name = 'obstacles.world'
    world_path = os.path.join(pkg_share, 'worlds', world_file_name)

    # 0. Cấu hình biến môi trường
    install_dir = os.path.dirname(pkg_share)
=======
    package_name = 'robot2t' # Đảm bảo tên này khớp với tên thư mục package của bạn

    # Lấy đường dẫn thư mục share của package
    pkg_share = get_package_share_directory(package_name)

    # 0. Cấu hình biến môi trường để Gazebo tìm thấy file mesh
    # Lấy thư mục cha của share để Gazebo có thể resolve "package://"
    install_dir = os.path.dirname(pkg_share) 
    # install_dir thường là .../install/robot2t/share
    
>>>>>>> 895e434610b068c9ee05b7b7b49194167d756d06
    gz_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=install_dir
    )

<<<<<<< HEAD
    # 1. Chạy RSP (Robot State Publisher)
=======
    # 1. Gọi lại file rsp.launch.py để lấy mô tả robot
>>>>>>> 895e434610b068c9ee05b7b7b49194167d756d06
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            pkg_share, 'launch', 'rsp.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

<<<<<<< HEAD
    # 2. Chạy Gazebo Sim
=======
    # 2. Khởi chạy Gazebo
>>>>>>> 895e434610b068c9ee05b7b7b49194167d756d06
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'
        )]),
<<<<<<< HEAD
        launch_arguments={'gz_args': '-r ' + world_path}.items()
    )

    #Tha robot vao world
    # 3. Spawn Robot de thay robot vao trong Gazebo Sim 
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-topic', 'robot_description', '-name', 'robot2t', '-z', '0.5'],
        output='screen'
    )

    # 4. Bridge (Cầu nối ROS-Gazebo) để kết nối các topic cần thiết giữa ROS 2 và Gazebo
=======
        launch_arguments={'gz_args': '-r empty.sdf'}.items()
    )

    # 3. Spawn (Thả) robot vào Gazebo
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-topic', 'robot_description', '-name', 'robot2t', '-z', '0.1'],
        output='screen'
    )

    # 4. Cầu nối ROS - Gazebo (Bridge)
>>>>>>> 895e434610b068c9ee05b7b7b49194167d756d06
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
<<<<<<< HEAD
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model',
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan'
=======
            # --- QUAN TRỌNG: THÊM DÒNG NÀY ---
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model'
            # ---------------------------------
>>>>>>> 895e434610b068c9ee05b7b7b49194167d756d06
        ],
        output='screen'
    )

<<<<<<< HEAD
    # 5. CHẠY RVIZ (Đã thêm use_sim_time để đồng bộ)
    rviz_config_file = os.path.join(pkg_share, 'config', 'final_config.rviz') 
    
    node_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

=======
>>>>>>> 895e434610b068c9ee05b7b7b49194167d756d06
    return LaunchDescription([
        gz_resource_path,
        rsp,
        gazebo,
        spawn_entity,
<<<<<<< HEAD
        bridge,
        node_rviz
    ])
=======
        bridge
    ])
>>>>>>> 895e434610b068c9ee05b7b7b49194167d756d06
