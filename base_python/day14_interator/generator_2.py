# -*- conding:utf-8 -*-
print('sdfs')
def generator2():
   print('这是个生成器')
   def inner():
      v = yield i
      print(v)

   for i in range(10):
      print(i,'+++before  ...........')
      print('暂停之后生成器函数！')
   return inner()
gg=generator2()
print(gg)
print(gg.send(None))
print(gg.__next__())
#print(gg.send(8))
# print(gg.send(9))