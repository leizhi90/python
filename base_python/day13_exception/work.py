# -*- conding:utf-8 -*-
# 编写程序，验证AttributeError的产生场合。
class F:
   pass
#print(F.name)
f=F()
#print(f.age)
# 输入一个日期，格式为年/月/日，如果格式正确，
# 则返回该日期是当年的第几天，否则日期默认为今天，返回今天是当年的第几天。
from datetime import datetime,date
def days(str):
   try:
      time = datetime.strptime(str,'%Y/%m/%d')
      d=time.timetuple().tm_yday
   except ValueError as  ve:
      print(ve)
      time = datetime.now()
      return time.timetuple().tm_yday
   else:
      return d

print(days('2018/4/2'))
import time
def time_days(str):
   try:
      dt=time.strptime(str,'%Y/%m/%d')
   except ValueError:
      dt=time.localtime()
   return dt.tm_yday

# 实现银行提款程序，并自定义一个异常类InsufficientFundsError。
# 当余额不足时，产生该错误。并且调用端能够处理捕获该错误。
class InsufficientFundsError(Exception):
   def __init__(self,msg):
      self.msg=msg
class Card:
   def __init__(self,id,name,money):
      self.id=id
      self.name=name
      self.money=money

class ATM:
   def __init__(self,card):
      self.card=card
   def draw_money(self,number):
      if self.card.money < number:
         raise InsufficientFundsError('余额不足')
      self.card.money -= number
      return self.card.money
c=Card('001','lz',666)
atm=ATM(c)
try:
   atm.draw_money(1000)
except InsufficientFundsError as ie:
   print(ie.msg)
else:
   print(c.money)

# 将一个列表中所有元素转换成浮点类型，如果不能转换，则丢弃该元素。
def train_float(li):
   l=[]
   for i in li:
      try:
         i = float(i)
      except ValueError:
         pass
      else:
         l.append(i)
   return l
li=['2',3,4,'r33','u33']
print(train_float(li))
