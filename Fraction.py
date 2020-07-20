
class fraction():
      def __init__(self, numerator, denominator):
       
          if denominator != int(denominator):
             self.numerator = None
             self.denominator = None
          else:
              if numerator == int(numerator):
                 self.numerator = int(numerator)
                 self.denominator = int(denominator)
              else:
                 n, d = self.convert_to_type_int(numerator)
                 tmp_d = d * denominator
                 g = self.gcd(n, tmp_d)
                 self.numerator = int(n / g)
                 self.denominator = int(tmp_d / g)
         
         
      def convert_to_type_int(self, x):
          base = 10
          max_loop = 100
          
          tmp_x = x
          loop_i = 1
          factor = 1
          while ((tmp_x != int(tmp_x)) and (loop_i <= max_loop)): 
                factor *= base
                tmp_x = x * factor
                loop_i += 1
      
          if (loop_i > max_loop):
              return None, None
          
          g = self.gcd(x * factor, factor)
          
          return int(tmp_x / g), int(factor / g)
      
      def gcd(self, x, y):
          g = y
          while (x>0):
                g = x
                x = y % x
                y = g
          return g
