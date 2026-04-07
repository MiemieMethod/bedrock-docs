# -*- coding: utf-8 -*-
'''
服务器信息处理。
'''
from neteaseCloudScript.cloudConsts import ProcessType, CloudItemType
import server.extraServerApi as serverApi
import lobbyGame.netgameApi as lobbyGameApi
#import neteaseCloudScript.timermanager as timermanager
import neteaseCloudScript.engineApi as engineApi
import logout
import neteaseCloudScript.playerMgr as playerMgr
import neteaseCloudScript.cloudDbApi as cloudDbApi
import ujson as json
import neteaseCloudScript.cloudConsts as cloudConsts

class SyncActionBase(object):
    def __init__(self, conf):
        self.Init(conf)

    def Init(self, conf):
        pass

    def Login(self, uid):
        pass

    def Logout(self, uid):
        pass

    def Destroy(self):
        pass

class NoAction(SyncActionBase):
    '''
    不做任何处理
    '''
    pass

class FilterMailAction(SyncActionBase):
    '''
    不使用和同步云端玩家信息，且进入服务器时清空本地信息（可配置清空的信息类型），
    离开服务器时特定类型的物品通过邮件发送给玩家；
    '''
    def Init(self, conf):
        self.mClearTypes = conf.get('clear_types', [])
        self.mSaveItemNames = conf.get('save_item_names', [])
        self.mMailTitle = conf.get('mail_title', [])
        self.mMailContent = conf.get('mail_content', [])
        self.mMailSender = conf.get('mail_sender', [])
        self.mMailExpire = conf.get('mail_expire', [])
        self.mApplyTag = conf.get('apply_tag', "")

    def Login(self, uid):
        #清空玩家身上物品
        playerId = lobbyGameApi.GetPlayerIdByUid(uid)
        if CloudItemType.INVENTORY in self.mClearTypes:
            engineApi.ClearUserInventories(playerId)
        if CloudItemType.ARMOR in self.mClearTypes:
            engineApi.ClearUserArmors(playerId)
        if CloudItemType.HANDS in self.mClearTypes:
            engineApi.ClearLeftHandItem(playerId)
        if CloudItemType.EFFECT in self.mClearTypes:
            engineApi.ClearEffects(playerId)

    def Logout(self, uid):
        mailSystem = serverApi.GetSystem("neteaseAnnounce", "neteaseAnnounceDev")
        if not mailSystem:
            logout.error('send mail error!neteaseAnnounceDev mod not exist!')
            return
        playerId = lobbyGameApi.GetPlayerIdByUid(uid)
        userInventories = engineApi.GetUserInventories(playerId)
        leftHandItem = engineApi.GetLeftHandItem(playerId)
        if leftHandItem:
            userInventories[-106] = leftHandItem
        sendItems = []
        for itemDict in userInventories.values():
            fullName = '%s:%s' % (itemDict['itemName'], itemDict['auxValue'])
            if fullName in self.mSaveItemNames:
                # mailItem = '%s:%s' % (fullName, itemDict['count'])
                sendItems.append(itemDict)
        userArmors = engineApi.GetUserArmors(playerId)
        for itemDict in userArmors.values():
            fullName = '%s:%s' % (itemDict['itemName'], itemDict['auxValue'])
            if fullName in self.mSaveItemNames:
                sendItems.append(itemDict)
        #邮件道具不能包含耐久度属性
        for info in sendItems:
            if 'durability' in info:
                del info['durability']
        if sendItems:
            #每封邮件最多携带7个item，需要分批发邮件
            oneMailNum = 7
            for i in xrange(0, len(sendItems), oneMailNum):
                mailItems = sendItems[i:i + oneMailNum]
                mailSystem.SendMailToUser([uid, ], self.mMailTitle, self.mMailContent, mailItems,
                                          self.mMailExpire, self.mMailSender)

