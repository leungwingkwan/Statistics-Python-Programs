import random

class bootstrap():
  def __init__(self, data, func_theta):
      #
      # data - input raw data
      # func_theta - function of estimate parameter thetha
      #
      self.data = data
      self.n = len(data)
      self.bootstrap_sample = []
      self.theta = func_theta(data)
  
  def sampling(self, n, B):
      #
      # n - number of item in a sample_list
      # B - number of samples
      #
      
      self.bootstrap_sample = []
      
      for i in range(B):
        sample_list = []
        for j in range(n):
            rnd = int(random.random() * self.n)
            sample_list.append(self.data[rnd])
        self.bootstrap_sample.append(sample_list)