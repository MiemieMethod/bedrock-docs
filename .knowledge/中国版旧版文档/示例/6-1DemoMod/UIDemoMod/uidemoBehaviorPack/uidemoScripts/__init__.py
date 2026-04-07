# -*- coding: utf-8 -*-

import logging
import sys

def makeLogger():
    # 配置log的生成器，输出log会按固定格式 [时间] [log等级] [UIDemo] [message]
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)7s][UIDemo] %(message)s'))
    log = logging.getLogger('UIDemo')
    log.addHandler(handler)
    log.propagate = False
    log.setLevel(logging.INFO)
    return log

# 生成log实例
logger = makeLogger()