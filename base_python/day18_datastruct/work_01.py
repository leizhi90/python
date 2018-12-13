# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/10 18:37
# 改写冒泡排序，将冒泡排序的最好时间复杂度改成O(n)。
def bubbling(li):
   goon = True
   for i in range(len(li)-1):
      for j in range(len(li)-i-1):
         if li[j+1] < li[j]:
            goon = False
            li[j+1],li[j] = li[j],li[j+1]
      if goon:
         break
li = [9,2,3,4,1,8,5]
bubbling(li)
print(li)

# 实现折半查找。
def half_find(li, target):
   left = 0
   right = len(li) - 1
   while left <= right:
      mid = (left + right) // 2
      if target == li[mid]:
         return mid
      elif target > li[mid]:
         left = mid +1
      else:
         right = mid - 1
li1 = [0,1,2,3,4,5,6,7]
print(half_find(li1,2))