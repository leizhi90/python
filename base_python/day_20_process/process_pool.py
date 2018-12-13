# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/16 10:25
"""
进程池
池：就是一个容器，进程池就是包含了很多进程的一个池子，一般一个池子都有一个最基本的参数，，即最大的元素数量
优势：提高使用效率 减少资源的重复创建和销毁

"""
import os
def count(n):
    i = 0
    for _ in range(n):
        i += 1
    print('计算后的i:', i)

import multiprocessing as mp
if __name__ == '__main__':
    pool = mp.Pool(processes=3)

    #阻塞的方式，start join 相似
    pool.apply(count,args=(10000,))
#**********apply*****
#apply(self, func, args=(), kwds={}):
#apply_async(self, func, args=(), kwds={}, callback=None,error_callback=None):
# callback 回调函数，就是把函数的方法值作为参数传入到callback指定的回调函数中执行
#error_callback 错误回调函数
#异步
#同步