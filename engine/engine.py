# -*- coding: utf-8 -*-
# (C) shan weijia, 2018
# All rights reserved

"""Description """

__author__ = 'shan weijia <shanweijia@jiaaocap.com>'
__time__ = '2019/1/3 10:07 AM'

from .base import BaseEngine


class Engine(BaseEngine):

    def send_task(self, task_msg):
        pass

    def task_decode(self, task_msg):
        pass

    def task_encode(self, task):
        pass

    def recv_task(self):
        pass
