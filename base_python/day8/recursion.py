# -*- conding:utf-8 -*-
# 递归，一个函数调用其自身，
#1、直接递归 A-->A
# 2、间接递归 A-->B-->A
# 递归分为：递推和回归
# 递推：将问题进行分解，直到得出一个解决方案【直到能够直接解决，不需要再进行分解为止
#回归：利用递推分解的结果，进行回溯

# 通过递归的方式
def s_re(start,end):
      if start == end:
            return start
      return start+s_re(start+1,end)

def ss(n):
      if n==1:
            return 1
      return n*ss(n-1)
print(ss(5))

def fb(n):
      if n==0 or n == 1:
            return n
      return fb(n-1)+fb(n-2)
print(fb(10))
