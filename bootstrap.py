import random
import numpy as np
import copy

class bootstrap():
  def __init__(self, data, func_theta = None):
      #
      # data - input raw data
      # func_theta - function of estimate parameter thetha
      #
      self.data = data
      self.n = len(data)
      self.bootstrap_sample = None
      if func_theta == None:
         self.theta = None
      else:
         self.theta = func_theta(data)

  
  def sampling(self, n, B, func_sampling = None, func_sampling_parm = None):
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
        if func_sampling == None:
           self.bootstrap_sample.append(sample_list)
        else:
           processed_list = func_sampling(sample_list, func_sampling_parm)  
           #
           # pack return value into list type
           if (type(processed_list) != tuple) and (type(processed_list) != list):
              processed_list = [processed_list]
           if self.bootstrap_sample == []:
              for i in range(len(processed_list)):
                  self.bootstrap_sample.append([])
                  self.bootstrap_sample[i].append(processed_list[i])
           else:
              for i in range(len(processed_list)):
                  self.bootstrap_sample[i].append(processed_list[i])
 
  def sample_standard_deviation(self, sample=None):
      if sample == None:
         return None
      else:
         return (np.var(sample, ddof = 1))** 0.5
      
  def MSE(self, sample = None, sample_mean = None):
      # error of mean squares
      if sample == None:
         return None
      if sample_mean == None:
         return None
         
      return np.square(np.subtract(sample, sample_mean)).mean()
  
  def bias(self, sample = None, estimation = None):
      if sample == None:
         return None
      if estimation == None:
         return None
      
      return np.subtract(sample, estimation).mean()
  
  def confidence_interval(self, alpha_left, alpha_right, input_sample=None):
      if input_sample == None:
         sample = copy.deepcopy(self.bootstrap_sample)
      else:
         sample = copy.deepcopy(input_sample)
         
      B = len(sample)
      k1 = max(int(B * alpha_left), 0)
      k2 = int(B * alpha_right) - 1
     
      sample.sort()
      left_margin = sample[k1]
      right_margin = sample[k2]
      del sample
      
      return left_margin, right_margin
   
  def trimmed_mean(self, sample, kw):
      B = len(sample)
      tmp = copy.deepcopy(sample)
      tmp.sort()
      k1 = max(int(B * kw['left_trim_pct']), 0)
      k2 = min(int(B * kw['right_trim_pct']), B)
      tmp_trimmed_mean = np.mean(tmp[k1:k2])
      del tmp
      return tmp_trimmed_mean
       
       
       
       
       
       
       
       
       
       
       
       
   