import Multi_Variate_Linear_Regression as MVLR
import math

# format : [x, [y1, y2, y3]]
data = [[10.0, [25.2, 27.3, 28.7]],\
        [15.0, [29.8, 31.1, 27.8]],\
        [20.0, [31.2, 32.6, 29.7]],\
        [25.0, [31.7, 30.1, 32.3]],\
        [30.0, [29.4, 30.8, 32.8]]]
        
###############################################################
#Question 1
###############################################################
print('===================Question 1===================')
expanded_data = []
for item in data:
    x = item[0]
    for i in range(len(item[1])):
        y = item[1][i]
        expanded_data.append([[x], y])

mvlr = MVLR.multi_variate_linear_regression(expanded_data)
mvlr.draw()

###############################################################
#Question 2
###############################################################
print('===================Question 2===================')
expanded_data = []
for item in data:
    x = item[0]
    for i in range(len(item[1])):
        y = item[1][i]
        expanded_data.append([[x, x**2], y])
mvlr = MVLR.multi_variate_linear_regression(expanded_data)
mvlr.estimate_coeffient()
print('Y = ', mvlr.B[0], '+', mvlr.B[1],'* x +', mvlr.B[2], '* x^2')