# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/12 21:42
def buble_sort(li):
   for i in range(len(li)-1):
      for j in range(len(li)-i-1):
         if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
def choice_sort(li):
   for i in range(len(li)-1):
      min = i
      for j in range(i+1,len(li)):
         if li[j] <li[min]:
            min = j
      if i != min:
         li[i], li[min]= li[min], li[i]