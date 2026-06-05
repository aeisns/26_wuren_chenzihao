from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    node = Node(package="map_to_visualize", executable="map_vis")
    bag_path = "/home/chenzihao/ros2_homework_advanced_ws/map_to_visualize"
    bag_play = ExecuteProcess(cmd=["ros2","bag","play",bag_path])
    return LaunchDescription([node, bag_play])
