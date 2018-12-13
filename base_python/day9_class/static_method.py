# -*- conding:utf-8 -*-
# 静态方法 @staticmethod 没有固定的参数
#建议：通过类名去访问静态方法
#静态方法没有 cls self 与当前类 对象无关
#当某个函数的功能完全是为某个类服务的，为了逻辑上的相关联性，将该函数移动到类的内部，令其成为静态方法
class Person:
      def __init__(self,name):
            self.name=name
      @staticmethod
      def sm():
            print('这是静态方法')
      @staticmethod
      def make_friends(p1, p2):
            print(f'{p1.name}与{p2.name}叫朋友')
def make_friends(p1,p2):
      print(f'{p1.name}与{p2.name}叫朋友')
p1=Person('a')
p2=Person('b')
Person.make_friends(p1,p2)
