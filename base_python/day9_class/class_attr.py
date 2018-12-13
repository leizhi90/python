# -*- conding:utf-8 -*-
#类属性 实例属性
#类属性：直接定义在类的内部
#实例属性：指的是类说创建的对象属性
#区别
#1、属性的归属不同， 为类所有  绑定当前对象
#2、访问方式不同    通过类名和对象    创建的对象
class Person:
      #类属性
      desc='描述的信息'
      age=9
      #实例属性
      def __init__(self):
            self.name='名字'
            self.age=99
p=Person()
print(p.desc)
print(Person.desc)
print(p.age)
print(Person.age)
p.desc='discrib  infor'
Person.infor='infor'
print(p.infor)
# 尽管通过类所创建的对象也能访问到类属性，但是建议不要这样做
#建议：总是通过类名来访问类属性

