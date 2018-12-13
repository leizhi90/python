# -*- conding:utf-8 -*-
import re

"""
re 模块正则表达式的匹配
匹配文本有两种格式
1、str 对应的 正则模式必须是str
2、bytes 对应的正则模式必须是bytes
"""

a = re.search('1d','ew31d1dewrw')
#AttributeError: 'NoneType' object has no attribute 'group' 空值 None没有任何属性
print(a)
print(a.group())
# 特殊字符 . 一个字符str（包含中文）  gbk 2个字节 utf-8 三个 utf-32 四个
b = re.search(r'w\.4','w.4wew')
print(b.group())
#r 正则表达式前面需要r python编译器原
c = re.search(r'12\\aa',r'ada12\aaaaa')
d = re.search('12\\\\aa',r'12\aaaadf')
print(c.group())
print(d.group())
# []匹配中括号内的任意一个字符 asscis 码中连续的一部分
e = re.search(r'3[0~9a~zA~Z中国]',r'3中7886532314')
print(e.group())

#[^]不
f = re.search(r'23[^1234]',r'238')
print(f.group())

#\d str类型匹配十进制数字不只是0~9 bytes类型匹配[0-9]
