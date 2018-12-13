# -*- conding:utf-8 -*-
#property的使用
#最早的方式，直接访问属性，实现简单，但是暴露了底层的实现细节（类中定义的属性），不利于以后类的更新与升级
class Person:
   def __init__(self,name):
      self.name=name
#整改，不直接访问类中定义的属性。而是提供公有接口间接进行访问


#通过property定义属性，来实现既能够简单进行访问，又能提供好的封装性
#1、通过property函数
#2、通过property装饰器
class Personn:
   def __init__(self,name):
      self._name=name
   #(self, fget=None, fset=None, fdel=None, doc=None)
   #get,该方法在读取属性值得时候，会调用
   #set,修改属性的时间调用
   #del 删除属性的时候调用
   #说明文档
   def get_name(self):
      print('get fun ')
      return self._name
   def set_name(self,name):
      print('set fun')
      self._name=name
   def del_name(self):
      print('del fun')
      del self._name
   name=property(get_name,set_name,del_name,'这是伪造的属性，真实的是受保护的')
   #当name属性为只读时，仅提供get不提供set del即可
pp=Personn('lz')
print(pp.name)
#print(pp.get_name)
pp.name='dadfd'
del pp.name
print(Personn.name.__doc__)
# get fun
# lz
# set fun
# del fun
# 这是伪造的属性，真实的是受保护的