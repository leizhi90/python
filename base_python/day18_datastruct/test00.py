# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/14 19:27
li = [5,1,8,3,2,7,6]
def bubble_sort(li):
    for i in range(len(li) -1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1],li[j]
    return li
#print(bubble_sort(li))
def choice_sort(li):
    for i in range(len(li)-1):
        min = i
        for j in range(i+1,len(li)):
            if li[min] > li[j]:
                min = j
        if min != i :
            li[i],li[min] =li[min],li[i]
    return li
#print(choice_sort(li))
def insert_sort(li):
    for i in range(1,len(li)):
        key = li[i]
        for j in range(i-1,-1,-1):
            if key < li[j]:
                li[j+1] = li[j]
            else:
                if j - i !=1:
                    li[j+1] =key
                break
        else:
            li[0] = key
    return li
#print(insert_sort(li))
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
    quick_sort(l, start, i-1)
    quick_sort(l, i+1, end)
    return l