# -*- conding:utf-8 -*-
#高阶函数
# 一个函数中，接收另外一个函数作为该函数的参数，或者该函数将另外一个函数作为返回值

# map
# 第一个参数，一个函数
# 第二个参数，可迭代对象
# 将可迭代对象中的每个元素，一次传递给第一个参数指定的函数，获取返回值，然后将返回值进行返回（返回的类型是一个可迭代对象
li=[1,2,3,4,5,-3,-3]
r=map(lambda i:i**2,li)
print(r)
print(list(r))

#filter 实现的是一个过滤功能，将满足条件的留下，不满足条件的去掉
# 第一个参数：一个函数，用来指定过滤功能，该函数接收一个参数，如果返回值为True,则保留否则去掉
# 第二个参数：可迭代对象
f=filter(lambda x:x>3,li)
print(f)
print(list(f))
# map 和 fliter通常组合在一起使用
r=map(lambda i:i**2,filter(lambda x:x>2,li))
print(list(r))
#列表推导式可以表达

import functools
#实现的是一个缩减操作（重复性的二合一，直到剩下一个元素位置
# 第一个参数，函数，指定二合一的规则，该函数接收两个参数，返回合并之后的结果
# 第二个参数，可迭代对象
# 第三个参数，（可选）指定初始元素
r=functools.reduce(lambda x,y:x+y,li,10)
print(r)
print(functools.reduce(lambda x,y:x if x>y else y ,li))