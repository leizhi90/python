# -*- conding:utf-8 -*-
import math
import random
import sys
print(math.floor(2.9))
print(math.pi)
print(random.randint('3434dssd'))
# 搜索顺序 路径
print(sys.path)
#模块的搜索顺序
#1、内置于解释器的模块
#2、作为脚本运行模块所在的路径（模块.py)
#3、pythonPath 环境变量指定的路径
#4、与python解释器安装相关的路径

#搜索是按以上步骤为准，先找到谁用谁
#LEGB 内建的具有最低的优先级，因此会导致内建名称不可用
sum=0
li=[1,2.3,4]
#sum(li)
#模块的缓存
#为了提高模块的载入速度，.pyc 文件，位于脚本运行的路径下__pucaher__目录下，
#.pyc 是.py编译后的版本，是字节码文件，与平台无关
#1、提高载入速度，不会提高运行速度
#2、作为脚本执行的模块是不会被缓存的，只用通过import导入的才会
#3、.pyc字节码文件可以独立运行
