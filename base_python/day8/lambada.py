# -*- conding:utf-8 -*-
# 在python中一切都是对象，函数也不例外
#对于函数，也支持类似与变量的操作
#1、将函数名赋值给另外一个名称（变量）
#2、将函数作为实参，传递给另外一个函数
# 3、函数也可以作为返回值，由另外一个函数返回

def f():
      print("函数是一等对象")

f2=f
# 经过赋值之后，f2也就绑定了f所绑定的对象，通过f2也能调用函数
def f3(p):
      p()
f3(f)

def f3():
      def inner():
            print('这是一个内部函数')
      return  inner
r=f3()
r()

# 如果函数体比较简单，我们可以通过lambada表达式创建，该表达式创建的函数没有名字，因此也称为匿名函数
# lambada（函数的参数列表】：函数的返回值
def square(n):
      return n**2
v=lambda n:n**2
print(v(2))
# lambada 使用场合
#1、函数体比较简单
#2、lambada 的函数只使用一次
