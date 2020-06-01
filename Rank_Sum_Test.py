class Rank_Sum_Test():
    def __init__(self, sample1, sample2, build_rank_indicator):

        #
        # Only list or int data type is accepted, 
        # self.success == -1 will prevent all methods runs
        #                  1 (int), can run isf, ppf functions
        #                  2 (list), can run calc_R1, isf, ppf functions
        self.success = -1
        if ((type(sample1) == int) and (type(sample2) == int)):
            self.success = 1
            self.n1 = sample1
            self.n2 = sample2
            self.data1 = None
            self.data2 = None
            self.R1 = -1
            self.R2 = -1
            self.ti = []
            
        if ((type(sample1) == list) and (type(sample2) == list)):
            self.success = 2
            self.n1 = len(sample1)
            self.n2 = len(sample2)
            self.data1 = sample1
            self.data1.sort()
            self.data2 = sample2
            self.R1, self.R2, self.ti = self.calc_R1_R2()

        #
        # Continue to initialize variables
        if self.success > 0:
           self.n1_n2_list = [i for i in range(1, self.n1 + self.n2 + 1)]
           self.max_num = self.n1_n2_list[len(self.n1_n2_list) - 1]
           self.min_num = self.n1_n2_list[0]
           self.min_list = [self.min_num for i in range(self.n1)]
           self.max_list = [self.max_num for i in range(self.n1)]
           self.build_rank_indicator = build_rank_indicator
           #
           # pdf_list - density of distribution (x, in ascending order, 1, 2, 3, ...)
           # cdf_list - accumulative of density (<=x, in ascending order, 1,2, 3, ...)
           # sf_list - accumulative of density (x>=, in descending order, 10, 9, 8, ...)
           #
           # It's too time comsuming to build rank table, here an indicator build_rank_indicator 
           # as a switch to run build_rank function
           if self.build_rank_indicator == True:
           #
           # Apporach to generate full list of combination and filter out duplicate items 
              #self.pdf_list, self.cdf_list, self.sf_list = self.build_rank(True)
           #
           # Approach to call recursive function
              #self.loop_idx_list = []
              #self.rank_list = []
              #self.pdf_list, self.cdf_list, self.sf_list = self.build_rank_recursive()
           #
           # Approach to call exec()  
              self.pdf_list, self.cdf_list, self.sf_list = self.build_rank_exec()

           else:
              self.pdf_list = []
              self.cdf_list = []
              self.sf_list = []
              
        else:
           print('Wilcoxon_Rank_Sum_Test __init__ failed')

    def calc_R1_R2(self):
        #
        # Calculate R of in data1

        # Only valid if lists in sample1 and sample2 are provided 
        if self.success != 2:
           return -1. -1, -1

        R1 = 0
        #
        # Combine two list data1 and data2
        # all_data format [data, from data1 or data2, occupied by data1 or data2]
        all_data = []
        for item in self.data1:
            all_data.append([item, 1, 0])
        for item in self.data2:
            all_data.append([item, 2, 0])
        all_data.sort()

        for item in self.data1:
            for i in range(len(all_data)):
                if item == all_data[i][0]:
                   if all_data[i][2] == 0:
                      all_data[i][2] = 1
        for item in self.data2:
            for i in range(len(all_data)):
                if item == all_data[i][0]:
                   if all_data[i][2] == 0:
                      all_data[i][2] = 2

        #
        # Supress the duplicate items, all_data is in ascending order

        if (len(all_data) == 0):
            return -1, -1, -1
        else:
            suppress_array = []
            previous_data = all_data[0][0]
            sum_rank = 0
            cn_rank = 0
            for i in range(len(all_data)):
                proc_data = all_data[i][0]
                if proc_data == previous_data:
                   #
                   # i starts from 0
                   sum_rank = sum_rank + i + 1
                   cn_rank = cn_rank + 1
                else:
                   suppress_array.append([previous_data, sum_rank, cn_rank])
                   previous_data = proc_data
                   sum_rank = i + 1
                   cn_rank = 1
            suppress_array.append([previous_data, sum_rank, cn_rank])
      
            #
            # Calculate R1
            R1 = 0
            for item in self.data1:
                for proc_data, sum_rank, cn_rank in suppress_array:
                    if item == proc_data:
                       R1 = R1 + sum_rank / cn_rank
                       break                
            #
            # Calculate R2
            R2 = 0
            for item in self.data2:
                for proc_data, sum_rank, cn_rank in suppress_array:
                    if item == proc_data:
                       R2 = R2 + sum_rank / cn_rank
                       break                  
            #
            # Calculate ti
            ti = []
            for proc_data, sum_rank, cn_rank in suppress_array:
                if cn_rank > 1:
                   ti.append(cn_rank)

            return R1, R2, ti

    def build_rank(self, de_duplication):
        #
        # Common module to build standard ranks
        #    Parameter: de_duplication - True, supress duplicated combination, like, [1,1,2], [2,2,4] etc
        #                              - False, do not supress
        #
        n1_idx = []
        n1_idx = self.min_list
        result_list = []

        running = True
        
        #
        # Build rank list with some kind of duplicated data, like [1,2,3] and [3,2,1] are created in different order
        #
        while (running):
            
            tmp_list = []
            for item in n1_idx:
                tmp_list.append(item)
            
            #
            # Suppress duplicated data, i.e., [1,1,2], [3,4,4]
            if de_duplication == True:
               d_ind = self.detect_duplication(tmp_list)
               if d_ind == False:
                  result_list.append(tmp_list)
            else:
                result_list.append(tmp_list)
            #
            # Get next "number"
            running, n1_idx = self.add_one(n1_idx)

        #
        # Suppress duplicated data, like [1,2,3] and [3,2,1] are the same but in different order
        tmp_sort_filter_list = []
        tmp_sort_filter_list = self.sort_filter(result_list)

        return self.calc_pdf_cdf_sf(tmp_sort_filter_list)

    def calc_pdf_cdf_sf(self, tmp_sort_filter_list):

        #
        # Sum up of each combination, e.g. [1,2,3] ranks 6 = 1 + 2 + 3
        total_num_of_result = len(tmp_sort_filter_list)
        tmp_rank_list = []

        for item in tmp_sort_filter_list:
            tmp_rank_list.append(sum(item))

        #
        # Find unique rank
        unique_rank_list = []

        for item in tmp_rank_list:
            if item not in unique_rank_list:
               unique_rank_list.append(item)
 
        unique_rank_list.sort()

        #
        # Calculate pdf for each rank, in ascending order
        rank_list_p_equ = []
        for item in unique_rank_list:
            cn = tmp_rank_list.count(item)
            rank_list_p_equ.append([item, cn, cn / total_num_of_result])
        
        #
        # Calcualte cdf for each rank, in ascending order
        rank_list_p_less_equ = []

        for i in range(len(rank_list_p_equ)):
            tmp_c = 0
            tmp_i = rank_list_p_equ[i][0]
            for j in range(0, i + 1, 1):
                tmp_c = tmp_c + rank_list_p_equ[j][1]
            rank_list_p_less_equ.append([tmp_i, tmp_c, tmp_c / total_num_of_result])

        #
        # Calculate ppf for each rank, in descending order
        rank_list_p_greater_equ = []
        for i in range(len(rank_list_p_equ) - 1, -1, -1):
            tmp_c = 0
            tmp_i = rank_list_p_equ[i][0]
            for j in range(len(rank_list_p_equ) - 1, i - 1, -1):
                tmp_c = tmp_c + rank_list_p_equ[j][1]           
            rank_list_p_greater_equ.append([rank_list_p_equ[i][0], tmp_c, tmp_c / total_num_of_result])

        return rank_list_p_equ, rank_list_p_less_equ, rank_list_p_greater_equ


    def add_one(self, num_item):
        #
        # Get next "number" of input num_item

        #
        # if input number reaches the max_list, cannot find next number
        if num_item >= self.max_list:
           return False, self.max_list

        return_item = []
        return_item = num_item
        indicator = True
        
        for i in range(self.n1 - 1, -1, -1):
            tmp_idx = return_item[i]
            #
            # if the curent processing number does not reach the max_list, add "1" to current processing sub-item
            if tmp_idx < self.max_num:
               #
               # Get next "number"
               ind, tmp_idx = self.find_next(tmp_idx)
               if ind == True:
                  return_item[i] = tmp_idx
                  break
               else:
                  return False, self.max_num
            else:
            #
            # if the current process sub-item reaches max_list, set it to min_num and process the upper sub-item (add 1)
               if i == 0:
                  indicator = False
                  break
               else: 
                  tmp_idx = self.min_num
                  return_item[i] = tmp_idx
        return indicator, return_item
    
    def find_next(self, num_item):
        #
        # Get next "Number" upon n1_n2_list

        hit = False
        for i in self.n1_n2_list:
            if hit == True:
               return True, i

            else:
               if num_item == i:
                  hit = True

        return False, self.max_num

    def detect_duplication(self, num_item):
        #
        # filter out duplicate item, e.g. [1,1,2], [3,4,4]
        indicator = False
        for i in range(len(num_item) - 1):
            for j in range(i + 1, len(num_item), 1):
                if (num_item[i] == num_item[j]):
                   indicator = True
                   break
        return indicator

    def sort_filter(self, num_list):
        #
        # Suppress duplicated data, like [1,2,3] and [3,2,1] are the same but in different order
        tmp_list = []
        tmp_list = num_list
        del_idx = []
        return_list = []
        for i in range(len(tmp_list)):
            tmp_item = tmp_list[i]
            tmp_item.sort()
            tmp_list[i] = tmp_item
            cn = tmp_list.count(tmp_item)
            if cn > 1:
               del_idx.append(i)

        for i in range(len(tmp_list)):
           if i not in del_idx:
              return_list.append(tmp_list[i])    
        
        return return_list

    def build_rank_recursive(self):
        #
        # buind rank array for Rank Sum Test in a much quicker way
        #  
        for i in range(self.n1):
            #
            # format : processing index, start index, end index
            #
            self.loop_idx_list.append([i, i, self.n2 + i + 1])
   
        self.loop(0)

        return self.calc_pdf_cdf_sf(self.rank_list)

    def loop(self, lvl):
        #
        # Perform multi-level loop in this recursive function
        # 

        tmp_lvl = lvl - 1
        if tmp_lvl >= 0:
           tmp_start_num = self.loop_idx_list[tmp_lvl][0] + 1
        else:
           tmp_start_num = self.loop_idx_list[0][0]

        tmp_end_num = self.loop_idx_list[lvl][2]

        if (lvl == (self.n1 - 1)):
          for i in range(tmp_start_num, tmp_end_num):
              tmp_item = []
              for j in range(lvl):
                  tmp_idx = self.loop_idx_list[j][0]
                  tmp_item.append(self.n1_n2_list[tmp_idx])
              tmp_item.append(self.n1_n2_list[i])
              self.rank_list.append(tmp_item)
        else:   
           for i in range(tmp_start_num, tmp_end_num):
               self.loop(lvl + 1)
               self.loop_idx_list[lvl][0] += 1

           tmp_end_idx = self.loop_idx_list[lvl][2]
           reset_idx = self.loop_idx_list[lvl][1] + 1
           if reset_idx > tmp_end_num:
              reset_idx = tmp_end_num
           self.loop_idx_list[lvl][0] = reset_idx
           self.loop_idx_list[lvl][1] = reset_idx

           next_lvl = lvl + 1
           last_lvl = len(self.loop_idx_list) - 1
           while (next_lvl < last_lvl):
               prev_idx = next_lvl - 1
               self.loop_idx_list[next_lvl][0] = self.loop_idx_list[prev_idx][0] + 1
               self.loop_idx_list[next_lvl][1] = self.loop_idx_list[prev_idx][1] + 1
               next_lvl += 1

    def build_rank_exec(self):
        #
        # buind rank array for Rank Sum Test in a much quicker way
        #  
        leading_space = ''
        rank_dict = {}
        pgm_str = 'for i_1 in range(0, self.n2 + 1): \r'
        for i in range(1, self.n1):
            leading_space = leading_space + ' '
            pgm_str = pgm_str + leading_space + 'for i_' + str(i + 1) + ' in range(i_' + str(i) + ' + 1, self.n2 + ' + str(i) + ' + 1): \r'
        
        leading_space = leading_space + ' '
        pgm_str = pgm_str + leading_space + 'sub_rank_sum = self.n1_n2_list[i_1]'
        for i in range(1, self.n1):
            pgm_str = pgm_str + ' + self.n1_n2_list[i_' + str(i + 1) + ']'

        pgm_str = pgm_str + '\r'
        pgm_str = pgm_str + leading_space + 'if sub_rank_sum in rank_dict.keys(): \r'
        pgm_str = pgm_str + leading_space + '   rank_dict[sub_rank_sum] += 1 \r'
        pgm_str = pgm_str + leading_space + 'else: \r'
        pgm_str = pgm_str + leading_space + '   rank_dict[sub_rank_sum] = 1 \r'

        exec(pgm_str)
        return self.calc_pdf_cdf_sf_from_dict(rank_dict)

    def calc_pdf_cdf_sf_from_dict(self, rank_dict):

        #
        # Sum up of each combination, e.g. [1,2,3] ranks 6 = 1 + 2 + 3
        total_num_of_result = 0
        for v in rank_dict.values():
            total_num_of_result += v
        #
        # Calculate pdf for each rank, in ascending order
        rank_list_p_equ = []
        for k in rank_dict.keys():
            v = rank_dict[k]
            rank_list_p_equ.append([k, v, v / total_num_of_result])
        
        rank_list_p_equ.sort()
        
        #
        # Calcualte cdf for each rank, in ascending order
        rank_list_p_less_equ = []
        for k in rank_dict.keys():
            tmp_c = 0
            for k_1 in rank_dict.keys():
                if k >= k_1:                    
                   tmp_c += rank_dict[k_1]
            rank_list_p_less_equ.append([k, tmp_c, tmp_c / total_num_of_result])
        rank_list_p_less_equ.sort()

        #
        # Calculate ppf for each rank, in descending order
        rank_list_p_greater_equ = []
        for k in rank_dict.keys():
            tmp_c = 0
            for k_1 in rank_dict.keys():
                if k <= k_1:
                   tmp_c += rank_dict[k_1]
            rank_list_p_greater_equ.append([k, tmp_c, tmp_c / total_num_of_result])
        rank_list_p_greater_equ.sort(reverse=True)
        return rank_list_p_equ, rank_list_p_less_equ, rank_list_p_greater_equ

        
