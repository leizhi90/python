# -*- conding:utf-8 -*-

def print_star(line):
      for i in range(line):
            print('***')

def print_star(line,char):
      for i in range(line):
            print(char*5)
print_star(5,'*')

# python 定义函数时，可以为形参指定默认值，当调用函数时，如果没有
#传递默认值，就用默认，如果有就传递实参
def print_star2(line,char="*"):
      for i in range(line):
            print(char*5)
print_star2(3)
print_star2(4,'&')

#含有默认值参数的优势
#1、可以为用户提供一种默认的选择，简化用户操作
#2、可以对以前程序的一种兼容

#顺序
#含有默认值的参数必须定义在没有默认值的参数后面