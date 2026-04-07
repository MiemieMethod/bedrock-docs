# -*- coding: utf-8 -*-
import time

# 这个类的作用是延迟执行给定的函数
# 使用参考每个具体使用的地方，yield 正数为时间，负数为帧数
class CoroutineMgr(object):
    coroutines = {}  # 循环清单
    globalEnd = []  # 提前结束清单
    addCoroutines = {}  # 待添加清单

    @classmethod
    def StartCoroutine(cls, iter):
        """
        “延迟执行”一些逻辑
        :param iter: 生成器对象，即def出来的方法中有yield关键字的方法直接执行所得到的对象
        :return: 返回已添加至“待添加清单”的生成器对象，可以用于缓存，或者一些特殊判断的场合需要取消延迟执行（即下方StopCoroutine的入参）
        """
        cls.addCoroutines[iter] = 0
        return iter

    @classmethod
    def StopCoroutine(cls, iter):
        """
        停止执行指定的“延迟函数”
        :param iter: 生成器对象，由StartCoroutine方法添加过的生成器对象才可能被取消
        """
        cls.globalEnd.append(iter)

    @classmethod
    def Tick(cls):
        if cls.addCoroutines:
            for c,v in cls.addCoroutines.iteritems():  # 每帧先添加由StartCoroutine添加的生成器函数
                cls.coroutines[c] = v
        cls.addCoroutines = {}  # 添加完了清掉“待添加清单”，下帧就不会重复把一样的东西添加至循环了
        if cls.globalEnd:
            for c in cls.globalEnd:
                if cls.coroutines.get(c):  # 若有由外部手动调用StopCoroutine方法中止的生成器函数对象表明不需要执行则直接从循环清单中清除
                    del cls.coroutines[c]
            cls.globalEnd = []
        ended = []
        for c, v in cls.coroutines.iteritems():  # 开始循环，并判断与处理各生成器的状态
            try:
                if v < 0:  # 负数为帧数
                    v += 1  # 每次调用为1帧，最后会加至0，即走到下面的if
                    # 由于该值的初始值为yield提供
                    # 且表示将在此Tick函数中经过若干次调用后才会走到下方if处执行下一次next
                    # 达到“延迟”的效果
                    cls.coroutines[c] = v
                if v == 0 or (v > 0 and time.time() >= v):  # 第一次走进来永远是0，因为第13行处为外部调用的入口；第二次走进来则可能为帧数倒计至0或者指定秒数的时间到达
                    # 第一次走进来
                    # 生成器会调用至yield处并从此处中断执行
                    # 可以简易理解为从yield处上方到yield所在的行为一个函数
                    # 并在yield出return出yield后面的变量
                    # 若再次调用next方法
                    # 则解释器从“上一次”中断的yield处继续执行生成器后面的代码直到找到下一个yield并重复上次的流程在此处中断
                    # 若整个生成器函数跳出（即执行完毕）且并未发现下一个yield
                    # next函数则抛出一个StopIteration异常
                    # 代表该生成器函数已全部执行完毕
                    newv = c.next()
                    if newv > 0:  # 为正数则代表为秒数，当前时间time.time()加上yield处指定的秒数则为开始执行yield后部分代码的时间
                        newv = newv + time.time()
                    cls.coroutines[c] = newv
            except StopIteration:
                # 在第50行处引发异常
                ended.append(c)  # 添加至列表中用于标记该函数已经执行完毕
        for c in ended:
            del cls.coroutines[c]  # 清除引用
