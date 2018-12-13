# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/13 14:22
import threading
import time
lo = threading.RLock()
#def acquire(self, blocking=True, timeout=-1)
num = 0
class MyLockTest(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)
    def run(self):
        global lo, num
        print('in........')
        print(self.name,num,'iniiin.....')
        lo.acquire()
        time.sleep(0.2)
        num += 1
        lo.release()
        print(self.name, num, 'after.....')

myl = MyLockTest('thread__1')
my2 = MyLockTest('thread__2')
my3 = MyLockTest('thread__3')
my4 = MyLockTest('thread__4')

myl.run()
my2.run()
my3.run()
my4.run()