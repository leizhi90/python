# -*- conding:utf-8 -*-
#包
#


#__init__.py 用来标记当前的目录是一个包，而不是一个普通路径

#可以影响导入包的时候，包的搜索优先级，
#__init__.py 作为包的代表，可以写一些初始化语句
import math
import sys
print(math)
print(sys)
import random
print(random)