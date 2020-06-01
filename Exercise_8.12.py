from scipy.stats import chi2

s = 0.007
n = 9
std_deviation = 0.005

test_value = (n-1) * (s ** 2) / (std_deviation ** 2)

print('test_value = ', test_value)

# Right side test

alpha = 0.05

right_side_pos = chi2.isf(alpha, n - 1)
print('right side position =', right_side_pos)