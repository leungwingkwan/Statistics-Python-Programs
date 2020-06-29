import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t
import math


class univariate_linear_regression():
      def __init__(self, data):
          #
          # data format:
          # [[x1, y1], [x2, y2], ..., [xn, yn]]
          #
          self.x = []
          self.y = []
          self.n = len(data)
          for i in range(len(data)):
              self.x.append(data[i][0])
              self.y.append(data[i][1])
          #
          # coeffienct vairable a & b, where
          # y = a + b * x1
          #
          self.a = None
          self.b = None
          #
          # intermedia statistic result
          #
          self.mean_x = None
          self.mean_y = None
          self.S_xx = None
          self.S_xy = None
          self.S_yy = None
          #
          # variance of espilon
          #
          self.sigma_sqr_of_epsilon = None
          #
          # test assumption H0
          #
          self.H0_valid = None
          self.H0_test_value = None
          self.H0_t_value = None
          #
          # confidence interval
          #
          self.lower_bound = None
          self.upper_bound = None
      def draw(self):
          plt.plot(self.x, self.y, "ro")
          plt.plot(self.x, self.y)
          plt.show()
    
      def estimate_coeffient(self):
          #
          # estimate coeffienct a & b, where
          # y = a + b * x1
          #
          x = np.array(self.x)
          y = np.array(self.y)
          self.mean_x = np.mean(self.x)
          self.mean_y = np.mean(self.y)
          self.S_xx = sum((x - self.mean_x)** 2)
          self.S_yy = sum((y - self.mean_y)** 2)
          self.S_xy = sum((x - self.mean_x)*(y - self.mean_y))
          
          self.b = self.S_xy / self.S_xx
          self.a = self.mean_y - self.b * self.mean_x

      def var_of_epsilon(self):
          Qe = self.S_yy - self.b * self.S_xy
          self.sigma_sqr_of_epsilon = Qe / (self.n - 2)
      
      def test_b_is_zero(self, alpha):
          self.H0_test_value = self.b * math.sqrt(self.S_xx) / math.sqrt(self.sigma_sqr_of_epsilon)
          self.H0_t_value = t.isf(alpha / 2, self.n - 2)
          if self.H0_test_value >= self.H0_t_value:
             self.H0_valid = False
          else:
             self.H0_valid = True
      
      def confidence_interval_of_b(self,alpha):
          self.upper_bound = self.b + t.isf(alpha / 2, self.n - 2) * math.sqrt(self.sigma_sqr_of_epsilon) / math.sqrt(self.S_xx)
          self.lower_bound = self.b - t.isf(alpha / 2, self.n - 2) * math.sqrt(self.sigma_sqr_of_epsilon) / math.sqrt(self.S_xx)
          
      def confidence_interval_of_mu_x(self, x0, alpha):
          y0 = self.a + self.b * x0
          t_value = t.isf(alpha / 2, self.n - 2)
          sigma = math.sqrt(self.sigma_sqr_of_epsilon)
          others = math.sqrt((1 / self.n) + (x0 - self.mean_x) ** 2 / self.S_xx)
          self.upper_bound = y0 + t_value * sigma * others
          self.lower_bound = y0 - t_value * sigma * others

      def prediction_interval_of_Y(self, x0, alpha):
          y0 = self.a + self.b * x0
          t_value = t.isf(alpha / 2, self.n - 2)
          sigma = math.sqrt(self.sigma_sqr_of_epsilon)
          others = math.sqrt(1 + (1 / self.n) + (x0 - self.mean_x) ** 2 / self.S_xx)
          self.upper_bound = y0 + t_value * sigma * others
          self.lower_bound = y0 - t_value * sigma * others
         
      
