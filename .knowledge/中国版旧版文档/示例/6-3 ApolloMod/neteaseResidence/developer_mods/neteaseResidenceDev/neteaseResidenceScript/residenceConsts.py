# -*- coding: utf-8 -*-

#整个Mod的一些绑定配置
ModVersion = "1.0.1"
ModNameSpace = "neteaseResidence"
ServerSystemName = "neteaseResidenceServer"
MasterSystemName = "neteaseResidenceMaster"
ClientSystemName = 'neteaseResidenceClient'
ClientSystemClsPath = 'neteaseResidenceScript.residenceClientSys.ResidenceClientSys'
ServerSystemClsPath = 'neteaseResidenceScript.residenceServerSys.ResidenceServerSys'
MasterSystemClsPath = 'neteaseResidenceScript.residenceMasterSys.ResidenceMasterSys'

# http配置
QueryPlayerResidenceInfoUrl = '/residence/query/player-residence-info'		# 运营指令：查询某个玩家的全部领地
QueryServerResidenceInfoUrl = '/residence/query/server-residence-info'		# 运营指令：查询指定服务器中的所有领地信息，但不包括对应所有者玩家列表。
SetResidenceInfoUrl = '/residence/create-residence'							# 运营指令：创建新领地（将某个服务器地图的某个区域指定为某个玩家的领地）
DelResidenceUrl = '/residence/delete-residence'								# 运营指令：删除某个领地
AddPlayerToResidenceUrl = '/residence/add-player-to-residence'				# 运营指令：给已经存在的领地添加一个新的所有者
RemovePlayerFromResidenceUrl = '/residence/remove-player-from-residence'	# 运营指令：为已经存在的领地移除一个所有者
ChangeResidenceAuthorityUrl = '/residence/change-residence-authority'		# 运营指令：修改指定领地权限
ChangeResidenceBornPosUrl = '/residence/change-residence-teleport-pos'		# 运营指令：修改一个领地的传送点
ChangePlayerResidenceAuthorityUrl = '/residence/change-player-residence-authority'	# 运营指令：修改指定外部玩家在指定领地的权限
ReleasePlayerResidenceLockUrl = '/residence/release-player-residence-lock'	# 运营指令：强制释放玩家领地操作锁
#
SuccessCode = 1		# 返回码：成功
FailCode = 2		# 返回码：失败

# event
QueryServerResidenceEvent = 'QueryServerResidenceEvent'		# master向server发送【查询当前server领地信息】的运营指令（需指定offset和limit）
HttpResponseEvent = 'HttpResponseEvent'						# server向master返回运营指令的执行结果
SetPlayerResidenceEvent = 'SetPlayerResidenceEvent'			# master向server发送【创建新领地】的运营指令
HttpDelResidenceEvent = 'HttpDelResidenceEvent'				# master向server发送【删除指定领地】的运营指令
LoginRequestEvent = 'LoginRequestEvent'						# client向server发送客户端加载完毕事件
LoginResponseEvent = 'LoginResponseEvent'					# server向client发送，服务端加载角色完毕，并返回角色基础信息的事件
SyncResidenceDataEvent = 'SyncResidenceDataEvent'			# server向client同步领地信息
SyncPersonalDataEvent = 'SyncPersonalDataEvent'				# server向client同步领地相关玩家信息与权限信息
# SyncAllResidenceEvent = 'SyncAllResidenceEvent'
# SyncPlayerResidenceEvent = 'SyncPlayerResidenceEvent'
# MoveToOtherResidenceEvent = 'MoveToOtherResidenceEvent'
AddPlayerToResidenceEvent = 'AddPlayerToResidenceEvent'				# master向server发送【给已经存在的领地添加一个新的所有者】的运营指令
RemovePlayerFromResidenceEvent = 'RemovePlayerFromResidenceEvent'	# master向server发送【为已经存在的领地移除一个所有者】的运营指令
ChangeResidenceAuthorityEvent = 'ChangeResidenceAuthorityEvent'		# master向server发送【修改指定领地权限】的运营指令
ChangePlayerResidenceAuthorityEvent = 'ChangePlayerResidenceAuthorityEvent'		# master向server发送【修改指定外部玩家在指定领地的权限】的运营指令
ChangeResidenceBornPosEvent = 'ChangeResidenceBornPosEvent'				# master向server发送【修改一个领地的传送点】的运营指令
ReleasePlayerResidenceLockEvent = 'ReleasePlayerResidenceLockEvent'		# master向server发送【强制释放玩家领地操作锁】的运营指令
DelResidenceFromServerEvent = "DelResidenceFromServerEvent"				# server向client同步被删除领地的信息
RemovePlayerResidentFromServerEvent = "RemovePlayerResidentFromServerEvent"		# server向client同步被从领地所有者中删除的信息


