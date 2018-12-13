# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/16 14:01
from concurrent import futures
import os
import time
"""
并发

"""
def count(n, name='nono'):
    print('进入count方法', os.getpid())
    num = 0
    for i in range(n):
        num += 1
    print('计算完毕，', i)
    return num

start = time.time()
#多线程
# with futures.ThreadPoolExecutor(max_workers=2) as pool:
#     for _ in range(4):
#         r = pool.submit(count, 5000000, name='name')
#         print('返回值,', r.result())
# print('执行结束，', time.time()-start)
#多进程
if __name__ == '__main__':
    with futures.ProcessPoolExecutor(max_workers=4) as pool:
        li = []
        for _ in range(4):
            r = pool.submit(count, 5000000)
            li .append(r)
        for i in li:
            print('done', i.done())
        print(futures.wait(li))
print('执行结束，', time.time()-start)

"""
IO密集型 频繁的读取一些资源如：文件 网络
CPU密集型：高频率的CPU GPU的计算
并发 3中
1、 多线程，由于gil的存在，子对io密集型的项目有效
2、多进程，利用cup的多核同时处理几个任务，单核的CPU不存在多进程
3、协程：微型线程，是运行在单个线程上的，不同任务之间的频切换，不由CPU控制，由代码控制
"""