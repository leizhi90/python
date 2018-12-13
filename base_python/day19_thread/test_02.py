# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/13 16:55
import threading
def f_f(a):
    print(a)
t = threading.Thread(target=f_f,args=('args',))
t.start()