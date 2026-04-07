# -*- coding: utf-8 -*-

# 获取客户端Component的基类
import mod.client.extraClientApi as clientApi
ComponentCls = clientApi.GetComponentCls()

# Component要继承于基类才能生效
class ShootComponentClient(ComponentCls):
    def __init__(self, entityId):
        ComponentCls.__init__(self, entityId)
        # 这里设置了一个开关来开关更新射击
        self.mShoot = False

    @property
    def shoot(self):
        return self.mShoot

    @shoot.setter
    def shoot(self, val):
        self.mShoot = val