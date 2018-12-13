# -*- conding:utf-8 -*-
class MyIterable:
   def __init__(self,data):
      self.date=data
   def __iter__(self):
      return MyIterator(self.date)
class MyIterator:
   def __init__(self,data):
      self.data=data
      self.index = len(data)
   def __iter__(self):
      pass
   def __next__(self):
      if self.index>0:
         self.index -= 1
         return self.data[self.index]
      else:
         raise StopIteration

li = (5,2,4,8,1)
m=MyIterable(li)
for i in m:
   print(i)
print(m)
from collections.abc import Iterable,Iterator
print(issubclass(tuple,Iterable))
print(issubclass(tuple,Iterator))
print(issubclass(Iterator,Iterable))
print(isinstance(Iterator,Iterable))