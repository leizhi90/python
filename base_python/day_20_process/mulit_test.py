# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/16 17:01
import os
import multiprocessing as mp
import time
def count(n):
    print('进行count 运算', os.getpid())
    i = 0
    for _ in range(n):
        i += 1
    print('计算后的i：', i)
    return i
def callback_func(r):
    print('callback操作:', r, os.getpid())
    time.sleep(3)

def error_callback_func(e):
    print('error_callback操作：', e, os.getpid())

def count_raise_error(n):
    print('进行count 运算', os.getpid())
    i = 0
    for _ in range(2):
        i += 1
    print('计算后的i：', i)
    raise Exception('count方法出错了！！！！')

if __name__ == '__main__':
    # processes 参数，就是最大进程数
    # 哪怕你创建再多的进程，这个pool也只会允许最大进程数量的进程同时运行
    # pool = mp.Pool(processes=4)
    #
    # r = pool.apply(count, args=(50000000, ))
    # print("返回值：", r)
    # r = pool.apply(count, args=(50000000, ))
    # print("返回值：", r)
    #
    # print('执行结束')
    print('当前主进程', os.getpid())
    pool = mp.Pool(processes=4)
    r = pool.apply_async(count, args=(51000000, ), callback=callback_func, error_callback=error_callback_func)
    # print('返回值：', r)
    print('返回值get后的值：', r.get())
    r = pool.apply_async(count, args=(49000000, ), callback=callback_func, error_callback=error_callback_func)
    # print('返回值：', r)
    print('返回值get后的值：', r.get())

    # close 是关闭 进程池，不允许继续对进程池操作
    pool.close()
    pool.join()
    print('执行结束')