import Univariate_Linear_Regression as ULR
import math

data = [[3, [28, 33, 22]],\
        [4, [10, 36, 24]],\
        [9, [15, 22, 10]],\
        [15, [6, 14, 9]],\
        [40, [1, 1]]]
        
###############################################################
#Question 1
###############################################################
expanded_data = []
for item in data:
    x = item[0]
    for i in range(len(item[1])):
        y = item[1][i]
        expanded_data.append([x, y])
ulr = ULR.univariate_linear_regression(expanded_data)
#ulr.draw()
###############################################################
#Question 2
###############################################################
expanded_data = []
for item in data:
    x = item[0]
    for i in range(len(item[1])):
        y = math.log(item[1][i])
        expanded_data.append([x, y])

ulr = ULR.univariate_linear_regression(expanded_data)
#ulr.draw()
ulr.estimate_coeffient()
print('n =', ulr.n)
print('S_xx =', ulr.S_xx, ', S_yy =', ulr.S_yy, ', S_xy =', ulr.S_xy)
print('ln Y  = ln(', ulr.a, ') + ', ulr.b, ' * x')
print('Y = ', str(math.exp(ulr.a)) + '* e ^(', ulr.b, ' * x)')