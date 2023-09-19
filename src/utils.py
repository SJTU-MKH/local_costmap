###
# 计算功率谱密度函数，以及功率谱密度的积分，在[1,30]Hz内的
###

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
import pandas as pd


# 加载IMU数据，假设data是一个包含加速度计数据的Numpy数组
data = pd.read_csv("/home/khm/project/local_costmap/data/imu_data.csv")
a_z_column = data['linear_acceleration_z']

Fs = 100  # 采样频率为50 Hz

# 使用Welch方法计算功率谱密度

frequencies, power_density = welch(a_z_column, fs=Fs, nperseg=256, noverlap=128)

# 绘制频谱图
plt.semilogy(frequencies, power_density)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectrum Density')
plt.title('Power Spectrum Density using Welch Method')
plt.grid()
plt.show()


## 频段积分
low_freq = 1
high_freq = 30

# 找到频率数组中低频和高频的索引
low_idx = np.argmax(frequencies >= low_freq)
high_idx = np.argmax(frequencies >= high_freq)

# 对功率谱密度在指定频率范围内进行积分
integral = np.trapz(power_density[low_idx:high_idx], frequencies[low_idx:high_idx])

print("积分值:", integral)



mean = 0
std_dev = 0.5
size_m = 10

rand_b_m = np.random.normal(mean,std_dev, size_m)

gamma_v = []
v = 2
for i in range(size_m):
    gamma_v.append(np.cos(2*np.pi*rand_b_m[i]*2))
    gamma_v.append(np.sin(2*np.pi*rand_b_m[i]*2))

print(gamma_v)