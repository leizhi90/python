# -*- conding:utf-8 -*-
from datetime import datetime
def formart_1(format):
   def inner_1(func):
      def inner(*args,**kwargs):
         print(datetime.now().strftime(format))
         r=func(*args,**kwargs)
         return r
      return inner
   return inner_1
@formart_1('%Y-%m-%d')
def f(name,age):
   print(name,age)
f('lz',66)



