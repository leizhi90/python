# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 17:07
from collections import namedtuple
import asyncio
# 1、使用yield构造的生成器，每次使用前，都必须next或者send(None) 一次，怎么一劳永逸的解决？不用每次构造生成器的时候都这样调用？不考虑for循环
# yield from
def gen_f(func):
    def inner():
        f =  func()
        f.send(None)
        return f
    return inner
@gen_f
def gen():
    print('预激活成功')
    a = 10
    b = yield a
    print('end')
f= gen()
#f.send(4)

# 2、使用asyncio实现教材中 yield 实现的 sender 和receiver
async def receiver(n):
    print('consumer receive msg: ', n)
    receipt = f'{n} is ok'
    return receipt
async def sender():
    n = 0
    while n < 3:
        n += 1
        print('produce send msg:', n)
        receipt =await receiver(n)
        print("consumer return msg:", receipt)

loop = asyncio.get_event_loop()
loop.run_until_complete(sender())
# 3、使用asyncio的协程编写3个嵌套函数，一个输出3次数字 168，一个输出6次字母 'ok'，一个输出9次中文 '很好'

async def func3():
    for _ in range():
        await asyncio.sleep(1)
        print("很好")
async def func2():
    for _ in range(2):
        print('ok')
    await func3()
async def func1():
    for _ in range(3):
        print(168)
        await func2()
loop = asyncio.get_event_loop()
loop.run_until_complete(func1())