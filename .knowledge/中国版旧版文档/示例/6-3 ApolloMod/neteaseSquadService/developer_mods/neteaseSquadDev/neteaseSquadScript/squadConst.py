# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseSquad"
ClientSystemName = "neteaseSquadBeh"
ClientSystemClsPath = "neteaseSquadScript.squadClientSystem.SquadClientSystem"
ServerSystemName = "neteaseSquadDev"
ServerSystemClsPath = "neteaseSquadScript.squadServerSystem.SquadServerSystem"
ServiceSystemName = "neteaseSquadService"
ServiceSystemClsPath = "neteaseSquadScript.squadServiceSystem.SquadServiceSystem"
MasterSystemName = "neteaseSquadMaster"
MasterSystemClsPath = "neteaseSquadScript.squadMasterSystem.SquadMasterSystem"

# UI
squadUIName = "squadUI"
squadUIClsPath = "neteaseSquadScript.squadClientUI.SquadScreen"
squadUIScreenDef = "squadUI.main"

CfgKeyUsers = 'Users'
CfgKeySquads = 'Squads'
CfgKeyMembers = 'Members'

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"
AddServerPlayerEvent = 'AddServerPlayerEvent'
DelServerPlayerEvent = 'DelServerPlayerEvent'
AddLevelEvent = 'AddLevelEvent'

# 事件
SquadPlayerUpdateEvent = 'SquadPlayerUpdateEvent'
SquadPlayerServerSwitchEvent = 'SquadPlayerServerSwitchEvent'
SquadPlayerDisconnectEvent = 'SquadPlayerDisconnectEvent'
SquadPlayerReconnectEvent = 'SquadPlayerReconnectEvent'
SquadPlayerOfflineEvent = 'SquadPlayerOfflineEvent'
SquadApplyListEvent = 'SquadApplyListEvent'
SquadAppendPlayerEvent = 'SquadAppendPlayerEvent'
SquadRejectPlayerEvent = 'SquadRejectPlayerEvent'
SquadApplicantsClearEvent = 'SquadApplicantsClearEvent'
SquadInvitePlayerEvent = 'SquadInvitePlayerEvent'
SquadPlayerCheckEvent = 'SquadPlayerCheckEvent'
SquadPlayerRecruitEvent = 'SquadPlayerRecruitEvent'
SquadPlayerLeaveEvent = 'SquadPlayerLeaveEvent'
SquadRecruitListEvent = 'SquadRecruitListEvent'
SquadRecruitmentApplyEvent = 'SquadRecruitmentApplyEvent'
SquadApplicationNoticeEvent = 'SquadApplicationNoticeEvent'
JoinSquadEvent = 'JoinSquadEvent'
SetupSquadEvent = 'SetupSquadEvent'
DissolveSquadEvent = 'DissolveSquadEvent'
SquadChiefTransferEvent = 'SquadChiefTransferEvent'
KickSquadPlayerEvent = 'KickSquadPlayerEvent'
QuerySquadByOrderEvent = 'QuerySquadByOrderEvent'
AssembleEvent = 'AssembleEvent'
ForwardEvent = 'ForwardEvent'
PreForwardEvent = 'PreForwardEvent'
PostForwardEvent = 'PostForwardEvent'
TeleportEvent = 'TeleportEvent'
AssembleOptionEvent = 'AssembleOptionEvent'
LeaveOptionEvent = 'LeaveOptionEvent'

# 错误码
RespCodeSuccess = 1  # 请求成功
RespCodeInvalidParameter = 4  # 请求参数有误
RespCodeInvalidUser = 2  # 用户不存在或不在线
RespCodeTimeout = 2  # 请求超时
RespCodeDBError = 3  # 数据库操作失败
