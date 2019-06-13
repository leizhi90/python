# -*- conding:utf-8 -*-
#  位置参数与关键字参数
# 含有默认值的参数
#位置参数与关键字参数
# 参数传递的两种新式
#1、位置参数（进行对位传递
def f(a,b):
      print(a,b)
f(1,2)
# 关键字参数（根据参数名进行匹配传递
#2、
f(a=1,b=2)

def box(length, width, height):
      print('盒子')
box(5,4,3)

# 关键字参数的优势
#1、更好的可读性，
#2、不用考虑形参定义时的顺序
#3、当多个参数具有默认值时，使用关键字可以更好的进行定位

# 位置参数与关键字参数可以同时使用
# 位置参数需要出现在关键字参数的前面
# 同一个参数不能多次传递

# 强制使用关键字
def print_star(line,char='*'):
      for i in range(line):
            print(char*5)
print_star(3,'&')
# 可读性更好
print_star(3,char='@')
#在位置参数后面，加上一个占位的参数
#* 后面的参数强制使用关键字参数（不能使用位置参数传递
def print_star2(line,*,char='*'):
      for i in range(line):
            print(char*5)

print_star2(2)

print_star2(3,char='&')
print('ada','addfd')