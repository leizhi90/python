# -*- conding:utf-8 -*-
# 编写函数，可以对任意数量的参数求和，最大值与最小值。（类似min，max）
def add(*args):
      sum=0
      for i in args:
            sum +=i;
      return sum
def min_max(*args):
      if args:
            max = args[0]
            min = args[0]
            for i in args:
                  if max<i:
                        max=i
                  if min>i:
                        min=i
            return (max,min)
print(add(3,4,5,6,6,7))
print(min_max(11,23,4,5,6,8,92,))
# 位置可变参数后面的参数是否限制为关键字参数，为什么？
#是的，位置可变参数可以接收多个参数，如果后面没有限定关键字参数，那么在其后面的参数接收不到
# 编写程序，练习其他序列类型的拆包。
# bytes list tuple str

# 编写函数，第一个参数指定今天是星期几（1 ~ 7），第二个参数指定天数n，返回n天后是星期几。
def day_of_week():
      now=input("请输入今天是星期几：")
      after=input("请输入天数：")
      day(now,after);
def day(now,after):
      n=int(now)
      a=int(after)
      t=(n+a)%7
      if t==0:
            t=7
      print(t)
day_of_week()
# 证明运算符优先级高会影响结合性，但不会像数学上那样，先进行计算。例如：a + b * c，会首先计算a（使用函数来证明）。
def fist_less(*args):
    print(args)
a=1
b=2
c=3
fist_less(a+b*c)

# 3 <= x <=4 与x >=3 and x <=4完全等价吗？

# 给定含有字典的列表，实现对列表的排序。（根据字典中指定键的值排序）
d=[{'k':23,'kk':'sfsfd','kkk':'w23ds'},{'k':902},{'k':2,'kkkk':9},{'k':23}]
def ord(item):
      pass
print(d.sort(key=ord))