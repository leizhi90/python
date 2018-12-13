# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/13 15:54
import threading
tackets = 1000000
lock = threading.Lock()
t1_num =0
t2_num =0
t3_num =0
t4_num =0
class MyTackets(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)
    def run(self):
        __class__.ff(self)
    def ff(self):
        global tackets, t1_num, t2_num, t3_num, t4_num, lock
        while True:
            lock.acquire()
            if tackets > 0:
                if self.name == 't1':
                    t1_num += 1
                    tackets -= 1
                elif self.name == 't2':
                    t2_num += 1
                    tackets -= 1
                elif self.name == 't3':
                    t3_num += 1
                    tackets -= 1
                elif self.name == 't4':
                    t4_num += 1
                    tackets -= 1
                lock.release()
            else:
                lock.release()
                break


t1 = MyTackets('t1')
t2 = MyTackets('t2')
t3 = MyTackets('t3')
t4 = MyTackets('t4')
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(t1_num,t2_num,t3_num,t4_num,t1_num+t2_num+t3_num+t4_num)

