# -*- coding: utf-8 -*-
# (C) shan weijia, 2018
# All rights reserved

'''Description '''

__author__ = 'shan weijia <shanweijia@jiaaocap.com>'
__time__ = '2019/1/2 4:58 PM'

import asyncio
import logger
import functools
from message import BaseMessage
from task import BaseTask


class BaseEngine(object):
    """engine 基础类"""

    def __init__(self, message=None, task=None, loop=None, log=None):
        """
        :param message: 消息中间件实例
        :param task: 任务存储解析类实体
        :param loop: 事件循环
        :param log: 日志实例
        """
        self.loop = loop or asyncio.get_event_loop()
        self.log = log or logger.get_logger()
        self.message = message or BaseMessage()
        self.task = task or BaseTask

    def run_forever(self):
        try:
            self.loop.run_forever()
        except KeyboardInterrupt as e:
            asyncio.gather(*asyncio.Task.all_tasks()).cancel()
        finally:
            self.loop.close()

    def task_decode(self, task_msg):
        """用于解析认为从message上获取的任务报文，解析成task实例，向schedule传递"""
        raise NotImplementedError("engine.task_decode方法必须实现")

    def task_encode(self, task):
        """用于将task打包成任务报文，向message发送"""
        raise NotImplementedError("engine.task_encode方法必须实现")

    def send_task(self, task_msg):
        """将任务通过message实例发送"""
        raise NotImplementedError("engine.send_task方法必须实现")

    def recv_task(self):
        """从message中获取消息"""
        raise NotImplementedError("engine.recv_task方法必须实现")

    @staticmethod
    def register(func):
        """用于注册spider实体类"""

        @functools.wraps(func)
        def route(*args, **kwargs):
            return func(*args, **kwargs)

        return route
