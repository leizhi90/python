# -*- conding:utf-8 -*-
# 将二维列表中每个在[5, 10]之间的元素保留，并且要保证每个一维列表中原有元素的和大于25。（一条语句）


li=[[3,24,34,7],[2,3,5],[3,6,8,9,9],[1,5]]
print ( [[i for i  in item  if i in range(5,10) if sum(item)>25  ] for item in li])
print ([[i for i in item if 5<=i<=10]for item in li if sum(item)>25])
# 实现二维列表（矩阵）的转置（m * m）。（一条语句）

li2=[[1,2,3],[4,5,6],[7,8,9]]
print ([[i for i in enumerate(item) ] for item in li])
print (list(map(list,zip(*li2))))
# r=[]
# for i in range(0,3):
#     t=[]
#     for item in i:
#         t.append(item[i])
#     r.append(t)
# print (r)
li=[[1,2,3],[4,5,6],[7,8,9]]
print ([[item[i] for item in li]for i in range(0,3)])

# del是否可以应用于元组，字符串与字节类型，为什么？
# 不可以，一旦定义，是不可变的
# 编写程序，能够判断一个str中是否仅包含阿拉伯数字0 ~ 9，或是否仅包含小写字母（a ~ z）。
s=''
for c in s:
    if 48<=ord(c)<=57:
        continue

# 对元组进行复制，会发生什么情况？总结。
import copy
a=[1,2,3]
b=copy.copy(a)
print (b is a)
#元祖元素都是不可变元素，都不会拷贝，而是直接将元素返回
t=(1,2,3)
s=copy.copy(t)
print (t is t)
w=copy.deepcopy(t)
print (w is t)

t1=([1,2,3])
t2=(1,3,2,[2,34])
s1=copy.copy(t1)
print (s1 is t1)
w1=copy.deepcopy(t1)
print (w1 is t1)
#元祖里面的元素原本不可变则元祖不可变 如果有可变元素 则可变元素可变 元祖可变 引用的仅是地址


# 以列表，元组类型分别测试，x += y与x = x + y是否存在差异性，并总结其原因。
x=[1,2,3]
y=[4,5,6]
print (id(x))
x += y
print (id(x))
x=x+y
print (id(x))
#两者的区别在于


x=(1,2,3)
y=(4,5,6)
print (id(x))
x +=y
print (id(x))
x=x+y
print (id(x))

# 证明isnumeric范围最大，isdigit其次，isdecimal最小。

# 0 48  9 57  a 97 A 65
#0x110000 0~10ffff
# for i range(oX110000):
#     c=chr(i)
#     if c.isdigit() and  not c.isnumeric():
#         print ("digit 不全是 numeric")
#         break
# else:
#     print ("digit 都是 numeric")
l=[[1,2,3],[4,5,6],[7,8,9]]
ll=[]
for i in range(len(l)):
      t = []
      for item in l:
            t.append(item[i])
      ll.append(t)
print(ll)
print([[item[i] for item in l]for i in range(len(l))])