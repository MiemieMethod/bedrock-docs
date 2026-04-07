# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseMapAttrs"
ServerSystemName = "neteaseMapAttrsServer"
MasterSystemName = "neteaseMapAttrsMaster"
ClientSystemName = 'neteaseMapAttrsClient'
ClientSystemClsPath = 'neteaseMapAttrsScript.mapAttrsClientSys.MapAttrsClientSys'
ServerSystemClsPath = 'neteaseMapAttrsScript.mapAttrsServerSys.MapAttrsServerSys'
MasterSystemClsPath = 'neteaseMapAttrsScript.mapAttrsMasterSys.MapAttrsMasterSys'

# http配置
SuccessCode = 1
FailCode = 2

# 维度
DimensionIdUnknown = -1
DimensionIdOverWorld = 0

# event
class ServerEvent(object):
	LoginResponse = "LoginResponse"
	HttpResponse = "HttpResponse"

class ClientEvent(object):
	PlayerEnter = "PlayerEnter"

class MasterEvent(object):
	SetMapArea = "SetMapArea"
