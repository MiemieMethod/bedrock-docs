# -*- coding: utf-8 -*-
#匹配状态。
class MatchStatus(object):
	SUCCESS = 0#匹配成功
	TIMEOUT = 1#匹配超时
	CREATE_ROOM_FAIL = 2#创建房间失败


MATCHING_TIMEOUT = 30 #匹配超时时间，30s
MATCHSUCCESS_TIMEOUT = 10#匹配成功后，确认分配房间超时时间，10s
MATCH_PLAYER_NUM = 5#匹配一个房间需要的人数
#创建房间状态。
class CHECK_ROOM_STATUS(object):
	SUCCESS = 0
	FAIL = 1