# -*- conding:utf-8 -*-
#面向对象的三大特征
# 封装 继承 多态
# 封装就是隐藏底层的实现细节，这样，当底层实现细节发生改变的时候，不至于对外界造成影响
# 封装在程序中的体现，对于类中的属性。不要让外界直接访问（因为如果外界直接进行访问就不利于以后的更新，属性发生改变，对外界就会造成影响）而是提供操作属性的方法（共有的对外接口）让外界进行访问
#好处：以后属性发生改变，之哟啊提供共有接口不发生改变，对外界就没有影响

class Person:
	 def __init__(self):
			self.name='lz'
	#公有的对外接口
	 def get_name(self):
			return self.name
	 def set_name(self,name):
			self.name=name
p=Person()
print(p.name)

