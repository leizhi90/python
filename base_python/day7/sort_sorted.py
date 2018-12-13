# -*- conding:utf-8 -*-
# sorted 是内建函数
# list sort list方法
#区别
# sorted 返回排序之后的结果，原列表不会改变
# sort 是 就地排序，会修改原列表
li= [3,'54',45,'2342d']
#li.sort() 不能直接排序 类型不支持
# ***源码***def sort(self, key=None, reverse=False)
# key参数，指定排序规则
#1、容器中元素类型不支持大小比较
# 2、容器中的元素类型支持比较，但是不是我们想要的排序方式
#key 指定一个函数，该函数有一个参数，具有一个返回值，每个元素调用一次该函数，将元素作为实参进行传递，分别获得返回的结果，然后根据每个元素调用函数的返回值进行排序
# reverse 是否对排序的结果进行反转（逆序），默认false

#自定义排序函数
def order(item):
      return str(item)
li2=[3,'we',124,33,30,'love',520]
li2.sort(key=order)
print(li2)
#li.sort() 会改变原有的列表
#
li3 = sorted(li2,key=order,reverse=True)
print(li3)
# 完全可以这样做 abs str 内建函数
li4=sorted(li2,key=str)
