# -*- conding:utf-8 -*-
import re
a = re.match(r'asd[233]',r'asd34213dd')
print(a.group())
b = re.match(r'de\dw',r'de4ww')
print(b.group())
# 特殊字符
# \d [0-9] str 不仅限还有其他
# 、\D 非数字字符
#\s 空白符，空格 \t \v \n \f str不仅限于这
# \S 除了空白符以外的
# \w [0-9a-zA-Z_] str不仅限于此，可以匹配中文
#\W 除了
# . 匹配所有的除了 \n
#.*?

# * [0~多个  特殊字符 []*************&&&&&&8***
# + [1~多个
# ? 单独使用0 或 1 次
#* + 为贪婪模式 尽可能多  ？ 非贪婪模式最少可能
c = re.match(r's\d*',r's567')
c2 = re.match(r's\d+',r's3456')
print(c.group())
print(c2.group())

#指定次数 {m} {m,n} [m,n] {,n}最多n次 {m,}最少m次
text="""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
t = re.search(r'Beautiful .*',text)
print(t.group())
t1 = re.search(r'Beautiful (.*?\s){4}',text)
print(t1.group())
t2 = re.search(r'Beautiful .*\.',text)
print(t2.group())
# 根据 obvious way 匹配到  'one-- and preferably only one'
t3 = re.search(r'be.*?--obvious way',text)
print(t3.group())
#************************边界相关********************
print(30*'*')
#^开头字符串
"""re.RegexFlag.
   I:不区分大小写
   M：多行匹配
   S：就是.号匹配\n
"""
l = re.search(r'^d','sdfdsafa',re.RegexFlag.M)

tt = re.search(r'^[0-9]*',r'fdfs')
print(tt.group())#是个空，不会报错 + 会报错
#$ 匹配字符串末尾， 写在尾部
tt2 = re.search(r'[0-9]*$',r'sfsd4343')
print(tt2.group())
# \A：仅仅匹配整个文本的起始位置，不理会多行模式
# \Z：仅仅匹配整个文本的结束位置，不理会多行模式

#字符串前边有个\b
#     末尾也有个\b
#*****空格之间也有 个\b
"""
    \b
    匹配 \w与\W之间的 间隔 ，是个 空白 ""
    字符串的第一个字符的前面会有一个  \b
    字符串的最后一个字符的后面会有一个  \b

    例如：
    'You are beautifulaaaa13520341658aaa23123'
    ' 和 Y           之间有一个 \b
    u 和 ' are'      之间会有一个 \b
    'are' 和 ' beau' 之间会有一个 \b
    23123 和 '       之间会有一个 \b

"""
tt3 = re.search(r'\B.+?\B',r'dfd')
print(tt3.group())
tt4 = re.search(r'\b.+?\b',r'd24f3d')
print(tt4.group())
#group(num) 匹配到 第n个 从1开始

#\number 这个 number是正则表达式中前面分组出现（）中匹配的内容的下表
# aa = re.search(r'<(?P<al>\w+?)><(\w+?)>(.*?)</\2></\1>',r'<asd><b>ccccc</asd></b>')
# print(aa.group(2))
n = re.search(r':([0-9]{3})-|:([0-9]{4})-',r'电换:0376-1234567')
print(n.group())
print(n.group(1))
print(n.group(2))

n2 = re.search(r':[0-9]{3,4}-',r'电换:0376-1234567')
print(n2.group())
print(22*'@')
a = re.split(',+| +','a,,,,a,b,bd,a d, a,s')
print(a)
#sub(pattern, repl, string, count=0, flags=0):
"""

"""
print(re.sub('a','b','addfwsfadsa',count=0))
c = re.compile('([0-9]+),')

a = re.search(r'[0-9]+$', 'You are beatifulsdfs434\naaaa13520341658\nssssss3434', re.RegexFlag.M)
print(a.group())