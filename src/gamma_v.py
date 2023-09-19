import numpy as np


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