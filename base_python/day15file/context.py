# -*- conding:utf-8 -*-
"""
with 上下文管理
大多数情况下用于取代 try finally
一个对象，实现了__enter__(self) __exit__(self,exc_type, exc_val, exc_tb)
就是一个上下文管理器
上下文管理器的3步骤
1，
"""

class MyContextManager:
   def __enter__(self):
      """"
      上下文管理器的一些初始化工作，譬如端口打开，链接建立，文件的打开
      """
      print('enter__')
   def __exit__(self, exc_type, exc_val, exc_tb):
      """
      上下文管理器离开with时，用于对象的释放，如文件关闭
      :param exc_type:异常的对象类型
      :param exc_val:异常的对象实例
      :param exc_tb:traceback 对象
      :return:
      """
      print('__exit__')
with MyContextManager() as f:
   print('test')
   # try:
   #    raise Exception('错误异常，')

# enter__
# test
# __exit__

from contextlib import contextmanager
@contextmanager
def context():
   print('inin....')
   try:
      yield print('yield......')
   except:
      print('except.....')
   finally:
      print('finally..........')
   print('end end.....')
print('*'*22)
with context() as f:
   print('first ........')
   f
   print('beging .....')
   raise Exception('contextmanager 抛出异常')

print(33*'*')
@contextmanager
def gen():
    print('gen的第一次打印')
    print('gen的第一次打印111')
    try:
        yield print('gen的yield111')
    except Exception as e:
        print('处理错误')
    finally:
        print('gen的第二次打印')
        print('gen的第二次打印222')

with gen() as f:
    print('进入with')
    print(f)
    print('结束with')

    raise Exception('contextmanager 抛出异常')
