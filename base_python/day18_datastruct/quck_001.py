# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/12 20:30
def quick_sort(l, start, end):
   if start >= end:
      return
   i, j = start, end
   key = l[i]
   while i < j:
      while l[j] > key:
         j -= 1
      if i < j:
         l[i], l[j] = l[j], l[i]
         i += 1
      while l[i] < key:
         i += 1
      if i < j:
         l[i], l[j] = l[j], l[i]
         j -= 1
   quick_sort(l, start, i - 1)
   quick_sort(l, i + 1, end)
   return l