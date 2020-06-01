import Wilcoxon_Rank_Sum_Test as WRST

def main():
    d1 = [1.9, 0.5, 0.9, 2.1]
    d2 = [3.1, 5.3, 1.4, 4.6, 2.8]
    rank_sum_test = WRST.Wilcoxon_Rank_Sum_Test(d1, d2)
    print('isf = ', rank_sum_test.isf(0.05))
    print('ppf = ',rank_sum_test.ppf(0.05))
    print('R1=', rank_sum_test.R1)
    
if __name__ == '__main__':
   main()