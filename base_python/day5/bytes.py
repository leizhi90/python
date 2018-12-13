# -*- conding:utf-8 -*-
#字节类型 bytes
# bytes 是由若干个字节构成的，每个字节的取值范围为0~255 [0,255]
# bytes使用b或B前缀的字符串进行表示
s='abc'
k=b'abc'
print (type(s),type(k))
# bytes常量只能包含单字节字符，不能包含多个字节的字符
# k=b'abc行'
#bytes 是不可变对象
#k[0]=b'x'
# bytes 支持索引，切片，运算，遍历
#索引
print (k[1])
#切片
print (k[0:2])
# 运算
print (b'abc'+b'cde')
print (b'abc'*3)
print (b'ab' in b'abde')
print (b'abc' > b'aba')
#bytes 转换成布尔类型，如果bytes类型含有元素，则为true，否则为false
print (bool(b''))
print (bool(b'dd'))

for item in b'abc':
    print (item)
b=b'acd'
print (b'abcd'.upper())
c=b.upper()
b=b.upper()
print(b)
print(c)
print(1+1)
# 链接学习
#https://segmentfault.com/a/1190000004450876