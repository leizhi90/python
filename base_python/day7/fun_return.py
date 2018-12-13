# -*- conding:utf-8 -*-
#函数可以使用return 返回一个值给调用端

def add(a,b):
    s=a + b
    return s
r= add(1,3)
print (r)
#默认返回None
def no_return():
    pass
print(no_return())
#不能使用多个return ，执行后函数体就会结束
# 返回 元祖 列表 字典 集合等

def compute(a,b):
    # return a + b
    # return a + b
    return [a +b,a-b]
#一般用元祖不用列表 安全 不可修改
def r():
      return 2
      pass

print(r())

