from scipy.stats import t
import numpy as np
import math

a = [16, 25, 21, 20, 23, 21, 19, 15, 13, 23, 17, 20, 29, 18, 22, 16, 22]

a_mean = np.mean(a)
print('a_mean =', a_mean)
a_var  = np.var(a, ddof=1)
print('a_var = ', a_var)
a_n    = len(a)
print('a_n = ', a_n)

miu_0 = 21
alpha = 0.05

sample_t = (a_mean - miu_0) / math.sqrt(a_var / a_n)

student = t.isf(alpha, a_n - 1)

print('sample_t = ', sample_t)
print('student = ', student)