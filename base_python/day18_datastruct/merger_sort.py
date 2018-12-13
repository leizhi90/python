# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/12 16:18
def merger_02(li1, li2):
   temp = []
   i,j = 0,0
   while i < len(li1) and j < len(li2):
      if li1[i] < li2[j]:
         temp.append(li1[i])
         i +=1
      else:
         temp.append(li2[j])
         j +=1
   if i < len(li1):
      temp += li1[i:]
   if j < len(li2):
      temp +=li2[j:]
   return temp
li1 = [2,3,4,5]
li2 = [6,7,8]
print(merger_02(li1,li2))

def merger_01(li):
   if len(li) <= 1:
      return li
   mid =len(li) // 2
   li_left = merger_01(li[:mid])
   li_right = merger_01(li[:mid])
   return merger_02(li_left,li_right)

print(33*'*')


def merge(list1, list2):
   # 建立一个新的列表
   temp = []
   # i 是第一个元素的下标，  j 是第二个元素的下标
   i = j = 0
   while i < len(list1) and j < len(list2):
      # 判断2个数组的未比较过的第一个元素，进行比较
      if list1[i] < list2[j]:
         # list1的元素符合条件
         temp.append(list1[i])
         i += 1
      else:
         # list2的元素符合条件
         temp.append(list2[j])
         j += 1
   # 判断一个列表结束 ，但是另外一个列表中还有未添加的数据，添加 temp 的尾部
   if i == len(list1):
      temp += list2[j:]
   else:
      temp += list1[i:]
   return temp
# list1 = [1,2,4,6]
# list2 = [5,6,7,9]
# print(merge(list1, list2))
def merge_sort(l):
   # 列表是一个元素时，不需要拆分
   if len(l) <= 1:
      return l
   # 取到列表的中间 下标
   mid = len(l) // 2
   # 拆分左边列表
   list_left = merge_sort(l[:mid])
   # 拆分右边列表
   list_right = merge_sort(l[mid:])
   return merge(list_left, list_right)
l = [6, 3, 9, 4, 7, 2, 8, 10]
print(merge_sort(l))


