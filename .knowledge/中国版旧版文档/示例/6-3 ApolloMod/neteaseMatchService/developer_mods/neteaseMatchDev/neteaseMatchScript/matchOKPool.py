# -*- coding: utf-8 -*-
import neteaseMatchScript.playerInfo as playerInfo
import logout
import neteaseMatchScript.apiUtil as apiUtil
import neteaseMatchScript.serviceConsts as serviceConsts
class MatchOKPool(object):
	'''
	匹配成功信息
	'''
	def __init__(self, data):
		self.mActivityData = data
		self.mRoomConfirmList = []

	def AddRoom(self, room):
		'''
		新增匹配成功结果
		'''
		rommConfirmInfo = playerInfo.RoomConfirmInfo(room)
		self.mRoomConfirmList.append(rommConfirmInfo)
		groupUIDs = room.GetGroupUIDs()
		logout.info("match success.room id:%d.group uids:" % rommConfirmInfo.mId, groupUIDs)
		eventData = {
			'code': serviceConsts.CodeSuccess,
			'message': serviceConsts.Code2Message[serviceConsts.CodeSuccess],
			'activity_id': self.mActivityData['id'],
			'group_uids': groupUIDs,
			'ui_id' : rommConfirmInfo.mId,
		}
		for uids in groupUIDs:
			apiUtil.BroadcastToServer(uids, serviceConsts.MatchResultServiceEvent, eventData)

	def ConfirmOk(self, id, uid):
		'''
		玩家受到匹配结果了
		'''
		cnt = 0
		for idx, info in enumerate(self.mRoomConfirmList):
			if info.mId == id:
				info.Check(uid)
				if info.IsChecked():
					self.mRoomConfirmList[idx] = None
					cnt += 1
		for i in xrange(cnt):
			self.mRoomConfirmList.remove(None)

	def PlayerLogout(self, uid):
		'''
		玩家退出游戏
		'''
		cnt = 0
		for idx, info in enumerate(self.mRoomConfirmList):
			if info.mId == id and info.IsNeedCheck():
				info.Logout(uid)
				if info.IsChecked():
					self.mRoomConfirmList[idx] = None
					cnt += 1
		for i in xrange(cnt):
			self.mRoomConfirmList.remove(None)

	def ComfirmToUser(self, uid):
		'''
		告知玩家匹配结果
		'''
		for info in self.mRoomConfirmList:
			if info.IsNeedCheck(uid):
				groupUIDs = info.mGroupInfo.GetGroupUIDs()
				eventData = {
					'code': serviceConsts.CodeSuccess,
					'message': serviceConsts.Code2Message[serviceConsts.CodeSuccess],
					'activity_id': self.mActivityData['id'],
					'group_uids': groupUIDs,
					'ui_id': info.mId,
				}
				apiUtil.NotyfToServerByUID(uid, serviceConsts.MatchResultServiceEvent, eventData)

	def Update(self):
		'''
		处理匹配结果，匹配结果只保留10s
		'''
		if not self.mRoomConfirmList:
			return
		confirmInfo = self.mRoomConfirmList[0]
		if confirmInfo.IsTimeout():
			logout.info("not receive player confirm message.room id:%d.uids:" % confirmInfo.mId,
						confirmInfo.mNeedConfrimUIDs)
			self.mRoomConfirmList.remove(confirmInfo)