import random
import numpy as np
import math

def bootstrap_sampling(data, n, B):

    return_list = []
    data_len = len(data)
    for i in range(B):
        sample_list = []
        for j in range(n):
            rnd = int(random.random() * data_len)
            sample_list.append(data[rnd])
        return_list.append(sample_list)
    return return_list

sample_data = [18.2, 9.5, 12.0, 21.1, 10.2]

n = 5
B = 10


sampling_list = bootstrap_sampling(sample_data, n, B)
theta_list = []
for item in sampling_list:
    median_theta = np.median(item)
    theta_list.append(median_theta)
    print(item, ':', median_theta)
    
theta_median = np.median(sample_data)
sigma = 0
for item in theta_list:
    sigma = sigma + (item - theta_median) ** 2
sigma = math.sqrt(sigma / (len(theta_list) - 1))
print('sigma = ', sigma)


