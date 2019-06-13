# -*- conding:utf-8 -*-
from datetime import datetime
def checkin_new(format):
    def checkin_new_inner(func):
        def inner(*args,**kwargs):
             print(datetime.now().strftime(format))
             result=func(*args,**kwargs)
             return result
        return inner
    return checkin_new_inner
@checkin_new("%Y-%m-%d")
def on_duty(name,age):
    print("%s上班了%s" %( name,age))
    #return "success"
@checkin_new("%Y-%m-%d")
def off_duty(name,age):
    print("%s下班了 %s"  %( name,age))
# on_duty=checkin_new(on_duty)  缺点在于所有调用了onduty的位置，都要去写这一句
# 调用扩展上下班函数之后的功能
r=on_duty("bill",30)
print(r)
off_duty("bill",30)