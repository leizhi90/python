# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/10 17:03
li = [8,3,1,9,3,6,2,7]
def bubbling(li):
   for i in range(len(li)-1):
      for j in range(len(li) - i-1):
         if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]
bubbling(li)
print(li)
