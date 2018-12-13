# -*- conding:utf-8 -*-
# 编写三个类，矩形与正方形两个类，求周长与面积。分别使用不继承与继承两种方式，并总结出继承的优势。
class Rectangle:
   def __init__(self,length,high):
      self.length=length
      self.high=high
   def perimeter(self):
      return 2*(self.length + self.high)
   def area(self):
      return self.length*self.high
class Square:
   def __init__(self,length):
      self.length=length
   def perimeter(self):
      return 3*self.length
   def area(self):
      return self.length*self.length
class Squares(Rectangle):
   def __init__(self,length):
      self.length=length
      super().__init__(length,length)
r=Rectangle(3,4)
print(r.perimeter())
print(r.area())
ss=Squares(5)
print(ss.perimeter())
print(ss.area())
# 编写一个分页显示类，构造器传入记录总数。可以设置每页记录数与页码，
# 能够返回当前页显示的记录区间。如果页码不正确，则将页码恢复成1，并显示错误提示信息。每页记录数与页码使用property实现。
class Paging:
   def __init__(self,total):
      self.total=total
      self.__every_page=10
      self.__now_page=1
   @property
   def every_page(self):
      return self.__every_page
   @every_page.setter
   def every_page(self,p):
      self.__every_page=p
   @every_page.deleter
   def every_page(self):
      del self.__every_page
   @property
   def now_page(self):

      return self.__now_page
   @now_page.setter
   def now_page(self,p):
      self.now_page=p

# 编写电脑类，提供一个方法，能够与移动设备（U盘，MP3，移动硬盘）进行读写交互。如果参数类型不是移动设备的类型，则打印错误信息。MP3除了读与写之外，还额外具有一个播放音乐的功能。
class Movie:
   def read(self):
      print('read fun')
class Computer:
   def __init__(self,m):
      self.move=m
   def judge(self):
      if isinstance(self.move,Movie):
         pass
      else:
         print('is not movie type!')
class U(Movie):
   pass
class MP3(Movie):
   def music(self):
      print('music on.......')
class Disk(Movie):
   pass
# 编写如下的继承结构，类C继承（A，B），类D继承（B，A），类E继承（C，D）或者（D，C），会出现什么情况？
class A:
   pass
class B:
   pass
class C(A,B):
   pass
class D(B,A):
   pass
# class E(C,D):
#    pass

# 实现矩阵的转置。（zip）
li=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#print ([[i for i in enumerate(item) ] for item in li])
print(*li)
print (list(map(list,zip(*li))))
age=[1,2]
name=['a','b']
print(li)
print(list(zip(name,age)))

# 使用sorted函数实现reverse的功能。但是顺序不改变。
li=[3,1,5,9]
def ord(i):
   pass
print(sorted(li,reverse=True))
print(li)
print(*li)