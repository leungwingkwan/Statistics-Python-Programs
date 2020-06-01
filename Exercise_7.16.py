from scipy.stats import norm
import numpy as np
sample = [6.0, 5.7, 5.8, 6.5, 7.0, 6.3, 5.6, 6.1, 5.0]
num_of_sample = len(sample)
mean_of_sample = np.mean(sample)
print('mean_of_sample = ', mean_of_sample)
var_of_dist = 0.6

isf_of_dist = norm.isf((1-0.95) / 2)

upper = mean_of_sample + var_of_dist * isf_of_dist / (num_of_sample ** (1/2))
lower =  mean_of_sample - var_of_dist * isf_of_dist / (num_of_sample ** (1/2))

print('upper = ', upper)
print('lower = ', lower)

from scipy.stats import t

var_of_sample = np.var(sample)
print('var_of_sample = ', var_of_sample)
print('var_of_sample = ', var_of_sample * 9 / 8)
var_of_sample = np.var(sample) * num_of_sample / (num_of_sample - 1)

t_of_dist = t.isf((1-0.95)/2, num_of_sample - 1)
print('t_of_dist = ', t_of_dist)
upper = mean_of_sample + (var_of_sample ** (1/2)) * t_of_dist / (num_of_sample ** (1/2))
lower = mean_of_sample - (var_of_sample ** (1/2)) * t_of_dist / (num_of_sample ** (1/2))

print('upper = ', upper)
print('lower = ', lower)