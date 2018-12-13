# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/13 9:31
"""
进程就是操作系统中一个正在运行的执行程序，每个进程最少要有一个线程，是主线程，这个线程是进程的最小执行单元
主线程一旦结束，进程就关闭了
"""

"""
GIL global interpreter lock（Cpython独有） 全局解释器锁 解释器层面上进行的，同一时刻只有一个线程在运行，其他线程都是挂起状态，在IO密集型的应用才有实际意义
"""

import threading
import time

def count_time():
    start_time = time.time()
    num = 0
    for i in range(1000000):
        num += i
    end_time = time.time()
    print(end_time - start_time)
def f(s):
    time.sleep(1)
    print('thread')
# t = threading.Thread(target=count_time())
# t1 = threading.Thread(target=f,arg=('args',))
# t.start()

class MyThread(threading.Thread):

    # def __init__(self,name):
    #    super.__init__(self)

    def __init__(self,name):
        # 需执行父类的初始化方法
        threading.Thread.__init__(self,name=name)
        self.name = name
    def run(self):
        start_time = time.time()
        num = 0
        for i in range(10000000):
            num += i
        end_time = time.time()
        print(end_time - start_time)
test1 = MyThread('my')
test1.start()
test1.daemon()
# test1.start()
# *******RuntimeError: threads can only be started once*****************
print('end.........')
"""
run start 
start 开启一个新线程，
"""
#******************************方法************************
# current_thread() 获取电器活动线程的对象
# active_count 当前存在线程数
#enumerate() 当前活动线程对象的列表
# get_ident() 获得当前线程的一个标记，多个线程之间不会重复
#main_thread() 主线程的对象
#*************************对象方法***********************
#start 开启一个新线程
#join（timeout=None)等待目标线程对象执行完毕， 时间是超时时间S 等待时间
#ident 线程的标识
#daemon() 守护线程，默认False前台线程，True后台线程
#join 的优先级高于 daemon