class CloudAction(SyncActionBase):
    '''
    使用云端玩家信息，可配置要使用的云端信息类型，进入服务器（包括登录和切换）时会同步云端信息到本地，
    而且信息变化时会同步到云端。
    '''
    def Init(self, conf):
        self.mSaveTypes = conf.get('save_types', [])
        self.mApplyTag = conf.get('apply_tag', "")
        self.mCloudCache = {} #uid => dict(cloud items)
        #self.mSyncCoudTimer = timermanager.timerManager.addRepeatTimer(10, self.OnAskSync)
        self.mGameComp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "game")
        self.mSyncCoudTimer = self.mGameComp.AddRepeatedTimer(10, self.OnAskSync)

    def Login(self, uid):
        cloudDbApi.GetCloudItems(uid, self.mApplyTag, lambda records: self.GetCloudCb(uid, records))

    def GetCloudCb(self, uid, records):
        if records is None:
            logout.error('query cloud error!uid:%s' % uid)
            return
        if 0 == len(records):
            userCloud = {}
            cloudDbApi.InsertCloudItems(uid, userCloud, self.mApplyTag)
        else:
            userRecord = records[0]
            userCloud = cloudDbApi.UnicodeConvert(json.loads(userRecord[0]))
            def _toIntKey(src):
                to = {}
                for k, v in src.items():
                    to[int(k)] = v
                return to
            if 'armor' in userCloud:
                userCloud['armor'] = _toIntKey(userCloud['armor'])
            if 'inventory' in userCloud:
                userCloud['inventory'] = _toIntKey(userCloud['inventory'])
        self.mCloudCache[uid] = userCloud
        self.InitUserFromCloud(uid)

    def InitUserFromCloud(self, uid):
        playerId = lobbyGameApi.GetPlayerIdByUid(uid)
        engineApi.ClearUserInventories(playerId)
        engineApi.ClearUserArmors(playerId)
        engineApi.ClearLeftHandItem(playerId)
        engineApi.ClearEffects(playerId)
        engineApi.CleanWholeExtraData(playerId, uid)
        userCloud = self.mCloudCache[uid]
        playerId = lobbyGameApi.GetPlayerIdByUid(uid)
        if CloudItemType.INVENTORY in self.mSaveTypes:
            inventories = userCloud.get(CloudItemType.INVENTORY, {})
            engineApi.SpawnItemsToPlayerInv(inventories, playerId, uid)
        if CloudItemType.ARMOR in self.mSaveTypes:
            armors = userCloud.get(CloudItemType.ARMOR, {})
            engineApi.SetUserArmors(armors, playerId, uid)
        if CloudItemType.HANDS in self.mSaveTypes:
            hands = userCloud.get(CloudItemType.HANDS, {})
            leftHand = hands.get('left', None)
            if leftHand:
                engineApi.SpawnItemToPlayerLeftHand(leftHand, playerId, uid)
            right = hands.get('right', None)
            if right is not None:
                engineApi.ChangeSelectSlot(right, playerId, uid)
        if CloudItemType.EFFECT in self.mSaveTypes:
            effects = userCloud.get(CloudItemType.EFFECT, [])
            engineApi.AddEffectsToUser(effects, playerId, uid)
        if CloudItemType.EXTRA_DATA in self.mSaveTypes:
            data = userCloud.get(CloudItemType.EXTRA_DATA, {})
            engineApi.SetExtraData(data, playerId)
        eventData = {'uid' : uid, "apply_tag":self.mApplyTag}
        engineApi.BroadcastEvent(cloudConsts.FinishSyncCloudItemEvent, eventData)

    def Logout(self, uid):
        if uid in self.mCloudCache:
            self.SaveUserCloud(uid)
            del self.mCloudCache[uid]

    def OnAskSync(self):
        for uid in self.mCloudCache:
            self.SaveUserCloud(uid)

    def SaveUserCloud(self, uid):
        userCloud = self.mCloudCache[uid]
        playerId = lobbyGameApi.GetPlayerIdByUid(uid)
        if CloudItemType.INVENTORY in self.mSaveTypes:
            inventories = engineApi.GetUserInventories(playerId)
            userCloud[CloudItemType.INVENTORY] = inventories
        if CloudItemType.ARMOR in self.mSaveTypes:
            armors = engineApi.GetUserArmors(playerId)
            userCloud[CloudItemType.ARMOR] = armors
        if CloudItemType.EFFECT in self.mSaveTypes:
            effects = engineApi.GetAllEffects(playerId)
            userCloud[CloudItemType.EFFECT] = effects if effects is not None else {}
        if CloudItemType.HANDS in self.mSaveTypes:
            handItemDict = {
                'right' : playerMgr.instanceMgr.GetUserSlot(uid),
                'left' : engineApi.GetLeftHandItem(playerId)
            }
            userCloud[CloudItemType.HANDS] = handItemDict
        if CloudItemType.EXTRA_DATA in self.mSaveTypes:
            extraData = engineApi.GetWholeExtraData(playerId)
            print "GetWholeExtraData", playerId, extraData
            userCloud[CloudItemType.EXTRA_DATA] = extraData
        cloudDbApi.UpdateCloudItems(uid, userCloud, self.mApplyTag)

    def Destroy(self):
        if self.mSyncCoudTimer:
            #timermanager.timerManager.delTimer(self.mSyncCoudTimer)
            #self.mCheckFloatTimer = None
            self.mGameComp.CancelTimer(self.mSyncCoudTimer)

def CreateSyncAction(serverConf):
    """
    信息处理方式包含三种
    0表示不做任何处理
    1表示不使用和同步云端玩家信息，且进入服务器时清空本地信息（可配置清空的信息类型），离开服务器时特定类型的物品通过邮件发送给玩家
    2表示使用云端玩家信息，可配置要使用的云端信息类型，进入服务器（包括登录和切换）时会同步云端信息到本地，而且信息变化时会同步到云端
    """
    processType = serverConf.get('process_type', 0)
    if ProcessType.NO_ACTION == processType:
        return NoAction(serverConf)
    elif ProcessType.FILTER_ACTION == processType:
        return FilterMailAction(serverConf)
    elif ProcessType.CLOUD_ACTION == processType:
        return CloudAction(serverConf)
    return None