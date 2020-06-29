import Two_Way_Anova as TWA

data = [[[1.63], [1.35], [1.27]],
        [[1.34], [1.30], [1.22]],
        [[1.19], [1.14], [1.27]],
        [[1.30], [1.09], [1.32]]]


ST, SA, SB, SAXB, SE, r, s, t, n = TWA.quadratic_sum_resolution(data)

print('ST =', ST)
print('SA =', SA)
print('SB =', SB)
print('SAXB =', SAXB)
print('SE =', SE)

alpha = 0.05
test_FA, F_A, reject_ind_F_A, \
test_FB, F_B, reject_ind_F_B, \
test_FAXB, F_AXB, reject_ind_F_AXB = TWA.region_of_rejection(SA, SB, SAXB, SE, r, s, t, alpha)

print('FA:', test_FA, ':', F_A, ':', reject_ind_F_A)
print('FB:', test_FB, ':', F_B, ':', reject_ind_F_B)
print('FAXB:', test_FAXB, ':', F_AXB, ':', reject_ind_F_AXB)