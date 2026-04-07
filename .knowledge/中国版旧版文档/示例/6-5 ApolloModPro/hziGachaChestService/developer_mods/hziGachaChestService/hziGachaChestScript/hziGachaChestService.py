# -*- coding: utf-8 -*-
# @Author : uni_kevin(可乐)

import json
import logging
import time
import weakref

from apolloCommon import commonNetgameApi
import service.serviceConf as serviceConf
import apolloCommon.mysqlPool as mysqlPool
import mod.server.extraServiceApi as serviceApi

ServiceSystem = serviceApi.GetServiceSystemCls()

class HziGachaChestService(ServiceSystem):

    def __init__(self, namespace, systemName):
        ServiceSystem.__init__(self, namespace, systemName)
        self.manager = {}
        config = commonNetgameApi.GetModJsonConfig('hziGachaChestScript')
        if not config or not 'mysql_pool_size' in config:
            logging.error('[抽奖插件]读取 mysql_pool_size 配置失败')
            return
        try:
            mysqlPool.InitDB(config['mysql_pool_size'])
        except:
            logging.error('[抽奖插件]连接数据库失败')
            return
        for moduleName in serviceConf.get_module_names():
            if moduleName.startswith('hziGachaChest'):
                self.manager[moduleName] = HziGachaChestServiceManager(self, moduleName)

    def Destroy(self):
        for mgr in self.manager.itervalues():
            mgr.Destroy()
        self.manager.clear()
        mysqlPool.Finish()
        ServiceSystem.Destroy(self)

class HziGachaChestServiceManager(object):

    def __init__(self, system, moduleName):
        super(HziGachaChestServiceManager, self).__init__()
        logging.debug('[抽卡插件]ServiceManager进程启动')
        self.mSystem = weakref.proxy(system)
        self.mModuleName = moduleName
        self.mTempState = {}
        self.mSystem.RegisterRpcMethod(moduleName, 'RequestCardPoolData', self.RequestCardPoolData)
        self.mSystem.RegisterRpcMethod(moduleName, 'InsertGachaData', self.InsertGachaData)
        self.mSystem.RegisterRpcMethod(moduleName, 'UpdateGachaData', self.UpdateGachaData)
        self.mSystem.RegisterRpcMethod(moduleName, 'ReprocessOrder', self.ReprocessOrder)
        self.mSystem.RegisterRpcMethod(moduleName, 'BroadcastNewData', self.BroadcastNewData)
        self.mSystem.ListenForEvent('HziGachaChest', 'HziGachaChestMaster', 'SetPoolEnable', self, self.SetPoolEnable)

    def GetCardPoolData(self):
        config = commonNetgameApi.GetModJsonConfig('hziGachaChestScript')
        if not config or not 'card_pool' in config:
            logging.error('[抽奖插件]读取 card_pool 配置失败')
            return None
        for cardPool in config['card_pool']:
            for identifier, enable in self.mTempState.iteritems():
                if cardPool['identifier'] == identifier:
                    cardPool['enable'] = enable
                    cardPool['enableTime'] = None
        return config['card_pool']

    def RequestCardPoolData(self, serverId, callbackId, e):
        data = self.GetCardPoolData()
        if not data:
            self.mSystem.ResponseToServer(serverId, callbackId, {'msg': '读取配置失败'})
            return
        self.mSystem.ResponseToServer(serverId, callbackId, {'data': data})

    def InsertGachaData(self, serverId, callbackId, e):
        """
        插入抽奖记录
        :param callbackId:
        :param serverId:
        :param e['uid'] 玩家uid
        :param e['identifier'] 请求的奖池标识符
        :param: data['prize_data'] 奖品数据
        :return: result 是否插入成功
        """
        config = commonNetgameApi.GetModJsonConfig('hziGachaChestScript')
        if not config or not 'card_pool' in config:
            logging.error('[抽奖插件]读取配置失败')
            return
        sql = 'INSERT INTO `hzistudioGachaChestData` (uid, poll_identifier, prize_data, create_time)' \
              ' VALUES (%s, "%s", \'%s\', "%s")'
        params = (e['uid'], e['identifier'], e['prize_data'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        def CallBack(order):
            self.mSystem.ResponseToServer(serverId, callbackId, {'order': order})
        mysqlPool.AsyncInsertOneWithOrderKey(e['uid'], sql % params, (), CallBack)

    def UpdateGachaData(self, serverId, callbackId, e):
        """
        记录发放状态
        :param callbackId:
        :param serverId:
        :param e['order'] 订单id
        :return: result 是否记录成功
        """
        sql = 'UPDATE `hzistudioGachaChestData` SET status=1, prize_time="%s" WHERE _id=%s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), e['order'])
        def CallBack(suc):
            logging.debug('[抽奖插件]订单(id=%s)派发奖品成功' % e['order'])
            self.mSystem.ResponseToServer(serverId, callbackId, {'code': suc})
        mysqlPool.AsyncExecuteWithOrderKey(e['order'], sql, (), CallBack)

    def ReprocessOrder(self, serverId, callbackId, e):
        """
        根据指定 uid 重新派发奖品
        :return:
        """
        sql = 'SELECT * from `hzistudioGachaChestData` where uid=%s and `status`=0' % e['uid']
        def CallBack(data):
            for note in data:
                prizeData = json.loads(note[3])
                eventData = {
                    'uid': str(e['uid']),
                    'orderId': str(note[0]),
                    'prizeData': dict(prizeData),
                }
                self.mSystem.NotifyToServerNode(e['serverId'], 'ReprocessOrder', eventData)
            r = '{"code":200,"message":"Found %s Records.%s"}' % (len(data), 'Check Running Results On Service Server' if len(data) > 0 else 'Nothing to do')
            self.mSystem.ResponseToServer(serverId, callbackId, r)
            if not data:
                self.mSystem.ResponseToServer(serverId, callbackId, '{"code":500,"message":"Not Found Order"}')
        mysqlPool.AsyncQueryWithOrderKey(e['uid'], sql, (), CallBack)

    def SetPoolEnable(self, e):
        """
        设置临时奖池状态
        """
        config = commonNetgameApi.GetModJsonConfig('hziGachaChestScript')
        if not config or not 'card_pool' in config:
            logging.error('[抽奖插件]读取配置失败')
            return
        for cardPool in config['card_pool']:
            if e['identifier'] == cardPool['identifier']:
                """
                控制服更改内存, 让滚动更新新增的lobby/game拉取正确数据
                """
                self.mTempState[e['identifier']] = e['enable']
                """
                广播给当前lobby/game更改内存
                """
                self.BroadcastData()

    def BroadcastNewData(self, serverId, callbackId, e):
        """
        下发新的数据给 lobby/game 服
        """
        r = self.BroadcastData()
        if not r is None:
            self.mSystem.ResponseToServer(serverId, callbackId, '{"code":200,"message":"%s Pool Data Have Been Broadcast."}' % r)
        else:
            self.mSystem.ResponseToServer(serverId, callbackId, '{"code":500,"message":"Service Server Error"}')

    def BroadcastData(self):
        data = self.GetCardPoolData()
        if data:
            for cardPool in data:
                for serverType in cardPool['serverType']:
                    self.mSystem.BroadcastToServerByType(serverType, 'SetNewData', data)
            return len(data)

    def Destroy(self):
        self.mSystem = None