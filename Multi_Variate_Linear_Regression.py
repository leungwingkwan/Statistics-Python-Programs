import matplotlib.pyplot as plt
import numpy as np

class multi_variate_linear_regression():
      def __init__(self, data):
          #
          # data format:
          # [[x1, x2, ..., xn], y]
          #
          M_X = []
          M_Y = []
          for i in range(len(data)):
              list_x = [1]
              for item in data[i][0]:
                  list_x.append(item)
              M_X.append(list_x)
              M_Y.append([data[i][1]])
          self.X = np.array(M_X)
          self.Y = np.array(M_Y)

      def estimate_coeffient(self):
          m_tmp = np.dot(self.X.transpose(), self.X)
          m_tmp = np.linalg.inv(m_tmp)
          m_tmp = np.dot(m_tmp, self.X.transpose())
          self.B = np.dot(m_tmp, self.Y)
      
      def draw(self, x_index = 0, draw_line=True, draw_estimation_line=False):
          x = []
          y = []
          for i in range(len(self.Y)):
              x.append(self.X[i][x_index + 1])
              y.append(self.Y[i])
          plt.plot(x, y, "ro")
          plt.show()
