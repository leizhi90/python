# -*- conding:utf-8 -*--
#生成器for 迭代循环一次性显示，生成器不会一次性计算出所有结果，而是按需分配
#实现生成器：使用生成器表达式 使用生成器函数
lig = (i**2 for i in range(10))
print(lig)
lig.__next__()
for i in lig:
   pass
   #print(i)
print(lig)
#lig.__next__()#是迭代器不是迭代对象
#生成器的底层就是迭代器产生的，可以作为迭代器用
def f():
   print('this is gener function')
   for i in range(11):
      yield i
      print('after stop going gogogo')
      #print(i)
      #yield
g=f()
print(g.__next__())
print(g.__next__())
#生成器函数遇到yield之后会暂停，当执行下一个next函数会继续执行生成器函数
print('*'*11)
def fbi():
   a=0
   b=1
   for i in range(11):
      a,b=b,(a+b)
      yield a,b
b=fbi()
for item in b:
   print(item)
# for i in range(11):
#    print(b.__next__())

#生成器函数和普通函数的区别
#生成器函数会包含一个以上的yield
#被调用时，返回一个迭代器，当调用next方法才会执行
#一旦函数执行的时候遇到yield，就会暂停
#当生成器函数迭代终止时，如果调用者仍在调用，会抛出异常StopIteration
print(17*'*')
def genera():
   for i in range(10):
      print(i)
      if i==6:
         yield i
f=genera()
f.__next__()
print(16*"&")

def generator2():
   print('这是个生成器')
   for i in range(10):
      print(i,'+++before  ...........')
      v = yield i
      print(v)
      print('暂停之后生成器函数！')
gg=generator2()
print(gg.send(None))
print(gg.__next__())
# print(gg.send(8))
# print(gg.send(9))
