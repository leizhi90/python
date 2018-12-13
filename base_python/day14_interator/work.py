# -*- conding:utf-8 -*-
# 使用生成器，生成2 ~ 100内所有的质数。
# prime_number=((i for j in range(2,i+1) if i%j ==0 ) for i in range(2,100)  )
def prime_number(n):
   li =[2]
   for j in range(3,n+1):
      for i in range(2,j):
         if j%i ==0:
            break
      else:
         li.append(j)
   yield li
prime = prime_number(10)
v=prime.send(None)
print(v)
# 为现有函数增加一个执行时间的功能，前提是不能修改函数体，也不能修改函数的调用方式。（使用两种方式实现）
import time
def count_time(func):
   def inner():
      start_time = time.time()
      func()
      end_time = time.time()
      print(end_time - start_time)
   return inner
@count_time
def consume_time():
   sum = 0
   for i in range(99999):
      sum +=i
   time.sleep(1)
consume_time()

class Count_time:
   def __init__(self,func):
      self.func = func
   def __call__(self, *args, **kwargs):
      start_time = time.time()
      self.func()
      end_time = time.time()
      print(end_time - start_time)
@Count_time
def consume_time_2():
   sum = 0
   for i in range(99999):
      sum +=i
   time.sleep(1)
consume_time_2()
# 编写一个程序，初始为传入一个点的坐标。然后可以对该点进行移动。在多次移动时，能够保留上一次移动的结果。（使用两种方式实现）
import random
def move(x,y):
   li=[(0,0),(x,y)]
   def move_test():
      nonlocal x,y,li
      x +=random.randint(1,9)
      y +=random.randint(1,9)
      li[1],li[0] =(x,y),li[1]
      return li
   return move_test
m=move(5,5)
print('one',m())
print('two',m())
print('three',m())

class Move:
   def __init__(self,x,y):
      self.x = x
      self.y = y
      self.li=li = [(0, 0), (self.x,self.y )]
   def __call__(self, *args, **kwargs):
      self.x += random.randint(1, 9)
      self.y += random.randint(1, 9)
      self.li[1], self.li[0] = (self.x, self.y), self.li[1]
      return self.li
mm=Move(9,9)
print('one',mm())
print('two',mm())
print('three',mm())