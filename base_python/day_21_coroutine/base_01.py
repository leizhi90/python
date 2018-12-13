# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 10:23
def receiver():
    receipt = ''
    while 1:
        n = yield  receipt
        print('consumer receiver msg: %s'%n)
        receipt = f'{n} is ok'
def sender():
    c = receiver()
    c.send(None)

    n= 0
    while n<3:
        n += 1
        print('produce send msg %s'%n)
        receipt = c.send(n)
        print('consumer return msg :%s'%receipt)
    c.close()


sender()