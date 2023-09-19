# encoding: utf-8
import rosbag
import csv


def extract_imu(bag_file, topic, csvfile):
    # 打开ROS bag文件
    bag = rosbag.Bag(bag_file, 'r')

    # 创建CSV文件并写入列名
    with open(output_csv_file, 'w') as csvfile:

        fieldnames = ['timestamp', 'angular_velocity_x', 'angular_velocity_y', 'angular_velocity_z', 'linear_acceleration_x', 'linear_acceleration_y', 'linear_acceleration_z']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 遍历ROS bag文件中的消息
        for topic, msg, t in bag.read_messages(topics=[imu_topic]):
            # 提取IMU数据并写入CSV文件
            writer.writerow({
                'timestamp': str(t),
                'angular_velocity_x': msg.angular_velocity.x,
                'angular_velocity_y': msg.angular_velocity.y,
                'angular_velocity_z': msg.angular_velocity.z,
                'linear_acceleration_x': msg.linear_acceleration.x,
                'linear_acceleration_y': msg.linear_acceleration.y,
                'linear_acceleration_z': msg.linear_acceleration.z
            })

    # 关闭ROS bag文件
    bag.close()



bag_file = './2023-09-12-16-23-19.bag'  # 你的ROS bag文件名称
imu_topic = '/airsim_node/drone_1/imu/Imu'  # IMU话题名称
output_csv_file = 'imu_data.csv'  # 保存IMU数据的CSV文件

extract_imu(bag_file, imu_topic, output_csv_file)
