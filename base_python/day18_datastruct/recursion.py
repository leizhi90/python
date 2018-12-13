# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/10 14:10
# 递归后面的函数 压栈式 执行
def f_recursion(i):
   if i > 10:
      print('over ..........')
      return
   print(i,'ininininin..........')
   i += 1
   f_recursion(i)
   print(i,'leave ..........')#******这行很重要**
f_recursion(1)