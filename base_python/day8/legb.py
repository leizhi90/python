# -*- conding:utf-8 -*-
v = 1
def change_v():

      pass
      global v
      v=4
      print(v)
      w = 5
      def inner_v():
            nonlocal w
            w=6
            print(w)
      inner_v()
change_v()
print(globals())
print(vars())
print(locals())
def test():
      i = 1
      h = 2
      print(vars())
      print(locals())
test()