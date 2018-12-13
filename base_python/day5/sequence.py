# -*- conding:utf-8 -*-
x=tuple('ssd')
print(x)
xx=tuple(b'ssss')
print(xx)
x=list()
li=[1,2,3,4,5]
for i,v in enumerate(li,0):
      print(i,v)
# zip函数，能够同时遍历多个可迭代对象。
name = ["张", "王", "李", "赵"]
age = [51, 60, 71, 82, 90]
h=[1,2,3,4,5,5,6,7]
# zip 每次循环返回一个元组。
for item in zip(name, age,h):
    print(item)

# 如果zip中涉及的多个可迭代对象长度不一致，则以长度短的为准。当其中一个可迭代对象没有元素时，
# 循环就会停止。
for n, a in zip(name, age):
    print(n, a)