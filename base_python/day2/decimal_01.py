# -*- conding:utf-8 -*-
# 由于浮点类型是不精确的，我们计算的时候可能会出现偏差，如果
# 想要精确的浮点类型计算结果，可以使用Decimal类型进行计算。

import decimal

x = decimal.Decimal(0.1)
y = decimal.Decimal(0.2)
print(x)
print(y)
print(x + y)

# 使用字符串形式传递准确的数值（浮点值）
x = decimal.Decimal("0.1")
y = decimal.Decimal("0.2")
print(x)
print(y)
print(x + y)

print(0.1 + 0.2)

# 获取decimal计算的上下文环境
context = decimal.getcontext()
# prec 表示计算的精度。默认为28。
print(context.prec)
# 我们可以设置prec属性，进而改变计算的进度。
context.prec = 5

x = decimal.Decimal(0.1)
y = decimal.Decimal(0.2)
print(x + y)
x = decimal.Decimal(0.1)
y = decimal.Decimal(0.1)
print(x == y)
print(x is y)