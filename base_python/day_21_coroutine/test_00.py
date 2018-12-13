# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 20:15
import asyncio
def normal_func():
    print("this is normal func")
def yield_func():
    a = yield
    print('this is yield func')
async def coroutine_func2():
    asyncio.sleep(1)
    print('这是原生协程2')
async def coroutine_func():
    print('这是原生协程函数')
    a = await coroutine_func2()
def callback_async(v):
    print(v)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    fs = asyncio.ensure_future(coroutine_func())
    fs.add_done_callback(callback_async)
    loop.run_until_complete(asyncio.ensure_future(coroutine_func()))
    loop.close()
    print('end.....')