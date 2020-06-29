import Univariate_Linear_Regression as ULR

data = [[17.1, 16.7], [10.5, 10.4], [13.8, 13.5], [15.7, 15.7], [11.9, 11.6],\
        [10.4, 10.2], [15.0, 14.5], [16.0, 15.8], [17.8, 17.6], [15.8, 15.2],\
        [15.1, 14.8], [12.1, 11.9], [18.4, 18.3], [17.1, 16.7], [16.7, 16.6],\
        [16.5, 15.9], [15.1, 15.1], [15.1, 14.5]]
ulr = ULR.univariate_linear_regression(data)
ulr.draw(False, False)

ulr.estimate_coeffient()
print('y = ', str(ulr.a), '+', str(ulr.b) + ' * x')
ulr.draw(False, True)


ulr.prediction_interval_of_Y(14, 0.05)
print('prediction interval of Y is [', ulr.lower_bound, ',', ulr.upper_bound, ']')