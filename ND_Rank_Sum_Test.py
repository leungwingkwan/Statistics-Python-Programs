import Rank_Sum_Test as RST

class ND_Rank_Sum_Test(RST.Rank_Sum_Test):
    #
    # ND = Normal Distribution
    def __init__(self, sample1, sample2):
        super(ND_Rank_Sum_Test, self).__init__(sample1, sample2, False)
        
        if ((self.n1 < 10) or (self.n2 < 10)):
           self.success = -1
           print('n1 < 10 or n2 < 10, ND_Rank_Sum_Test.__init__ failed')
           
        if self.success > 0:        
            self.E_R1 = self.calc_E_R1()
            self.D_R1 = self.calc_D_R1()
        
    def calc_E_R1(self):
    
        if self.success < 0:
           return -1
           
        return self.n1 * (self.n1 + self.n2 + 1) / 2
    
    def calc_D_R1(self):
        if self.success < 0:
           return -1
        
        if (len(self.ti) == 0):
           return self.n1 * self.n2 * (self.n1 + self.n2 + 1) /12
        else:
           n1 = self.n1
           n2 = self.n2
           n = n1 + n2
           sum_ti = 0
           for ti_item in self.ti:
               sum_ti = sum_ti + ti_item * (ti_item ** 2 - 1)
           numerator = n1 * n2 * (n * (n ** 2 - 1) - sum_ti)
           denominator = 12 * n * (n - 1)
           return numerator / denominator