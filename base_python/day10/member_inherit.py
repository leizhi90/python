# -*- conding:utf-8 -*-
#子类能够继承父类的实例属性，类属性 实例方法 静态方法 类方法
#实例属性：如果子类有__init__方法时不会调用父类的
#私有成员实际上子类也是可以继承的。只是继承的名字不是我们定义的名字 Student._Persion__pro
class Person:
   __pro=2
   #Student._Persion__pro
   def __init__(self):
      self.age=4
   def in_m(self):
      pass
   @classmethod
   def c_m(cls):
      pass
   @staticmethod
   def s_m():
      pass
class Student(Person):
   pass

