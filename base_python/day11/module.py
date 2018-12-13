# -*- conding:utf-8 -*-
#模块 一个文件  文件是物理上的划分，模块是逻辑上的划分
#模块的作用
#1、将大的项目进行划分，每个人负责其中一个部分，有利于协作开发
#2、提供了独立的命名空间（全局）有效解决命名冲突
#3、功能的划分有利于程序的复用性，相似的功能放入同一个模块中
# import 模块名
import another as a

#模块导入时，就会解析，但是不会重复解析
def f():
   print('bas...')
f()
from  another import f

f()
# 如果有冲突，以后绑定的为准，解绑
class A:
   pass
class B:
   pass
print(isinstance(A,B))
print(isinstance(A,object))
#参数可以指定一个对象，返回当前命名空间中存在的名称
print(dir())
print(dir('a'))
print(dir(a))
import random
print(dir(random))
#模块的别名 原有的名称不可用
#优势：通过模块别名可以解决命名冲突 以简带繁

# import * 的限制
#1、以下划线开头的命名
#2、定义__all__变量关联一个列表，
#__all__=[]存在仅导入里面指定的包括_


from another import *

#__name__变量可以返回一个名称
#对于一个模块可以有两种执行方式
#以脚本的方式来运行模块（在控制台上一python程序运行的模块）
#当import一个模块是，该模块也会得到执行
#当以脚本方式来执行模块是，__name__的值为__main__
#2、当以import来执行时，__name__的值时模块的名字
print(__name__)

if __name__ == '__main__':
   print('测试；；；；')