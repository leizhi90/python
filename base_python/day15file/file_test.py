# -*- conding:utf-8 -*-
#文件包含二进制文件和文本文件
#打开文件，读 写
#open(file 路径,mode 获取文件方式,buffering,encoding)
#绝对路径和相对路径
# w 覆盖写 r只读 a 追加写 + 扩充写
#t 以字符串  b 以字节
#f=open('D:/a.text','r')
#FileNotFoundError: [Errno 2] No such file or directory: 'D:/a.text'
# 文件的关闭 f.close() 当文件打开时报错无法关闭文件
# 下面的方法比较麻烦
f = None
try:
   f=open('D:/ff.text','r')
except FileNotFoundError:
   pass
finally:
   f.close()
#with 模块中
with open('D:/aa.text','r+') as f:
   f.write('aaaa')
# a+ 追加写，可以读，如果没有文件 会创建
# w+ 可以覆盖写，可以读，没有回创建
# r+ 可以读，可以覆盖写，没有报错

#读取文件 read 按需读取 readline 读取一行会保留末尾格式没有时返回空窜 readlines 返回一个列表，列表中每FileNotFoundError: [Errno 2] No such file or directory: 'D:/a.text'个元素为文件的一行内容，保留尾部格式
#文件就是迭代器，可以按照迭代器的方式读取文件
with open('/s','rt') as f:
   for i in f:
      print(i,end='')
#read(size =n)n可以负数 不写 整数，负数不写读取整个文件，整数只读n大小的
#当读取文件内容之后，被读取的内容不能再次读
# rt 字符 rb字节
with open('../a.text','rb') as f:
   print(f.read())
#encoding 指定文件的编码格式


#write（content）
#writelines（） 以列表格式写入内容
with open('path','wt') as f:
   f.write('sfsfsfsf')
with open('path','wt') as f:
   f.writelines('[][]')

#文件指针
#当进行文件操作时，文件是存在文件指针的，是下一次读取或写时的位置，不同的操作，指针位置不同
# r w 指针在初始位置

#tell 返回当前文件指针的位置
#seek（偏移量，方式）
import os
#os.SEEK_SET 0 起始
#os.SEEK_CUR 1 当前
#os.SEEK_END 2 终止

#关于文件与路径
#os 模块
#创建目录mkdir ，必须是父目录有，子目录无
os.mkdir('path')
os.makedirs('path',exist_ok=False)
os.rmdir('path')

