import numpy as np

data_1 = [[0,    1,   0,   0,   0],
         [1/3, 1/3, 1/3,   0,   0],
         [0,   1/3, 1/3, 1/3,   0],
         [0,     0, 1/3, 1/3, 1/3],
         [0,     0,   0,   1,   0]]

def determine_m(P):
    max_loop = 1000
    found_ind = False
    
    loop_i = 1
    tmp_p = np.diag(np.ones(len(P)))
    while((found_ind == False) and (loop_i <= max_loop)):
         tmp_p = np.matmul(tmp_p, P)
  
         zero_found = False
         
         for line in tmp_p:
             for item in line:
                 if item == 0:
                    zero_found = True
                    break
             if zero_found == True:
                break
         
         if zero_found == False:
            found_ind = True
            break
         else:
            loop_i +=1
     
    if found_ind == True:
       return loop_i, tmp_p
    else:
       return None, None

####################
# Step 1: 遍历性
####################
p = np.array(data_1)
print('Data 1=========================')
m, p_m = determine_m(p)
print('m =', m)
print('p ^', str(m), '=', p_m)

###################
# Step 2:
###################
p_rank = np.linalg.matrix_rank(p)
print('p rank = ', p_rank)
print('p = ')
print(p)
#
# use first 4 lines instead
#
p_t = np.transpose(p)
print('p_t = ')
print(p_t)
p_1 = np.eye(len(p))
print('p_1 = ')
print(p_1)
p_x = p_t - p_1
print('p_x = ')
print(p_x)
p_x_a = p_x[0:p_rank - 1]
p_x_a = np.vstack((p_x_a, np.ones(len(p))))
print('p_x_a = ')
print(p_x_a)

b = [[0], [0], [0], [0], [1]]
print('b = ')
print(b)
x = np.linalg.solve(p_x_a, b)
print('x =')
print(x)
