# -*- conding:utf-8 -*-
# 类方法  实例方法
class Person:
      def walk(self):
            print('walk walk')
       #类方法，使用装饰器来修饰 惯例：cls表示
      @classmethod
      def cm(cls):
            print('this is classmethod')
Person.cm()
Person.walk(Person)

p=Person()
p.walk()
p.cm()