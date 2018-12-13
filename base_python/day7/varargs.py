# -*- conding:utf-8 -*-
# 可变参数
def add(a,b,c=0,d=0,e=0):
      return a+b+c+d+e
# 1、可变位置参数 *a 可以接收0到多个位置参数
# 2、可变关键字参数 **a 可以接收0到多个关键字参数
# 打包成tuple
def add2(*args):
      print(args)
      print(type(args))
      sum=0
      for item in args:
            sum+=item
      return sum
add2()
add2(1,2,3,4)
#打包成字典类型
def add3(**kwargs):
      print(kwargs)
      print(type(kwargs))
add3(a=1,b=3,c=5)

def add4(a,b,*args):
      print(a,b,args)
add4(1,2,3,4,5)
#1 2 (3, 4, 5)
# 可变位置参数可以接收所有未匹配的位置参数
def add5(a,b,**kwargs):
      print(a,b,kwargs)
add5(1,b=2,d=3,g=4,o=5)
#1 2 {'d': 3, 'g': 4, 'o': 5}
# 位置可变参数后面定义的参数，将自动成为关键字参数,强制使用关键字参数
def add6(a,*args,d):
      print(a,args,d)
add6(1,34,45,5,6,d=7)

def add7(a,b,*args,**kwargs):
      print(a,b,args,kwargs)
add7(1,3,34,5,6,6,7,c='i',d='p')
#可变位置参数和可变关键字参数最多只能定义一个
# 万能参数列表
def f(*args,**kwargs):
     pass

