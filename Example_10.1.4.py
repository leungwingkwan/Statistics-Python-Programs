import bootstrap as BS
import numpy as np

data = [136.3, 136.6, 135.8, 135.4, 134.7, 135.0, 134.1, 143.3, 147.8,\
        148.8, 134.8, 135.2, 134.9, 149.5, 141.2, 135.4, 134.8, 135.8,\
        135.0, 133.7, 134.4, 134.9, 134.8, 134.5, 134.3, 135.2]

print('======================Question 1======================')
bs = BS.bootstrap(data, np.median)
print('bs.theta =', bs.theta)
bs.sampling(len(data), 10000, np.median)

alpha_left = 0.05 / 2
alpha_right = 1 - 0.05 / 2
left_margin, right_margin = bs.confidence_interval(alpha_left, alpha_right, bs.bootstrap_sample[0])
print('confidence interval is [', left_margin, ',', right_margin, ']')

print('======================Question 2======================')
bs2 = BS.bootstrap(data)
#
# trimmed mean percentage xx% stands for trimming xx% smallest samples and xx% largest samples 
# here trims 20% smallest samples and 20% largest samples
#
bs2.sampling(len(data), 2, bs2.trimmed_mean, {'left_trim_pct':0.2, 'right_trim_pct':0.8})
alpha_left = 0.05 / 2
alpha_right = 1 - 0.05 / 2
left_margin, right_margin = bs2.confidence_interval(alpha_left, alpha_right, bs2.bootstrap_sample[0])
print('confidence interval is [', left_margin, ',', right_margin, ']')