# -*- conding:utf-8 -*-
# 可迭代对象 iterable
#实现了只要实现了Iterable类中的 __iter__方法
from collections.abc import Iterable,Iterator
print(issubclass(list,Iterable))
print(issubclass(tuple,Iterable))
print(isinstance([1,2,3],Iterable))
#特殊说明：版本兼容实现了getIterm
#迭代器：是迭代对象的扩展类，__iter__,__next__方法
#迭代对象：__iter__
print(issubclass(Iterator,Iterable))
li=[1,2,3,4,5,6]
#要遍历对象，获得他的迭代对象
it = li.__iter__()
print(it.__next__())
print(next(it))
#StopIteration 异常
for i in li:
   print(i)
# for 循环底层也是通过__iter__方法获得可迭代对象高端迭代器，每次都先生成一个迭代器

#自定义迭代器
class MyIterable:
   def __iter__(self):
      self.li=[1.9,4,2]
      return MyItertor(self.li)
class MyItertor:
   def __init__(self,data):
      self.li=data
      self.index=0
   def __iter__(self):
      pass
   def __next__(self):
      if self.index <len(self.li):
         r=self.li[self.index]
         self.index +=1
         return r
      else:
         raise StopIteration

# print(issubclass(MyIterable,Iterable))
# print(issubclass(MyItertor,Iterator))
# print(issubclass(MyIterable,MyItertor))
m=MyIterable()
for item in m:
   print(item)

class Iterable1:
   def __init__(self,itr):
      self.itr=itr
   def __iter__(self):
      return Itor(self.itr)
class Itor:
   def __init__(self,itr):
      self.data=itr
      self.index=len(itr)
      pass
   def __iter__(self):
      pass
   def __next__(self):
      if self.index >0:
         self.index -=1
         return self.data[self.index]
      raise StopIteration
l=[7,1,3,5,9]
mm=Iterable1(l)
for item in mm:
   print(item)