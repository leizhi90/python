# -*- conding:utf-8 -*-
import sys
def f():
      pass
print(sys.getrefcount(f()))
sys.setrecursionlimit(3)