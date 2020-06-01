import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

data =[90, 105, 101, 95, 100, 100, 101, 105, 93, 97]

origin_sigma = 14
origin_sigma_2 = origin_sigma ** 2

sample_sigma_2 = np.var(data, ddof=1)

n = len(data)

test_value = (n-1) * sample_sigma_2 / origin_sigma_2

alpha = 0.05
left_value = alpha / 2
right_value = alpha / 2

left_pos = chi2.ppf(left_value, n - 1)
right_pos = chi2.isf(right_value, n - 1)

print('test_value = ', test_value)

print('===============================================')
print('two sided test: (level of significance %f)' %left_value)
print('left_pos = ', left_pos)
print('right_pos = ', right_pos)

pos_ppf = chi2.ppf(alpha, n - 1)
pos_isf = chi2.isf(alpha, n - 1)
print('===============================================')
print('left sided test (level of significance %f)' %left_value)
print('pos_ppf = ', pos_ppf)
print('===============================================')
print('right sided test (level of significance %f)' %right_value)
print('pos_isf = ', pos_isf)

start_x = 0
end_x = 30
step = 0.01
x = []
y_cdf = []
y_pdf = []

i = start_x
while (i <= end_x):
       x.append(i)
       y_cdf.append(chi2.cdf(i, n - 1))
       y_pdf.append(chi2.pdf(i, n - 1))
       i += step

plt.plot(x, y_cdf, linewidth=2)
plt.plot(x, y_pdf, linewidth=2)
plt.show()