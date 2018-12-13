# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/16 9:39
"""
os.fork()
所有的子进程其实都是通过他的机制来执行的
在window平台
"""
import os
import multiprocessing as mp
import time
print('准备子进程，', os.getpid(), __name__)
if __name__ == '__main__':
    start_time = time.time()
    os.fork()
