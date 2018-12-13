# -*- conding:utf-8 -*-
#str 字符串提供的方法
s='abcdeafag'
print(s.count('a'))
print(s.count('a',44,11))
print(s.index('af'))
print(s.find('d'))
print('join',s.join('12  34'))#每个空格也是
print(s.replace('a','4',1))
print('  w e r  '.strip())
print('aabbbabsdf s f habsbaaaa'.strip('abs'))#df s f h******
print('aasfdsa'.lstrip('a'))
print('aasdsfa'.rstrip('a'))
print('2018-03-25'.split('-'))
print('2018-03-25'.split('-',1))
print('a-s-d-f--a----sa'.split('-'))
print('a-d-ssds--sa---a--a'.rsplit('-'))
print('a\nb\ncd'.splitlines(True))
print('abcde'.partition('e'))
print('adc'.ljust(5,'+'))
print('abd'.center(6,'&'))
# 判断当前字符串中的每一个字符是否都是字母型字符，是返回True，否则返回False。
print("asd汉字3".isalpha())
# 判断当前字符串中的每一个字符是否都是数值型字符，是返回True，否则返回False。
print("234二三四".isnumeric())
# 判断当前字符串中的每一个字符是否都是数字型字符，是返回True，否则返回False。
print("234234二三四".isdigit())
# # 判断当前字符串中的每一个字符是否都是十进制数字型字符，是返回True，否则返回False。
print("234".isdecimal())
# 关于isnumeric，isdigit与isdecimal
# 范围：isnumeric > isdigit > isdecimal
# 判断当前字符串是否是合法的标示符。是返回True，否则返回False。
print("ads#f".isidentifier())
# 判断当前字符串是否是大写形式，是返回True，否则返回False。
# print("ABC".isupper())
# 判断当前字符串是否是小写形式，是返回True，否则返回False。
# print("abc".islower())
# 判断当前字符串中的字符是否都为空白符，是返回True，否则返回False。
print(" \t\n".isspace())
print('sdfsf''sfsf')
print(id(''))
print(id(""))
print(id('  '))
print(id('     '))
d={"":1,"  ":4,False:3,True:4,None:2,'d':None}
print(d)