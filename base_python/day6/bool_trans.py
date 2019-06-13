# -*- conding:utf-8 -*-
#布尔类型的转换
# 在Pyton中，任何类型都可以转换成布尔类型
#任何类型都可以用在if  while 的条件判断中国，不需要线上转换
# 一切都可以隐式转换

# int 类型 非0 为真 0 为False
print (bool(2),bool(0))
# float
print (bool(4.3),bool(0.0))

# comple
print (bool(5j),bool(0j))
#序列（list tuples str bytes
# 空为 False

#字典 集合
# 空为false

#None 转换成 False
print (bool(None))
print (type(None))
