import numpy as np
data_x = [20, 25, 30, 35, 40, 50, 60, 65, 70, 75, 80, 90]
data_y = [1.81, 1.70, 1.65, 1.55, 1.48, 1.40, 1.30, 1.26, 1.24, 1.21, 1.20, 1.18]

M_1 = np.ones(len(data_x))
M_x = np.array(data_x)
M_x_2 = M_x * M_x
X = np.vstack((M_1, M_x, M_x_2)).transpose()

Y = np.array(data_y).reshape(len(data_y), 1)

Z = np.dot(X.transpose(), X)
M_tmp = np.dot(np.linalg.inv(Z), X.transpose())
B = np.dot(M_tmp, Y)

print(' Y = ', B[0], ' + ', B[1], ' * x + ', B[2], ' * x**2')