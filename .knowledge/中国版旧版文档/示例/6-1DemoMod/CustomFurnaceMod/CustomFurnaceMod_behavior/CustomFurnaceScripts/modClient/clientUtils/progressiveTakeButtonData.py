# -*- coding: utf-8 -*-

import math

"""
长按分堆管理器
TODO: 
1）抬起如果GetTakeAmount为0，那么调用Reset；否则鼠标持有GetTakeAmount数量，原来的物品数量减掉；
2）按下时如果IsActive，需要将鼠标持有的物品处理调，然后Reset
"""
class ProgressiveTakeButtonData(object):
    def __init__(self):
        self.FULL_STACK_HOLD_TIME = 30
        self.mHeldTime = 0
        self.mStartHeldTime = 0
        self.mIsActive = False
        self.mCnt = 0
        self.mStackSize = 0
    
    def Tick(self):
        self.mCnt += 1
        if self.mIsActive:
            self.CalculateHeldTime()
    
    def Init(self, stackSize):
        """
        按钮按下
        """
        self.mStartHeldTime = self.mCnt
        self.mIsActive = True
        self.mStackSize = stackSize

    def IsActive(self):
        """
        分堆进度是否显示
        """
        return self.mIsActive

    def Reset(self):
        """
        停止分堆
        """
        self.mHeldTime = 0
        self.mStartHeldTime = 0
        self.mIsActive = False

    def GetPercentTaken(self):
        """
        分堆进度
        """
        share = float(self.mHeldTime) / float(self.FULL_STACK_HOLD_TIME)
        return min(share, 1)

    def GetTakeAmount(self):
        """
        分堆数量
        """
        return math.floor(self.GetPercentTaken() * self.mStackSize)

    def CalculateHeldTime(self):
        self.mHeldTime = self.mCnt - self.mStartHeldTime
