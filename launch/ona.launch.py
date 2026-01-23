# Copyright 2020 Open Source Robotics Foundation, Inc.
# All rights reserved.
#
# Software License Agreement (BSD License 2.0)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the following
#   disclaimer in the documentation and/or other materials provided
#   with the distribution.
# * Neither the name of {copyright_holder} nor the names of its
#   contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""Launch the cmd_vel_mux node with default configuration."""

import os

import ament_index_python.packages
import launch
import launch_ros.actions

import yaml


def generate_launch_description():
    share_dir = ament_index_python.packages.get_package_share_directory('cmd_vel_mux')
    
    params_file = os.path.join(share_dir, 'config', 'ona_simu_params.yaml')
    with open(params_file, 'r') as f:
        params = yaml.safe_load(f)['cmd_vel_mux']['ros__parameters']

    cmd_vel_mux_node = launch_ros.actions.Node(
        package='cmd_vel_mux',
        executable='cmd_vel_mux_node',
        output='screen',
        parameters=[params],
        remappings=[('cmd_vel', 'ona2/cmd_vel')]
    )

    default_cmd_vel_pub = launch_ros.actions.Node(
        package='cmd_vel_mux',
        executable='default_cmd_vel_publisher',
        output='screen',
        remappings=[('cmd_vel', 'ona2/default/cmd_vel')]
    )

    return launch.LaunchDescription([cmd_vel_mux_node, default_cmd_vel_pub])
