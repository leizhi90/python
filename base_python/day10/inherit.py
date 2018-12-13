# -*- conding:utf-8 -*-
#继承
#继承体现的是一种一般与特殊的关系
#子类继承了父类，子类就成了一种特殊的父类，子类变具有了父类的一切能力
# object类是python中所有类的父类
#继承的优势：带来了代码的复用，无需重复性定义，当以后功能更新也只需要改变父类的实现，无需改变每个子类
class Person:
   def __init__(self):
      self.age=99
   def walk(self):
      print('walk....')

class Student(Person):
   def __init__(self):
      self.age=66
   def walk(self):
      print('student walk.....')
   pass
p=Person()
s=Student()
s.walk()
print(s.age)
#定义子类的原因：父类的功能只能够满足一部分，吸收父类功能的同时在父类功能上进行扩展
#父类的功能并不完全适合子类，对父类的方法重写
#继承的思维
#提取共性的功能