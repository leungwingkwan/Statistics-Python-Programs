import Univariate_Linear_Regression as ULR

data = [[1952, 29.3], [1956, 28.8], [1960, 28.5], [1964, 28.4], [1968, 29.4],\
        [1972, 27.6], [1976, 27.7], [1980, 27.7], [1984, 27.8], [1988, 27.4],\
        [1992, 27.8], [1996, 27.1], [2000, 27.3], [2004, 27.1]]
###################################################################################
# Qquestion 1
###################################################################################
print('=================Question 1=================')
print('=================converted data=================')
converted_data = []
for item in data:
    x = (item[0] - 1952) / 4 + 1
    y = item[1] - 20
    converted_data.append([x, y])

ulr = ULR.univariate_linear_regression(converted_data)
ulr.estimate_coeffient()
print('y = ' + str(ulr.a) + '+', str(ulr.b), '* x')
print('=================original data=================')
ulr_year = ULR.univariate_linear_regression(data)
ulr_year.estimate_coeffient()
print('y = ' + str(ulr_year.a) + '+', str(ulr_year.b), '* x')
###################################################################################
# Qquestion 2
###################################################################################
print('=================Question 2=================')
ulr.test_b_is_zero(0.05)
print('H0_test_value =', ulr.H0_test_value)
print('H0_t_value =', ulr.H0_t_value)
print('H0_valid =', ulr.H0_valid)
###################################################################################
# Qquestion 3
###################################################################################
print('=================Question 3=================')
print('=================converted data=================')
x0 = (2008 - 1952) /4 + 1
print('projection is ', str(ulr.projection(x0) + 20))
print('=================original data=================')
x0 = 2008
print('projection is ', str(ulr_year.projection(x0)))