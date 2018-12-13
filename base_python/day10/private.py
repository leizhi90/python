# -*- conding:utf-8 -*-
#私有成员
#通过定义私有成员，可以实现更好的分装性
#私有成员：以两个下划线开始，并且不能以多于两个下划线结尾_
#符合这样的名称规范，私有成员仅能在内部进行访问，类的外部无法访问
class Person:
   def __init__(self):
			#定义私有成员
      self.__name='lz'
   def set_name(self,name):
      #私有成员在类内部是可以访问的
	    self.__name = name
   def get_name(self):
      return self.__name
p=Person()
p.set_name('aaa')
# 解释器会把私有的
#访问私有成员
print(p.get_name())

#但是私有成员也并非真正的私有
print(p._Person__name)

#受保护的成员
#名称前加一个下划线，则该成员就是受保护的成员，没有特殊的语法
#约定：受保护的成员在外界（类的外部）不应该直接访问，因为在以后的升级过程中，受保护的成员可能不会提供一致性的支持（对以前进行兼容）