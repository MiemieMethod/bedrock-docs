# -*- coding: utf-8 -*-
# @Author : uni_kevin(可乐)

import copy
import json
import logging
import random
import time
import mod.server.extraServerApi as serverApi
import lobbyGame.netgameApi as lobbyGameApi
from mod.common.minecraftEnum import ItemPosType

ServerSystem = serverApi.GetServerSystemCls()


def NeteaseAlert(client, text, seconds, xRatio, yRatio):
    neteaseAlert = serverApi.GetSystem('neteaseAlert', 'neteaseAlertDev')
    if neteaseAlert:
        neteaseAlert.Alert(client, text, seconds, xRatio, yRatio)
    else:
        serverApi.GetEngineCompFactory().CreateCommand(client).SetCommand('/tellraw @s {"rawtext":[{"text":"%s"}]}' % text.replace('&', '§'))
        logging.error('[抽奖插件]依赖插件 neteaseAlert 未安装!!')

class HziGachaChestDev(ServerSystem):

    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.cardPoolData = []
        self.transactionsCost = {}
        self.cachePrize = {}
        self.cacheOrder = {}
        self.ListenForEvent('HziGachaChest', 'HziGachaChestBeh', 'RequestGacha', self, self.RequestGacha)
        self.ListenForEvent('HziGachaChest', 'HziGachaChestBeh', 'OnMenusNavigate', self, self.OnMenusNavigate)
        self.ListenForEvent('HziGachaChest', 'HziGachaChestBeh', 'SendRequest', self, self.RequestGacha)
        self.ListenForEvent('HziGachaChest', 'HziGachaChestBeh', 'AnimationStop', self, self.AnimationStop)
        self.ListenForEvent('HziGachaChest', 'HziGachaChestMaster', 'PlayerShowUIFromMaster', self, self.PlayerShowUIFromMaster)
        self.ListenForEvent('HziGachaChest', 'HziGachaChestService', 'ReprocessOrder', self, self.ReprocessOrder)
        self.ListenForEvent('HziGachaChest', 'HziGachaChestService', 'SetNewData', self, self.SetNewData)

    def GetCardPool(self, func, *args, **kwargs):
        if not self.cardPoolData:
            self.RequestCardPoolData(func, *args, **kwargs)
        return self.cardPoolData

    def SetNewData(self, data):
        self.cardPoolData = data

    def RequestCardPoolData(self, func, *args, **kwargs):
        def Callback(suc, result):
            if suc and 'data' in result:
                self.cardPoolData = result['data']
                logging.debug('[抽奖插件]从功能服拉取配置成功')
                """
                把同步 return 掉的事情在拉取到数据后重新执行
                """
                func(*args, **kwargs)
            else:
                for client in serverApi.GetPlayerList():
                    NeteaseAlert(client, '系统错误, 请联系服主(code=4)', 2, 0.5, 0.8)
                logging.error('[抽奖插件]从功能服拉取配置失败')

        self.RequestToService('hziGachaChest', 'RequestCardPoolData', None, Callback)

    @staticmethod
    def CommonServiceCallBack(client, suc, result):
        if not suc:
            NeteaseAlert(client, '系统错误, 请联系服主(code=6)', 2, 0.5, 0.8)
            return False
        if 'msg' in result and result['msg']:
            NeteaseAlert(client, result['msg'], 2, 0.5, 0.8)
        return True

    def GetRandomPrize(self, prizeList, uid):
        """
        按照权重(也就是相对概率)抽取一个奖品
        :param prizeList: 奖品列表
        :param uid: 玩家uid
        :return: prize: 某个奖品
        """
        totalWeights = 0
        for item in prizeList:
            totalWeights += item['weights']
        i = random.randint(1, totalWeights)
        def a(j):
            total = 0
            for prize in prizeList[:j - 1]:
                total += prize['weights']
            return total + 1
        def b(j):
            total = 0
            for prize in prizeList[:j]:
                total += prize['weights']
            return total
        for j, prize in enumerate(prizeList):
            j += 1
            if a(j) <= i <= b(j):
                eventData = self.CreateEventData()
                eventData.update({
                    'uid': copy.copy(uid),
                    'prizeList': copy.deepcopy(prizeList),
                    'prize': prize,
                })
                self.BroadcastEvent('PlanningPrizeEvent', eventData)
                return eventData['prize']

    def RequestGacha(self, e):
        """
        玩家请求抽奖
        :param e['client'] 客户端
        :param e['identifier'] 请求的奖池标识符
        :return: data['slot'] 如果成功, 奖品槽位
        :return: data['msg'] 如果失败, 提示信息
        :return: data['notHide'] 是否要不关闭界面, 默认关闭
        """
        client = e['client']
        # --- by xltang
        # --- BUG？ 
        # 看GetCardPool函数的实现，假如没有获取到cardPoolData的话，会请求service获取cardPoolData
        # 然后service回调的函数里面，会重新执行一次RequestGacha，也就是其实最终还是触发了抽奖逻辑
        # 这里直接先返回给客户端【系统错误】，然后service请求cardPoolData返回后还是进行了抽奖
        # 会给玩家带来很大的迷惑
        # --- end
        if not self.GetCardPool(self.RequestGacha, e):
            NeteaseAlert(client, '系统错误, 请联系服主(code=2)', 2, 0.5, 0.8)
            self.NotifyToClient(client, 'RequestReturn', {'notHide': True})
            return
        # --- by xltang
        # --- 建议
        # 配置里面奖池数据是list，但是其实内存中可以转化一下变成字典的
        # 每次抽奖都要遍历一次全部奖池着实没有必要
        # --- end
        for cardPool in self.cardPoolData:
            # --- by xltang
            # --- BUG？
            # 假如遍历全部奖池之后，没有找到identifier一致的奖池
            # 也需要给客户端一个回应，这里缺失了
            # --- end
            if cardPool['identifier'] == e['identifier']:
                """
                打开奖池界面和点击抽奖按钮之间存在时间差, 所以还是检查一下
                """
                if not cardPool['enable']:
                    NeteaseAlert(client, '奖池暂未开放', 2, 0.5, 0.8)
                    self.NotifyToClient(client, 'RequestReturn', {'notHide': True})
                    return
                # --- by xltang
                # --- 建议
                # 同样建议对原始的配置信息做一个转换，转换为更适合程序判定的数据
                # 每次抽奖都要转换时间戳同样没有必要
                # --- end
                if 'enableTime' in cardPool and cardPool['enableTime']:
                    t1 = int(time.mktime(time.strptime(cardPool['enableTime'][0], '%Y-%m-%d %H:%M:%S')))
                    t2 = int(time.mktime(time.strptime(cardPool['enableTime'][1], '%Y-%m-%d %H:%M:%S')))
                    if not t1 < time.time() < t2:
                        NeteaseAlert(client, '限时奖池暂未开放', 2, 0.5, 0.8)
                        self.NotifyToClient(client, 'RequestReturn', {'notHide': True})
                        return

                needAir = 1
                comp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                for prize in cardPool['prizeList']:
                    info = comp.GetItemBasicInfo(prize['newItemName'])
                    if not info or not 'maxStackSize' in info:
                        NeteaseAlert(client, '系统错误, 请联系服主(code=8)', 2, 0.5, 0.8)
                        self.NotifyToClient(client, 'RequestReturn', {'notHide': True})
                        return
                    maxStackSize = comp.GetItemBasicInfo(prize['newItemName'], prize['newAuxValue'])['maxStackSize']
                    n = int(prize['count'] / maxStackSize)
                    if prize['count'] % maxStackSize:
                        n = n + 1
                    if n > needAir:
                        needAir = n
                hasAir = 0
                comp = serverApi.GetEngineCompFactory().CreateItem(client)
                inventory = comp.GetPlayerAllItems(ItemPosType.INVENTORY)
                for item in inventory:
                    if item is None:
                        hasAir += 1
                if hasAir < needAir:
                    NeteaseAlert(client, '需要 %s 个背包空位' % needAir, 2, 0.5, 0.8)
                    self.NotifyToClient(client, 'RequestReturn', {'notHide': True})
                    return

                uid = lobbyGameApi.GetPlayerUid(client)
                costCurrency, costItem = None, None
                if 'costCurrency' in cardPool:
                    costCurrency = cardPool['costCurrency']
                if 'costItem' in cardPool:
                    costItem = cardPool['costItem']
                
                # --- by xltang
                # --- BUG？
                # 纯看逻辑，self.transactionsCost、self.cacheOrder和self.cachePrize都是以client为key做hash的，同时，整个抽奖逻辑是异步的
                # 那么建议应该对抽奖的行为做一个以client为单位的锁，一个client没有完成一次抽奖前，不允许开始第二次抽奖
                # 虽然可能客户端用动画之类的方式做了限制，但是还是需要在服务端做限制比较好
                # --- end
                def InsertCallback(suc, result):
                    """
                    功能服插入数据库回调
                    成功给客户端发slot播放动画, 失败回滚扣除事务
                    """
                    self.CommonServiceCallBack(client, suc, result)
                    if 'order' in result and not result['order'] is None:
                        self.cacheOrder[client] = result['order']
                        self.NotifyToClient(client, 'RequestReturn', {'slot': self.cachePrize[client]['slot']})
                        del self.transactionsCost[client]
                    else:
                        NeteaseAlert(client, '系统错误, 请联系服主(code=5)', 2, 0.5, 0.8)
                        self.NotifyToClient(client, 'RequestReturn', {'notHide': True})
                        self.transactionsCost[client].RollBack(self)

                def RunCallBack(suc):
                    """
                    扣除玩家货币/物品后回调, 是否成功扣除
                    """
                    if suc:
                        prize = self.GetRandomPrize(cardPool['prizeList'], uid)
                        self.cachePrize[client] = prize
                        pop = ['slot', 'weights', 'borderStayTime', 'showTips']
                        prizeData = json.dumps(dict((key, value) for key, value in prize.iteritems() if not key in pop))
                        data = {
                            'uid': uid,
                            'identifier': e['identifier'],
                            'prize_data': prizeData
                        }
                        self.RequestToService('hziGachaChest', 'InsertGachaData', data, InsertCallback)
                    else:
                        NeteaseAlert(client, '系统错误, 请联系服主(code=3)', 2, 0.5, 0.8)
                        self.NotifyToClient(client, 'RequestReturn', {'notHide': True})

                def InitCallBack(suc, transactionsCost=None):
                    """
                    检查玩家是否有足够货币/物品后回调
                    """
                    eventData = self.CreateEventData()
                    eventData.update({
                        'uid': copy.copy(uid),
                        'identifier': copy.copy(e['identifier']),
                        'enough': suc,
                        'cancel': False,
                        'cancelMsg': ''
                    })
                    self.BroadcastEvent('PlayerGachaEvent', eventData)
                    if eventData['cancel']:
                        if eventData['cancelMsg']:
                            NeteaseAlert(client, eventData['cancelMsg'], 2, 0.5, 0.8)
                        self.NotifyToClient(client, 'RequestReturn', {'notHide': True})
                        return
                    if eventData['enough']:
                        self.transactionsCost[client] = transactionsCost
                        transactionsCost.Run(self, RunCallBack)
                    else:
                        NeteaseAlert(client, cardPool['notEnoughMsg'], 2, 0.5, 0.8)
                        self.NotifyToClient(client, 'RequestReturn', {'notHide': True})

                TransactionsCost(client, uid, InitCallBack, costCurrency, costItem)

    def ReprocessOrder(self, e):
        """
        重新派发奖品, 运营指令
        :param e['uid'] 玩家uid
        :param e['orderId'] 订单id
        :param e['prizeData'] 奖励数据
        """
        client = lobbyGameApi.GetPlayerIdByUid(int(e['uid']))
        self.AnimationStop({'client': client}, e['orderId'], e['prizeData'])

    def AnimationStop(self, e, orderId=None, prizeData=None):
        """
        :param orderId: 订单id
        :param prizeData: 奖励数据
        :param e['client'] 客户端
        动画结束发放奖品
        本地操作从缓存中读取, 来自运营指令的重处理从参数获取数据
        """
        client = e['client']
        cache = False
        if orderId is None or prizeData is None:
            cache = True
            orderId = self.cacheOrder[client]
            prizeData = self.cachePrize[client]
        data = {
            'order': orderId
        }
        eventData = self.CreateEventData()
        eventData.update({
            'uid': copy.copy(lobbyGameApi.GetPlayerUid(client)),
            'orderId': copy.copy(orderId),
            'prizeData': copy.deepcopy(prizeData),
            'cancel': 0,
        })
        self.BroadcastEvent('PlayerAcquirePrizeEvent', eventData)
        if eventData['cancel'] == 2:
            return
        def CallBack(suc, result):
            self.CommonServiceCallBack(client, suc, result)
            if 'code' in result and result['code']:
                if eventData['cancel'] == 0:
                    comp = serverApi.GetEngineCompFactory().CreateItem(client)
                    comp.SpawnItemToPlayerInv(prizeData, client)
            else:
                NeteaseAlert(client, '奖励发放失败, 请联系服主(code=7)', 2, 0.5, 0.8)
                if cache:
                    """
                    本地操作才通知客户端, 重处理就不用发了
                    """
                    self.NotifyToClient(client, 'RequestReturn', {'notHide': True})
        self.RequestToService('hziGachaChest', 'UpdateGachaData', data, CallBack)

    def OnMenusNavigate(self, e):
        """
        玩家点击菜单插件的按钮, 检查是否要打开卡池界面
        :param: client 客户端
        :param: name 点击按钮名称, 客户端已预处理
        """
        if not self.GetCardPool(self.OnMenusNavigate, e):
            return
        for cardPool in self.cardPoolData:
            for menuName in cardPool['neteaseMenus']:
                if e['name'] == menuName:
                    self.ShowUI(e['client'], cardPool['identifier'])

    def PlayerShowUIFromMaster(self, e):
        """
        来自控制服的http运营指令, 玩家打开奖池界面
        """
        self.ShowUIByUid(e['uid'], e['identifier'])

    def ShowUIByUid(self, uid, identifier, enforce=False):
        client = lobbyGameApi.GetPlayerIdByUid(uid)
        self.ShowUI(client, identifier, enforce)

    def ShowUI(self, client, identifier, enforce=False):
        """
        通过奖池标识符让客户端打开界面
        :param client: 客户端
        :param identifier: 奖池标识符
        :param enforce: 强制开启, 无视 enable 和 enableTime(仅浏览)
        :return: 是否成功发送数据到客户端(不代表成功打开)
        """
        if not self.GetCardPool(self.ShowUI, client, identifier, enforce=False):
            return False
        for cardPool in self.cardPoolData:
            if identifier == cardPool['identifier']:
                if not cardPool['enable'] and not enforce:
                    NeteaseAlert(client, '奖池暂未开放', 2, 0.5, 0.8)
                    return False
                # --- by xltang
                # --- BUG？
                # 按照enforce的注释：强制开启, 无视 enable 和 enableTime(仅浏览)
                # 这里判定开启时间的时候却没有考虑enforce参数
                # --- end
                if 'enableTime' in cardPool and cardPool['enableTime']:
                    t1 = int(time.mktime(time.strptime(cardPool['enableTime'][0], '%Y-%m-%d %H:%M:%S')))
                    t2 = int(time.mktime(time.strptime(cardPool['enableTime'][1], '%Y-%m-%d %H:%M:%S')))
                    if not t1 < time.time() < t2:
                        NeteaseAlert(client, '限时奖池暂未开放', 2, 0.5, 0.8)
                        return False
                self.NotifyToClient(client, 'ShowUI', cardPool)
                if 'openMsg' in cardPool and cardPool['openMsg']:
                    msg = str(cardPool['openMsg']).replace('&', '§')
                    NeteaseAlert(client, msg, 2, 0.5, 0.8)
                return True
        return False

