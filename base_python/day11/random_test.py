# -*- conding:utf-8 -*-
#随机数
#说明：并非是真正的随机数，伪随机数
import random

print(random.random())#[0,1)
print(random.random.__doc__)
print(random.randint(1,5))#[a,b]
print(random.randrange(5))#[0,3)
print(random.randrange(5,9,3))#步长默认1
#以上空区间会错误，uniform不会
print(random.uniform(1.3,1.4))#[a,b]浮点数
print(random.uniform(9,8))
print(random.choice([2,3,4,5]))
print(random.choices([1,4,3,2],k=8,weights=[0.1,0.1,0.1,0.7]))#放回抽样
print(random.sample([2,3,45,6],2))#不放回
li=[1,2,3,4,5]
random.shuffle(li)#就地洗牌
print(li)