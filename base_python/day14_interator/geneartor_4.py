# -*- conding:utf-8 -*-
def generat():
   x = 0
   while True:
      msg = yield x
      print(x)
      if msg == 'big':
         x -=1
      elif msg == 'small':
         x +=1
g= generat()
g.send(None)
while True:
   x =g.send(msg)
