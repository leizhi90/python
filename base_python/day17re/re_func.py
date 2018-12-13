# -*- coding:utf-8 -*-
import re
"""
    search   函数
    根据 正则表达式 到文本中进行匹配，匹配第一个文本，成功后返回
    匹配的文本， 通过 group() 获取整个文本，  group(下标)  获取 正则表达式 中 () 分组的内容
    compile  函数
    返回一个 pattern 对象，通过这个对象 进行 search
    和
    search 函数  的区别就是
    需要手动调用 compile
    内部实现是：
    compile:   return _compile(pattern, flags)
    search ：  return _compile(pattern, flags).search(string)
    compile 的应用场景：
    同一个正则表达式的模式，需要到多个文本中进行匹配，
    使用 compile， 可以不用多次 在 search 函数中执行 _compile(pattern, flags)
    即 return _compile(pattern, flags) 的对象 可以复用的情况下， 使用 compile
"""
text = '我的家庭电话是:0731-1234567'
p = r':([0-9]{3})-|:([0-9]{4})-'
c = re.compile(p)
a = c.search(text)
print(a.group())
print(a.group(1))
print(a.group(2))
print("------------------------------")
a = re.search(p, text)
print(a.group())
print(a.group(1))
print(a.group(2))
print(44*'*')

"""
    match 函数
    用于匹配 文本 是否符合 正则表达式 的匹配， 从字符串头开始进行匹配
    match('正则表达式')
    等同于 
    search('^正则表达式')
"""
a = re.match('我的(.*?)电话是:0731-1234567', text)
print(a.group())
print(a.group(1))

a = re.search('^我的(.*?)电话是:0731-1234567', text)
print(a.group())
print(a.group(1))
print(44*'@')
"""
    findall  函数
    查找所有，返回值是 list
    多个分组时， 返回的list中的内容是 元组 ，如  [('1354789548', '你的'), ('13265475214', '他的')]

    即使是匹配到一个成功的文本，返回的也是list，不过list中只有 1 个元素
    匹配不成功，返回一个 [] 空的列表
"""
a = re.search('([0-9]+),(.{2})', '我的电话13547896548,你的电话13265475214,他的电话139875454,')
print(a.group())
print(a.group(1))
print(a.group(2))
a = re.findall('([0-9]+),(.{2})(.{2})', '我的电话1354789548,你的电话13265475214,他的电话139875454,')
print(a) # [('1354789548', '你的', '电话'), ('13265475214', '他的', '电话')

"""
    finditer 函数
    返回一个 迭代器 对象， 迭代的 对象是 match
"""
i = re.finditer('([0-9]+),(.{2})(.{2})', '我的电话1354789548,你的电话13265475214,他的电话139875454,')
for a in i:
    print(a.group())
    print(a.group(1))
    print(a.group(2))
    print(a.group(3))
print(44*'--')
"""
    split 函数
    对目标文本进行 拆分 ，通过 正则表达式的方式
"""
# 字符串的方式
l = 'a,,b,,c,,,,d'.split(',')
print(l)

a = re.split(',+', 'a,,b,,c,,,,d')
print(a)
print(44*'++')
#以 1或N个 , 或者 1或N个 空格 进行 拆分 字符串
a = re.split(',+| +', 'a,,b,,c,,,,d   dd')
print(a)

"""
    sub() 函数
    参数 pattern, repl, string, count=0, flags=0
    pattern ： 正则表达式
    repl : 要替换的文本
    string: 要进行匹配的文本
    count: 替换几次
    flags：正则表达式的控制标记

    在指定文本中 替换符合 正则表达式 的内容
"""
a = re.sub(',+', '|', 'a,,b,,c,,,,d', count=2)
print(a)


"""
    使用compile
    pos 
    endpos
"""
c = re.compile('([0-9]+),(.{2})')
a = c.search('我的电话13547896548,你的电话13265475214,他的电话139875454,')
print(a.group()) #  13547896548,你的
print(a.span()) # (4, 18)

a = c.search('我的电话13547896548,你的电话13265475214,他的电话139875454,', 17)
a = c.search('的电话13265475214,他的电话139875454,', 0)
print(a.group()) # 13265475214,他的
print(a.span()) #

a = c.search('我的电话13547896548,你的电话13265475214,他的电话139875454,', 17)
print(a.group())
print(a.span())