import numpy as np
import math
import random
import bootstrap as BS

def estimate_theta(Xm, Xmn, Xn):
    return (Xmn + 2 * Xn) / (2 * Xm + 2 * Xmn + 2 * Xn)
    
estimated_theta = estimate_theta(342, 500, 187)
print('estimated_theta =', estimated_theta)

Pm = (1 - estimated_theta) ** 2
Pmn = 2 * estimated_theta * (1 - estimated_theta)
Pn = estimated_theta ** 2
print('Pm =', Pm, ', Pmn =', Pmn, ', Pn =', Pn)

Pm_L = 0
Pm_R = Pm
Pmn_L = Pm_R
Pmn_R = Pm + Pmn
Pn_L = Pmn_R
Pn_R = 1

theta_list = []
for i in range(10):
    Pm_cnt = 0
    Pmn_cnt = 0
    Pn_cnt = 0
    
    for j in range(1029):
        rnd = random.random()
        if ((rnd >= Pm_L) and (rnd < Pm_R)): 
             Pm_cnt += 1
        if ((rnd >= Pmn_L) and (rnd < Pmn_R)): 
             Pmn_cnt += 1
        if ((rnd >= Pn_L) and (rnd <= Pn_R)): 
             Pn_cnt += 1
    theta_list.append(estimate_theta(Pm_cnt, Pmn_cnt, Pn_cnt))


bs = BS.bootstrap(theta_list)
lb, ub = bs.confidence_interval(0.05, 0.95, theta_list)
print('lower bound =', lb)
print('upper bound =', ub)
