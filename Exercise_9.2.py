from scipy.stats import f, t
import numpy as np
import math

data_I = [14, 13, 9, 15, 11, 13, 14, 11]
data_II = [10, 12, 7, 11, 8, 12, 9, 10, 13, 9, 10, 9]
data_III = [11, 5, 9, 10, 6, 8, 8, 7]

n_I = len(data_I)
n_II = len(data_II)
n_III = len(data_III)
n = n_I + n_II + n_III
s = 3
data_all = data_I + data_II + data_III

ST = np.var(data_all, ddof=1) * (n - 1)
print('ST =', ST)
mean_all = np.mean(data_all)
SA = n_I * (np.mean(data_I) - mean_all) ** 2 + n_II * (np.mean(data_II) - mean_all) ** 2 +n_III * (np.mean(data_III) - mean_all) ** 2 
print('SA =', SA)
SE = ST - SA
print('SE =', SE)

F_test_value = (SA / (s - 1)) / (SE / (n - s))
alpha = 0.05
right_pos = f.isf(alpha, s - 1, n - s)
print('F test value = ', F_test_value)
print('F distribution isf = ', right_pos)

SE_mean = SE / (n - s)

alpha = 1 - 0.95
range_1_2_left = np.mean(data_I) - np.mean(data_II) -  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_I + 1 / n_II))
range_1_2_right = np.mean(data_I) - np.mean(data_II) +  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_I + 1 / n_II))
print('mu_I - mu_II range = [', range_1_2_left, ',', range_1_2_right, ']')

range_1_3_left = np.mean(data_I) - np.mean(data_III) -  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_I + 1 / n_III))
range_1_3_right = np.mean(data_I) - np.mean(data_III) +  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_I + 1 / n_III))
print('mu_I - mu_III range = [', range_1_3_left, ',', range_1_3_right, ']')

range_2_3_left = np.mean(data_II) - np.mean(data_III) -  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_II + 1 / n_III))
range_2_3_right = np.mean(data_II) - np.mean(data_III) +  t.isf(alpha / 2, n - s) * math.sqrt(SE_mean * (1 / n_II + 1 / n_III))
print('mu_II - mu_III range = [', range_2_3_left, ',', range_2_3_right, ']')
