import bootstrap as BS
import numpy as np

data = [9, 8, 10, 12, 11, 12, 7, 9, 11, 8, 9, 7, 7, 8, 9, 7,\
        9, 9, 10, 9, 9, 9, 12, 10, 10, 9, 13, 11, 13, 9]

print('======================Question 1======================')
def mu_sigma(sample, _):
    mu = np.mean(sample)
    sigma = np.var(sample, ddof=1) ** 0.5
    return mu, sigma
    
bs = BS.bootstrap(data)
bs.sampling(len(data), 10000, mu_sigma)


mu_list = bs.bootstrap_sample[0]
sigma_list = bs.bootstrap_sample[1]

alpha_left = 0.1 / 2
alpha_right = 1 - 0.1 / 2
left_margin, right_margin = bs.confidence_interval(alpha_left, alpha_right, mu_list)
print('confidence interval of mu is [', left_margin, ',', right_margin, ']')

left_margin, right_margin = bs.confidence_interval(alpha_left, alpha_right, sigma_list)
print('confidence interval of sigma is [', left_margin, ',', right_margin, ']')