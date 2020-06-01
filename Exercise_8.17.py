from scipy.stats import t
from scipy.stats import f
import numpy as np
import math

x = [101, 100, 99, 99, 98, 100, 98, 99, 99, 99]
y = [100, 98, 100, 99, 98, 99, 98, 98, 99, 100]

# Question 1

print('Question 1 ====================')
var2_x = np.var(x, ddof=1)
var2_y = np.var(y, ddof=1)
n_x = len(x)
n_y = len(y)

alpha = 0.05

# Two sided test
test_value = var2_x / var2_y
print('test_value =', test_value)

right_pos = f.isf(alpha / 2, n_x - 1, n_y - 1)
left_pos = f.ppf(alpha / 2, n_x - 1, n_y - 1)
print('right_pos = ', right_pos)
print('left_pos = ', left_pos)

# Question 2
print('Question 2 ====================')
mean_x = np.mean(x)
mean_y = np.mean(y)
print(mean_x, ':', mean_y)
sw2 = ((n_x - 1) * var2_x + (n_y - 1) * var2_y) / (n_x + n_y - 2)
print('sw2 = ', sw2)
test_value = (mean_x - mean_y) / math.sqrt(sw2 * ( 1 / n_x + 1 / n_y ) )
print('test_value = ', test_value)

# Two sided test
right_pos = t.isf(alpha / 2, n_x + n_y - 2)
left_pos = t.ppf(alpha / 2, n_x + n_y - 2)
print('right_pos = ', right_pos)
print('left_pos = ', left_pos)
