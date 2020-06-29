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
          self.n = len(data)
          #for i in range(len(data)):
          #    self.x.append(data[i][0])
          #    self.y.append(data[i][1])
          #
          # coeffienct vairable a & b, where
          # y = a + b * x1
          #
          self.a = None
          self.b = None
          #
          # intermedia statistic result
          #
          data.sort()
          data_array = np.array(data)
          self.x = np.hsplit(data_array, [1])[0].reshape(-1)
          self.y = np.hsplit(data_array, [1])[1].reshape(-1)
          del data_array
          self.mean_x = np.mean(self.x)
          self.mean_y = np.mean(self.y)
          self.S_xx = sum((self.x - self.mean_x)** 2)
          self.S_yy = sum((self.y - self.mean_y)** 2)
          self.S_xy = sum((self.x - self.mean_x)*(self.y - self.mean_y))
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
          
      def draw(self, draw_line=True, draw_estimation_line=False):
          plt.plot(self.x, self.y, "ro")
          if draw_line:
             plt.plot(self.x, self.y)
          if draw_estimation_line:
             if ((self.a != None) and (self.b != None)):
                min_x = min(self.x)
                max_x = max(self.x)
                tmp_x = []
                tmp_y = []
                num_of_x = 100
                interval_of_x = (max_x - min_x) / num_of_x
                for i in range(num_of_x):
                    x_i = min_x + interval_of_x * i
                    tmp_x.append(x_i)
                    tmp_y.append(self.a + self.b * x_i)
                plt.plot(tmp_x, tmp_y)
          plt.show()
    
      def estimate_coeffient(self):
          #
          # estimate coeffienct a & b, where
          # y = a + b * x1
          #

          self.b = self.S_xy / self.S_xx
          self.a = self.mean_y - self.b * self.mean_x

      def var_of_epsilon(self):
          Qe = self.S_yy - self.b * self.S_xy
          self.sigma_sqr_of_epsilon = Qe / (self.n - 2)
      
      def test_b_is_zero(self, alpha):
          if self.sigma_sqr_of_epsilon == None:
             self.var_of_epsilon()
          self.H0_test_value = abs(self.b * math.sqrt(self.S_xx) / math.sqrt(self.sigma_sqr_of_epsilon))
          self.H0_t_value = t.isf(alpha / 2, self.n - 2)
          if self.H0_test_value >= self.H0_t_value:
             self.H0_valid = False
          else:
             self.H0_valid = True
      
      def confidence_interval_of_b(self,alpha):
          if self.sigma_sqr_of_epsilon == None:
             self.var_of_epsilon()
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
          if self.sigma_sqr_of_epsilon == None:
             self.var_of_epsilon()
          sigma = math.sqrt(self.sigma_sqr_of_epsilon)
          others = math.sqrt(1 + (1 / self.n) + (x0 - self.mean_x) ** 2 / self.S_xx)
          self.upper_bound = y0 + t_value * sigma * others
          self.lower_bound = y0 - t_value * sigma * others
         
      def projection(self, x):
          if ((self.a == None) or (self.b == None)):
             return None
          else:
             return self.a + self.b * x
              
