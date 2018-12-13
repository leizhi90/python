# -*- conding:utf-8 -*-
import math
print(math.fmod(9,7), 9%7,9/7,9//7)
print(math.fmod(9,-7), 9%-7,9/-7,9//-7)
print(math.fmod(-9,7), -9%7,-9/7,-9//7)
print(math.fmod(-9,-7), -9%-7,-9/-7,-9//-7)
assert True,print('sdsdf')
# assert False , print('fffff')
v=2
print((v << 2) + (v << 1) + (v << 0))
print(27>>2)
print(-27<<3)
li = [1, 2, 3]
li2 = [4, 5, 6]
print(li + li2)
print(li * 2)
print([1, 2] == [1, 2])
print([1, 2] is [1, 2])
print(1 is 1)
print([1] is [1])
print(" \t\n".isspace())
print('   '.isspace())