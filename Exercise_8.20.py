from scipy.stats import norm

sigma_2 = 2.5
alpha = 0.05
beta = 0.05

miu = 15
miu_2 = 13
delta = miu - miu_2

za = norm.isf(alpha)
zb = norm.isf(beta)
sigma = sigma_2 ** 0.5

n = ((za + zb) * sigma / delta) ** 2

print('n = ', n)