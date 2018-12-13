# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/12 10:25
def insert_sort(li):
   for i in range(1,len(li)):
      item = 0
      for j in range(i-1):
         if li[i] > li[j]:
            item = j
      li.insert(item,li[i])
#li = [2,6,5]
#insert_sort(li)
#print(li)

def insertionSort(lyst):
   i = 1
   while i <len(lyst):
      itemTinset = lyst[i]
      j = i - 1
      while j >= 0:
         if itemTinset <lyst[j]:
            lyst[j+ 1] = lyst[j]
            j -= 1
         else:
            break
      lyst[j+1] = itemTinset
      i +=1
def quick_sort(li, start, end):
   if start >= end:
      return None
   #第一个和最后一个比
   key = li[start]
   i, j = start, end
   while i < j :
      while li[j] > key:
         j -= 1
      li[i] ,li[j] = li[j],li[i]
      #如果交换了和左边比，
      while li[i] < key:
         i += 1
      li[i], li[j] = li[j], li[i]
   quick_sort(li, start,i-1)
   quick_sort(li,j+1,end)
li = [4,1,2,3,5,6,7,8]
quick_sort(li,0,len(li)-1)
print(li)