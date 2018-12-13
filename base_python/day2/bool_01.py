# -*- conding:utf-8 -*-
# 布尔类型
# 逻辑上的运算
#and or  not
print(not 2==1)
# and or 链接的表达式不一定是布尔类型，可以是任何类型
# 对于and or 结果总是会返回两个表达式中的一个
print(4 and 3)
print(0 and 3)
print(4 or 3)
print( True and False)
# 对于and，当第一个表达式为False时（或者转换之后为False），返回第一个表达式的值。
# 否则，返回第二个表达式的值。
print(4 and 3)
print(0 and 3)
# 对于or，当第一个表达式的值为True时（或者转换之后为True），返回第一个表达式的值，
# 否则，返回第二个表达式的值。
print(4 or 3)
print(0 or 3)
#*** 谁个能决定 返回谁**********
# and 与 or的短路
# 当计算and或or，第一个表达式就能够决定整个表达式值的时候，就不会再进行计算第二个表达式。
# 这种现象就是and与or的短路。

# 证明and与or的短路。
True and print("执行1")
False and print("执行2")
True or print("执行3")
False or print("执行4")
d={None:1,True:2,False:4}
print(d)
# *********布尔类型（bool）是整数类型(int)的子类型。
# 实际上，True就是1，False就是0。***********************
print(5 == 1)
print(True == 1)
print(False == 0)
print(True==3)
print(id(1))
print(id(True))
print(5 * 3)
# 布尔类型也可以参与数学上的数值运算。
# 但是，我们不要这样去做，因为会造成不必要的混淆。
# 我们应该把布尔类型应用到逻辑判断的领域，而不要应用到数值计算的领域。
print(True + 3)

import decimal
x = decimal.Decimal(0.1)
y = decimal.Decimal(0.1)
print(x == y)
print(x is y)
