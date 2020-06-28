
import One_Way_Anova as OWA

data = [[8, 6, 4, 2],
        [6, 6, 4, 4],
        [8, 10, 10, 10, 12],
        [4, 4, 2]]

ST, SA, SE, s, n = OWA.quadratic_sum_resolution(data)
print('ST=', ST, ', SA =', SA, ', SE =', SE, ',s = ', s, ',n = ', n)
alpha = 0.05
test_value, F_value, reject_ind = OWA.region_of_rejection(SA, SE, s, n, alpha)
print('test_value = ', test_value, ', F_value = ', F_value, ', reject_ind =', reject_ind)