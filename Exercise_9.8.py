import Univariate_Linear_Regression as ULR

data = [[300, 40], [400, 50], [500, 55], [600, 60], [700, 67], [800, 70]]

ulr = ULR.univariate_linear_regression(data)
ulr.draw()

ulr.estimate_coeffient()
print('y = ', str(ulr.a), '+', str(ulr.b) + ' * x')



