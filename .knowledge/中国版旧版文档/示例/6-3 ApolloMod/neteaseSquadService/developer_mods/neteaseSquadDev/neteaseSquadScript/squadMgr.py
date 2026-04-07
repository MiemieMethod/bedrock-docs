# -*- coding: utf-8 -*-

from collections import OrderedDict, Counter
import logout
import neteaseSquadScript.squadConst as squadConst
import neteaseSquadScript.timermanager as timermanager
import apolloCommon.commonNetgameApi as commonNetgameApi
import time
import weakref
import server.extraServiceApi as serviceApi


class SquadMgr(object):
	def __init__(self, system, moduleName):
		super(SquadMgr, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = moduleName
		self.mSquadMemberCountLimit, self.mSquadApplicantCountLimit, self.mSquadRecruitCD, self.mSquadAssembleCD, self.mRecruitmentShowLimit = self.mSystem.GetSquadCfg()
		self.mSquadOrder = 0
		self.mSquadData = {
			squadConst.CfgKeyUsers: {},
			squadConst.CfgKeySquads: OrderedDict(),
			squadConst.CfgKeyMembers: {},
		}
		self.mSquadInvolvedServers = set()
		self.mSquadDisconnectedPlayers = Counter()
		self.mSquadSwitchedPlayers = Counter()
		self.mPopSquadDisconnectedPlayersTimer = timermanager.timerManager.addRepeatTimer(60, self.PopSquadDisconnectedPlayers)
		self.mPopSquadSwitchedPlayersTimer = timermanager.timerManager.addRepeatTimer(60, self.PopSquadSwitchedPlayers)

		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadPlayerServerSwitchEvent, self.OnSquadPlayerServerSwitchReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadPlayerDisconnectEvent, self.OnSquadPlayerDisconnectReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadPlayerUpdateEvent, self.OnSquadPlayerUpdateReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadPlayerRecruitEvent, self.OnSquadPlayerRecruitReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadPlayerLeaveEvent, self.OnSquadPlayerLeaveReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadApplyListEvent, self.OnSquadApplyListReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadRecruitListEvent, self.OnSquadRecruitListReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadRecruitmentApplyEvent, self.OnSquadRecruitmentApplyReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SetupSquadEvent, self.OnSetupSquadReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.DissolveSquadEvent, self.OnDissolveSquadReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadChiefTransferEvent, self.OnSquadChiefTransferReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.KickSquadPlayerEvent, self.OnKickSquadPlayerReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadInvitePlayerEvent, self.OnSquadInvitePlayerReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadAppendPlayerEvent, self.OnSquadAppendPlayerReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadRejectPlayerEvent, self.OnSquadRejectPlayerReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadApplicantsClearEvent, self.OnSquadApplicantsClearReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.SquadPlayerCheckEvent, self.OnSquadPlayerCheckReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.QuerySquadByOrderEvent, self.OnQuerySquadByOrderReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.JoinSquadEvent, self.OnJoinSquadReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.AssembleEvent, self.OnAssembleReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.ForwardEvent, self.OnForwardReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.PreForwardEvent, self.OnPreForwardReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.TeleportEvent, self.OnTeleportReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.AssembleOptionEvent, self.OnAssembleOptionReq)
		self.mSystem.RegisterRpcMethod(moduleName, squadConst.LeaveOptionEvent, self.OnLeaveOptionReq)

		self.mSystem.ListenForEvent(
			serviceApi.GetEngineNamespace(),
			serviceApi.GetEngineSystemName(),
			'UpdateServerStatusEvent',
			self, self.VerifyInvolvedServers
		)

	def VerifyInvolvedServers(self, m):
		for serverId in list(self.mSquadInvolvedServers):
			if m.get(str(serverId)) != '1':
				self.mSquadInvolvedServers.discard(serverId)

	def Destroy(self):
		self.mSystem.UnListenForEvent(
			serviceApi.GetEngineNamespace(),
			serviceApi.GetEngineSystemName(),
			'UpdateServerStatusEvent',
			self, self.VerifyInvolvedServers
		)

		if self.mPopSquadDisconnectedPlayersTimer:
			timermanager.timerManager.delTimer(self.mPopSquadDisconnectedPlayersTimer)
			self.mPopSquadDisconnectedPlayersTimer = None
		if self.mPopSquadSwitchedPlayersTimer:
			timermanager.timerManager.delTimer(self.mPopSquadSwitchedPlayersTimer)
			self.mPopSquadSwitchedPlayersTimer = None
		self.mSystem = None

	def SquadMgrRender(self, serverId, callbackId, data):
		respData = {
			'code': data['code'],
			'message': data.get('message', ''),
			'entity': data.get('entity', {})
		}
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def PopSquadDisconnectedPlayers(self):
		"""
		每60秒执行一次，每次执行，离线状态的每个玩家自身计数+1（当玩家再次上线/离线时会立刻归零），当玩家计数>=4时，会被踢出队伍（每次执行，最多只会踢出累积计数最高的44位玩家）
		"""
		if not self.mSquadDisconnectedPlayers:
			return
		self.mSquadDisconnectedPlayers.update(dict.fromkeys(self.mSquadDisconnectedPlayers.keys(), 1))
		done = []
		still = True
		while still:
			if not self.mSquadDisconnectedPlayers:
				break
			for uid, count in self.mSquadDisconnectedPlayers.most_common(44):
				if count > 4:
					self.mSquadDisconnectedPlayers.pop(uid, -1)
					self.mSquadData[squadConst.CfgKeyUsers].pop(uid, -1)
					squad = self.mSquadData[squadConst.CfgKeyMembers].pop(uid, None)
					if squad:
						squad['members'].pop(uid, -1)
						if squad not in done:
							done.append(squad)
				else:
					still = False
					break
		for squad in done:
			for member in squad['members'].values():
				self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerUpdateEvent, {
					'code': squadConst.RespCodeSuccess,
					'message': '',
					'entity': {'uid': member['uid'], 'squad': squad}
				})

	def PopSquadSwitchedPlayers(self):
		"""
		每60秒执行一次，每次执行，转服状态的每个玩家自身计数+1（当玩家再次上线/离线时会立刻归零），当玩家计数>=10时，会被踢出队伍（每次执行，最多只会踢出累积计数最高的10位玩家）
		"""
		for line in self.mSquadData[squadConst.CfgKeySquads].values():
			squad = line['squad']
			if len(squad['members']) >= self.mSquadMemberCountLimit:
				self.mSquadData[squadConst.CfgKeySquads].pop(squad['order'], -1)
		if not self.mSquadSwitchedPlayers:
			return
		self.mSquadSwitchedPlayers.update(dict.fromkeys(self.mSquadSwitchedPlayers.keys(), 1))
		still = True
		while still:
			if not self.mSquadSwitchedPlayers:
				break
			for uid, count in self.mSquadSwitchedPlayers.most_common(10):
				if count > 10:
					self.mSquadSwitchedPlayers.pop(uid, -1)
					self.OnSquadPlayerDisconnectReq(None, None, {'uid': uid})
				else:
					still = False
					break

	def OnSquadRecruitmentApplyReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【申请加入正在招募队员的队伍】
		"""
		uid = data.get('uid')
		order = data.get('order')
		# if not (isinstance(uid, int) and isinstance(order, int)):
		# 	self.mSystem.ResponseToServer(serverId, callbackId, {
		# 		'code': squadConst.RespCodeInvalidParameter,
		# 		'message': '',
		# 		'entity': {'order': order}
		# 	})
		# 	return
		info = self.mSquadData[squadConst.CfgKeyUsers].get(uid)
		if not info or info.get('offline'):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§c玩家 {} 不在线'.format(uid),
				'entity': {'order': order}
			})
			return
		if uid in self.mSquadData[squadConst.CfgKeyMembers]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§e您已在队伍中',
				'entity': {'order': order}
			})
			return
		recruitment = self.mSquadData[squadConst.CfgKeySquads].get(order, {})
		squad = recruitment.get('squad')
		if not squad:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§c队伍不存在',
				'entity': {'order': order}
			})
			return
		if len(squad['members']) >= self.mSquadMemberCountLimit:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§e队伍已满员',
				'entity': {'order': order}
			})
			return
		if uid in recruitment['applicants']:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§e您已在该队伍的申请列表中',
				'entity': {'order': order}
			})
			return
		if self.mSquadApplicantCountLimit - len(recruitment['applicants']) <= 0:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§e队伍申请人数过多',
				'entity': {'order': order}
			})
			return
		recruitment['applicants'].add(uid)
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
			'entity': {'order': order}
		})
		chief = squad['members'].get(squad['chief'])
		chief and self.mSystem.NotifyToServerNode(chief['serverId'], squadConst.SquadRecruitmentApplyEvent, {'chief': chief['uid']})

	def OnSquadApplyListReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【获取加入队伍申请列表】
		"""
		chief = data.get('uid')
		if not chief:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(chief)
		if not (squad and squad.get('chief') == chief):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '非队长'
			})
			return
		applicants = []
		for uid in self.mSquadData[squadConst.CfgKeySquads].get(squad['order'], {}).get('applicants', ''):
			info = self.mSquadData[squadConst.CfgKeyUsers].get(uid)
			if info and not info.get('offline') and uid not in self.mSquadData[squadConst.CfgKeyMembers]:
				applicants.append(info)
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
			'entity': {'uid': chief, 'applicants': applicants}
		})

	def OnSquadRecruitListReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【获取正在招募队员的队伍列表】
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		recruitment = []
		for line in self.mSquadData[squadConst.CfgKeySquads].values():
			squad = line['squad']
			applicants = line['applicants']
			info = self.mSquadData[squadConst.CfgKeyUsers].get(squad['chief'])
			if info:
				recruitment.append({
					'order': squad['order'],
					'chief': squad['chief'],
					'name': squad['members'][squad['chief']]['name'],
					'count': len(squad['members']),
					'label': squad['label'],
					'applicable': uid not in applicants and (self.mSquadApplicantCountLimit - len(applicants))
				})
		if self.mRecruitmentShowLimit >= 0:
			recruitment = recruitment[0-self.mRecruitmentShowLimit:]
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
			'entity': {'uid': uid, 'recruitment': recruitment}
		})

	def OnSquadPlayerServerSwitchReq(self, serverId, callbackId, data):
		"""
		记录玩家开始转服（因为转服离开游戏服/大厅服）
		"""
		uid = data.get('uid')
		# if not isinstance(uid, int):
		# 	return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not squad:
			return
		self.mSquadSwitchedPlayers[uid] = 0

	def OnSquadPlayerDisconnectReq(self, serverId, callbackId, data):
		"""
		记录玩家离线，队长离线会立刻转让队长
		"""
		uid = data.get('uid')
		# if not isinstance(uid, int):
		# 	return
		self.mSquadData[squadConst.CfgKeyUsers].get(uid, {})['offline'] = 1
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not squad:
			return
		if squad['chief'] == uid:
			self.mSquadData[squadConst.CfgKeyMembers].pop(uid, -1)
			squad['members'].pop(uid, -1)
			if squad['members']:
				# 需要转让队长
				usurper = max(squad['members'].values(), key=lambda info: (-1 if info.get('offline') else info['lv']))
				if usurper.get('offline'):
					# 解散队伍
					self.mSquadData[squadConst.CfgKeySquads].pop(squad['order'], -1)
					for member in squad['members'].values():
						self.mSquadData[squadConst.CfgKeyMembers].pop(member['uid'], -1)
				else:
					squad['chief'] = usurper['uid']
					for member in squad['members'].values():
						self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerUpdateEvent, {
							'code': squadConst.RespCodeSuccess,
							'message': '§e玩家`{}`成为新队长'.format(usurper['name']),
							'entity': {'uid': member['uid'], 'squad': squad}
						})
			else:
				self.mSquadData[squadConst.CfgKeySquads].pop(squad['order'], -1)
		else:
			self.mSquadDisconnectedPlayers[uid] = 0
			for member in squad['members'].values():
				if member['uid'] != uid:
					self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerDisconnectEvent, {
						'code': squadConst.RespCodeSuccess,
						'message': '§e玩家`{}`失去连接'.format(squad['members'][uid]['name']),
						'entity': {'uid': member['uid'], 'offline': uid}
					})

	def OnSquadPlayerLeaveReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【离开当前的队伍】
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not squad:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '不在队伍中'
			})
			return
		if squad.get('trap') or self.mSystem.GetSquadRestrictions(serverId).get('trap'):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '队伍当前处于禁止离开状态'
			})
			return
		self.mSquadData[squadConst.CfgKeyMembers].pop(uid, -1)
		info = self.mSquadData[squadConst.CfgKeyUsers].get(uid, {'name': '史蒂夫'})
		squad['members'].pop(uid, -1)
		if uid == squad['chief']:
			if not squad['members']:
				self.mSquadData[squadConst.CfgKeySquads].pop(squad['order'], -1)
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': squadConst.RespCodeSuccess,
					'message': '队伍已解散',
					'entity': {'uid': uid}
				})
				return
			else:
				# 需要转让队长
				usurper = max(squad['members'].values(), key=lambda info: (-1 if info.get('offline') else info['lv']))
				if usurper.get('offline'):
					# 解散队伍
					self.mSquadData[squadConst.CfgKeySquads].pop(squad['order'], -1)
					for member in squad['members'].values():
						self.mSquadData[squadConst.CfgKeyMembers].pop(member['uid'], -1)
				else:
					squad['chief'] = usurper['uid']
					for member in squad['members'].values():
						self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerUpdateEvent, {
							'code': squadConst.RespCodeSuccess,
							'message': '§e玩家`{}`成为新队长'.format(usurper['name']),
							'entity': {'uid': member['uid'], 'squad': squad}
						})
		else:
			for member in squad['members'].values():
				self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerUpdateEvent, {
					'code': squadConst.RespCodeSuccess,
					'message': '§e玩家`{}`离开队伍'.format(info['name']),
					'entity': {'uid': member['uid'], 'squad': squad}
				})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '您已离队',
			'entity': {'uid': uid}
		})

	def OnSquadPlayerRecruitReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【发布队员招募】
		"""
		uid = data.get('uid')
		label = data.get('label')
		# if not (uid and isinstance(label, str)):
		if not isinstance(label, str):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not (squad and squad.get('chief') == uid):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '非队长'
			})
			return
		if len(squad['members']) >= self.mSquadMemberCountLimit:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '队伍已满员'
			})
			return
		if not commonNetgameApi.CheckNameValid(label):
			logout.info('OnSquadPlayerRecruitReq invalid label: {}'.format(label))
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': '存在敏感词'
			})
			return
		now = time.time()
		order = squad['order']
		recruitment = self.mSquadData[squadConst.CfgKeySquads].get(order)
		if recruitment:
			if now - recruitment['squad']['polish'] < self.mSquadRecruitCD:
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': squadConst.RespCodeInvalidUser,
					'message': '操作频繁'
				})
				return
			del self.mSquadData[squadConst.CfgKeySquads][order]
		else:
			recruitment = {'squad': squad, 'applicants': set()}
		squad['label'] = label
		squad['polish'] = now
		self.mSquadData[squadConst.CfgKeySquads][order] = recruitment
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '发布成功',
			'entity': {'uid': uid}
		})

	def OnSquadPlayerUpdateReq(self, serverId, callbackId, data):
		"""
		更新玩家个人信息
		"""
		uid = data.get('uid')
		name = data.get('name')
		lv = data.get('lv')
		if not (isinstance(name, str) and isinstance(lv, int) and uid):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		self.mSquadData[squadConst.CfgKeyUsers].setdefault(uid, {}).clear()
		self.mSquadData[squadConst.CfgKeyUsers][uid].update({'uid': uid, 'name': name, 'lv': lv, 'serverId': serverId})
		self.mSquadInvolvedServers.add(serverId)
		self.OnSquadPlayerCheckReq(serverId, callbackId, {'uid': uid, 'broadcast': 1})

	def OnSquadPlayerCheckReq(self, serverId, callbackId, data):
		"""
		client初始化完成发送给server，server处理一些内部逻辑后发送给service的请求，service需要查询并返回对应玩家当前的队伍信息
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		respData = {
			'code': squadConst.RespCodeSuccess,
			'message': '',
			'entity': {'uid': uid}
		}
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if squad:
			# squad = {'chief': 10086, 'members': {10086: user, ..., 10010: user}, 'label': '中国移不动'}
			respData['entity']['squad'] = squad
			order = squad['order']
			if order in self.mSquadData[squadConst.CfgKeySquads]:
				respData['entity']['recruiting'] = 1
			if data.get('broadcast'):
				self.mSquadSwitchedPlayers.pop(uid, -1)
				if uid in self.mSquadDisconnectedPlayers:
					# 重新连接
					self.mSquadData[squadConst.CfgKeyUsers].get(uid, {}).pop('offline', -1)
					self.mSquadDisconnectedPlayers.pop(uid, -1)
					for member in squad['members'].values():
						# {'uid': uid, 'name': name, 'lv': lv, 'serverId': serverId}
						if uid != member['uid'] and squad is self.mSquadData[squadConst.CfgKeyMembers].get(member['uid']):
							self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerReconnectEvent, {
								'code': squadConst.RespCodeSuccess,
								'message': '§e玩家`{}`重新连接'.format(squad['members'][uid]['name']),
								'entity': {'uid': member['uid'], 'online': uid}
							})
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnQuerySquadByOrderReq(self, serverId, callbackId, data):
		"""
		根据队伍编号获得队伍信息
		"""
		order = data.get('order')
		# if not (order and isinstance(order, int)):
		# 	self.mSystem.ResponseToServer(serverId, callbackId, {
		# 		'code': squadConst.RespCodeInvalidParameter,
		# 		'message': ''
		# 	})
		# 	return
		respData = {
			'code': squadConst.RespCodeSuccess,
			'message': '',
			'entity': {}
		}
		squad = self.mSquadData[squadConst.CfgKeySquads].get(order, {}).get('squad')
		if squad:
			respData['entity']['squad'] = squad
		else:
			for squad in self.mSquadData[squadConst.CfgKeyMembers].values():
				if order == squad['order']:
					respData['entity']['squad'] = squad
					break
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnPreForwardReq(self, serverId, callbackId, data):
		"""
		来自server的队长所在的serverId，发送消息给队伍所在的server，获取队长所在的维度和位置坐标
		"""
		uid = data.get('uid')
		destination = data.get('destination')
		# if not (isinstance(uid, int) and isinstance(destination, str)):
		if not isinstance(destination, str):
			return
		info = self.mSquadData[squadConst.CfgKeyUsers].get(uid)
		if not info or info.get('offline'):
			logout.error('玩家 {} 传送时无自身信息或不在线'.format(uid))
			return
		self.mSystem.NotifyToServerNode(info['serverId'], squadConst.ForwardEvent, {
			'uid': uid, 'destination': destination, 'serverId': serverId,
			'msg': '§e即将传送，请稍候……'
		})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
		})

	def OnForwardReq(self, serverId, callbackId, data):
		"""
		来自server的准备集合请求，获取队长所在的serverId，发送消息给队伍所在的server，获取队长所在的维度和位置坐标
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		chief = squad['members'].get(squad['chief'])
		if not (squad and chief):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§c队伍不存在'
			})
			return
		self.mSystem.NotifyToServerNode(chief['serverId'], squadConst.PreForwardEvent, {
			'chief': chief['uid'], 'uid': uid
		})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
		})

	def OnJoinSquadReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【同意加入队伍的邀请】
		"""
		uid = data.get('uid')
		order = data.get('order')
		# if not (isinstance(uid, int) and isinstance(order, int)):
		# 	self.mSystem.ResponseToServer(serverId, callbackId, {
		# 		'code': squadConst.RespCodeInvalidParameter,
		# 		'message': ''
		# 	})
		# 	return
		info = self.mSquadData[squadConst.CfgKeyUsers].get(uid)
		if not info or info.get('offline'):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§c玩家 {} 不在线'.format(uid),
			})
			return
		if uid in self.mSquadData[squadConst.CfgKeyMembers]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§e您已在队伍中'
			})
			return
		squad = self.mSquadData[squadConst.CfgKeySquads].get(order, {}).get('squad')
		if not squad:
			for squad in self.mSquadData[squadConst.CfgKeyMembers].values():
				if order == squad['order']:
					break
			else:
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': squadConst.RespCodeInvalidUser,
					'message': '§c队伍不存在'
				})
				return
		if len(squad['members']) >= self.mSquadMemberCountLimit:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§e队伍已满员',
			})
			return
		applicants = self.mSquadData[squadConst.CfgKeySquads].get(squad['order'], {}).get('applicants', set())
		applicants.discard(uid)
		self.mSquadData[squadConst.CfgKeyMembers][uid] = squad
		squad['members'][uid] = info
		if len(squad['members']) >= self.mSquadMemberCountLimit:
			self.mSquadData[squadConst.CfgKeySquads].pop(squad['order'], -1)
		for member in squad['members'].values():
			self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerUpdateEvent, {
				'code': squadConst.RespCodeSuccess,
				'message': '§a玩家`{}`加入队伍'.format(info['name']),
				'entity': {'uid': member['uid'], 'squad': squad}
			})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
		})

	def OnDissolveSquadReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【解散队伍】
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not (squad and squad.get('chief') == uid):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '非队长'
			})
			return
		self.mSquadData[squadConst.CfgKeySquads].pop(squad['order'], -1)
		for uid in squad['members'].keys():
			self.mSquadData[squadConst.CfgKeyMembers].pop(uid, -1)
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '队伍已解散',
			'entity': {'uid': uid}
		})
		# squad.pop('polish', -1)
		for serverId in self.mSquadInvolvedServers.copy():
			self.mSystem.NotifyToServerNode(serverId, squadConst.DissolveSquadEvent, {
				'code': squadConst.RespCodeSuccess,
				'message': '队伍已解散',
				'entity': {
					'squad': squad,
				}
			})

	def OnSetupSquadReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【创建队伍】
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		self.mSquadInvolvedServers.add(serverId)
		if uid in self.mSquadData[squadConst.CfgKeyMembers]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '已在队伍中'
			})
			return
		info = self.mSquadData[squadConst.CfgKeyUsers].get(uid)
		if not info or info.get('offline'):
			logout.error('玩家 {} 创建队伍时无自身信息或不在线'.format(uid))
			return
		squad = {'order': self.mSquadOrder, 'chief': uid, 'members': {uid: info}}
		self.mSquadOrder += 1
		self.mSquadData[squadConst.CfgKeyMembers][uid] = squad
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '创建队伍成功',
			'entity': {'uid': uid, 'squad': squad}
		})
		for serverId in self.mSquadInvolvedServers.copy():
			self.mSystem.NotifyToServerNode(serverId, squadConst.SetupSquadEvent, {
				'code': squadConst.RespCodeSuccess,
				'message': '',
				'entity': {
					'squad': squad,
				}
			})

	def OnSquadChiefTransferReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【转让队长】
		"""
		print 'OnSquadChiefTransferReq', data
		chief = data.get('chief')
		uid = data.get('uid')
		# if chief == uid or not (isinstance(chief, int) and isinstance(uid, int)):
		if chief == uid:
			return
		info = self.mSquadData[squadConst.CfgKeyUsers].get(uid)
		if not info or info.get('offline'):
			logout.warning('玩家 {} 转让队长时无玩家 {} 信息或不在线'.format(chief, uid))
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '§c无法将队长转让给不在线的玩家'
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(chief)
		if not (squad and squad.get('chief') == chief):
			logout.warning('OnSquadChiefTransferReq 非队长 chief: {} uid: {}'.format(chief, uid))
			return
		if uid not in squad['members']:
			logout.warning('OnSquadChiefTransferReq 非同队 chief: {} uid: {}'.format(chief, uid))
			return
		squad['chief'] = uid
		for member in squad['members'].values():
			self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerUpdateEvent, {
				'code': squadConst.RespCodeSuccess,
				'message': '§e玩家`{}`变更为队长'.format(info['name']),
				'entity': {'uid': member['uid'], 'squad': squad}
			})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': ''
		})

	def OnKickSquadPlayerReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【踢掉队伍中的玩家】
		"""
		chief = data.get('chief')
		uid = data.get('uid')
		# if chief == uid or not (isinstance(chief, int) and isinstance(uid, int)):
		if chief == uid:
			# self.mSystem.ResponseToServer(serverId, callbackId, {
			# 	'code': squadConst.RespCodeInvalidParameter,
			# 	'message': ''
			# })
			return
		info = self.mSquadData[squadConst.CfgKeyUsers].get(uid)
		if not info:
			logout.error('玩家 {} 踢人时无玩家 {} 信息'.format(chief, uid))
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(chief)
		if not (squad and squad.get('chief') == chief):
			logout.warning('OnKickSquadPlayerReq 非队长 chief: {} uid: {}'.format(chief, uid))
			# self.mSystem.ResponseToServer(serverId, callbackId, {
			# 	'code': squadConst.RespCodeInvalidUser,
			# 	'message': '非队长'
			# })
			return
		if uid not in squad['members']:
			logout.warning('OnKickSquadPlayerReq 非同队 chief: {} uid: {}'.format(chief, uid))
			# self.mSystem.ResponseToServer(serverId, callbackId, {
			# 	'code': squadConst.RespCodeInvalidUser,
			# 	'message': '非同队'
			# })
			return
		if squad.get('trap') or self.mSystem.GetSquadRestrictions(serverId).get('trap'):
			logout.info('OnKickSquadPlayerReq 队伍当前处于禁止离开状态 squad: {}'.format(squad))
			# self.mSystem.ResponseToServer(serverId, callbackId, {
			# 	'code': squadConst.RespCodeInvalidUser,
			# 	'message': '队伍当前处于禁止离开状态'
			# })
			return
		self.mSquadData[squadConst.CfgKeyMembers].pop(uid, -1)
		squad['members'].pop(uid, -1)
		self.mSystem.NotifyToServerNode(info['serverId'], squadConst.SquadPlayerUpdateEvent, {
			'code': squadConst.RespCodeSuccess,
			'message': '§e您被请离队伍',
			'entity': {'uid': info['uid']}
		})
		for member in squad['members'].values():
			# {'uid': uid, 'name': name, 'lv': lv, 'serverId': serverId}
			if uid != member['uid'] and squad is self.mSquadData[squadConst.CfgKeyMembers].get(member['uid']):
				self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerUpdateEvent, {
					'code': squadConst.RespCodeSuccess,
					'message': '§e玩家`{}`被队长请离队伍'.format(info['name']),
					'entity': {'uid': member['uid'], 'squad': squad}
				})

	def OnSquadInvitePlayerReq(self, serverId, callbackId, data):
		"""
		邀请一个玩家加入队伍
		"""
		chief = data.get('chief')
		uid = data.get('uid')
		dealer = data.get('dealer')
		# if chief == uid or not (isinstance(chief, int) and isinstance(uid, int) and isinstance(dealer, int)):
		if chief == uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': '参数不合法',
			})
			return
		info = self.mSquadData[squadConst.CfgKeyUsers].get(uid)
		if not info or info.get('offline'):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '玩家 {} 不在线'.format(uid),
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(chief)
		if not (squad and squad.get('chief') == chief):
			logout.warning('OnSquadInvitePlayerReq 非队长 chief: {} uid: {}'.format(chief, uid))
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '玩家 {} 非队长'.format(chief),
			})
			return
		if uid in self.mSquadData[squadConst.CfgKeyMembers]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '玩家 {} 已组队'.format(uid),
			})
			return
		if len(squad['members']) >= self.mSquadMemberCountLimit:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '队伍已满员',
			})
			return
		d = self.mSquadData[squadConst.CfgKeyUsers].get(dealer)
		c = self.mSquadData[squadConst.CfgKeyUsers].get(chief)
		if not (d and c):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '玩家 {} 或 {} 不在线'.format(dealer, chief),
			})
			return
		self.mSystem.NotifyToServerNode(info['serverId'], squadConst.SquadInvitePlayerEvent, {
			'code': squadConst.RespCodeSuccess,
			'message': '收到组队邀请',
			'entity': {'uid': info['uid'], 'order': squad['order'], 'msg': '玩家`{}`邀请您加入`{}`的队伍'.format(d['name'], c['name'])}
		})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '成功发送邀请'
		})

	def OnSquadAppendPlayerReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【同意指定玩家的加入队伍申请】
		"""
		chief = data.get('chief')
		uid = data.get('uid')
		dealer = data.get('dealer')
		# if chief == uid or not (isinstance(chief, int) and isinstance(uid, int) and isinstance(dealer, int)):
		if chief == uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': '参数不合法',
				'entity': {'uid': uid}
			})
			return
		info = self.mSquadData[squadConst.CfgKeyUsers].get(uid)
		if not info or info.get('offline'):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '玩家 {} 不在线'.format(uid),
				'entity': {'uid': uid}
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(chief)
		if not (squad and squad.get('chief') == chief):
			logout.warning('OnSquadAppendPlayerReq 非队长 chief: {} uid: {}'.format(chief, uid))
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '玩家 {} 非队长'.format(chief),
				'entity': {'uid': uid}
			})
			return
		if uid in self.mSquadData[squadConst.CfgKeyMembers]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '玩家 {} 已组队'.format(uid),
				'entity': {'uid': uid}
			})
			return
		if len(squad['members']) >= self.mSquadMemberCountLimit:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '队伍已满员',
				'entity': {'uid': uid}
			})
			return
		applicants = self.mSquadData[squadConst.CfgKeySquads].get(squad['order'], {}).get('applicants', set())
		applicants.discard(uid)
		self.mSquadData[squadConst.CfgKeyMembers][uid] = squad
		squad['members'][uid] = info
		# if len(squad['members']) >= self.mSquadMemberCountLimit:
		# 	self.mSquadData[squadConst.CfgKeySquads].pop(squad['order'], -1)
		for member in squad['members'].values():
			self.mSystem.NotifyToServerNode(member['serverId'], squadConst.SquadPlayerUpdateEvent, {
				'code': squadConst.RespCodeSuccess,
				'message': '§a玩家`{}`加入队伍'.format(info['name']),
				'entity': {'uid': member['uid'], 'squad': squad}
			})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
			'entity': {'uid': uid}
		})

	def OnSquadRejectPlayerReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【拒绝指定玩家的加入队伍申请】
		"""
		chief = data.get('chief')
		uid = data.get('uid')
		# if chief == uid or not (isinstance(chief, int) and isinstance(uid, int)):
		if chief == uid:
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(chief)
		if not (squad and squad.get('chief') == chief):
			logout.warning('OnSquadRejectPlayerReq 非队长 chief: {} uid: {}'.format(chief, uid))
			return
		applicants = self.mSquadData[squadConst.CfgKeySquads].get(squad['order'], {}).get('applicants', set())
		applicants.discard(uid)

	def OnSquadApplicantsClearReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【清空申请入队列表】
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not (squad and squad.get('chief') == uid):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '非队长'
			})
			return
		applicants = self.mSquadData[squadConst.CfgKeySquads].get(squad['order'], {}).get('applicants', set())
		applicants.clear()
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
			'entity': {'uid': uid}
		})

	def OnAssembleReq(self, serverId, callbackId, data):
		"""
		处理server转发的客户端界面操作：【队伍集合】
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not (squad and squad.get('chief') == uid):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '非队长'
			})
			return
		if squad.get('lost') or self.mSystem.GetSquadRestrictions(serverId).get('lost'):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '队伍当前处于禁止召集状态'
			})
			return
		now = time.time()
		if now - squad.get('call', 0) < self.mSquadAssembleCD:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidUser,
				'message': '操作频繁'
			})
			return
		squad['call'] = now
		for member in squad['members'].values():
			if member['uid'] != squad['chief']:
				self.mSystem.NotifyToServerNode(member['serverId'], squadConst.AssembleEvent, {
					'code': squadConst.RespCodeSuccess,
					'message': '收到集合请求',
					'entity': {'uid': member['uid'], 'msg': '前往当前队长的所在地'}
				})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '已向当前其余队员发送集合请求',
		})

	def OnTeleportReq(self, serverId, callbackId, data):
		"""
		将一个队伍内的所有玩家传送到某个服务器的某个位置
		"""
		uid = data.get('uid')
		destination = data.get('destination')
		serverId = data.get('serverId')
		# if not (serverId and isinstance(uid, int) and isinstance(destination, str)):
		if not isinstance(destination, str):
			logout.warning('OnTeleportReq 参数有误 data: {}'.format(data))
			return
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not squad:
			logout.warning('OnTeleportReq 玩家 {} 不在队伍中'.format(uid))
			return
		for member in squad['members'].values():
			if not member.get('offline'):
				self.mSystem.NotifyToServerNode(member['serverId'], squadConst.ForwardEvent, {
					'uid': member['uid'], 'destination': destination, 'serverId': serverId,
					'msg': '§e即将前往{}，请稍候……'.format('`{}`'.format(data['label']) if 'label' in data and data['label'] else '')
				})

	def OnAssembleOptionReq(self, serverId, callbackId, data):
		"""
		禁用或开启一个队伍的“召集队友”功能
		"""
		uid = data.get('uid')
		ban = data.get('ban')
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not squad:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': '队伍不存在'
			})
			return
		if ban:
			squad['lost'] = 1
		else:
			squad.pop('lost', -1)
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
			'entity': {'uid': uid, 'ban': ban}
		})

	def OnLeaveOptionReq(self, serverId, callbackId, data):
		"""
		禁用或开启一个队伍的“离开队伍”功能
		"""
		uid = data.get('uid')
		ban = data.get('ban')
		squad = self.mSquadData[squadConst.CfgKeyMembers].get(uid)
		if not squad:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': squadConst.RespCodeInvalidParameter,
				'message': '队伍不存在'
			})
			return
		if ban:
			squad['trap'] = 1
		else:
			squad.pop('trap', -1)
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': squadConst.RespCodeSuccess,
			'message': '',
			'entity': {'uid': uid, 'ban': ban}
		})
