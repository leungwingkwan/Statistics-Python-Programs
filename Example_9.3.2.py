import numpy as np

x = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
y = [45, 51, 54, 61, 66, 70, 74, 78, 85, 89]


x_mean = np.mean(x)
y_mean = np.mean(y)

S_xx = 0
for xi in x:
    S_xx = S_xx + (xi - x_mean) ** 2
print('S_xx = ', S_xx)
    
S_yy = 0
for yi in y:
    S_yy = S_yy + (yi - y_mean) ** 2
print('S_yy = ', S_yy)

S_xy = 0
for i in range(len(x)):
    S_xy = S_xy + (x[i] - x_mean)*(y[i] - y_mean)
print('S_xy = ', S_xy)
    
b = S_xy / S_xx
a = y_mean - b * x_mean

print('y = ', a, ' + ', b, ' * x')
