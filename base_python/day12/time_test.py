# -*- conding:utf-8 -*-
import time
#返回与世界标准世界（UTC)相差秒数
print(time.timezone)#秒
print(time.timezone/3600)
#1970-01-01 00:00:00 到现在程序走过的秒数
print(time.time())
#返回时间元祖 time.struct_time（命名元祖）(tm_year=2018,）namedtuple,不仅可以通过索引还可以通过名称来访问元素
print(time.localtime(time.time()))
print(time.localtime())
t=time.localtime()
print(t[0])
print(t.tm_year)
print(time.gmtime())#参照UTC时间
#mktime 与localtime 恰好相反
print(time.mktime(time.localtime()))
print(time.asctime(time.localtime()))
#将秒数代表的时间以字符串新式显示
print(time.ctime())
#令程序休眠时间，单位秒
time.sleep(2.123)
# 格式化时间， 1、模板 2、时间元祖（可无）
print(time.strftime('%Y-%m-%d %H:%M:%S'))
#时间元祖
print(time.strptime('2018-03-30 11:29:34','%Y-%m-%d %H:%M:%S'))

