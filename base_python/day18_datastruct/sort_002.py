# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/12 19:46
li = [9,1,3,7,8,5,6,2]
def shell_sort(l):
   step = len(l) // 2
   while step > 0:
      for i in range(0, step):
         for j in range(i + step, len(l), step):
            key = l[j]
            while j >= step and key < l[j - step]:
               l[j] = l[j - step]
               j -= step
            else:
               l[j] = key
      step = step // 2
   return l
#print(shell_sort(li))
def shell_01(li):
   step = len(li) //2
   while step >0:
      for i in range(0, step):
         for j in range(i + step,len(li), step):
            key = li[j]
            while j >= step and key < li[j-step]:
               li[j] = li[j- step]
               j -= step
            else:
               li[j] = key


def shell_sort1(l):
   step = len(l) // 2
   while step > 0:
      for j in range(step, len(l)):
         key = l[j]
         while j >= step and key < l[j - step]:
            l[j] = l[j - step]
            j -= step
         else:
            l[j] = key
      step = step // 2
   return l

print(shell_sort1(li))
