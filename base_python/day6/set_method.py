# -*- conding:utf-8 -*-
s=set()
# 向集合中加入指定元素，已经存在的无法加入
s.add(5)
s.add(7)
print (s)
#删除参数指定的元素，如果没有出错KeyError: 51
#s.remove(51)
# 删除 如果没有 None
s.discard(33)
print (s)

#删除并返回一个元素，(具体是哪一个，不清楚，空集合会产生错误
s.pop()

#删除集合中所有元素
s.clear()
#对当前集合拷贝
s2=s.copy()
#返回在当前集合中存在，在参数集合中不存在的元素构成的集合（返回两个集合的差集
c={1,3,4}
print (c.difference({3,4,6}))

# 原有集合会不会变
c.difference_update({2,3})
print (c)

#返回在当前集合中，同时也在参数集合中的元素构成的集合 返回两个集合的交集
# s.intersection
# s.intersection_update
# s.union()
#返回当前集合存在，会在参数集合中存在，但是不同时存在
