#!/bin/bash
set -e

# ROS ortamını yükle
source /opt/ros/humble/setup.bash
source /ws/install/setup.bash

# Launch dosyasını başlat
exec ros2 launch command_server_pkg system_launch.py
