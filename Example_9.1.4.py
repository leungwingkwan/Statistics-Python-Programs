from scipy.stats import f

machine_1 = [0.236, 0.238, 0.248, 0.245, 0.243]
machine_2 = [0.257, 0.253, 0.255, 0.254, 0.261]
machine_3 = [0.258, 0.264, 0.259, 0.267, 0.262]

all_data = machine_1 + machine_2 + machine_3
s = 3
n_1 = len(machine_1)
n_2 = len(machine_2)
n_3 = len(machine_3)
n = n_1 + n_2 + n_3

Sum_Xij_sqr = 0
T = 0
for Xij in all_data:
    Sum_Xij_sqr = Sum_Xij_sqr + Xij ** 2
    T = T + Xij

St = Sum_Xij_sqr - (T ** 2) / n
print('St =', St)

Sa = sum(machine_1) ** 2 / n_1 + sum(machine_2) ** 2 / n_2 + sum(machine_3) ** 2 / n_3 - (T ** 2) / n  
print('Sa =', Sa)
Se = St - Sa
print('Se =', Se)

Sa_mean = Sa / (s - 1)
print('Sa_mean =', Sa_mean)
Se_mean = Se / (n - s)
print('Se_mean =', Se_mean)

alpha = 0.05

test_value = Sa_mean / Se_mean
print('test_value = ', test_value)

right_pos = f.isf(alpha, s - 1, n - s)
print('right_pos = ', right_pos)
	


