# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 15:31
def receiver():
    receipt = ''
    while True:
        n = yield receipt
        print('consumer receive msg %s'%n)
        receipt = '%s ok'%n
def sender():
    c =receiver()
    c.send(None)
    n = 0
    while n< 3:
        n += 1
        print('produce send msg %s'%n)
        receipt = c.send(n)
        print('consumer return msg %s'%receipt)
    c.close()
sender()