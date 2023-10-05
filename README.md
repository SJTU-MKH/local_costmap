# 论文复现

《How Does It Feel? Self-Supervised Costmap Learning for Off-Road Vehicle Traversability》 ICRA 2023


## bag parse
```
/cmd                                 960 msgs    : geometry_msgs/TwistStamped                 
/controls                            671 msgs    : racepak/rp_controls                        
/deep_cloud                          179 msgs    : sensor_msgs/PointCloud2                    
/dynamixel_state                      52 msgs    : dynamixel_workbench_msgs/DynamixelStateList
/goal_dynamixel_position             300 msgs    : sensor_msgs/JointState                     
/joy                                 300 msgs    : sensor_msgs/Joy                            
/local_height_map                    178 msgs    : grid_map_msgs/GridMap                      
/local_rgb_map                       178 msgs    : sensor_msgs/Image                          
/multisense/imu/imu_data            3631 msgs    : sensor_msgs/Imu                            
/multisense/left/image_rect          179 msgs    : sensor_msgs/Image                          
/multisense/left/image_rect_color    179 msgs    : sensor_msgs/Image                          
/multisense/right/image_rect         179 msgs    : sensor_msgs/Image                          
/odom                                489 msgs    : nav_msgs/Odometry                          
/odometry/filtered_odom              489 msgs    : nav_msgs/Odometry                          
/ros_talon/current_position           60 msgs    : std_msgs/Float32                           
/ros_talon/steering_angle            300 msgs    : std_msgs/Float32                           
/shock_pos                           671 msgs    : racepak/rp_wheel_encoders                  
/tf_static                             1 msg     : tf2_msgs/TFMessage                         
/wheel_rpm                           671 msgs    : racepak/rp_wheel_encoders
```

## 数据提取 & 问题汇总
[github仓库](https://github.com/castacks/tartan_drive)

操作流程：
```
git clone https://github.com/castacks/tartan_drive.git
# src下
cd ..
# 编译
catkin_make
source devel/setup.zsh

## 创建conda环境
conda create -n ros
conda activate ros
# Q2
pip3 install ros-rospy
cd rosbag_to_dataset
pip3 install .

# Q1
cd ../wheeledsim_rl
cp ../README.md .
pip3 install .
# Q3
pip3 install pycryptodomex gnupg
conda install pytorch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0 pytorch-cuda=11.7 -c pytorch -c nvidia

# Q4,5
pip3 install opencv-python gym roslz4
sudo apt install -y ros-melodic-ackermann-msgs ros-melodic-grid-map-msgs

## 处理数据
cd ..
python ./dataset/multi_convert_bag.py --bag_dir Your_path --save_to ./dataset/data/torch --use_stamps True --torch True --zero_pose_init True --config_spec ./specs/2021_atv_3.yaml
```
- Q1: 在`wheeledsim_rl`下进行`install`报错 README.md 找不到
  - A: 将README.md 移动到wheeledsim_rl下即可 `cp ../README.md .`
- Q2: rospy 安装: `pip3 install rospy`
- Q3: 运行代码报错:`ModuleNotFoundError: No module named ‘Cryptodome`
  - A: `pip3 install pycryptodomex gnupg`
- Q4: 缺少某某库:`pip3 install opencv-python gym roslz4`
- Q5: 缺少`ackermann_msgs, gridmap_msgs`:
  - A: `sudo apt install -y ros-melodic-ackermann-msgs ros-melodic-grid-map-msgs`