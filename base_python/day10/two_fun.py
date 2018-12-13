# -*- conding:utf-8 -*-
#两个内建函数
#isinstance(obj,cls) 对象 类型  是True 否False
#子类对象也一定是父类类型
# issubclass(cls1,cls2) 类型 类型
class Person:
   pass
class Student(Person):
   pass
p=Person()
s=Student()
print(isinstance(p,Person))
print(isinstance(s,Person))
print(issubclass(Student,Person))
print(issubclass(Person,object))