# -*- conding:utf-8 -*-
#分组相关
"""
    ()
    进行分组，在程序中，获取特定的数据，丢弃一些我们不关注的信息
    通过 group(下标) 来获取，记住， 下标 从 1 开始！！！
"""
import re
a = re.search(r'beautiful ([0-9]*?) phone ([0-9]*)', 'You 12457896532 are beautiful 13520341658 phone 13546985752')
print(a.group())
print(a.group(1))
print(a.group(2))
print(33*"*")
"""
    \number   
    这个 number 就是 正则表达式 中 前面的分组， 这个分组就是前面出现的 () 中匹配的内容  的下标， 从 1 开始
    更直白的讲，就是 \1  就是前面的第一个 () 中匹配的内容   \2 就是前面的 第二个 () 内匹配的内容
"""
a = re.search(r'<(\w+?)><(\w+?)>(.*?)</\2></\1>', '<area><a>测试数据</a></area>')
print(a.group())
print(a.group(1))
print(a.group(2))
print(a.group(3))
print(33*'*')
"""
    (?:表达式)   
    匹配()内的字符，但是不会进行分组。()内匹配的内容也无法单独提取，或者在后面使用\number引用。
"""
a = re.search(r'<(\w+?)><(?:\w+?)>(.*?)</\w+?></\1>', '<area><a>测试数据</a></area>')
print(a.group())
print(a.group(1))
print(a.group(2)) # 会匹配到  测试数据
print(33*'*')

"""
    (?P<name>表达式)   (?P=name)
        定义             引用
    进行分组
    也和 \number 一样的引用，第二种引用方式是 (?P=name)
    这个 小括号的() 分组， 既拥有 下标 ，也拥有 别名，  2种方式都可以引用

    在很短的正则表达式中，一般使用 下标 进行引用就可以了
    但是，在一些复杂的正则表达式中，很多个分组，用 下标 容易混乱， 
    那么使用具有描述意义的 别名 来引用就更加的清晰明了
"""
a = re.search(r'<(?P<ele1>\w+?)><(\w+?)>(.*?)</\2></(?P=ele1)>', '<area><a>测试数据</a></area>')
print(a.group())
print(a.group(1))
print(a.group(2))
print(a.group(3))

print(33*'@')
"""
    |
    或的意思的， 连接 多个不同的表达式 ，满足其中一个条件即可
    r'<are>|<b>|<c>|<a>'
    的意思 展开就是： <are> or <b> or <c> or <a> 等式中有一个条件匹配成功
    多个 | 连接的表达式之间， () 分组的下标是共享的，即 前面的表达式即使没有匹配成功，也一样会占用掉分组的下标
    譬如： r':([0-9]{3})-|:([0-9]{4})-'  中 ([0-9]{4}) 匹配到的内容，需要使用  group(2) 来获取
"""
a = re.search(r'<area>|<b>|<c>|<a>', '<area><a>测试数据</a></area>')
print(a.group())

a = re.search(r':([0-9]{3})-|:([0-9]{4})-', '电话:0376-12345667')
print(a.group())
print(a.group(1))
print(a.group(2))