# 宏定义--维度
DimensionIdUnknown = -1		# 未定义维度
DimensionIdOverWorld = 0	# 主世界

# 空气方块的Identifier
IdentifierAir = "minecraft:Air"

# 领地名字的长度限制
ResidenceNameLimit = 40

# 数据库查询与http请求相关的参数限制
QueryLimitOnce = 10		# 单次查询运营指令默认返回的领地信息数量
FetchLimitOnce = 100	# 服务器启动时，单次数据库查询返回的领地信息数量

# 领地区块分割AOI
# 为了能够在单服领地数量数以万计乃至十万计的时候，也能快速根据坐标定位领地，快速查询一块指定区域有哪些领地
# 把整个地图按照32*32分割为网格，进行hash
# 利用类似AOI的算法，维护每个领地占据的网格
ResidenceAoiGrid = 32
# 返回指定维度和坐标所属的网格
def FindChunkByPos(dim, pos):
	x = pos[0] // ResidenceAoiGrid
	if pos[0] % ResidenceAoiGrid > 0:
		x += 1
	z = pos[2] // ResidenceAoiGrid
	if pos[2] % ResidenceAoiGrid > 0:
		z += 1
	return (dim, x, z)

# 返回指定维度的指定AABB包围盒占据的网格列表
def FindChunkByArea(dim, minPos, maxPos):
	xMin, xMax = minPos[0] // ResidenceAoiGrid, maxPos[0] // ResidenceAoiGrid
	if maxPos[0] % ResidenceAoiGrid > 0:
		xMax += 1
	zMin, zMax = minPos[2] // ResidenceAoiGrid, maxPos[2] // ResidenceAoiGrid
	if maxPos[2] % ResidenceAoiGrid > 0:
		zMax += 1
	result = []
	for x in xrange(xMin, xMax + 1):
		for z in xrange(zMin, zMax + 1):
			result.append((dim, x, z))
	return result

# 领地权限的配置的类型，目前有bool和list两种类型
AuthorityValueType = {
	"place_on_block_items_limit":list,
	"can_destroy_block_limit":list,
	"cannot_interact_block_list":list,
	"can_block_be_exploded":bool,
	"can_block_be_stepon":bool,
	"can_block_be_mobgriefing":bool,
	"can_attack_player":bool,
	"can_attack_mob":bool,
	"can_projectile_take_effect":bool,
	"can_interact_entity_list":list,
	"can_ride":bool,
	"can_flow_into":bool,
	"can_other_player_enter":bool,
	"can_other_player_teleport":bool,
	"can_dragon_egg_teleport_into":bool,
	"can_piston_effect_into":bool,
}

# 领地权限的配置，是否支持针对特定玩家独立配置
AuthorityForPlayer = {
	"place_on_block_items_limit":True,
	"can_destroy_block_limit":True,
	"cannot_interact_block_list":True,
	"can_block_be_exploded":False,
	"can_block_be_stepon":True,
	"can_block_be_mobgriefing":True,
	"can_attack_player":True,
	"can_attack_mob":True,
	"can_projectile_take_effect":True,
	"can_interact_entity_list":True,
	"can_ride":True,
	"can_flow_into":False,
	"can_other_player_enter":True,
	"can_other_player_teleport":True,
	"can_dragon_egg_teleport_into":False,
	"can_piston_effect_into":False,
}

SERVER_PLAYER_UID = 1				# 所有者的UID是这个值，则认为此领地属于系统
SERVER_PLAYER_PLAYERID = "-1"		# 所有者的entityId是这个值，则认为此领地属于系统
SERVER_PLAYER_NICKNAME = "无属主"	# 系统作为领地所有者时，显示的领地所有者名字	

