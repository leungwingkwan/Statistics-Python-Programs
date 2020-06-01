from scipy.stats import f
import numpy as np

n1 = 60
n2 = 40
s1 = 15.46
s2 = 9.66

alpha = 0.05

test_value = s1 / s2

# Right sided test
right_pos = f.isf(alpha, n1 - 1, n2 - 1)

print('test_value = ', test_value)
print('right_pos = ', right_pos)