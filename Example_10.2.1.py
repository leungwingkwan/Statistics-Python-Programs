import numpy as np
import math
import random
import bootstrap as BS

data = [142.84, 97.04, 32.46, 69.14, 85.67, 114.43, 41.76, 163.07, 108.22, 63.28]

def estimate_eta(data):
    return (np.multiply(data, data).sum() / len(data)) ** 0.5

def Weibull_Distribution(beta, eta, x):
    if ((x <= 0) or (beta <= 0) or (eta <= 0)):
       return None
    else:
       return (1 - math.exp(-1*(x / eta)**beta))

def generate_Weibull_x(eta, capacity, num_of_sample):
    return_array = []
    for i in range(num_of_sample):
        sample_array = []
        for j in range(capacity):
            U = random.random()
            X = eta*(-1 * math.log(U))**0.5
            sample_array.append(X)
        return_array.append(sample_array)
    return return_array
        


print('===============================Question 1=====================')
estimated_eta = estimate_eta(data)
print('estimated eta =', estimated_eta)
print('===============================Question 2=====================')
tmp_data = generate_Weibull_x(estimated_eta, 10, 5000)

eta_list = []
for sub_array in tmp_data:
    tmp_eta = estimate_eta(sub_array)
    eta_list.append(tmp_eta)

bs = BS.bootstrap(eta_list)
left_95, _ = bs.confidence_interval(0.05, 1.00, eta_list)
left_90, _ = bs.confidence_interval(0.10, 1.00, eta_list)
print('left_95 =', left_95)
print('left_90 =', left_90)

R_95 = 1 - Weibull_Distribution(2, left_95, 50)
R_90 = 1 - Weibull_Distribution(2, left_90, 50)
print('R_95 =', R_95)
print('R_90 =', R_90)
 





