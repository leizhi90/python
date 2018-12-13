# -*- conding:utf-8 -*-
# 类方法与实例方法对属性进行访问
class Person:
      desc='类属性'

      def __init__(self):
            self.name='实例属性'
      def instance_method(self):
            #访问实例属性
            print(self.name)
            #访问类属性
            #属于硬编码
            #动态的获取类，然后进行访问
            #self.
            __class__.desc=''
            print(Person.desc)

      @classmethod
      #类方法的参数cls，代表的是当前的类
      def cm(cls, other):
            #可以访问，当无推荐
            Person.desc="sdf"
            #推荐方法
            cls.desc='ssfdfdd'
            #类方法中不能访问实例属性
            cls.name='names'
p=Person()
print(p.__class__)
#每个对象都有实例属性，彼此无影响
#类属性，所有类共享

#类方法的作用
#通常提供一种另外的方式来创建对象
#需求：根据不同的情况创建对象
#创建一个与已知盒子一模一样的对象
class Box:
      def __init__(self,length,width,height):
            self.length=length
            self.width=width
            self.height=height

      @classmethod
      def copy(cls,box):
            return cls(box.length,box.width,box.height)
b=Box(1,23,3)
b2=Box.copy(b)
print(b2.height)