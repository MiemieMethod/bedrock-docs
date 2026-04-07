# -*- coding: utf-8 -*-

import time


# 这个类的作用是延迟执行给定的函数
# 使用参考每个具体使用的地方，yield 正数为时间，负数为帧数
class CoroutineMgr(object):
    def __init__(self):
        self.coroutine_dict = {}
        self.coroutine_join_dict = {}
        self.global_end_list = []

    def delay_exec_func(self, func, delay, *args, **kwargs):
        def delay_func():
            yield delay
            func(*args, **kwargs)

        self.start_coroutine(delay_func())

    def start_coroutine(self, iter_func):
        self.coroutine_join_dict[iter_func] = 0
        return iter_func

    def stop_coroutine(self, iter_func):
        self.global_end_list.append(iter_func)

    def tick(self):
        if self.coroutine_join_dict:
            for c, v in self.coroutine_join_dict.iteritems():
                self.coroutine_dict[c] = v
        self.coroutine_join_dict = {}
        if self.global_end_list:
            for c in self.global_end_list:
                if self.coroutine_dict.get(c):
                    del self.coroutine_dict[c]
            self.global_end_list = []
        end_list = []
        for c, v in self.coroutine_dict.iteritems():
            try:
                if v < 0:
                    v += 1
                    self.coroutine_dict[c] = v
                if v == 0 or (time.time() >= v > 0):
                    next_v = c.next()
                    if next_v > 0:
                        next_v = next_v + time.time()
                    self.coroutine_dict[c] = next_v
            except StopIteration:
                end_list.append(c)
        for c in end_list:
            del self.coroutine_dict[c]

    def destroy(self):
        self.coroutine_dict = {}
        self.coroutine_join_dict = {}
        self.global_end_list = []
