import Univariate_Linear_Regression as ULR

data = [[9.00, 6.50], [8.50, 6.25], [9.25, 7.25], [9.75, 7.00], [9.00, 6.75],\
        [10.00, 7.00], [9.50, 6.50], [9.00, 7.00], [9.25, 7.00], [9.50, 7.00],\
        [9.25, 7.00],  [10.00, 7.50], [10.00, 7.25], [9.75, 7.25], [9.50, 7.25]]
        
ulr = ULR.univariate_linear_regression(data)
ulr.draw(True, False)

ulr.estimate_coeffient()
print('y = ', str(ulr.a), '+', str(ulr.b) + ' * x')
ulr.draw(False, True)


ulr.confidence_interval_of_b(0.05)
print('confidence interval of b is [', ulr.lower_bound, ',', ulr.upper_bound, ']')