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
def rsmat(arbmat):
    """ Convert an arbitrary matrix to a simplest matrix """
    arbmat = arbmat.astype(float)
    row_number, column_number = arbmat.shape
    if row_number == 1:
        if arbmat[0, 0] != 0:
            return (arbmat/arbmat[0, 0])
        else:
            return arbmat
    else:
        rc_number = min(row_number, column_number)
        anarbmat = arbmat.copy()
        r = 0
        for n in range(rc_number):
            s_row = -1
            for i in arbmat[r:row_number, n]:
                s_row += 1
                if abs(i) > 1e-10:
                    anarbmat[r, :] = arbmat[s_row+r, :]
                    for j in range(r, row_number):
                        if j < s_row+r:
                            anarbmat[j+1, :] = arbmat[j, :]
                    arbmat = anarbmat.copy()
            if abs(anarbmat[r, n]) > 1e-10:
                anarbmat[r, :] = anarbmat[r, :] / anarbmat[r, n]
                for i in range(row_number):
                    if i != r:
                        anarbmat[i, :] -= \
                        anarbmat[i, n]*anarbmat[r, :]
            arbmat = anarbmat.copy()
            if abs(arbmat[r, n]) < 1e-10:
                r = r
            else:
                r = r + 1
        for m in range(column_number):
            if abs(arbmat[-1, m]) > 1e-10:
                arbmat[-1, :] = arbmat[-1, :]/arbmat[-1, m]
                for i in range(row_number-1):
                    arbmat[i, :] -= \
                    arbmat[i, m]*arbmat[-1, :]
                break
            
        return arbmat

####################
# Step 1: 遍历性
####################
p = np.array(data_1)
print('=======================Step 1=======================')
m, p_m = determine_m(p)
print('m =', m)
print('p ^', str(m), '=')
print(p_m)

###################
# Step 2:
###################
print('=======================Step 2=======================')
p_rank = np.linalg.matrix_rank(p)
#
# use first 4 lines instead
#
p_t = np.transpose(p)

p_1 = np.eye(len(p))
p_x = p_t - p_1
p_x_a = p_x[0:4]
p_x_a = np.vstack((p_x_a, np.ones(len(p))))
print('Correct Answer=====================')
print('p_x_a = ')
print(p_x_a)

b = [[0], [0], [0], [0], [1]]
x = np.linalg.solve(p_x_a, b)
print('b =')
print(b)
print('Correct Answer: x =')
print(x)

print('Inorrect Answer=====================')
print('p_x =')
print(p_x)
b1 = [[0], [0], [0], [0], [0]]
print('b1 =')
print(b1)
x1 = np.linalg.solve(p_x, b1)
print('inorrect Answer: x1 =')
print(x1)