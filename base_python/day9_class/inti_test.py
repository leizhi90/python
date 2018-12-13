# -*- conding:utf-8 -*-
#对象的属性
# __init__是对象初始化方法该方法在创建对象时自动得到调用执行
class Person:
      def __init__(self):
            print('__init__方法')
Person()
Person()
#考虑到__init__的特征，进行对象的初始化时非常合适的
class Personn:
      def __init__(self,name):
            self.name=name
            self.age=name
p=Personn('aaa2')
print(p.name)
print(p.age)
#在创建对象时，通过构造器为__init__方法传递参数
# __init__方法不足，
p.id=1001
#如果属性名不存在，则进行新增，有则改
# 动态增加的属性仅对当前对象有用
def walk(self):
      print('walk walk')
p.walk=walk
p.walk(p)
#动态增加的方法，需要我们显示传递self对象（当前对象）
