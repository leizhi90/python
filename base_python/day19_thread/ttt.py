# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/13 17:25
import threading
import time

lock_num = threading.RLock()
lock_price = threading.RLock()
class NumThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
    def run(self):
        global lock_num, lock_price
        # 获取 lock 如果这个 lock 已经被其他线程 acquire了，那么就会阻塞在这里，等待 线程 release 这个 lock
        print(self.name, '进入 run')
        lock_num.acquire()
        print(self.name, '开始执行操作')
        time.sleep(1)
        try:
            b = lock_price.acquire()
            time.sleep(1)
            lock_price.release()
        except:
            pass
        print(self.name, '准备结束操作')
        # 释放锁
        lock_num.release()
class PriceThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
    def run(self):
        global lock_num, lock_price
        # 获取 lock ， 如果 这个 lock 已经被其他线程 acquire 了，那么就会阻塞在这里，等待 线程 release 这个 lock
        print(self.name, '进入 run')
        lock_price.acquire()
        print(self.name, '开始执行操作')
        try:
            time.sleep(1)
            lock_num.acquire()
            time.sleep(1)
            lock_num.release()
        except:
            # traceback.print_exc()
            pass
        print(self.name, '准备结束操作')
        # 释放锁
        lock_price.release()
num_t = NumThread('num_thread')
#price_t = PriceThread('price_thread')
#price_t = PriceThread('price_thread')
num_t.start()
#price_t.start()

def light():
    linght_time = 0
    if not event.is_set():
        event.set()  # Flag = True, 阻塞
    while True:
        time.sleep(1)
        if linght_time < 10:
            print("Green is on....")
        elif linght_time < 13:
            print("Yellow is on ....")
        elif linght_time < 16:
            print("Red is on ......")
            if event.is_set():
                event.clear()
        else:    # 大于16, 该重新调绿灯了
            linght_time = 0
            event.set()

        linght_time += 1

def car_run(carnum):
    while True:
        time.sleep(2)
        if event.is_set():
            print("car %s is run" % carnum)
        else:
            print("CAR %s IS WAITTING........" % carnum)

if __name__ == "__main__":
    event = threading.Event()
    l = threading.Thread(target=light, )
    l.start()
    for i in range(3):
        c = threading.Thread(target=car_run, args=(str(i), ))
        c.start()
