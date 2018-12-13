# -*- conding:utf-8 -*-
#元素扩大十倍
x =[[1,2,3],[4,5,6]]
print ([[i* 10 for i in item] for item in x])

# 99乘法表放入列表中
print ([str(j)+'*'+str(i)+'='+str(j*i) for i in range(1,10) for j in range(i,i+1)])
# 二维列表转换成一位列表
x=[[1,2,3],[4,5,6]]
print ([i for item in x for i in item])
# 转换
# li=[]
# while True:
#     v=input('请输入数值：')
#     if v=='stop':
#         break
#     li.append(float(v))
# print ([(item-32)/1.8 for item in li])
#
# # 求最大 最小 和 平均值
# while True:
#     v=input('请输入数值：')
#     if v=='stop':
#         break
#
#     li.append(float(v))
# max_value=li[0]
# min_value=li[0]
# s=0
# for item in li:
#     if item>max_value:
#         max_value=item
#     if item<min_value:
#         min_value=item
#     s+=item
# s/len(li)
#
# #判断是否为关键字
# key=input("请输入一个字符：")
# import keyword
# if key in keyword.kwlist:
#     print ('是关键字')
# else:
#     print ('不是关键字')

# 列表的重复
# *  进行的列表重复是一个拷贝{浅拷贝}
# 列表的copy方法与切片执行的都是浅拷贝
li=[1,2]
li2=li*2
li[0]=90
print (li2)
li=[[1,2]]
li=li*2
li[0][0]=100
print(li[1][0])
print (li)
# 浅拷贝的讲解***********
#http://python.jobbole.com/82294/