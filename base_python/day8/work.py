# -*- conding:utf-8 -*-
# 编写一个函数，参数为一个列表（或元组）类型，能够遍历输出列表中的元素。列表中的元素可能还是列表，嵌套列表要求能够单个元素输出，并且可能会出现多层嵌套。
li=[[1,3],[12,[2,5,6],[34]],[10],9]
def traverse(li):
      for items in li:
            if type(items)==list:
                  traverse(items)
            else:
                  print(items,end=' ')
traverse(li)
# 打印菲波那切数列的第n项。
#1、1、2、3、5、8、13、21
def fab(n):
      a,b=0,1
      for i in range(n):
            a,b=b,a+b
      return a

def fb(n):
      s = 0
      if n ==2 or n== 1:
            s=1
      if n > 2:
            s1=1
            s2=1
            for i in range(n-1):
                  s=s2
                  s2=s1+s
                  s1=s
      return s
print(fb(8),end='\n')

# 不使用nonlocal与global，来修改外围函数中的变量与全局变量。

# 在其他语言中，函数名称相同，但是参数列表不同的函数，成为函数重载。Python中支持函数重载吗？如果在程序定义了同名的函数，会出现什么情况？


# 编写函数，（两个参数），combination (s , num)，s为一个字符串，n为个数，输出从s中选择n个字符的所有组合。



# 编写函数（两个参数），permutation (s , num)，s为一个字符串，n为个数，输出从s中选择n个字符的所有排列。

def combination(s, n):
    if n == 1:
        return list(s)
    if n == len(s):
        return [s]
    r = []
    pre = combination(s[1:], n - 1)
    for item in pre:
        r.append(s[0] + item)
    r.extend(combination(s[1:], n))
    return r

print(combination("12345", 2))

def permutation(s, n):
    if n == 1:
        return list(s)
    r = []
    pre = permutation(s[1:], n - 1)
    for item in pre:
        for i in range(0, len(item) + 1):
            r.append(item[0:i] + s[0] + item[i:])
    if len(s) > n:
        r.extend(permutation(s[1:], n))
    return r

print(permutation("abcd", 4))
# value = int(input("请输入一个数值："))
# for i in range(9, -1, -1):
#     if value >= 2 ** i:
#         print(2 ** i, end="")
#         value -= 2 ** i
#         # 如果当前值依然不为0，则说明后面还有元素，补+
#         if value > 0:
#             print(" + ", end="")
#         else:
#             break
r = []
for i in range(1, 6):
    if i != 1 and i != 4:
        for j in range(1, 6):
            if j != 3 and j != 5:
                r.append([i, j])
print(r)
# 列表推导式
r1 = [ [i, j] for i in range(1, 6) if i != 1 and i != 4 for j in range(1, 6) if j != 2 and j != 5]
print(r1)

r2 = []
for i in range(1,6):
    for j in range(1,6):
        if i !=j:
            r2.append([i,j])
print(r2)
print([1, 2] == [1, 2])
print([1, 2] is [1, 2])

t = (3,4,(3,4,3),3)
print(t.count(3))

s = "abcdefab"
print(''.join(["ab", "cd", "ef"]))