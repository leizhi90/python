# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/16 10:18
import multiprocessing as mp
class MyMultiprocess(mp.Process):
    def __init__(self, name='mymulti'):
        mp.Process.__init__(self, name=name)
    def run(self):
        i = 0
        for _ in range(100000):
            i += 1

if __name__ == '__main__':
    mp = MyMultiprocess('mymulti')
    mp.start()

