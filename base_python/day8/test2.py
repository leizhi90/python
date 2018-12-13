# -*- conding:utf-8 -*-
# map filter reduce
li=[-3,-1,3,6]
m=map(lambda i:i**2,li)
print(m)
print(list(m))
f=filter(lambda i : i>0,li)
print(list(f))
import functools
r=functools.reduce(lambda x,y:x+y,li)
print(r)
s=map(lambda i : i*4,filter(lambda i : i>0,li))
print(list(s))
# 汉诺塔程序

# level 当前第几层盘子
# A 盘子移动之前所在的座。
# B 移动过程中所借助的座。
# C 移动目标（最终目标）所在的座。
def h(level, A, B, C):
    if level == 1:
        print(f"{A}->{C}")
    else:
        h(level - 1, A, C, B)
        print(f"{A}->{C}")
        h(level - 1, B, A, C)

# h(5, "源", "经过", "目标")
h(2, "A", "B", "C")

