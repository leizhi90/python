# -*- conding:utf-8 -*-
class Python:
   def __init__(self,name,group):
      self.name=name
      self.group=group
   def introduce(self):
      print(f'my name is {self.name}所在的组是{self.group}')
   def teach(self):
      print('open pycharm')
      print('teaching.......')

class Java:
   def __init__(self,name,group):
      self.name=name
      self.group=group
   def introduce(self):
      print(f'my name is {self.name}在的组是：{self.group}')
   def teach(self):
      print('open eclipse')
      print('teaching.....')

p=Python('lll',66)
j=Java('zzzzz',9999)
p.introduce()
p.teach()
j.introduce()
j.teach()