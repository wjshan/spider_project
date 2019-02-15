# -*- coding: utf-8 -*-
# (C) shan weijia, 2018
# All rights reserved

'''Description '''

__author__ = 'shan weijia <454273687@qq.com>'
__time__ = '2019/1/2 5:08 PM'

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_logger():
    logger = logging.getLogger(__name__)
    return logger
