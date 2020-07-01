import bootstrap as BS
import numpy as np

data = [18.2, 9.5, 12.0, 21.1, 10.2]

bs = BS.bootstrap(data, np.median)
print('bs.theta =', bs.theta)
bs.sampling(5, 10, np.median)
print('bs.bootstrap_sample =', bs.bootstrap_sample)
print('mean of bs.bootstrap_sample =', np.mean(bs.bootstrap_sample[0]))
print('sigma = ', bs.sample_standard_deviation(bs.bootstrap_sample[0]))

# Verify example 1 data
print('===============example 1 sample data=====================')
theta_star = [12.0, 12.0, 10.2, 12.0, 18.2, 10.2, 12.0, 18.2, 18.2, 10.2]
print('theta_star_median =', np.median(theta_star))
print('theta_start_mean =', np.mean(theta_star))
theta_star_sigma = (np.var(theta_star, ddof=1)) ** 0.5
print('theta_star_sigma = ', theta_star_sigma)
print('It\'s proven, theta_start_mean is used in deviation of theta')