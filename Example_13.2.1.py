import numpy as np
import Fraction as f

def print_array(a):

    for line in a:
        line_str = ''
        for item in line:
            tmp = f.fraction(item, 1)
            line_str = line_str + str(tmp.numerator) + '/' + str(tmp.denominator) + ','
        print('[' + line_str[:-1] + ']')       

data = [[3/4, 1/4, 0],
        [1/4, 1/2, 1/4],
        [0, 3/4, 1/4]]
        
P = np.array(data)
print('P = ')
print_array(P)

P_2 = np.matmul(P, P)
print('P_2 = ')
print_array(P_2)