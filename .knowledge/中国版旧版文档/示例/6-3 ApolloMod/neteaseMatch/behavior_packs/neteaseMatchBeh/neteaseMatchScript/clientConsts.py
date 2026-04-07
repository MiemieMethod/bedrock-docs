# -*- coding: utf-8 -*-
# mod信息
ModName = 'neteaseMatch'
ModVersion = '1.0.0'
ClientSystemClsPath = 'neteaseMatchScript.matchClientSystem.MatchClientSystem'
ClientSystemName = 'neteaseMatchClient'
ServerSystemName = 'neteaseMatchServerSystem'

# 服务端自定义事件
ResponseModJsonDataEvent = 'ResponseModJsonDataEvent'
ShowWaitUIServerEvent = 'ShowWaitUIServerEvent'
WaitNumChangedServerEvent = 'WaitNumChangedServerEvent'
MatchResultServerEvent = 'MatchResultServerEvent'
ClearMatchUIServerEvent = 'ClearMatchUIServerEvent'
ApplyErrServerEvent = 'ApplyErrServerEvent'
# 客户端事件
GetModJsonDataEvent = 'GetModJsonDataEvent'
MatchResultEvent = 'MatchResultEvent'
ApplyToMatchClientEvent = 'ApplyToMatchClientEvent' #申请匹配客户端事件
ApplyToMatchLocalEvent = 'ApplyToMatchLocalEvent' #申请匹配客户端事件
DefaultApplyToMatchEvent = 'DefaultApplyToMatchEvent'
RetryApplyToMatchLocalEvent = 'RetryApplyToMatchLocalEvent'
ApplyToMatchResultEvent = 'ApplyToMatchResultEvent'
ConfirmOKClientEvent = 'ConfirmOKClientEvent'
GetLoginUIClientEvent = 'GetLoginUIClientEvent'
RequestCancelMatchClientEvent = 'RequestCancelMatchClientEvent'

#错误提示信息
CodeSuccess = 0
ApplyCodeNotMatchFregment = 1
ApplyCodeGroupIdNotExist = 2
ApplyCodeTeamToManyPeopleToGroup = 3
ApplyCodeApplyModeErr = 4#参悟信息参见mod.json中not_match_mode_error_message配置
ApplyCodeActivityNotExist = 5
ApplyCodeInMatching = 6
ApplyCodeTeamPlayerInMatching = 7
MatchCodeTimeoutNoRetry = 100
MatchCodeTimeoutCanRetry = 101
MatchCodeAutoCancelMatch = 102
MatchCodeCancelMatch = 103
MatchCodeCanceBySelf = 104
ReMatchCodeNotInPool = 200
Code2Message = {
	CodeSuccess : "成功",
	ApplyCodeNotMatchFregment : '%s不在同一分段，报名失败',
	ApplyCodeGroupIdNotExist : '阵营不存在，报名失败',
	ApplyCodeTeamToManyPeopleToGroup : '组队人员过多，报名失败',
	ApplyCodeActivityNotExist : '活动不存在，报名失败',
	ApplyCodeInMatching:'你已报名',
	ApplyCodeTeamPlayerInMatching:'%s已报名',
	MatchCodeTimeoutNoRetry:'报名超时',
	MatchCodeTimeoutCanRetry:'报名超时',
	MatchCodeAutoCancelMatch:'取消报名',
	MatchCodeCancelMatch:"%s已取消报名",
	ReMatchCodeNotInPool:'还没报名，不能重新报名',
	MatchCodeCanceBySelf:'你已取消报名'
}
