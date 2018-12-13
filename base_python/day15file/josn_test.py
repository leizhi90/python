# -*- conding:utf-8 -*-
# csv文件序列化
# 数据元素的存储方式一般是以,分隔
# csv写入方法 writerow ，一次写入一行
import csv
# with open("c:/test.csv","wt") as f:
#     #获取csv的writer对象，使用对象下的writerow方法。如果用f下面的write方法，可以写入但是不能读取
#     writer=csv.writer(f)
#     writer.writerow(["姓名","年龄","分组"])
#     writer.writerow(["张三","18","1组"])
# csv写入方法 writerow ，一次写入多行
# newline 参数可以去除每一个元素下面的换行
# with open("c:/test2.csv","wt",newline="") as f:
#     writer=csv.writer(f)
#     writer.writerows([["姓名","年龄","分组"],["张三","18","1组"],["李四","28","2组"]])
#json格式的序列化
# 向json格式的文件中写入数据dump方法
d={
    "bg": "green",
    "title": {
        "data": ["data1", "data2", "data3", "data4"],
        "align": "左对齐"
    }
}
import json
# with open("c:/test.json","wt") as f:
#     #dump向文件中写入json格式的数据 第一个参数要写入的数据，第二个参数是文件对象
#     #ensure_ascii指定吸入的时候显示非ascii字符集，默认值是True
#     json.dump(d,f,ensure_ascii=False)
# # 读取json类型的文件使用load方法
# with open("c:/test.json","rt") as f:
#     d=json.load(f)
#     print(type(d))
#     print(d)
#序列化就是把对象换成字符串，对象--->字符串
#反序列化，就是把字符串，转换成对象  字符串--->对象
#序列化，把d对象转换成字符串
s=json.dumps(d,ensure_ascii=False)
# print(type(s))
# #反序列化，把s字符串转换成字典
# d2=json.loads(s)
# print(type(d2))
# 现在下面d字典（对象）变成字符串：序列化，看一下python中数据类型跟json中的数据类型如何匹配
# d={
#     "布尔类型":True,
#     "空值类型":None,
#     "整数类型":1,
#     "浮点类型":1.5,
#     "字符串类型":"abc",
#     "数组类型":[1,2,3],
#     "对象类型":{"one":"1","two":2}
# }
# jsonstr=json.dumps(d,ensure_ascii=False)
# print(json.dumps(d,ensure_ascii=False))
# #从字符串jsonstr转换成字典（对象）
# d2=json.loads(jsonstr)
# print(d2)
#如果我自己写一个对象，写一个雷，能不能序列化？
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person("bill",20)
# json.dumps(p)
#目前如果不做处理，使用默认的形式(json.JSONEncoder)，不能把自定义的类型转换成json数据，序列化
#如果希望序列化自定义的类型，可以自定义一个encode类型来处理数据
class PersonEncoder(json.JSONEncoder):
    #需要继承json.JSONEncoder，实现里面的defalut方法，在这个方法中，给出序列化的形式
    def default(self,o):
        if isinstance(o,Person):
            return {"name":o.name,"age":o.age+1}
        else:
            return super(PersonEncoder, self).default(o)
json_str=json.dumps(p,cls=PersonEncoder)
print(type(json_str))
print(json.dumps(p,cls=PersonEncoder))
