# -*- conding:utf-8 -*-
datas=""""{
   "k0": "df",
   "k22" : "vvvvv"
}
"""
import json
# print(type(datas))
# d1 = json.loads(datas)
# print(type(d1))

d={
    "布尔类型":True,
    "空值类型":None,
    "整数类型":1,
    "浮点类型":1.5,
    "字符串类型":"abc",
    "数组类型":[1,2,3],
    "对象类型":{"one":"1","two":2}
}
jsonstr=json.dumps(d,ensure_ascii=False)
print(json.dumps(d,ensure_ascii=False))
print(type(jsonstr))
#从字符串jsonstr转换成字典（对象）
d2=json.loads(jsonstr)
print(d2)
print(type(d2))
class Person:
   def __init__(self,name, age):
      self.name=name
      self.age=age
class PersonEncode(json.JSONEncoder):
   def default(self, o):
      if isinstance(o , Person):
         return {"name": o.name,"age":o.age}
      else:
         return super(PersonEncode, self).default(o)
p = Person('lz',18)
pj = json.dumps(p ,cls=PersonEncode)
print(pj)
print(type(pj))
pp = json.loads(pj)
print(pp)
print(type(pp))