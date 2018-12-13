# -*- conding:utf-8 -*-
#动态属性操作
#hasattr(obj,name)
# 对象 属性名 存在 返回True 无False
class Person:
      pass
p=Person()
print(hasattr(p,'name'))

#getattr(obj ,name，default)
#无则出错 定义 default返回
#AttributeError: 'Person' object has no attribute 'name'
print(getattr(p,'name','default'))

#setatt(obj,name,value)
#设置对象属性 存在修改 无则新增
print(setattr(p,'age',45))
print(getattr(p,'age'))
#delattr(obj,name) 删除属性
#不使用函数的形式简单，使用函数操作属性的方式复杂
#必须在写代码的时刻就需要明确知道属性名是什么
#运行时动态传递