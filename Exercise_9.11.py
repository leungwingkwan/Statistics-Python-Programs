import Univariate_Linear_Regression as ULR

data = [[20.0, 31.4], [16.0, 22.0], [19.8, 34.1], [18.4, 29.1], [17.1, 27.0],\
        [15.5, 24.0], [14.7, 20.9], [17.1, 27.8], [15.4, 20.8], [16.2, 28.5],\
        [15.0, 26.4], [17.2, 28.1], [16.0, 27.0], [17.0, 28.6], [14.4, 24.6]]
        
ulr = ULR.univariate_linear_regression(data)
ulr.draw(True, False)

ulr.estimate_coeffient()
print('y = ', str(ulr.a), '+', str(ulr.b) + ' * x')
ulr.draw(False, True)


ulr.prediction_interval_of_Y(14, 0.05)
print('prediction interval of Y is [', ulr.lower_bound, ',', ulr.upper_bound, ']')