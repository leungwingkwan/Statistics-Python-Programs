import Rank_Sum_Test as RST

class Wilcoxon_Rank_Sum_Test(RST.Rank_Sum_Test):
    def __init__(self, sample1, sample2):
        super(Wilcoxon_Rank_Sum_Test, self).__init__(sample1, sample2, True)

    def isf(self, alpha):
        # sf_list - accumulative of density (x>=, in descending order, 10, 9, 8, ...)

        if self.success < 0:
           return -1, -1

        last_idx = -1
        for i in range(len(self.sf_list)):
            if alpha <= self.sf_list[i][2]:
               return self.sf_list[last_idx][0], self.sf_list[last_idx][2]
            last_idx = i
        return -1, -1

    def ppf(self, alpha):
        # cdf_list - accumulative of density (<=x, in ascending order, 1,2, 3, ...)

        if self.success < 0:
           return -1, -1

        last_idx = -1
        for i in range(len(self.cdf_list)):
            if alpha <= self.cdf_list[i][2]:
               return self.cdf_list[last_idx][0], self.cdf_list[last_idx][2]
            last_idx = i
        return -1, -1
