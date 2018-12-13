# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 11:36
#生成器协程
from collections import namedtuple
ResClass = namedtuple('lz','count average')
def averager():
    total = 0.0
    count = 0
    average =None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return ResClass(count, average)
def grouper(storages, key):
    while True:
        storages[key] = yield from averager()
def client():
    process_date ={
        'boy_1':[39, 21, 66],
        'boy_2':[1,2,3]
    }
    storages = {}
    for k, v in process_date.items():
        coroutine = grouper(storages, k)
        next(coroutine)
        for dt in v:
            coroutine.send(dt)
        coroutine.send(None)
    print(storages)
client()