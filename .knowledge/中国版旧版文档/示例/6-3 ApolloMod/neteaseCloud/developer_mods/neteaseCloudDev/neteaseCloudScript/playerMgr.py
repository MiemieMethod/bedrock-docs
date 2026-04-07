# -*- coding: utf-8 -*-
from neteaseCloudScript.cloudConsts import ModNameSpace, ClientSystemName, SyncRightHandSlotEvent
import lobbyGame.netgameApi as lobbyGameApi


class PlayerMgr(object):
    """
    玩家操作封装类
    简单的封装
    从服务端类抽离一些代码
    便于查阅
    """
    def __init__(self, system):
        self.mSystem = system
        self.mUserToRightSlotDict = {}
        self.mSystem.ListenForEvent(ModNameSpace, ClientSystemName, SyncRightHandSlotEvent,
                            self, self.OnSyncRightHandSlot)  # 主手槽位
        self.mPlayerIdToUid = {}

    def Login(self, playerId, uid):
        # 登入
        self.mPlayerIdToUid[playerId] = uid

    def OnSyncRightHandSlot(self, data):
        playerId = data['playerId']
        slot = data['slot']
        uid = lobbyGameApi.GetPlayerUid(playerId)
        self.mUserToRightSlotDict[uid] = slot

    def Logout(self, playerId, uid):
        # 登出
        if uid in self.mUserToRightSlotDict:
            del self.mUserToRightSlotDict[uid]
        if playerId in self.mPlayerIdToUid:
            del self.mPlayerIdToUid[playerId]

    def GetPlayerUid(self, id):
        # 这里只有玩家的实体id
        return self.mPlayerIdToUid.get(id, None)

    def GetUserSlot(self, uid):
        # 主手槽位
        return self.mUserToRightSlotDict.get(uid, None)

    def Destroy(self):
        self.mSystem.UnListenForEvent(ModNameSpace, ClientSystemName, SyncRightHandSlotEvent,
                            self, self.OnSyncRightHandSlot)
        self.mSystem = None  # 清除引用


# 简易单例
instanceMgr = None
def Init(system):
    global instanceMgr
    instanceMgr = PlayerMgr(system)


