# -*- conding:utf-8 -*-
# 使用random.random函数实现返回[a, b]或[a, b)之间的整数。(a <=b)
import random
import math
def random_test(a,b):
   new_n=random.random()*(b-a)+a
   if a <= math.ceil(new_n):
      pass
   return math.ceil(new_n)
   #return int(new_n)
print(random_test(6,9))

# 自行计算常数e的近似值。（1 / 0! + 1 / 1! + 1 / 2! + 1 / 3! + ……）
def e_v():
   s=0
   for i in range(1000):
      s +=1/math.factorial(i)
   return s
print(e_v())
print(math.e)
# 编写一个抽奖的函数，返回（0-3），0表示未中奖，
# 1-30表示1-3等奖。1等奖概率为1%，二等奖5%，三等奖10%，其余为未中奖。
def catch():
   li=[0,1,2,3]
   c=random.choices(li,k=1,weights=[84,1,5,10])
   if 0 in c:
      print('0--未中奖')
   elif 1 in c:
      print('一等奖')
   elif 2 in c:
      print('二等奖')
   elif 3 in c:
      print('三等奖')
catch()
# 输入某一天，返回该天距离下一个国庆还有多少天。如果当天就是国庆，则返回0。
from datetime import date,datetime
def national_day(str):
   now_day=datetime.strptime(str,'%Y-%m-%d')
   na_day=now_day.replace(month=10,day=1)
   if na_day >= now_day:
      return (na_day - now_day).days
   else:
      na_day=na_day.replace(year=na_day.year+1)
      return (na_day - now_day).days

print(national_day('2018-9-1'))
# 输入某一天（年月日），返回该天是星期几。
def day_weekday(str):
   input_day=datetime.strptime(str,'%Y-%m-%d')
   i=input_day.weekday()
   li=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
   return li[i]
print(day_weekday('2018-3-30'))
# 输入年月，打印该月份的日历。
li=[['日','一','二','三','四','五','六']]
def calad(str):
   month=12
   input_day = date(year=2018,month=month,day=1)
   if month==12:
      days=31
   else:
      next_m = input_day.replace(month=month + 1)
      days = (next_m - input_day).days
   week_day=input_day.weekday()
   l=[]
   for i in range(week_day):
      l.append(' ')
   for i in range(1,days+1):
      l.append(i)
   if (days+len(l))%7==0:
      pass
   else:
      for i in range(7-(days+len(l))%7):
         l.append(' ')
   for i in range(math.floor(len(l)/7)):
      items = []
      for j in range(7):
         items.append(l[i*7+j])
      print(items)
      li.append(items)
print(calad('2018-3'))