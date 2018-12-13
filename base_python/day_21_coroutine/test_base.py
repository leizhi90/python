# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 20:54
import asyncio
async def do_some_work(x):
    print('waiting '+ str(x))
    await asyncio.sleep(x)
    print('waiting end' +str(x))
def done_calback(f):
    print('done....')
loop = asyncio.get_event_loop()
#loop.run_until_complete(asyncio.ensure_future(do_some_work(6)))
#loop.run_until_complete(do_some_work(3))
fs = asyncio.ensure_future(do_some_work(2))
fs.add_done_callback(done_calback)
loop.run_until_complete(fs)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    fs = [asyncio.ensure_future(do_some_work(2)),
          asyncio.ensure_future(do_some_work(1)),
          asyncio.ensure_future(do_some_work(3))]
    coros =[do_some_work(1),
            do_some_work(2),
            do_some_work(3)]
    #loop.run_until_complete(asyncio.gather(*fs))
    loop.run_until_complete(asyncio.gather(*coros))
