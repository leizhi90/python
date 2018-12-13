# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 14:13
from greenlet import greenlet
import gevent
def func1():
    print('func1 running  ')
    gevent.sleep(2)
    print('func1 end ')

def func2():
    print('func2 running ')
    gevent
    print('func2  end')

def func3():
    print('func3 running ')
    gevent.sleep()
    print(' func3  end')

tasks = [gevent.spawn(func1), gevent.spawn(func2), gevent.spawn(func3())]
gevent.joinall(tasks)
print('over .....')