# 申请但是没用最终使用的领地ID，会在服务器进程销毁的同时失效，合理地配置参数可以减少浪费
# 当没有可用领地ID时，创建新领地会失败，过于吝啬于领地ID的申请，会导致遇到此类状况的几率变大
QueryCheckTime = 3.0		# 每隔多少秒检查一次是否有足够的领地ID可用
QueryResIdLimitMin = 5		# 当可用的领地ID少于多少时，会申请新的可用领地ID
QueryResIdLimitOnce = 10	# 每次申请可用领地ID，会一次性的申请多少个

# 错误码
class ResponseCode(object):
	Suc = 1
	GetPlayerActionLockFail = 2
	ReachResidenceNumLimit= 3
	ResidenceNameEmpty = 4
	ResidenceNameLengthLimit = 5
	ResidenceNameConflict = 6
	ResidenceNameNotValid = 7
	ResidenceAreaWrong = 8
	SizeOverLimit = 9
	AreaConflictWithOther = 10
	PlayerNotExist = 11
	TargetResidenceNotExist = 12
	TargetResidenceNotTopLevel = 13
	AlreadyOwnerOfTarget = 14
	NoUsableResId = 15

# 错误信息
FMT_EN = {}
FMT_EN[ResponseCode.GetPlayerActionLockFail] = "player residence action is locked, please wait and try later."
FMT_EN[ResponseCode.ReachResidenceNumLimit] = "player already has too much toplevel residence."
FMT_EN[ResponseCode.ResidenceNameEmpty] = "residence name cannot empty."
FMT_EN[ResponseCode.ResidenceNameLengthLimit] = "residence name length over limit."
FMT_EN[ResponseCode.ResidenceNameConflict] = "residence name not unique."
FMT_EN[ResponseCode.ResidenceNameNotValid] = "residence name not legal."
FMT_EN[ResponseCode.ResidenceAreaWrong] = "residence area minPos > maxPos, please check input position."
FMT_EN[ResponseCode.SizeOverLimit] = "residence size over limit."
FMT_EN[ResponseCode.AreaConflictWithOther] = "residence area is conflict with other."
FMT_EN[ResponseCode.PlayerNotExist] = "player not exist."
FMT_EN[ResponseCode.TargetResidenceNotExist] = "target residence not exist."
FMT_EN[ResponseCode.TargetResidenceNotTopLevel] = "target residence not top level, cannot add owner."
FMT_EN[ResponseCode.AlreadyOwnerOfTarget] = "player already owner of target residence."
FMT_EN[ResponseCode.NoUsableResId] = "no usable residence id."
# 错误信息 -- 中文
FMT_CH = {}
FMT_CH[ResponseCode.GetPlayerActionLockFail] = "无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
FMT_CH[ResponseCode.ReachResidenceNumLimit] = "无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
FMT_CH[ResponseCode.ResidenceNameEmpty] = "由于名字重复或不合法，无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
FMT_CH[ResponseCode.ResidenceNameLengthLimit] = "由于名字重复或不合法，无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
FMT_CH[ResponseCode.ResidenceNameConflict] = "由于名字重复或不合法，无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
FMT_CH[ResponseCode.ResidenceNameNotValid] = "由于名字重复或不合法，无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
FMT_CH[ResponseCode.ResidenceAreaWrong] = "由于名字重复或不合法，无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
FMT_CH[ResponseCode.SizeOverLimit] = "当前选择的领地区域大小不符合要求，圈地失败；领地范围要求：东西{x0}~{x1}格，南北{z0}~{z1}格，高度{y0}~{y1}格"
FMT_CH[ResponseCode.AreaConflictWithOther] = "当前选中的领地区域与其他同层级领地有交叉，圈地失败"
FMT_CH[ResponseCode.PlayerNotExist] = "无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
FMT_CH[ResponseCode.TargetResidenceNotExist] = "目标领地不存在"
FMT_CH[ResponseCode.TargetResidenceNotTopLevel] = "目标领地不是顶层领地，不能添加所有者"
FMT_CH[ResponseCode.AlreadyOwnerOfTarget] = "已经是目标领地的所有者了，无法重复添加"
FMT_CH[ResponseCode.NoUsableResId] = "申请领地的请求太频繁了，请稍后重试"
