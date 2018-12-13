# -*- conding:utf-8 -*-
# 错误：程序在编译时期出现的问题
# 异常：程序执行的时候发生的
#Exception 所有异常的父类
# basException 扩展了Exception
#常见的异常都是扩展了的basException
#indentation 缩减异常
class F:
   def __init__(self):
      self.name = 'aa'
# unboundLocalError 未绑定局部变量异常
#assertionError 断言异常
#assert 7>11,'说个说的'
# noduleNotFoundError 模块为找到
#keyError 字典中key 不存在
#recursionError 递归异常
#stopiteration
li=[2]
it=li.__iter__()
# print(it.__next__())
# print(it.__next__())
#valutError
#syntaxError 语法错误
try:
   print(int(2))
   print('ininininn ')
except KeyError:
   print('sdfs')
   raise
# except ValueError as v:
#    print(v.args)
else:
   print('没有异常时 走的')
   print('else ... else')
finally:
   print('finally,最后一定会执行的代码块！')

#raise  ***************
def register(age):
   if age > 0:
      print('注册成功！')
   else:
      print('年龄输入的是负数：')
      raise print('年龄为正数')
register(-2)
print('goto....')

#else 在最后面
# finally总是会执行的尝试
# finally是否真的总是会执行呢，我们现在做出如下的尝试：
# 在循环中，通过break尝试跳过finally语句块。
# 在方法中，执行return尝试跳过finally语句块。
# 调用sys模块的exit方法，尝试跳过finally语句块。
# 从而发现，finally语句块确实总是会得到执行。在try中使用break、return或其他可能会跳过finally语句体的语法时，程序会检测当前是否存在finally，如果存在，则会首先执行finally语句体，然后才能放心的跳出或结束程序。




