# -*- conding:utf-8 -*-
import time
def genera():
   msg=''
   while True:
      print(msg,'ppppp')
      x = yield msg
      time.sleep(1)
      if x == 5:
         msg = 'big'
      elif x ==0:
         msg = 'small'
x = 0
t=genera()
t.send(None)
while True:
   print(x)
   msg=t.send(x)
   if msg == 'big':
      x -=1
   else:
      x +=1

