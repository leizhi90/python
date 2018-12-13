# -*- conding:utf-8 -*-
print('%d年%d月%d日'%(2018,3,24))
print('%#o,%#x'%(10,10))
print('%f'%2.1)
print('%g,%g,%g'%(4,0.0000333333333,3455678))
print('%c,%c'%('a',1114110))
print(0x110000)#1114112 %c 数值的最大范围
print("%#.0f"%3.3)
print("%#g"%300)
print("%+d"%500)
print("%05d"%30)
print("%-5d"%30)
print("%10.4f"%1.3)
print("%*.*f"%(5, 4, 1.3))
print('%%w.wrf,%.4f'%3.2)

print('{2}{0}{1}'.format(1,2,'a'))
print('{a}{b}'.format(a=2,b='4'))
print('{0}{{223}}'.format(2))
# 格式说明：!a  !s !r
# print("{0!a}".format("中国"))

# 格式说明：
# [[填充符]对齐方式][符号][#][0][最小宽度][分组选项][.精度][转换类型]
# 左对齐 <
print("{:<10}".format("abc"))
# 右对齐 >
print("{:>10}".format(300))
# 居中对齐 ^
print("{:^10}".format(300))
# 对齐时，可以在对齐符号的前面指定填充符
print("{:#>10}".format(-300))
# = 在+ - 号与数值之间进行填充。
print("{:#=10}".format(-300))

# 符号
# +  对正数，补充前缀+
print("{:+}".format(500))
# -  对正数，不使用+
print("{:-}".format(300))
# 空格， 对正数，使用空格前缀。
print("{: }".format(3000))

# # 与% 的# 意义相同
print("{:#b}".format(500))

# 0与最小宽度
print("{:05}".format(3))
print("{:0>5}".format(3))
# 如果对齐方式的填充符与最小宽度前面指定的0冲突，则以对齐方式前面指定的填充符为准。
print("{:2>05}".format(3))

# 分组选项  , _ 分别使用,或下划线分隔。
print("{:,}".format(1231231234))
print("{:_}".format(1231231234))

# 指定精度
print("{:.5f}".format(100.2))

# 输出格式 转换成%制进行输出。 将数值* 100，尾部加上% ，使用f格式。
print("{:.2%}".format(123))

# 动态模板
# 使用嵌套的{}来传递值。
print("{:10.3f}".format(23.56))
print("{0:{1}.{2}f}".format(23.56, 10, 3))
# 使用关键字的形式，可以具有更好的可读性。
print("{value:{width}.{precision}f}".format(value=23.56, width=10, precision=3))

# 第三种方式：格式化字符串常量，使用f或F前缀。
i = 10
j = 20
c = 3 + 5j
print("{} * {} = {}".format(i, j, i*j))
# 格式化字符串的优势：直接获取外部的变量，无需自行指定。
print(f"{i} * {j} = {i * j}")
print(f"{c.real}")