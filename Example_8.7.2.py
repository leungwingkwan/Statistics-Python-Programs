import ND_Rank_Sum_Test as ND_RST

def main():
    d_a = [7.0, 3.5, 9.6, 8.1, 6.2, 5.1, 10.4, 4.0, 2.0, 10.5]
    d_b = [5.7, 3.2, 4.2, 11.0, 9.7, 6.9, 3.6, 4.8, 5.6, 8.4, 10.1, 5.5, 12.3]
    rank_sum_test = ND_RST.ND_Rank_Sum_Test(d_a, d_b)
    print('R1 = ', rank_sum_test.R1)
    print('E(R1) = ',rank_sum_test.E_R1)
    print('D(R1) =', rank_sum_test.D_R1)
    
if __name__ == '__main__':
   main()