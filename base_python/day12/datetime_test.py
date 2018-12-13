# -*- conding:utf-8 -*-
from datetime import date,time,datetime
d=date(2018,3,7)
d2=date(2018,6,30)
print(d)
print(d.year,d.month,d.day)
print(d.max)
print(d.min)
print(date.min,date.max)
print(date.resolution)
print(type(date.resolution))#<class 'datetime.timedelta'>
#将当前对象指定的年月日进行替换
dd=d.replace(month=9)
print(dd)
print(d.timetuple())
print(d.weekday())
#序号 0001-01-01 1 0001-01-02 2
print(d.toordinal())
#格式化
print(d.strftime('%Y-%m-%d'))
#类方法 当前时间
print(date.today())
# 19070-01-01 走过的秒数
d2=date.fromtimestamp(60*60*24*21)
print(d2)
d=date.fromordinal(21)
print(d)

#time时间的操作 时分秒 微妙
t=time(9,9,9,1212)
print(t)
print(t.hour,t.minute,t.microsecond)
print(t.max,t.min)
t2=t.replace(21)
print(t2)
#格式化
print(t.strftime('%H :%M'))

#datetime
dt=datetime(2018,3,30,14,37,32,9999)
print(dt)
print(dt.microsecond)
print(dt.max,dt.min)
#分别返回日期 和 时间
print(dt.date())
print(dt.time())

print(dt.ctime())
print(dt.timetuple())
#0001-01-01 为1 0001-01-02 为2
print(dt.toordinal())
print(dt.strftime('%m-%d'))
#当前时间
print(datetime.today())
print(datetime.now())

