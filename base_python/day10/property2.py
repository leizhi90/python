# -*- conding:utf-8 -*-
#property 装饰器
#属性名与方法名相同
#当获取该属性值时，使用@property装饰的方法就会得到调用
#使用@属性名.setter  .deleter 当修改（设置）属性值时 删除时就会得到调用
# 如果要为创建的属性编写说明文档，写在获取方法中就可以
class Person:
   def __init__(self,name):
      self._name=name

   @property
   def name(self):
      """这是自己构建的一个属性
      :return:
      """
      print('property name')
      return self._name
   @name.setter
   def name(self,n):
      print('property set')
      self._name=n
   @name.deleter
   def name(self):
      print('property deleter')
      del self._name

p=Person('lz')
print(p.name)
p.name='setter property'
del p.name
print(Person.name.__doc__)