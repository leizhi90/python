# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/12 16:41
# 冒泡
def bubbling_sort(li):
   for i in range(len(li)-1):
      goon = False
      for j in range(len(li)-i-1):
         if li[j] > li[j+1]:
            goon = True
            li[j+1], li[j] = li[j], li[j+1]
      if not goon:
         break
li = [3,2,1,5,8,9]
#bubbling_sort(li)
#print(li)

#选择
def select_sort(li):
   for i in range(len(li)-1):
      min_index = i
      for j in range(i+1,len(li)):
         if li[min_index] > li[j]:
            min_index = j
      if min_index != i:
         li[i], li[min_index] = li[min_index], li[i]
   return li
print(select_sort(li))
#插入排序
def insert_sort(l):
   for i in range(1, len(l)):
      key = l[i]
      for j in range(i - 1, -1, -1):
         if l[j] > key:
            l[j + 1] = l[j]
         else:
            if j != i - 1:
               l[j + 1] = key
            break
      else:
         l[0] = key
   return l
# 插入排序
def insertion_sort(A):
   for j in range(1, len(A)):
      key = A[j]
      i = j - 1
      while i >= 0 and A[i] > key:
         A[i + 1] = A[i]
         i = i - 1
      A[i + 1] = key
A = [5, 2, 4, 6, 1, 3]
#insertion_sort(A)
#print(A)
def in_01(li):
   for i in range(1,len(li)):
      key = li[i]
      for j in range(i -1,-1,-1):
         if key < li[j]:
            li[j+1] = li[j]
         else:
            # if j != i-1:
            #    li[j+1] = key
            li[j + 1] = key
            break
      else:
         li[0] = key
li = [9,8,1,9,2,4,6,3,7]
