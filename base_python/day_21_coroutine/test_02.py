# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 20:22
import asyncio
async def do_some_thing(n):
    print('waiting:',n)
    await asyncio.sleep(n)
    print('waiting end')
loop =asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(do_some_thing(5)))
#loop.run_until_complete(do_some_thing(5))
