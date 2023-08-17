from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='people_detector',
            executable='video_publisher',
            name='pub'
        ),
        Node(
            package='people_detector',
            executable='people_detect_subscriber',
            name='sub'
        )

    ])
