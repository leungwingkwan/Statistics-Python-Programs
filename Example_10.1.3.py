import bootstrap as BS
import numpy as np

data = [136.3, 136.6, 135.8, 135.4, 134.7, 135.0, 134.1, 143.3, 147.8,\
        148.8, 134.8, 135.2, 134.9, 149.5, 141.2, 135.4, 134.8, 135.8,\
        135.0, 133.7, 134.4, 134.9, 134.8, 134.5, 134.3, 135.2]

bs = BS.bootstrap(data, np.median)
print('bs.theta =', bs.theta)
bs.sampling(len(data), 10000, np.median)

print('bias = ', bs.bias(bs.bootstrap_sample[0], bs.theta))
