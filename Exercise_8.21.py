import numpy as np
from scipy.stats import t
import math

data = [108, 124, 124, 106, 138, 163, 159, 134]
miu = 125
alpha = 0.05

print('Question 1 ==========================')

S = np.var(data, ddof=1)
n = len(data)
x_mean = np.mean(data)
print('x_mean = ', x_mean)

test_value = (x_mean - miu) / math.sqrt(S / n)

right_pos = t.isf(alpha, n - 1)

print('test_value = ', test_value)
print('right_pos = ', right_pos)

print('Question 2 ==========================')

i = 1
test_value = 2
alpha = 0.05
beta = 0.1


while (i < test_value):
      i += 1
      numerator = (t.isf(alpha, i - 1) + t.isf(beta, i - 1)) ** 2
      denominator = 1.4 ** 2
      test_value = numerator / denominator
      print(' i = ', i, ', test_value = ', test_value)
      
print(' standard answer in exercise book ============')
numerator = (t.isf(alpha, n - 1) + t.isf(beta, n - 1)) ** 2
denominator = 1.4 ** 2
test_value = numerator / denominator
print(' n = ', n, ', test_value = ', test_value)