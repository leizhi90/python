# -*- conding:utf-8 -*-
# 字典的运算

d={1:'a',2:'b',3:'c'}
#字典不支持 < >

# len 返回字典中返回键值对的个数

print (len(d))

#字典遍历
# keys
for k in d.items():
    print (k[0],k[1])
#元祖拆包
for k,v in d.items():
    print (k,v)

#字典推导式
#与列表推导式类似，
#当字典中的Kye v 是通过另外一个字典（或可迭代对象等）计算的出时
#我们就可以使用字典推导式
print ({k:2*k for k in range(1,11)})
