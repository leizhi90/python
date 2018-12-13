# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/13 16:13
#队列
"""
queue.Queue(maxsize=0)
一般的队列 先进先出
queue.LifoQueue(maxsize=0)
类似栈 后进先出
queue.PriorityQueue(maxsize=0)
优先级的队列对象
"""
import queue
#def put(self, item, block=True, timeout=None):
# item元素 block 是否阻塞，当队列满的时间  timeout等待超时时间S Full Excepton
#def get(self, block=True, timeout=None):
# 空时   等待超时 Empty exception异常

q = queue.Queue()
q1 = queue.LifoQueue()
q3 = queue.PriorityQueue()
import threading
import time
class ProduceThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global q
        for _ in range(10):
            for i in range(10):
                q.put(i)
            time.sleep(0.1)
class CusmorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global q
        for _ in range(15):
            print('get queue ',q.get())
            time.sleep(0.1)
t_p = ProduceThread()
t_c =CusmorThread()
t_p.start()
t_c.start()