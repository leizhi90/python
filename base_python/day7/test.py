# -*- conding:utf-8 -*-
def f(a=1,*args,li=[],**kwargs):
      a +=1;
      li.append(2)
      print(args)

print(f.__defaults__)
f()
print(f.__defaults__)

f()
print(f.__defaults__)
def f1(li=None):
    if li == None:
        li = []
    li.append(100)
    print(li)

f1()
f1()
c=2
def f3(b=c,li=[],*args):
    b+=3
    li.append(100)
    print(li)

print('defaults',f3.__defaults__)
f3()
print('default',f3.__defaults__)
f3()
