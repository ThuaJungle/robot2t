import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'robot2t' # Đảm bảo tên này khớp với tên thư mục package của bạn

    # Lấy đường dẫn thư mục share của package
    pkg_share = get_package_share_directory(package_name)

    # 0. Cấu hình biến môi trường để Gazebo tìm thấy file mesh
    # Lấy thư mục cha của share để Gazebo có thể resolve "package://"
    install_dir = os.path.dirname(pkg_share) 
    # install_dir thường là .../install/robot2t/share
    
    gz_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=install_dir
    )

    # 1. Gọi lại file rsp.launch.py để lấy mô tả robot
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            pkg_share, 'launch', 'rsp.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # 2. Khởi chạy Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'
        )]),
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
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
            # --- QUAN TRỌNG: THÊM DÒNG NÀY ---
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model'
            # ---------------------------------
        ],
        output='screen'
    )

    return LaunchDescription([
        gz_resource_path,
        rsp,
        gazebo,
        spawn_entity,
        bridge
    ])
