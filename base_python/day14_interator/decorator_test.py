# -*- conding:utf-8 -*-
#闭包 在内部函数中调用了外部函数的变量
#条件：嵌套函数  内部函数会访问到本地封闭范围之外的变量
# __clouser__
def out():
   x = 0
   def inner():
      print(x)
   return inner
print(out().__closure__)
def on_duty(name):
   times = 0
   def inner():
      nonlocal  times
      times += 1
      print('%s第%s次上班'%(name,times))
   return inner
duty=on_duty('lz')
duty()
duty()
duty()
#闭包类 重写call方法，
class OnDuty:
   def __init__(self,name):
      self.name=name
      self.times=0
   def __call__(self, *args, **kwargs):
      self.times +=1
      print('%s第%s次上班' % (self.name, self.times))
d=OnDuty('lz')
d()
d()
d()
print('$'*25)

#装饰器：用来修饰其他函数，扩展原来函数的功能，装饰器本身也是一个函数，
#装饰器传入的一定是被修饰的函数， 返回的也是函数名
from datetime import datetime
def new_f(func):
   def inner(name):
      print(datetime.now())
      func(name)
   return inner

@new_f
def du(name):
   print(name+'&&&&&&')
new_f(du)('lz')
du('lz')

#装饰器优化，含有的参数不定，
#如果装饰器需要参数，不能加载被修饰函数的那个层级上，只能在装饰器的外侧使用闭包

#类装饰器
class Checkin:
   def __init__(self,func):
      self.func=func
   def __call__(self, *args, **kwargs):
      print(datetime.now())
      self.func(*args,**kwargs)
