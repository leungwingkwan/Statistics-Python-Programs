
import One_Way_Anova as OWA

data = [[29.6, 24.3, 28.5, 32.0],
        [27.3, 32.6, 30.8, 34.8],
        [5.8, 6.2, 11.0, 8.3 ],
        [21.6, 17.4, 18.3, 19.0],
        [29.2, 32.8, 25.0, 24.2]]

ST, SA, SE, s, n = OWA.quadratic_sum_resolution(data)
print('ST=', ST, ', SA =', SA, ', SE =', SE, ',s = ', s, ',n = ', n)
alpha = 0.05
test_value, F_value, reject_ind = OWA.region_of_rejection(SA, SE, s, n, alpha)
print('test_value = ', test_value, ', F_value = ', F_value, ', reject_ind =', reject_ind)