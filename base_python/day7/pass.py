# -*- conding:utf-8 -*-
# 参数传递

def f(a):
      a=20
      print(a)
b=5
f(b)
# a--->b ==5  a--->20
print(b)
f(b)
print(b)
def svap(a,b):
      a,b=b,a
t1=1
t2=2
svap(t1,t2)
print(t1,t2)
#1 2

# 可变参数
def f2(li):
      li.append(33)
a=[2,3,4]
f2(a)
print(a)
#[2, 3, 4, 33]
# 当参数是可变对象时，参数传递中，实参与形参都绑定了同一个对象，则会对实参造成影响
def f3(li):
      li=[2,3,4]
a3=[1,2,3]
f3(a3)
print(a3)
#***此类问题一定要画内存图

# 不管参数类型是可变对象类型还是不可变对象类型，通过形参的改变，都无法作用于实参


