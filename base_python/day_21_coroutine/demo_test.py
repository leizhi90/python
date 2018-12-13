# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 16:00
import collections
Event = collections.namedtuple('Event','time texiNum action')
def taxi_process(texiNum, trip_num, start_time=0):
    time = yield Event(start_time, texiNum, '==出库==')
    for i in range(trip_num):
        time = yield Event(time, texiNum, '==载客==')
        time = yield Event(time, texiNum , '==下客==')
    yield Event(time, texiNum, '==回家==')
if __name__ == '__main__':
    t1 =taxi_process(1,1)
    a = next(t1)
    print(a)
    b = t1.send(a.time+6)
    print(b)
    c = t1.send(b.time+12)
    print(c)
    d = t1.send(c.time+1)
    print(d)
