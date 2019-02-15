# -*- coding: utf-8 -*-
# (C) shan weijia, 2018
# All rights reserved

'''Description '''

__author__ = 'shan weijia <454273687@qq.com>'
__time__ = '2019/1/3 9:41 AM'


class BaseTask(object):

    def __init__(self, enter=None, priority=None):
        """
        :param enter: 入口函数
        :param priority: 优先级
        """
        self.priority = priority or -1
        self.enter = enter

    def __lt__(self, other):
        if not hasattr(self, "priority"):
            self.priority = -1
        return self.priority < other.priority
