import bootstrap as BS
import numpy as np

data = [9, 8, 10, 12, 11, 12, 7, 9, 11, 8, 9, 7, 7, 8, 9, 7,\
        9, 9, 10, 9, 9, 9, 12, 10, 10, 9, 13, 11, 13, 9]

print('======================Original Date======================')

mean_x = np.mean(data)
n = len(data)
s = np.var(data, ddof=1)**0.5
print('n =', n)
print('mean_x =', mean_x )
print('s =', s)
print('s2=', np.var(data, ddof=1))


def w(sample, kw):
    mean_x = kw['mean_x']
    n = kw['n']
    xi = np.mean(sample)
    si = np.var(sample, ddof=1)**0.5
    return (xi - mean_x) / (si / (n ** 0.5))

bs = BS.bootstrap(data)
bs.sampling(len(data), 10000, w, {'mean_x':mean_x, 'n':n})

alpha_left = 0.1 / 2
alpha_right = 1 - 0.1 / 2
left_margin, right_margin = bs.confidence_interval(alpha_left, alpha_right, bs.bootstrap_sample[0])
print('lower bound of w =', left_margin)
print('upper bound of w =', right_margin)

###
### please note right & left margin match upper & lower bound
lower_bound = mean_x - right_margin * s / (n ** 0.5)
upper_bound = mean_x - left_margin * s / (n ** 0.5)
print('confidence interval is [', lower_bound, ',', upper_bound, ']')

