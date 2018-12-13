# -*- conding:utf-8 -*-
# 定义一个全局变量，然后在函数内修改这个全局变量的值。
# 在函数内，先输出该变量，然后修改该变量的值。
# 在函数内，将全局变量的值增1。
x = 3
def f(x):
      x=1
      print(x)
f(x)
print(x)
def f_1(x):
      print(x)
      x+=2
      print(x)
f_1(x)
print(x)