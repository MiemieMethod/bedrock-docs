# -*- coding: utf-8 -*-
# @Author : uni_kevin(可乐)

import json
import master.netgameApi as netMasterApi
import mod.server.extraMasterApi as extraMasterApi
import master.masterHttp as masterHttp

MasterSystem = extraMasterApi.GetMasterSystemCls()

# --- by xltang
# --- 建议
# 新增的API：RegisterOpCommand可以在游戏服中注册运营指令
# 不含有具体功能，纯转发用途的master端Mod，可以优化掉
# --- end
class HziGachaChestMaster(MasterSystem):

    def __init__(self, namespace, systemName):
        MasterSystem.__init__(self, namespace, systemName)
        masterHttp.RegisterMasterHttp('/hzi/gacha-show-ui', self, self.ShowUI)
        masterHttp.RegisterMasterHttp('/hzi/gacha-reprocess-order', self, self.ReprocessOrder)
        masterHttp.RegisterMasterHttp('/hzi/gacha-broadcast-new-data', self, self.BroadcastNewData)
        masterHttp.RegisterMasterHttp('/hzi/gacha-enable-pool', self, self.EnablePool)
        masterHttp.RegisterMasterHttp('/hzi/gacha-disable-pool', self, self.DisablePool)

    def ShowUI(self, clientId, requestData):
        """
        玩家打开奖池指令
        """
        requestData = json.loads(requestData)
        if not 'uid' in requestData or not isinstance(requestData['uid'], int):
            response = '{"code":400,"message":"Need key: uid(int)"}'
            masterHttp.SendHttpResponse(clientId, response + '\n')
            return
        if not 'identifier' in requestData:
            response = '{"code":400,"message":"Need key: identifier(str)"}'
            masterHttp.SendHttpResponse(clientId, response + '\n')
            return
        serverId = netMasterApi.GetServerIdByUid(requestData['uid'])
        if not serverId:
            response = '{"code":404,"message":"Not Found Online Player by uid: %s"}' % requestData['uid']
            masterHttp.SendHttpResponse(clientId, response + '\n')
            return
        self.NotifyToServerNode(serverId, 'PlayerShowUIFromMaster', requestData)
        response = '{"code":200,"message":"OK"}'
        masterHttp.SendHttpResponse(clientId, response + '\n')

    def ReprocessOrder(self, clientId, requestData):
        """
        根据指定 uid 重新派发奖品
        """
        requestData = json.loads(requestData)
        if not 'uid' in requestData or not isinstance(requestData['uid'], int):
            response = '{"code":400,"message":"Need key: uid(int)"}'
            masterHttp.SendHttpResponse(clientId, response + '\n')
            return
        serverId = netMasterApi.GetServerIdByUid(requestData['uid'])
        if not serverId:
            response = '{"code":404,"message":"Not Found Online Player by uid: %s"}' % requestData['uid']
            masterHttp.SendHttpResponse(clientId, response + '\n')
            return
        data = {
            'uid': requestData['uid'],
            'serverId': serverId
        }
        def CallBack(suc, e):
            if suc:
                masterHttp.SendHttpResponse(clientId, e + '\n')
            else:
                masterHttp.SendHttpResponse(clientId, '{"code":500,"message":"Connect Service Failed"}' + '\n')
        self.RequestToServiceMod('hziGachaChest', 'ReprocessOrder', data, CallBack)

    def BroadcastNewData(self, clientId, requestData):
        """
        功能服下发新的数据
        """
        def CallBack(suc, e):
            if suc:
                masterHttp.SendHttpResponse(clientId, e + '\n')
            else:
                masterHttp.SendHttpResponse(clientId, '{"code":500,"message":"Connect Service Failed"}' + '\n')
        self.RequestToServiceMod('hziGachaChest', 'BroadcastNewData', {}, CallBack)

    def EnablePool(self, clientId, requestData):
        """
        临时启用某个奖池
        """
        requestData = json.loads(requestData)
        if not 'identifier' in requestData:
            response = '{"code":400,"message":"Need key: identifier(str)"}'
            masterHttp.SendHttpResponse(clientId, response + '\n')
            return
        data = {
            'enable': True,
            'identifier': requestData['identifier']
        }
        self.BroadcastToService('SetPoolEnable', data)
        masterHttp.SendHttpResponse(clientId, '{"code":200,"message":"Command Has Been Sent"}' + '\n')

    def DisablePool(self, clientId, requestData):
        """
        临时禁用某个奖池
        """
        requestData = json.loads(requestData)
        if not 'identifier' in requestData:
            response = '{"code":400,"message":"Need key: identifier(str)"}'
            masterHttp.SendHttpResponse(clientId, response + '\n')
            return
        data = {
            'enable': False,
            'identifier': requestData['identifier']
        }
        self.BroadcastToService('SetPoolEnable', data)
        masterHttp.SendHttpResponse(clientId, '{"code":200,"message":"Command Has Been Sent"}' + '\n')