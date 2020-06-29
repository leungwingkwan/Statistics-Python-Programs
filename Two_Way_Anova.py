import numpy as np
from scipy.stats import f
# Two-Way Anova

def quadratic_sum_resolution(input_data):
    #
    # input_data format:
    # x[factor A][factor B] = [test 1,2,3,...]]
    #
    # r is number of factor A
    r = len(input_data)
    # s is number of factor BaseException
    s = len(input_data[0])
    # t is number of sample under factor A and B
    t = []
    n = 0
    sum_x = 0
    mean_x_ab = []
    for i in range(r):
        tmp_t = []
        tmp_mean = []
        for j in range(s):
            tmp_t.append(len(input_data[i][j]))
            n += len(input_data[i][j])
            sum_x += sum(input_data[i][j])
            tmp_mean.append(np.mean(input_data[i][j]))
        mean_x_ab.append(tmp_mean)
        t.append(tmp_t)

    # Calculate mean_x
    mean_x = sum_x / n
    # Calculate ST
    ST = 0
    for i in range(r):
        for j in range(s):
            for k in range(t[i][j]):
                ST += (input_data[i][j][k] - mean_x)** 2

    # Calculate SE (or use formula ST = SA + SB + SAXB + SE)
    SE = 0
    for i in range(r):
        for j in range(s):
            for k in range(t[i][j]):
                SE += (input_data[i][j][k] - mean_x_ab[i][j])** 2           
    # Calucate SA for factor A
    mean_x_a = []
    SA = 0
    t_r_a = []
    for i in range(r):
        cn_x_a = 0
        sum_x_a = 0
        for j in range(s):
            for k in range(t[i][j]):
                cn_x_a += 1
                sum_x_a += input_data[i][j][k]
        t_r_a.append(cn_x_a)
        mean_x_a.append(sum_x_a / cn_x_a)
    for i in range(r):
        SA = SA + t_r_a[i] * (mean_x_a[i] - mean_x) ** 2

    # Calucate SB for factor B
    mean_x_b = []
    SB = 0
    t_s_b = []
    for j in range(s):
        cn_x_b = 0
        sum_x_b = 0
        for i in range(r):
            for k in range(t[i][j]):
                cn_x_b += 1
                sum_x_b += input_data[i][j][k]
        t_s_b.append(cn_x_b)
        mean_x_b.append(sum_x_b / cn_x_b)
    for j in range(s):
        SB = SB + t_s_b[j] * (mean_x_b[j] - mean_x) ** 2
    
    #Calculate SAXB
    SAXB = 0
    for i in range(r):
        for j in range(s):
            SAXB = SAXB + t[i][j] * (mean_x_ab[i][j] -  mean_x_a[i] - mean_x_b[j] + mean_x) ** 2
    
    if t[0][0] == 1:
    #
    # single test
      SE = SAXB
      SAXB = None
      
    return ST, SA, SB, SAXB, SE, r, s, t[0][0], n

def region_of_rejection(SA, SB, SAXB, SE, r, s, t, alpha):

    if t > 1:
    #
    # repeated test
    #
      test_FA = (SA / (r - 1)) / (SE / (r*s*(t - 1)))
      F_A = f.isf(alpha, r - 1, r * s * (t - 1))
   
      test_FB = (SB / (s - 1)) / (SE / (r*s*(t - 1)))
      F_B = f.isf(alpha, r - 1, r * s * (t - 1))
    
      test_FAXB = (SAXB / ((r - 1)*(s - 1))) / (SE / (r*s*(t - 1)))
      F_AXB = f.isf(alpha, (r - 1)*(s - 1) , r * s * (t - 1))
    elif t == 1:
    #
    # single test
    #
      test_FA = (SA / (r - 1))/ ((SE / ((r - 1)*(s - 1))))
      F_A = f.isf(alpha, r - 1, (r - 1)*(s - 1))

      test_FB = (SB / (s - 1))/ ((SE / ((r - 1)*(s - 1))))
      F_B = f.isf(alpha, s - 1, (r - 1)*(s - 1))    
      
      test_FAXB = None
      F_AXB = None
    else:
      test_FA = None
      F_A = None
      test_FB = None
      F_B = None
      test_FAXB = None
      F_AXB = None
      
    return test_FA, F_A, determine_rejection(test_FA, F_A), \
           test_FB, F_B, determine_rejection(test_FB, F_B), \
           test_FAXB, F_AXB, determine_rejection(test_FAXB, F_AXB)

def determine_rejection(test_value, F_value):
    if ((test_value == None) or (F_value == None)):
       reject_ind = None
    elif test_value >= F_value:
       reject_ind = True
    else:
       reject_ind = False
    return reject_ind
        
            