 
一、项目启动命令流程
 
1.进入工作空间：cd ros2_homework_advanced_ws
2.清理缓存：rm build install log
3.编译：colcon build --packages-select fsd_common_msgs map_to_visualize
4.刷新环境变量：source install/setup.bash
5.启动：ros2 launch map_to_visualize launch.py
6.新开终端启动rviz2

这次作业让我掌握了基于ROS2读取自定义bag消息，
RViz三维可视化锥桶的完整项目流程， 从依赖消息包编译、C++节点代码编写，
到CMake安装配置一步步完成开发。开发途中遇到不少问题：一开始分不清自定义消息fsd_common_msgs 编译顺序，先编译可视化包导致报错；误打开ROS1rviz软件，出现无法连接master报错
本次作业完整走完了话题订阅→Marker发布→launch批量启动→RViz可视化整套流程，学会根据bag内容调试代码、排查异常，积累了实操经验。
 
