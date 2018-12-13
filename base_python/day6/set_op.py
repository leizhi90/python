# -*- conding:utf-8 -*-
# in not in
s={1,2,3,4,5}
s2={4,5,6,7}
#判断集合中是否存在
print (2 in s)
print (2 not in s)

# & 返回两个集合的交集，相当于x.intersection（y）
print (s & s2)
# | 返回两个集合的并集 ,相当于s.union(s2)
print (s | s2)
# - 返回两个集合的差集

#^ 返回两个集合的对称差集

#比较运算 == != > >= < <= is is not
# == ！= 判断两个集合中的元素是否一致

# < > 不是像序列那样进行对位的比较，而是进行父集与子集比较，是否包含的比较
print (s>{1,2})


# 布尔运算 and   or not
#集合转换为布尔类型，如果有元素为True 否则False
print (bool({1,2}))
print (bool(set()))


#集合推导式

print ({i *i for i in range(10)})