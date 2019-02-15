# -*- coding: utf-8 -*-
# (C) shan weijia, 2018
# All rights reserved

'''Description '''

__author__ = 'shan weijia <454273687@qq.com>'
__time__ = '2019/1/2 11:23 AM'

import asyncio
import uvloop


async def t1():
    print("开始等待t1")
    await asyncio.sleep(5)
    print("等待结束t1")


async def t2():
    print("开始等待t2")
    await asyncio.sleep(3)
    print("等待结束t2")


async def main():
    f1 = t1()
    f2 = t2()
    tasks = [
        asyncio.ensure_future(f1),
        asyncio.ensure_future(f2),
    ]
    return await asyncio.wait(tasks)


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())