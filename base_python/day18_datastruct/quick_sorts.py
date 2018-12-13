# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/12 15:04
def quick_sort1(array, left, right):
   if left >= right:
      return
   low = left
   high = right
   key = array[low]
   while left < right:
      while left < right and array[right] > key:
         right -= 1
      array[left] = array[right]
      while left < right and array[left] <= key:
         left += 1
      array[right] = array[left]
   array[right] = key
   quick_sort1(array, low, left - 1)
   quick_sort1(array, left + 1, high)
li = [6,5,4,1,2,3,0]
quick_sort1(li,0,6)
print(li)
print(33*'*')
def quick_sort2(array, l, r):
   if l < r:
      q = partition(array, l, r)
      quick_sort2(array, l, q - 1)
      quick_sort2(array, q + 1, r)
def partition(array, l, r):
   x = array[r]
   i = l - 1
   for j in range(l, r):
      if array[j] <= x:
         i += 1
         array[i], array[j] = array[j], array[i]
   array[i + 1], array[r] = array[r], array[i + 1]
   return i + 1
print(33*'--')

def quick_sort3(array, l, r):
   if l >= r:
      return
   stack = []
   stack.append(l)
   stack.append(r)
   while stack:
      low = stack.pop(0)
      high = stack.pop(0)
      if high - low <= 0:
         continue
      x = array[high]
      i = low - 1
      for j in range(low, high):
         if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
      array[i + 1], array[high] = array[high], array[i + 1]
      stack.extend([low, i, i + 2, high])

#quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

print(33*'^ ')
def quick_sort(l, start, end):
    if start >= end:
        return
    # 将 start，end 赋值给 i，j
    i, j = start, end
    # 取最左边的元素作为中心点 key
    key = l[i]  #  6
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
    quick_sort(l, start, i-1)
    # 将 中心点 右边的 列表数据 进行递归
    quick_sort(l, i+1, end)

    return l

l = [6, 3, 9, 4, 7, 2, 8, 10]
print(quick_sort(l, 0, len(l)-1))
