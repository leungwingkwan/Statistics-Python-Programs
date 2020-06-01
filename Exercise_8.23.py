import numpy as np
import math
from scipy.stats import chi2

fi = np.array([0, 1, 2, 3, 4, 5, 6, 7])
fi_page = np.array([36, 40, 19, 2, 0, 2, 1, 0])
alpha = 0.05

Ex = np.sum(fi * fi_page) / np.sum(fi_page)
Ex2 = np.sum(fi * fi * fi_page) / np.sum(fi_page)
Dx = Ex2 - (Ex) ** 2

print('Ex = ', Ex)
print('Dx = ', Dx)

# Take Lambda = Ex 
lambda_p = Ex

def poisson_distribution(lambda_p, k):
    return lambda_p ** k * math.exp((-1)* lambda_p) / math.factorial(k)


p_list = []

# Calculate possibility of poisson distribution from 1 - 6
for i in range(7):
    p_list.append(poisson_distribution(lambda_p, i))

# Calculate possibility of poisson distribtionm of >=7
p_list.append(1 - np.sum(p_list))
n = sum(fi_page)

combine_p = []
combine_fi = []
combine_fi_page = []
j = -1
for i in range(len(p_list)):
    a = p_list[i] * n

    if a >= 5:
       combine_p.append(p_list[i])
       combine_fi.append(fi[i])
       combine_fi_page.append(fi_page[i])
       j += 1
    else:
       if j > -1:
          combine_p[j] = combine_p[j] + p_list[i]
          combine_fi[j] = combine_fi[j] + fi[i]
          combine_fi_page[j] = combine_fi_page[j] + fi_page[i]
       else:
          j += 1
          combine_p.append(p_list[i])
          combine_fi.append(fi[i])
          combine_fi_page.append(fi_page[i])

for i in range(len(combine_p)):
    print(i, ':', combine_p[i], ':', combine_fi[i], ':', combine_fi_page[i])
    
# Test Value
n = np.sum(combine_fi_page)
test_value = 0 - n

for i in range(len(combine_fi_page)):
    test_value = test_value + combine_fi_page[i] ** 2 / (n * combine_p [i])

print('test_value =', test_value)

right_pos = chi2.isf(alpha, len(combine_fi_page) - 1 - 1)

print('right_pos = ', right_pos)
