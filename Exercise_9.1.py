import numpy as np
from scipy.stats import f
from scipy.stats import t
import math

data_a = [40, 42, 48, 45, 38]
data_b = [26, 28, 34, 32, 30]
data_c = [39, 50, 40, 50, 43]
data_all = data_a + data_b + data_c

s = 3
n_a = len(data_a)
n_b = len(data_b)
n_c = len(data_c)
n = n_a + n_b + n_c

ST = np.var(data_all, ddof=1) * (n-1)
print('ST = ', ST)
mean_all = np.mean(data_all)
SA = n_a * (np.mean(data_a) - mean_all) ** 2 + n_b * (np.mean(data_b) - mean_all) ** 2 + n_c * (np.mean(data_c) - mean_all) ** 2
print('SA = ', SA)
SE = ST - SA
print('SE = ', SE)

F_test = (SA / (s - 1)) / (SE / (n - s))
print('F test value = ', F_test)
right_pos = f.isf(0.05, s - 1, n - s)
print('F distribution isf = ', right_pos)

SE_mean = SE / (n - s)
alpha = 1 - 0.95
t_delta = t.isf(alpha / 2, n - s) * math.sqrt(SE_mean)

range_a_b_left = np.mean(data_a) - np.mean(data_b) -  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_a + 1 / n_b))
range_a_b_right = np.mean(data_a) - np.mean(data_b) +  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_a + 1 / n_b))
print('a - b range = [', range_a_b_left, ',', range_a_b_right, ']')

range_b_c_left = np.mean(data_b) - np.mean(data_c) -  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_b + 1 / n_c))
range_b_c_right = np.mean(data_b) - np.mean(data_c) +  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_b + 1 / n_c))
print('b - c range = [', range_b_c_left, ',', range_b_c_right, ']')

range_a_c_left = np.mean(data_a) - np.mean(data_c) -  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_a + 1 / n_c))
range_a_c_right = np.mean(data_a) - np.mean(data_c) +  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_a + 1 / n_c))
print('a - c range = [', range_a_c_left, ',', range_a_c_right, ']')
