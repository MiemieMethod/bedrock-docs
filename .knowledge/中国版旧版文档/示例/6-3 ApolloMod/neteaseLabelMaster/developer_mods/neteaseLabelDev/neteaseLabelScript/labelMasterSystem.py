# -*- coding: utf-8 -*-

import datetime
import master.masterHttp as masterHttp
import logout
import neteaseLabelScript.labelConst as labelConst
import json
import server.extraMasterApi as masterApi
import apolloCommon.mysqlPool as mysqlPool

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


json_loads = lambda s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kwargs: post_json_loads(json.loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kwargs))


class LabelMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		if not self.InitMysqlPool():
			return

		masterHttp.RegisterMasterHttp(labelConst.LabelRequestMapping.Insert, self, self.OnInsertReq)
		masterHttp.RegisterMasterHttp(labelConst.LabelRequestMapping.Delete, self, self.OnDeleteReq)

	def Destroy(self):
		mysqlPool.Finish()
		super(LabelMasterSystem, self).Destroy()

	def InitMysqlPool(self):
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("Exception in InitMysqlPool")
			return False
		return True

	def LabelMasterRender(self, clientId, respData):
		responseBody = json.dumps({
			'code': respData['code'],
			'message': respData.get('message', ''),
			'entity': respData.get('entity', {})
		})
		masterHttp.SendHttpResponse(clientId, responseBody)

	def OnInsertReq(self, clientId, requestBody):
		"""
		给指定uid的玩家解锁一个称号（仅仅修改数据库）
		"""
		reqData = json_loads(requestBody)
		print 'OnInsertReq', reqData
		if not ('uid' in reqData and 'labelId' in reqData and isinstance(reqData['labelId'], str)):
			return self.LabelMasterRender(clientId, {
				'code': labelConst.RespCodeInvalidParameter,
				'message': '请求参数不合法'
			})
		uid = reqData['uid']
		labelId = reqData['labelId']
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.Manipulate,
			'UNLOCK_LABELS_FOR_PLAYER_%s' % uid,
			lambda rowcount: self.LabelMasterRender(clientId, {
				'code': labelConst.RespCodeSuccess,
				'message': '请求成功',
				'entity': {
					'rowcount': rowcount
				}
			}) if isinstance(rowcount, int) else self.LabelMasterRender(clientId, {
				'code': labelConst.RespCodeDBError,
				'message': '数据库操作失败'
			}),
			'INSERT INTO {} (uid, label_id, recv_date, part, in_use) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE uid = uid'.format(labelConst.TableLabelData),
			(uid, labelId, datetime.datetime.now().isoformat(), -1, 0)
		)

	def OnDeleteReq(self, clientId, requestBody):
		"""
		删除指定uid的玩家的一个已经解锁的称号（仅仅修改数据库）
		"""
		reqData = json_loads(requestBody)
		print 'OnDeleteReq', reqData
		if not ('uid' in reqData and 'labelId' in reqData and isinstance(reqData['labelId'], str)):
			return self.LabelMasterRender(clientId, {
				'code': labelConst.RespCodeInvalidParameter,
				'message': '请求参数不合法'
			})
		uid = reqData['uid']
		labelId = reqData['labelId']
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.Manipulate,
			'DELETE_LABELS_FOR_PLAYER_%s' % uid,
			lambda rowcount: self.LabelMasterRender(clientId, {
				'code': labelConst.RespCodeSuccess,
				'message': '请求成功',
				'entity': {
					'rowcount': rowcount
				}
			}) if isinstance(rowcount, int) else self.LabelMasterRender(clientId, {
				'code': labelConst.RespCodeDBError,
				'message': '数据库操作失败'
			}),
			'DELETE FROM {} WHERE uid=%s AND label_id=%s'.format(labelConst.TableLabelData),
			(uid, labelId)
		)

	def Manipulate(self, conn, operation, parameters):
		try:
			c = conn.cursor()
			c.execute(operation, parameters)
			rowcount = c.rowcount
			conn.commit()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in Manipulate e: {} operation: {} parameters: {}'.format(e, operation, parameters))
			return False
		return len(rowcount)
