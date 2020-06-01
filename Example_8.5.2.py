from scipy.stats import t
from scipy.stats import norm
from scipy.stats import chi2

# Question 1:
print('Question 1 ====================')
# Sigma isn't defined, use 1 for calculation here
sigma = 1

# Main parameters
alpha = 0.05
beta = 0.05
miu_0 = 68
miu_1 = miu_0 + 1 * sigma
delta = miu_1 - miu_0
print('delta = ', delta)

#z_beta = norm.ppf(beta)
#print('z_beta = ', z_beta)

for n in range(2, 15):
    z_alpha = t.isf(alpha, n - 1)
    z_beta = norm.isf(beta)
    #chi_2 = chi2.cdf(n * (n - 1), n - 1)
    chi_2 = 1
    print(' n = ', n)
    print(' z_alpha = ', z_alpha)
    print('  z_bete = ', z_beta)
    print('    chi2 = ', chi_2)
    test_a =  n ** 0.5
    test_b = (z_alpha * chi_2 + z_beta) * (sigma / delta)
    print('  test_a = ', test_a)
    print('  test_b = ', test_b)
    print('           ', test_a >= test_b)
    
    
    
# Question 2:
print('Question 2 ====================')

# Sigma isn't defined, use 1 for calculation here
sigma = 1

# Main parameters
alpha = 0.05
miu_0 = 68
miu_1 = miu_0 + 0.75 * sigma
delta = miu_1 - miu_0
n = 30

z_alpha = t.isf(alpha, n - 1)
print('z_alpha = ', z_alpha)
chi_2 = chi2.cdf(n - 1, n - 1)
chi_2 = 1
print('chi_2 = ', chi_2)
z_beta = z_alpha * chi_2 - (n ** 0.5) * delta / sigma
print('        ', z_alpha * chi_2)
print('        ', (n ** 0.5) * delta / sigma)
print('z_beta = ', z_beta)
beta = norm.sf(z_beta * (-1))
print(' beta = ', beta)


