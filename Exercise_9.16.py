import Multi_Variate_Linear_Regression as MVLR
import math

# format : [x, [y1, y2, y3]]
data = [[[-1, -1, -1],7.6],\
        [[-1, -1, 1], 10.3],\
        [[-1, 1, -1], 9.2],\
        [[-1, 1, 1], 10.2],\
        [[1, -1, -1], 8.4],\
        [[1, -1, 1], 11.1],\
        [[1, 1, -1], 9.8],\
        [[1, 1, 1], 12.6]]
        
###############################################################
#Question 1
###############################################################
print('===================Question 1===================')
mvlr = MVLR.multi_variate_linear_regression(data)
mvlr.estimate_coeffient()
print('Y = ', mvlr.B[0], '+', mvlr.B[1],'* x1 +', mvlr.B[2], '* x2 +', mvlr.B[3], '* x3')

###############################################################
#Question 2
###############################################################
print('===================Question 2===================')
drop_data = []
for item in data:
    drop_data.append([[item[0][0], item[0][2]], item[1]])
mvlr2 = MVLR.multi_variate_linear_regression(drop_data)
mvlr2.estimate_coeffient()
print('Y = ', mvlr2.B[0], '+', mvlr2.B[1],'* x1 +', mvlr2.B[2], '* x3')
        
