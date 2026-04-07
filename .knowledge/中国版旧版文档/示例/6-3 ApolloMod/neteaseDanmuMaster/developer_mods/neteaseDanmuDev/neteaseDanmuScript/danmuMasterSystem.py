# -*- coding: utf-8 -*-

import master.masterHttp as masterHttp
import neteaseDanmuScript.danmuConst as danmuConst
import json
import server.extraMasterApi as masterApi
import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.redisPool as redisPool

MasterSystem = masterApi.GetMasterSystemCls()


def post_json_loads(p_object):
	if isinstance(p_object, dict):
		return {post_json_loads(key): post_json_loads(value) for key, value in p_object.iteritems()}
	elif isinstance(p_object, list):
		return [post_json_loads(item) for item in p_object]
	elif isinstance(p_object, unicode):
		return p_object.encode('utf-8')
	else:
		return p_object

# 用下面这个函数在python2中反序列化json字符串得到的数据结构内的字符串就不会是unicode格式
json_loads = lambda s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kwargs: post_json_loads(
	json.loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kwargs))


class DanmuMasterSystem(MasterSystem):
	"""
	该mod的master类
	提供两个http接口（运营指令）
	详见readme
	"""

	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)

		masterHttp.RegisterMasterHttp(danmuConst.DanmuRequestMapping.Forbid, self, self.OnForbidReq)
		masterHttp.RegisterMasterHttp(danmuConst.DanmuRequestMapping.Unlock, self, self.OnUnlockReq)

		mysqlPool.InitDB(5)
		redisPool.InitDB(5)

	def Destroy(self):
		super(DanmuMasterSystem, self).Destroy()
		mysqlPool.Finish()
		redisPool.Finish()

	def DanmuMasterRender(self, clientId, respData):
		"""
		格式化并回应http请求结果
		"""
		responseBody = json.dumps({
			'code': respData['code'],
			'message': respData.get('message', ''),
			'entity': respData.get('entity', {})
		})
		masterHttp.SendHttpResponse(clientId, responseBody)

	def OnForbidReq(self, clientId, requestBody):
		"""
		限制/解除限制发弹幕（针对全局）
		"""
		reqData = json_loads(requestBody)
		print 'OnForbidReq', reqData
		if 'ban' not in reqData:
			return self.DanmuMasterRender(clientId, {
				'code': danmuConst.RespCodeInvalidParameter,
				'message': '参数不合法',
			})
		ban = bool(reqData['ban'])
		redisPool.AsyncFuncWithKey(
			lambda conn, ban: conn.set('netease:danmu:ban', ban) if ban else conn.delete('netease:danmu:ban'),
			"forbid_all_danmu",
			lambda *args: self.DanmuMasterRender(clientId, {
				'code': danmuConst.RespCodeSuccess,
				'message': '请求成功',
			}),
			int(ban)
		)

	def ManipulateDanmuIcon(self, conn, uid, icon_id, lock):
		try:
			c = conn.cursor()
			if lock:
				c.execute('DELETE FROM neteaseDanmuIconInfo WHERE uid=%s AND icon_id=%s', (uid, icon_id))
			else:
				c.execute('INSERT INTO neteaseDanmuIconInfo VALUES (%s, %s) ON DUPLICATE KEY UPDATE uid = VALUES(uid)', (uid, icon_id))
			conn.commit()
		except Exception as e:
			conn.rollback()

	def OnUnlockReq(self, clientId, requestBody):
		"""
		解锁/锁定一个玩家的某个弹幕头像
		"""
		reqData = json_loads(requestBody)
		print 'OnUnlockReq', reqData
		if 'icon_id' not in reqData or 'lock' not in reqData or 'uid' not in reqData:
			return self.DanmuMasterRender(clientId, {
				'code': danmuConst.RespCodeInvalidParameter,
				'message': '参数不合法',
			})
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.ManipulateDanmuIcon,
			'MANIPULATE_DANMU_ICON',
			lambda *args: self.DanmuMasterRender(clientId, {
				'code': danmuConst.RespCodeSuccess,
				'message': '请求成功',
			}),
			reqData['uid'], reqData['icon_id'], reqData['lock']
		)