class TransactionsCost(object):
    def __init__(self, client, uid, callBack, costCurrency=None, costItem=None):
        """
        玩家扣除事务
        :param client: 客户端
        :param uid: 玩家uid
        :param callBack: 是否有足够货币和物品回调
        :param costCurrency: 扣除货币列表
        :param costItem: 扣除物品列表
        """
        self.client = client
        self.uid = uid
        self.callBack = callBack
        self.costCurrency = costCurrency[:]
        self.costItem = costItem[:] if not costItem is None else [] # 计数用, 要被 remove
        self.costItem_ = costItem[:] if not costItem is None else []
        """
        检查背包, 同步
        """
        if self.costItem:
            comp = serverApi.GetEngineCompFactory().CreateItem(client)
            a = comp.GetPlayerAllItems(ItemPosType.INVENTORY, True)
            c = comp.GetPlayerAllItems(ItemPosType.ARMOR, True)
            d = comp.GetPlayerAllItems(ItemPosType.OFFHAND, True)
            """
            合并同类物品, 仅凭 itemName 和 aux
            """
            from collections import defaultdict
            itemMap = defaultdict(int)
            for item in a + c + d:
                if item:
                    itemMap[item['newItemName'], item['newAuxValue']] += int(item['count'])
            for item in [{'newItemName': _[0], 'newAuxValue': _[1], 'count': count} for _, count in
                         itemMap.iteritems()]:
                if item:
                    for item_ in self.costItem:
                        temp = item_[:]
                        item_, count_ = str(item_).split('*')
                        itemName_, aux_ = str(item_).split('@')
                        if itemName_ == item['newItemName'] and int(aux_) == item['newAuxValue'] and item[
                            'count'] >= int(count_):
                            self.costItem.remove(temp)
        """
        查询库存货币, 异步
        """
        if self.costCurrency:
            def CallBack(success, data):
                if not success or not 'code' in data or data['code'] != 1:
                    logging.warning('[抽奖插件]查询玩家库存货币错误')
                    self.callBack(False)
                else:
                    for cost in self.costCurrency:
                        currency_, amount_ = str(cost).split('*')
                        if not currency_ in dict(data['entity']).keys():
                            """
                            玩家库存中没有要求此类货币记录
                            """
                            self.callBack(False)
                            return
                        for currency, amount in dict(data['entity']).iteritems():
                            if currency_ == currency and amount < int(amount_):
                                """
                                库存数量不足
                                """
                                self.callBack(False)
                                return
                    if len(self.costItem) == 0:
                        self.callBack(True, self)
                    else:
                        """
                        背包物品不足
                        """
                        self.callBack(False)

            tradeSystem = serverApi.GetSystem('neteaseTrade', 'neteaseTradeDev')
            if tradeSystem:
                tradeSystem.QueryPlayerDoughs(uid, CallBack)
            else:
                logging.error('[抽奖插件]没有安装依赖插件 neteaseTrade')
                self.callBack(False)
        else:
            if len(self.costItem) == 0:
                self.callBack(True, self)

    def Run(self, system, callBack):
        mod = {}
        for cost in self.costCurrency:
            currency_, amount_ = str(cost).split('*')
            mod.update({currency_: int(amount_) * -1})
        data = {'uid': self.uid, 'mod': mod}

        def CallBack(suc, result):
            if suc and result['code'] == 1:
                if self.costItem_:
                    comp = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
                    for item_ in self.costItem_:
                        item_, count_ = str(item_).split('*')
                        itemName_, aux_ = str(item_).split('@')
                        command = '/clear @s {} {} {}'.format(str(itemName_).replace('minecraft:', ''), aux_, count_)
                        comp.SetCommand(command, self.client)
                callBack(True)
            else:
                logging.warning('[抽奖插件]扣除货币失败')
                callBack(False)

        if self.costCurrency:
            system.RequestToService('neteaseTrade', 'UpdatePlayerDoughsEvent', data, CallBack)
        else:
            CallBack(True, {'code': 1})

    def RollBack(self, system):
        logging.warning('[抽奖插件]有玩家抽奖失败, 触发回滚')
        """
        回滚货币扣除
        """
        if self.costCurrency:
            mod = {}
            for cost in self.costCurrency:
                currency_, amount_ = str(cost).split('*')
                mod.update({currency_: int(amount_)})
            data = {'uid': self.uid, 'mod': mod}
            system.RequestToService('neteaseTrade', 'UpdatePlayerDoughsEvent', data, None)
        """
        回滚物品扣除
        """
        if not self.costItem_:
            return
        comp = serverApi.GetEngineCompFactory().CreateItem(self.client)
        for item_ in self.costItem_:
            item_, count_ = str(item_).split('*')
            itemName_, aux_ = str(item_).split('@')
            maxStackSize = comp.GetItemBasicInfo(itemName_, int(aux_))['maxStackSize']
            if maxStackSize and int(count_) > maxStackSize:
                for _ in int(count_) / maxStackSize:
                    itemDict = {
                        'newItemName': itemName_,
                        'newAuxValue': int(aux_),
                        'count': maxStackSize,
                    }
                    comp.SpawnItemToPlayerInv(itemDict, self.client)
                itemDict = {
                    'newItemName': itemName_,
                    'newAuxValue': int(aux_),
                    'count': int(count_) % maxStackSize,
                }
                comp.SpawnItemToPlayerInv(itemDict, self.client)
            else:
                itemDict = {
                    'newItemName': itemName_,
                    'newAuxValue': int(aux_),
                    'count': int(count_),
                }
                comp.SpawnItemToPlayerInv(itemDict, self.client)
