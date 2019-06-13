# -*- conding:utf-8 -*-
# 编写程序，将字典中的键与值互换。
d={1:'a',2:'b',3:'c'}
d1={}
for k,v in d.items():
    d1[v]=k
print (d1)
print ({v:k for k,v in d.items()})

# 元组是否可以总是可以作为字典的键值？
#如果元祖元素都是可哈希类型则可以 如果有不可哈希类型则不能

# d2={(1,[2,'34']):'3'}
# print (d2) TypeError: unhashable type: 'list'
# 自行求两个集合的交集，差集，并集，对称差集，判断是否为子集，父集。

s1={1,2,3,4,5,6}
#s2={4,5,6,7,8,9}
s2={1,4,6}
print (s1 & s2)
print ("s1",s1 - s2)
print (s2 - s1)
print (s1 | s2)
print (s1 ^ s2)
if bool(s1-s2):
    print ("s2 是s1 的子集")

if bool(s2-s1):
    print ("s1 是s2 的子集")

# 现存任意两个字符串s1与s2，判断s1中的字符在s2中存在的个数（重复的算1个，一条语句实现）。
ss1='aabbac abaa'
ss2='asdsfsdfcacabasbass'
print (len(set(ss1).intersection(set(ss2))))
print (len(set(ss1) & (set(ss2))))
# 实现一个人力资源管理员工管理（员工编号+姓名）的程序。功能：入职，离职，修改，查看所有员工信息，搜索指定员工，重置。
# key 员工编号+姓名   value 入职，离职，修改
while True:
    d={}
    v=input("请输入功能：in out  update  show  search  replace")
    if v=='stop':
        break
    elif v=="in":
        key=input("请输入信息：员工编号+姓名：")
        d[key]='入职'
        continue
    elif v == 'out':
        key = input("请输入信息：员工编号+姓名：")

    elif v == "update":
        key = input("请输入信息：员工编号+姓名：")
    elif v == "show":
        key = input("请输入信息：员工编号+姓名：")
    elif v == "search":
        key = input("请输入信息：员工编号+姓名：")
    elif v == "replace":
        key = input("请输入信息：员工编号+姓名：")

employee={}
info="""
1 入职 
2 离职
3 修改
4 查看
5 搜索
6 重置
7 退出
"""

while True:
    print (info)
    choice=input("请输入选择")
# 验证字典的copy方法。
d={1:'a',2:'c'}
d2=d.copy()#浅拷贝
print (d2)

#可变对象 深拷贝 对象
# 不可变 的