# -*- conding:utf-8 -*-
content=None
with open('D:/c.text','w+') as f:
   f.write('cc\tsd\nsfs\\\sdf')
with open('D:/c.text','r') as f:
   print(f.readline())
import csv
# with open('d/csv.txt','wt') as f:
#    write=csv.writer(f)
#    write.writerow(['a','b','c'])
#    write.writerow(['1','2','3'])
import os
#os.makedirs("d:/azc/def/ghi",exist_ok=False)
print('*'*22)
a =os.getcwd()
print(a)
for roots,dirs, files in os.walk(a):
    print(roots)
    print(dirs)
    print(files)
    print(os.path)
    print(type(os.path))
    for fn in files:
        fp_abspath=os.path.join(roots,fn)
        print(fp_abspath)
print('*'*22)
print(os.path.abspath('.'))
