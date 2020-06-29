import Univariate_Linear_Regression as ULR

data = [[0.10, 15], [0.30, 18], [0.40, 19], [0.55, 21],\
        [0.70, 22.6], [0.80, 23.8], [0.95, 26]]
ulr = ULR.univariate_linear_regression(data)
ulr.draw()

ulr.estimate_coeffient()
print('y = ', str(ulr.a), '+', str(ulr.b) + ' * x')

ulr.var_of_epsilon()
print('variance of epsilon = ', ulr.sigma_sqr_of_epsilon)

ulr.test_b_is_zero(0.05)
print('H0_test_value =', ulr.H0_test_value)
print('H0_t_value =', ulr.H0_t_value)
print('H0_valid =', ulr.H0_valid)

ulr.confidence_interval_of_b(0.05)
print('confidence interval of b is [', ulr.lower_bound, ',', ulr.upper_bound, ']')

ulr.confidence_interval_of_mu_x(0.5, 0.05)
print('confidence interval of mu(x) is [', ulr.lower_bound, ',', ulr.upper_bound, ']')

ulr.prediction_interval_of_Y(0.5, 0.05)
print('prediction interval of Y is [', ulr.lower_bound, ',', ulr.upper_bound, ']')