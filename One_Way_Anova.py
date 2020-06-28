import numpy as np
from scipy.stats import f
# One-Way Anova

def quadratic_sum_resolution(input_data):
    #
    # input_data format:
    # Level 1: x[1, j] (j = 1, ..., n1)
    # Level 2: x[2, j] (j = 1, ..., n2)
    # ...
    # Level S: x[s, j] (j = 1, ..., ns)
    s = len(input_data)
    #
    # mean_x = np.mean(input_data) prompts error, when n1, n2, ..., ns are not identical.
    nj = []
    sum_x = 0
    for i in range(s):
        nj.append(len(input_data[i]))
        sum_x = sum_x + sum(input_data[i])
    n = sum(nj)
    mean_x = sum_x / n

    # Calculate ST
    ST = 0
    for i in range(s):

        for j in range(nj[i]):
            ST = ST + (input_data[i][j] - mean_x) ** 2
    # Calculate SA
    mean_x_j = []
    for i in range(s):
        mean_x_j.append(np.mean(input_data[i]))

    SA = 0
    for i in range(s):
        SA = SA + nj[i] * mean_x_j[i] ** 2
    SA = SA - n * mean_x ** 2
    SE = ST - SA
    return ST, SA, SE, s, n
    
def region_of_rejection(SA, SE, s, n, alpha):
    test_value = (SA / (s - 1)) / (SE / (n - s))
    F_value = f.isf(alpha, s - 1, n - s)
    
    if test_value >= F_value:
       reject_ind = True
    else:
       reject_ind = False
    return test_value, F_value, reject_ind
        

    