import Two_Way_Anova as TWA

data = [[[14, 10], [11, 11], [13, 9], [10, 12]],
        [[9, 7], [10, 8], [7, 11], [6, 10]],
        [[5, 11], [13, 14], [12, 13], [14, 10]]]

ST, SA, SB, SAXB, SE, r, s, t, n = TWA.quadratic_sum_resolution(data)
alpha = 0.05
test_FA, F_A, reject_ind_F_A, \
test_FB, F_B, reject_ind_F_B, \
test_FAXB, F_AXB, reject_ind_F_AXB = TWA.region_of_rejection(SA, SB, SAXB, SE, r, s, t, alpha)

print('FA:', test_FA, ':', F_A, ':', reject_ind_F_A)
print('FB:', test_FB, ':', F_B, ':', reject_ind_F_B)
print('FAXB:', test_FAXB, ':', F_AXB, ':', reject_ind_F_AXB)

