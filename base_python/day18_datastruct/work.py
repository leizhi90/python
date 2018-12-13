# -*- coding:utf-8 -*-
# @Author : LZ
# @Time   : 2018/4/12 20:51
# ***************************冒泡排序***********************
li = [6,1,9,7,3,2,8,4]
def bubble_sort(li):
   n = len(li)
   while n > 1:
      i = 1
      while i < n:
         if li[i] > li[i-1]:
            li[i], li[i-1] = li[i-1], li[i]
         i += 1
      n -= 1
   return li
#print(bubble_sort(li))
#*******************************选择排序********
def choce_sort(li):
   for i in range(len(li)-1):
      max = i
      for j in range(i+1,len(li)):
         if li[j] > li[max]:
            max = j
      if i != max:
         li[i], li[max] = li[max], li[i]
   return li
#print(choce_sort(li))
#******************插入排序********************
def insert_sort(li):
   i = 1
   while i <len(li):
      item = li[i]
      j = i - 1
      while j >= 0:
         if item > li[j]:
            li[j+1] = li[j]
            j -= 1
         else:
            break
      li[j+1] = item
      i +=1
   return li
#print(insert_sort(li))
#************************希尔排序******************************
def shell_sort(li):
   step = len(li) // 2
   while step > 0:
      for j in range(step, len(li)):
         key = li[j]
         while j >= step and key > li[j-step]:
            li[j] = li[j-step]
            j -= step
         else:
            li[j] = key
      step = step // 2
   return li
#print(shell_sort(li))
#******************************归并排序***********************
def merge(li1,li2):
   temp = []
   i, j = 0, 0
   while i < len(li1) and j < len(li2):
      if li1[i] > li2[j]:
         temp.append(li1[i])
         i += 1
      else:
         temp.append(li2[j])
         j += 1
   if i == len(li1):
      temp += li2[j:]
   else:
      temp += li1[i:]
   return temp
def merge_sort(l):
   if len(l) <= 1:
      return l
   mid = len(l) // 2
   list_left = merge_sort(l[:mid])
   list_right = merge_sort(l[mid:])
   return merge(list_left, list_right)
print(merge_sort(li))