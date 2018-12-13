# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 10:52
from collections import namedtuple
Student = namedtuple('Student','name age')
#命名元祖
student_namedtuple = Student(name='lz', age=18)
print(student_namedtuple.name)
print(student_namedtuple.age)
#普通元祖
student_nomal = ('lz',19)
print(student_nomal[0])
print(student_nomal[1])