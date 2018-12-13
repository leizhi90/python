# -*- conding:utf-8 -*-
# r+，w+与a+都可以读取文件与写入文件，指出三者间的区别。
# r+:可以读，可以覆盖写，没有会报错。
# w+:可以覆盖写，可以读，没有会创建
# a+:追加写，可以读，没有会新建

# 重命名文件：编写一个函数，接收一个路径，去掉路径下所有的文件（包括子目录的文件），文件名末尾的特定字符串。
import os
def rename(path):
   del_other_path(path)
   pass
def del_other_path(path,endwith):
   for roots, dirs, files in os.walk(path):
      for fn in files:
         file = os.path.join(roots, fn)
         if file !=path or file.endswith(endwith):
            os.remove(file)
# 获取文本文件中最长一行的长度。（一条语句）
print(max(len(line.strip()) for line in open('d:/maxtest.txt') ))

# 使用异或来对文件进行简单加密。（bytes(iterable)构造器）

# 对两个文件进行合并。

def combine(path1,path2,new_path):
   read_file(os.listdir(path1),new_path)
   read_file(os.listdir(path2), new_path)
def read_file(path,new_path):
   for filename in path:
      filepath = new_path+'/'+filename
      f = open(filepath, 'w')
      for line in open(filepath):
         f.writelines(line)
         f.write('\n')
      f.close()
combine('d:/work01','d:/work02','d:/work')

# 查找文件夹中所有文件，只要包含Happy，New ，Year，任何一个词的文件就输出文件的名字
def all_files(path):
   list_file = []
   targets = ['Happy', 'New','Year']
   for roots,dirs, files in os.walk(path):
      for fn in files:
         file = os.path.join(roots,fn)
         for target in targets:
            if target in file:
               list_file.append(file)
   return list_file
print(all_files('d:/work02'))