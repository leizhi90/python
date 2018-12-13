# -*- conding:utf-8 -*-
# 参数默认值陷阱

#参数的默认值是在函数定义的时候进行计算的，不是在函数调用时候才去计算

#参数的默认值仅计算一次
a=1
def f(num=a):
      print(num)
f()
a=5
f()
# 1
# 1
def f2(li=[]):
      li.append(100)
      print(li)
f2()
f2()
# [100]
# [100, 100]
def f3(li=None):
      li=[]
      li.append(100)
      print(li)
f3()
f3()
# ***在地哦啊用函数时，如果没有为含有默认值的参数指定实际参数，，则会使用默认值来初始化形参
# 而不是我们看到的li=[]来进行的初始化（默认值仅在函数定义是计算一次

#我们可以使用函数对象的 __defaults__ 来查看函数的默认值
#返回一个元祖类型，保存每个参数的默认值
print(f3.__defaults__)
n=3
def f4(li=[5],a=n):
      li.append(100)
      a+=2
      print(li)
print(f4.__defaults__)
n=8
f4()
print(f4.__defaults__)
ll=[]
ll2=None
ll6=ll2
ll3=[]
ll4=None
print(id(ll))
print(id(ll2))
print(id(ll3))
print(id(ll4))
print(ll2==ll4)
print(ll4==ll6)
#  None 地址是相同的
def ad():
      pass
l11=ad()
print(l11==ll6)
print(id(1))
d={None:1}
print(d)
input()