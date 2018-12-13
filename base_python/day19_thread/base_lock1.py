# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/13 14:06
#lock线程之间进行互斥的锁，用于修改共享数据
import threading
import time
lock = threading.Lock()
num = 0

class MyUseLockTh(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self, name = name)
    def run(self):
        global lock,num
        print('ininii....',self.name,num)
        time.sleep(0.1)
        lock.acquire()
        num += 1
        time.sleep(1)
        print('after.....',self.name,num)
        lock.release()
t1 = MyUseLockTh('thread___1')
t2 = MyUseLockTh('thread___2')
t3 = MyUseLockTh('thread___3')
t1.start()
t2.start()
t3.start()
