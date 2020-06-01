from scipy.stats import t
import numpy as np
import math

data_a = [6.6, 7.0, 8.3, 8.2, 5.2, 9.3, 7.9, 8.5, 7.8, 7.5, 6.1, 8.9, 6.1, 9.4, 9.1]
data_b = [7.4, 5.4, 8.8, 8.0, 6.8, 9.1, 6.3, 7.5, 7.0, 6.5, 4.4, 7.7, 4.2, 9.4, 9.1]

delta = 0

# Approach A
mean_a = np.mean(data_a)
print('mean_a =', mean_a)
var_a = np.var(data_a, ddof=1)
len_a = len(data_a)

mean_b = np.mean(data_b)
print('mean_b =', mean_b)
var_b = np.var(data_b, ddof=1)
len_b = len(data_b)

sw_2_numerator = (len_a - 1) * var_a + (len_b - 1) * var_b
sw_2_denominator = (len_a + len_b - 2)
sw = math.sqrt(sw_2_numerator / sw_2_denominator)

test_t = (mean_a - mean_b - delta) / (sw * math.sqrt(1/len_a +1 / len_b))
dist_t = t.isf(0.05, len_a + len_b -2)

print('Approach A:')
print('test_t:', test_t)
print('dist_t:', dist_t)

# Approach B
array_c = np.array(data_a) - np.array(data_b)
mean_c = np.mean(array_c)
var_c = np.var(array_c, ddof=1)
len_c = len_a
miu = 0

test_t = (mean_c - miu) / math.sqrt(var_c / len_c)
dist_t = t.isf(0.05, len_c - 1)
print('Approach B:')
print('test_t:', test_t)
print('dist_t:', dist_t)



