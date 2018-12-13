# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/16 9:06
"""
多进程 效率的提升不是无限制的，取决于CPU的内核数
"""
import os
import multiprocessing as mp
import time
def count(n):
    i = 0
    for _ in range(n):
        i += 1
    print('计算后的i:', i)

print('准备开始子进程，', os.getpid(), os.getppid(),__name__)
if __name__ == '__main__':
    start_time = time.time()
    #**********p会复制上下文环境，无限递归***__main__*************
    p = mp.Process(target=count, args=(1000000,))
    p2 = mp.Process(target=count, args=(100000,))
    p.start()
    p2.start()
    p2.join()
    #没有开启一个新线程，等同于直接调用count(1000000)
    #p.run()
    p.join()
    print(time.time()-start_time)
"""
不在main 中建立子进程，会抛出RuntimeError
是无限递归，因为子进程开启时，会复制主进程的所有环境
只有在window会这样，Linux不会
所有项目的启动都在 __name__ == '__main__'
"""
# print(os.getpid())
# print('begin ......')
# p = mp.Process(target=count, args=(100000,))
# p.start()
# print('end.......')

# start 非阻塞的方式启动子进程
#run  在当前进程中
#join 配合start使用可等待子进程运行结束
