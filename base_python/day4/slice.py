# -*- conding:utf-8 -*-
#切片
li=[1,2,3,4,5,6,7,8,9]
li[2:5]=[99]
l=10
print(l)
print(li)
print(li[::-1])
print(li)
print(li[1:4:2])
print(li[-1:2:1])
print(li[-3::])
li[-2:-1]=[3,4]
print(li)
print([1] is [1])
l=[1,3]
ll=l
print(l is ll)
print(['1'] == ['1'])
li2=[[1,2],[4,5]]
for k in li2:
      for i in k:
            print(i)
print('kkkk',k)
print('iiiii',i)