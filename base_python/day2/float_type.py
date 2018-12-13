# -*- conding:utf-8 -*-
# 整数类型前面不能存在0，浮点类型可以
#x=0232
x=003.5
#整数类型可以支持四种进制，浮点类型仅支持十进制
# 浮点类型也可以使用科学计数法来表示
# float类型是存在取值范围的，具体的范围与实现相关。对于CPython，使用C中的double类型来进行表示。
import sys
# 通过sys模块的float_info可以获取float类型的相关信息。
print(sys.float_info)
# 最大值
print(sys.float_info.max)
# 最小值
print(sys.float_info.min)
for i in range(0,256):
      print(chr(i))