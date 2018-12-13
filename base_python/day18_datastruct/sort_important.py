# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/12 17:22
#  冒泡排序 相邻的交换位置
def bubble_sort_best_time(l):
   # 循环的次数
   for i in range(len(l) - 1):
      is_change = False
      # 进行元素的 下标 比对
      for j in range(len(l) - i - 1):
         # 这里不要用 >= ，不然就造成了不必要的交换，并且变成不稳定的排序了
         if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            is_change = True
      if not is_change:
         break
#***********************************************************************************
# 选择排序   假设最小的或最大的
def choice_sort(l):
   # 循环次数，从 0 开始，到  倒数第二个下标  结束
   for i in range(0, len(l) - 1):
      # 假定当前循环的第一个元素为 最小元素
      min = i
      for j in range(i + 1, len(l)):
         # 判断 下标 为 j 的元素 是否小于 当前最小元素，是，则替换当前最小元素下标为 j
         if l[j] < l[min]:
            min = j
      # 判断是否第一个元素就是最小的元素，不是，进行交换
      # 这个条件能够成立，必然是由于 i 之后的所有元素中，必然存在比 l[i] 小的元素
      if i != min:
         l[i], l[min] = l[min], l[i]
   return l

#*************************************插入排序**********************************
def insert_sort(l):
   # 从第二个元素，到最后一个元素，循环
   for i in range(1, len(l)):
      # 取到需要 插入 的元素
      key = l[i]
      # 从 当前位置 往前循环到 0
      for j in range(i - 1, -1, -1):
         # 判断下标为 j 的 元素  是否 大于 key ，大于，则往后移动一位
         if l[j] > key:
            l[j + 1] = l[j]
         # 当 下标为 j 的元素，小于等于 key
         else:
            # 把当前选中的 key， 插入到 小于等于key的元素的后面，即 j+1 的下标 位置
            if j != i - 1:
               l[j + 1] = key
            # key 已经找到合适的位置进行插入 ， 退出当前循环
            break
      else:
         # 当 需要插入的 key 是最小的元素时，上面的 for 循环会 循环 下标 j为0，并且不会进行key的插入
         # 在这里 else  把 key 插入到 list 的最前面
         l[0] = key
   return l

#***********************************希尔排序*******************************************
def shell_sort(l):
   step = len(l) // 2
   while step > 0:
      """
          根据 step 进行分组：
          l = [9, 3, 5, 4, 8, 2, 8, 10]
          step = len(l) // 2 
               = 4
          分组：
          [l[0], l[0+step]]  :  [9, 8]
          [l[1], l[1+step]]  :  [3, 2]  
          [l[2], l[2+step]]  :  [5, 8] 
          [l[3], l[3+step]]  :  [4, 10]   
          分为4个组
      """
      for i in range(0, step):
         """
             从每个组的第二个元素开始遍历到最后一个元素
         """
         for j in range(i + step, len(l), step):
            # 每个组使用 插入排序
            key = l[j]
 # 判断组内的 key 是否小于前一个元素 ， j 必须大于等于 step，不然在内容循环的时候 l[j-step]  会越界
            while j >= step and key < l[j - step]:
               l[j] = l[j - step]
               # 下标移动到前面一个元素
               j -= step
            else:
               # l[j-step+step] = key
               l[j] = key
      step = step // 2
   return l
def shell_sort1(l):
   step = len(l) // 2
   while step > 0:
      """
          从 step 开始
          1、比较第一个组的前面2个元素
          2、比较第二个组的前面2个元素
          3、比较第三个组的前面2个元素
          。。。。。。。
          4、比较第N个组的前面2个元素
          5、比较第一个组的前面3个元素
          6、比较第二个组的前面3个元素
          。。。。
          7、比较第N个组的前面3个元素
          。。。。。
          8。比较最后一个组的前面所有元素
      """
      for j in range(step, len(l)):
         # 每个组使用 插入排序
         key = l[j]
         # 判断组内的 key 是否小于前一个元素 ， j 必须大于等于 step，不然在内容循环的时候 l[j-step]  会越界
         while j >= step and key < l[j - step]:
            l[j] = l[j - step]
            # 下标移动到前面一个元素
            j -= step
         else:
            # l[j-step+step] = key
            l[j] = key
      step = step // 2
   return l

#*************************************快速排序****************************************
def quick_sort(l, start, end):
   if start >= end:
      return

   # 将 start，end 赋值给 i，j
   i, j = start, end
   # 取最左边的元素作为中心点 key
   key = l[i]  # 6
   # i 必须小于 j
   while i < j:
      # 从最右边的元素开始 和 key 进行比对，比 key 大，则继续比对 j -= 1
      while l[j] > key:
         j -= 1
      # 以上循环结束，遍历完结或者找到比 key 小的值， 将 l[j] 和 key 所在的 l[i]  进行交换
      if i < j:
         l[i], l[j] = l[j], l[i]
         i += 1

      # [2, 3, 9, 4, 7, 6, 8, 10]
      # 从最左边的元素+1开始 和 key 进行比对，比 key 小，则继续比对 i += 1
      while l[i] < key:
         i += 1

      # 以上循环结束，遍历完结或者找到比 key 大的值， 将 l[i] 和 key 所在的 l[j]  进行交换
      if i < j:
         l[i], l[j] = l[j], l[i]
         j -= 1
      # [2, 3, 6, 4, 7, 9, 8, 10]

   # 将 中心点 左边的 列表数据 进行递归
   quick_sort(l, start, i - 1)
   # 将 中心点 右边的 列表数据 进行递归
   quick_sort(l, i + 1, end)
   return l

#***********************************归并排序**********************************************
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