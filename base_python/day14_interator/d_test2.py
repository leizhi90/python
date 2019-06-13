# -*- conding:utf-8 -*-
#保留函数元信息
from datetime import datetime
from functools import wraps
def checkin_new(format):
    def checkin_new_inner(func):
        @wraps(func)  #wraps装饰器（带参数的装饰器）可以将被修饰函数的信息进行保留，参数就是被修饰的函数
        def inner(*args,**kwargs):
             print(datetime.now().strftime(format))
             result=func(*args,**kwargs)
             return result
        return inner
    return checkin_new_inner

@checkin_new("%Y-%m-%d")
def on_duty(name,age):
    """这是上班的函数
    """
    print("%s上班了%s" %( name,age))
    return "success"
@checkin_new("%Y-%m-%d")
def off_duty(name,age):
    print("%s下班了 %s"  %( name,age))
# on_duty=checkin_new(on_duty)  缺点在于所有调用了onduty的位置，都要去写这一句
# 调用扩展上下班函数之后的功能
r=on_duty("bill",30)
print(r)
off_duty("bill",30)
print(on_duty.__name__)
print(on_duty.__doc__)
