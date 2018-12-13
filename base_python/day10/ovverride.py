# -*- conding:utf-8 -*-
#重写
class Person:
   def __init__(self, name):
      self.__name = name

   def get_name(self):
      print("get方法得到调用")
      return self.__name

   def set_name(self, name):
      print("set方法得到调用")
      self.__name = name

   def del_name(self):
      print("del方法得到调用")
      del self.__name

   # property函数的4个参数
   # 第1个参数：提供一个get方法，该方法在读取属性值的时候，会得到调用。
   # 第2个参数：提供一个set方法，该方法在修改属性值的时候，会得到调用。
   # 第3个参数：提供一个删del方法，该方法在除属性的时候，会得到调用。
   # 第4个参数：属性的文档说明。

   # name = property(get_name, set_name, del_name, "这是伪造的属性name，真是对应的属性为受保护属性_name")

   # 当希望name属性为只读时，我们只需要仅提供get方法，不提供set与del即可。
   name = property(get_name,set_name,del_name)


p = Person("张某")
# 读取name属性的值，
print(p.name)
# 设置name属性的值
# p.name = "赵某"
del p.name
# 查看属性的说明文档。注意，此处需要通过类名来访问属性。
# print(Person.name.__doc__)