import numpy as np
import math
from scipy.stats import t
from scipy.stats import f
from scipy.stats import ttest_ind
from scipy.stats import ttest_ind_from_stats

fuel_a = [81, 84, 79, 76, 82, 83, 84, 80, 79, 82, 81, 79]
fuel_b = [76, 74, 78, 79, 80, 79, 82, 76, 81, 79, 82, 78]

mean_a = np.mean(fuel_a)
mean_b = np.mean(fuel_b)
print('mean_a = ', mean_a)
print('mean_b = ', mean_b)

var_a = np.var(fuel_a, ddof=1)
var_b = np.var(fuel_b, ddof=1)
print('var_a = ', var_a)
print('var_b = ', var_b)

num_a = len(fuel_a)
num_b = len(fuel_b)


Sw_2 = ((num_a - 1) * var_a + (num_b - 1) * var_b) / (num_a + num_b - 2)
Sw = math.sqrt(Sw_2)

#
# T test for mu_1 - mu_2
#
# Assuming mu_1 >= mu_2
#
t_calc = (mean_a - mean_b) / (Sw * math.sqrt( 1 / num_a + 1 / num_b))

alpha = 0.01
#print(' type alpha = ', type(alpha))
#print(' type num_a = ', type(num_a))
t_alpha = t.isf(alpha, num_a + num_b - 2)

print('t_calc = ', t_calc)
print('t_alpha = ', t_alpha)

#
# F test for sigma_1 / sigma_2
#
# 
alpha_sigma = 0.1
f_calc = 1 / (var_a / var_b)
f_alpha = f.isf(alpha_sigma, num_a - 1, num_b - 1)
print('f_calc = ', f_calc)
print('f_alpha = ', f_alpha)

#
# Use scipy.stats.ttest_ind
#
#
ttest_ind_value = ttest_ind(fuel_a, fuel_b)
print('ttest_ind_value = ', ttest_ind_value)

#
# Use scipy.stats.ttest_ind_from_stats
#
#
ttest_ind_from_stats_value = ttest_ind_from_stats(mean_a, var_a, num_a, mean_b, var_b, num_b)
print('ttest_ind_from_stats_value = ', ttest_ind_from_stats_value)