# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/16 15:13
import time
import threading
import multiprocessing as mp
from concurrent import futures
# 1、新建一个文本，往里面写 10M的内容，内容随意
#     每行1024个字节
# with open('d:/work/new_txt.txt', 'w+') as f:
#     for i in range(10240):
#         # li = []
#         # for j in range(1022):
#         #     li.append('g')
#         # li.append('\n')
#         # f.writelines(li)
#         str = ''
#         for j in range(1022):
#             str += 'f'
#         str += '\n'
#         f.writelines(str)
# with open('d:/work/new_txt.txt') as f:
#     for i in f:
#         print(i)
# 2、分别用同步单线程的方式、多线程和多进程，复制第一步的文本，不能高级的copy，只能用read 和 write 来实现
def copy(name):
    start_time = time.time()
    with open('d:/work/new_txt.txt')as f,open('d:/work/copy_txt.txt', 'w+') as ff:
        str =''
        for i in f:
            ff.writelines(f.readlines())
            ff.write('\n')
    print(name,'耗时：', time.time()-start_time)
# t = threading.Thread(target=copy, args=('单线程的方式',))
# t.start()

def MultiT():
    start = time.time()
    with futures.ThreadPoolExecutor(max_workers=2) as pool:
        for _ in range(4):
            r = pool.submit(copy, '多线程')
    print("执行结束，共耗时：", time.time() - start)
#MultiT()
if __name__ == '__main__':
    start = time.time()
    with futures.ProcessPoolExecutor(max_workers=2) as pool:
        for _ in range(4):
            r = pool.submit(copy, '多进程')
    print("执行结束，共耗时：", time.time()-start)
# 3、计算第二步3种方式，每种方式的时间


# 使用两个进程，对同一个全局变量进行修改多次，会出现什么情况。
#没有任何影响
# 如果在一个进程中，调用了n次fork，则共创建了几个进程（不算当前的进程）？

# 进程通讯时，将进程队列改为线程队列，可以吗？