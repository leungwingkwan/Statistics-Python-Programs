
import One_Way_Anova as OWA

data = [[192, 189, 176, 185, 190],
        [190, 201, 187, 196, 200],
        [188, 179, 191, 183, 194],
        [187, 180, 188, 175, 182]]

ST, SA, SE, s, n = OWA.quadratic_sum_resolution(data)
print('ST=', ST, ', SA =', SA, ', SE =', SE, ',s = ', s, ',n = ', n)
alpha = 0.05
test_value, F_value, reject_ind = OWA.region_of_rejection(SA, SE, s, n, alpha)
print('test_value = ', test_value, ', F_value = ', F_value, ', reject_ind =', reject_ind)