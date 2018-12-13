# -*- conding:utf-8 -*-
# 魔法方法 一些特殊的方法 __方法名__
#通常不会主动调用，在满足一定的条件下自动得到执行
class Magic:
      #当创建对象时，会调用，比init早
      #new创建对象 init初始化对象
      #new 是一个类方法，但是该方法不需要@classmethod来修饰
      #如果new方法中返回当前类型的对象，则后续会调用init方法对该对象进行初始化，否则init不会执行
      def __new__(cls, *args, **kwargs):
            print('new')
            return super().__new__(cls)
      def __init__(self):
            print('init')

      def __del__(self):
            print('对象销毁时调用')
      #以字符串的形式来描述对象，该方法在使用内建函数str format print的时候，会得到执行，该方法必须返回字符串的类型
      def __str__(self):
            return 'magic对象'
      #以字符串的形式来描述对象，必须返回字符串类型 repr()
      def __repr__(self):
            return '<magic at 0x3943>'
      # str() repr() 都是以字符串的形式来描述对象，不同的是 str是从人阅读的角度出发，repr返回更接近解释器的表示
      #当调用内建函数bytes 返回bytes类型
      def __bytes__(self):
            return b'dfs s'

      def __call__(self, *args, **kwargs):
             print('call')
m=Magic()
#进行了M 的换绑定，之前的对象就再也不用了，del

print(m)
print(str(m))
print(repr(m))
# 调用—str-方法时，类中没有，但是定义了-repr——方法，则会调用——str_
#把对象当做函数来执行
m()
#TypeError: 'Magic' object is not callable