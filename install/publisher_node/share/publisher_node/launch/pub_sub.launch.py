from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    return LaunchDescription([
        Node(
            package='publisher_node',
            executable='publisher_node',
            name='publisher_node',
            output='screen',
        ),
        Node(
            package='subscriber_node',
            executable='subscriber_node',
            name='subscriber_node',
            output='screen',
        ),
    ])
