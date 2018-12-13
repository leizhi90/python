# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 15:49
from collections import namedtuple
student = namedtuple('student','name age sex')
s = student('lz',22,'femal')
print(s)
student2 = namedtuple('student',['name','age','male'])
ss = student2('lz',12,'male')
print(ss)
print('%s is %d years old %s'%ss)
Result = namedtuple('Result','a, b')
def simple_corotine():
    a = 1
    b = 2
    while True:
        print('协程开始=====')
        x = yield
        if x== 12:
            break
        print('协程获得x:',x)
    return Result(a, b)
my_coro = simple_corotine()
next(my_coro)
my_coro.send(13)
my_coro.send(12)
try:
    my_coro.send(12)
except StopIteration as exc:
    result = exc.value
    print(result)