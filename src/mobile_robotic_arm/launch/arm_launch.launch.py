import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='init_pose',
            default_value='-x 0 -y 0 -z 0 -R 0 -P 0 -Y 0'
        ),
        launch_ros.actions.Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            parameters=[
                {
                    'robot_description': None
                },
                {
                    'my_robot': 'robot_arm'
                },
                {
                    'use_gui': 'False'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='tf',
            executable='static_transform_publisher',
            name='map_to_base',
            parameters=[
                {
                    'robot_description': None
                },
                {
                    'my_robot': 'robot_arm'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='controller_manager',
            executable='spawner',
            name='controller_spawner',
            output='screen',
            parameters=[
                {
                    'robot_description': None
                },
                {
                    'my_robot': 'robot_arm'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {
                    'robot_description': None
                },
                {
                    'my_robot': 'robot_arm'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='gazebo_ros',
            executable='spawn_model',
            name='spawn_urdf',
            output='screen',
            parameters=[
                {
                    'robot_description': None
                },
                {
                    'my_robot': 'robot_arm'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='rostopic',
            executable='rostopic',
            name='fake_joint_calibration',
            parameters=[
                {
                    'robot_description': None
                },
                {
                    'my_robot': 'robot_arm'
                }
            ]
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'gazebo_ros'), 'launch/empty_world.launch.py')
            ),
            launch_arguments={
                'world_name': get_package_share_directory('robot_arm') + '/launch/final_world.world'
            }.items()
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
