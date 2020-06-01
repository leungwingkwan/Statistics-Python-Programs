import ND_Rank_Sum_Test as ND_RST
import numpy as np
from scipy.stats import norm

def main():
    d_a = [82, 73, 91, 84, 77, 98, 81, 79, 87, 85]
    d_b = [80, 76, 92, 86, 74, 96, 83, 79, 80, 75, 79]
    rank_sum_test = ND_RST.ND_Rank_Sum_Test(d_a, d_b)
    print('R1 = ', rank_sum_test.R1)
    print('E(R1) = ',rank_sum_test.E_R1)
    print('D(R1) =', rank_sum_test.D_R1)
    print('mean of d_a:', np.mean(d_a))
    print('mean of d_b:', np.mean(d_b))
    
    # mean of d_a > mean of d_b
    # This is an right hand test
    
    z = (rank_sum_test.R1 - rank_sum_test.E_R1) / (rank_sum_test.D_R1 ** 0.5)
    print('z =', z)
    right_pos = norm.isf(0.05)
    print('right_pos = ', right_pos)
    
if __name__ == '__main__':
   main()