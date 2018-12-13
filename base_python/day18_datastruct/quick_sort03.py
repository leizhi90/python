# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/13 9:14
def quick_sort_by_temp_list(l):
    # 递归的终止条件， 当list 只有1个元素或者为空时，终止递归
    if len(l) <= 1:
        return l
    # 左边的临时 list
    left_list = []
    # 右边的临时 list
    right_list = []
    # 取第一个元素作为中心点 key
    key = l[0]
    # 从第二个元素开始和 key 进行对比
    for i in range(1, len(l)):
        # 比key 大元素，放入到 右边的list，是 升序 排序
        if l[i] > key:
            right_list.append(l[i])
        else:
            left_list.append(l[i])
    # 对左边 list 和右边的 list 分别进行递归，最后和 key 进行list的 粘连 ，  返回
    return quick_sort_by_temp_list(left_list) + [key] + quick_sort_by_temp_list(right_list)
