# -*- conding:utf-8 -*-
class MyException(Exception):
   def __init__(self,value):
      self.value=value
   def ex(self):
      try:
         int(age)
      except TypeError:
         print('请输入一个数字')
      if age < 0:
         print('年龄大于零！')
try:
   raise MyException('自定义异常')
except MyException as me:
   print(me.value)
   print(me.args)

#输入一个年龄，如果是数字，且>0注册成功，否则返回异常输出，其中异常自定义
mye =MyException('请输入一个数字')

def registion(age):
   try:
      int(age)
   except MyException(age) as me:
      me.ex()
   else:
      print('注册成功！')

while True:
   age = input('请输入年龄：')
   registion(age)