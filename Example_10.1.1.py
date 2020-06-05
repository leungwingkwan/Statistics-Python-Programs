import random
import numpy as np


def bootstrap_sampling(data, n, B):

    return_list = []
    for i in range(B):
        sample_list = []
        for j in range(n):
            rnd = int(random.random() * n)
            sample_list.append(data[rnd])
        return_list.append(sample_list)
    return return_list

sample_data = [18.2, 9.5, 12.0, 21.1, 10.2]

n = 5
B = 10


sampling_list = bootstrap_sampling(sample_data, n, B)
theta = []
for item in sampling_list:
    print(item)
    theta.append(np.median(item))

sigma = np.var(theta, ddof = 1)
print('sigma = ', sigma)
