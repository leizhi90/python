# -*- conding:utf-8 -*-
def f():
   try:
      return 1
   finally:
      return 3
print(f())

def ff():
   x = 1
   try:
      #return x
      1+9
      #raise IndexError
      assert 1==12
      print('23')
   except Exception as e:
      print(e.args)
      return 7
   else:
      x=10
      return 9
   finally:
      return 8

print(ff())
import dis

