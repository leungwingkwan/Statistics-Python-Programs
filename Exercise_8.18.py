from scipy.stats import f
from scipy.stats import t
import numpy as np
import math

data_1 = [1.79, 1.75, 1.67, 1.65,
          1.87, 1.74, 1.94,
          1.62, 2.06, 1.33,
          1.96, 1.69, 1.70]
data_2 = [2.39, 2.51, 2.86,
          2.56, 2.29, 2.49,
          2.36, 2.58,
          2.62, 2.41]

# Question 1
print('Question 1 =======================')
s_1 = np.var(data_1, ddof=1)
s_2 = np.var(data_2, ddof=1)
n_1 = len(data_1)
n_2 = len(data_2)
test_value = s_1 / s_2
alpha = 0.1
# Two sided test
left_pos = f.ppf(alpha / 2, n_1 - 1, n_2 - 1)
right_pos = f.isf(alpha / 2, n_1 - 1, n_2 - 1)
print('test_value = ', test_value)
print('left_pos = ', left_pos)
print('right_pos = ', right_pos)

# Question 1
print('Question 2 =======================')
mean_1 = np.mean(data_1)
mean_2 = np.mean(data_2)
Sw = ((n_1 - 1) * s_1 + (n_2 - 1) * s_2) / (n_1 + n_2 - 2)
test_value = (mean_1 - mean_2) / math.sqrt(Sw * ( 1 / n_1 + 1 / n_2))
left_pos = t.ppf(alpha / 2, n_1 + n_2 - 2)
right_pos = t.isf(alpha / 2, n_1 + n_2 - 2)
print('test_value = ', test_value)
print('left_pos = ', left_pos)
print('right_pos = ', right_pos)
