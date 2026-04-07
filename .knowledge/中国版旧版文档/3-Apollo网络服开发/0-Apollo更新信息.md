# Apollo更新信息

## Apollo相关文档已迁移到新版官网，详见[[新版开发者文档](http://mc.163.com/dev/mcmanual/mc-dev/mcdocs/2-Apollo/0-Apollo%E6%9B%B4%E6%96%B0%E4%BF%A1%E6%81%AF.html)]

## 2021.05.27  1.22更新内容

1. 详见[[新版开发者文档](http://mc.163.com/dev/mcmanual/mc-dev/mcdocs/2-Apollo/0-Apollo%E6%9B%B4%E6%96%B0%E4%BF%A1%E6%81%AF.html)]

## 2021.05.13  1.22更新内容

1. 详见[[新版开发者文档](http://mc.163.com/dev/mcmanual/mc-dev/mcdocs/2-Apollo/0-Apollo%E6%9B%B4%E6%96%B0%E4%BF%A1%E6%81%AF.html)]

## 2021.04.29  1.22更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.22.0.release20210429 |
| proxy   | 1.22.0.release20210429 |
| master  | 1.22.0.release20210429 |
| service | 1.22.0.release20210429 |

2. 新增[GetLastFrameTime](./4-SDK/6-大厅与游戏服API.html#GetLastFrameTime)，获取服务端脚本上一帧运行时间<!--by jishaobin-->
3. 调整[GetEngineActor](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#GetEngineActor)，返回结果中去掉当前已经确定要移除的实体<!--by xltang-->
4. 调整[SetCommand](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetCommand)，当命令执行成功时返回True，否则返回False<!--by xltang-->
5. 调整[SetPlayerAllItems](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetPlayerAllItems)，修正itemDict传入空字典时无法清空盔甲、裤子、鞋子部位装备的问题<!--by xltang-->
6. 调整[ServerChatEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#ServerChatEvent)，新增字段，表示被禁言。另外，禁言后，玩家聊天后告知玩家被禁言了<!--by yfg -->
7. 调整[NotifyToServiceNode](./4-SDK/8-服务器通信.html#NotifyToServiceNode)，发送的事件信息中自动包含玩家uid<!--by yfg -->
8. 新增可import的第三方库：[numpy]<!--by jishaobin -->
9. 新增回合战斗插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseRound目录。<!--by xltang-->
10. 领地插件迭代，新增获取与指定区域有重叠的顶级领地的ID列表的API，具体参见领地插件readme中“1.0.12版本”更新说明<!--by xltang-->
11. 地图属性插件迭代，新增判断指定区域是否在地图边界之内的API，具体参见地图属性插件readme中“1.0.2版本”更新说明<!--by xltang-->
12. 主菜单插件迭代，UI重新整合，提供UI工程，具体参见主菜单插件readme中“1.0.4版本”更新说明。
13. 商城插件迭代，不再需要填写环境、gameId等配置，具体参见商城插件readme中“1.0.2版本”更新说明。<!--by xltang-->
14. Apollo开启基于位移检测的反作弊检查<!--by jishaobin -->

## 2021.04.20  1.22更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.22.0.release20210420 |
| proxy   | 1.22.0.release20210420 |
| master  | 1.22.0.release20210420 |
| service | 1.22.0.release20210420 |

2、apollo引擎适配debian10 系统

## 2021.04.15  1.22更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.22.0.release20210415 |
| proxy   | 1.22.0.release20210415 |
| master  | 1.22.0.release20210415 |
| service | 1.22.0.release20210415 |

2. 新增[HidePlayerFootprint](./4-SDK/6-大厅与游戏服API.html#HidePlayerFootprint)，隐藏某个玩家的会员脚印外观。<!--by yfg -->
3. 新增[HidePlayerMagicCircle](./4-SDK/6-大厅与游戏服API.html#HidePlayerMagicCircle)，隐藏某个玩家的会员法阵外观。<!--by yfg -->
4. 新增[GetUIDByNickname](./4-SDK/启动器信息API.html#GetUIDByNickname)，根据玩家昵称获取玩家uid。<!--by yfg -->
5. 新增[BanUser](./4-SDK/4-控制服API.html#BanUser)，封禁某个玩家。<!--by yfg -->
6. 新增[UnBanUser](./4-SDK/4-控制服API.html#UnBanUser)，解除某个玩家的封禁。<!--by yfg -->
7. 新增[SilentByUID](./4-SDK/4-控制服API.html#SilentByUID)，禁言某个玩家。<!--by yfg -->
8. 新增[UnSilentByUID](./4-SDK/4-控制服API.html#UnSilentByUID)，解除某个玩家的禁言。<!--by yfg -->
9. 权限插件迭代，支持游戏内通过聊天框输入部分运营指令，具体参见权限插件readme中“1.0.2版本”更新说明<!--by yfg -->
10. 部分插件迭代，使用稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题。本次批量修改涉及到的插件有：外观管理插件，累积消费活动插件，公告插件，战斗系统插件，宝石插件，称号插件，聊天插件，副本管理插件，飞行插件，玩家意见反馈插件，好友插件，排行榜插件，领地插件，队伍插件，经济插件，面对面交易插件。<!--by xltang -->
11. 商城插件迭代，提高了订单发货速度，具体参见商城插件readme中“1.0.1版本”更新说明。<!--by xltang -->
12. PVP插件UI重新整合，具体参见PVP插件readme中“1.0.3版本”更新说明。<!--by jishaobin -->

## 2021.04.07  1.22更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.22.0.release20210408 |
| proxy   | 1.22.0.release20210408 |
| master  | 1.22.0.release20210408 |
| service | 1.22.0.release20210408 |

## 2021.04.01  1.21更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.21.0.release20210401 |
| proxy   | 1.21.0.release20210401 |
| master  | 1.21.0.release20210401 |
| service | 1.21.0.release20210401 |

2. 新增[GetApolloReviewStage](./4-SDK/7-公共API.html#GetApolloReviewStage)，获取游戏当前审核阶段。<!--by yfg -->
3. 新增[GetServerType](./4-SDK/5-功能服API.html#GetServerType)，获取服务器类型。<!--by yfg -->
4. 新增[GetServerIdsByServerType](./4-SDK/5-功能服API.html#GetServerIdsByServerType)，根据类型获取服务器id列表。<!--by yfg -->
5. 新增[GetOnlineNumByServerType](./4-SDK/4-控制服API.html#GetOnlineNumByServerType)，获取某类型服务器的在线人数。<!--by yfg -->
6. 新增[ApplyUserFriend](./4-SDK/启动器信息API.html#ApplyUserFriend)，申请添加为启动器中的好友。<!--by yfg -->
7. 新增[ShareApolloGame](./4-SDK/启动器信息API.html#ShareApolloGame)，在RN上拉起“网络游戏分享”的界面，界面包含游戏ICON以及描述。<!--by yfg -->
8. 新增[GetUserGuest](./4-SDK/启动器信息API.html#GetUserGuest)，获取启动器中玩家是否游客的信息。<!--by jishaobin -->
9. 新增[GetPeGameUserStars](./4-SDK/启动器信息API.html#GetPeGameUserStars)，获取玩家对本游戏的评分。<!--by jishaobin -->
10. 新增redis集群接口。
11. 新增随机传送插件。

## 2021.03.18  1.21更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.21.0.release20210318 |
| proxy   | 1.21.0.release20210318 |
| master  | 1.21.0.release20210318 |
| service | 1.21.0.release20210318 |

2. 新增[GetUserFriend](./4-SDK/启动器信息API.html#GetUserFriend)，获取启动器中玩家好友信息。<!--by yfg-->
3. 新增[GetUsersVIP](./4-SDK/启动器信息API.html#GetUsersVIP)，获取启动器中玩家会员信息。<!--by yfg-->
4. 升级公告插件，具体参见公告插件readme中“1.0.11版本”更新说明。
5. “Grafana服务器检测参数”文档中增加付费情况接入说明
6. 称号插件UI重新整合，具体参见称号插件readme中“1.0.3版本”更新说明
7. 外观管理插件UI重新整合，具体参见外观管理插件readme中“1.0.1版本”更新说明
8. 面对面交易插件UI重新整合，具体参见面对面交易插件readme中“1.0.1版本”更新说明

## 2021.03.04  1.21更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.21.0.release20210304 |
| proxy   | 1.21.0.release20210304 |
| master  | 1.21.0.release20210304 |
| service | 1.21.0.release20210304 |
2. 战斗插件UI重新整合，具体参见战斗插件readme中“1.0.11版本”更新说明
3. 经济插件UI重新整合，具体参见经济插件readme中“1.0.8版本”更新说明
4. 队伍插件UI重新整合，添加与聊天插件的互动功能，具体参见队伍插件readme中“1.0.6版本”更新说明
5. 公告插件UI重新整合，具体参见公告插件readme中“1.0.10版本”更新说明

## 2021.01.28  1.21更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.21.0.release20210128 |
| proxy   | 1.21.0.release20210128 |
| master  | 1.21.0.release20210128 |
| service | 1.21.0.release20210128 |
2. 新增[GetModJsonConfigByName](./4-SDK/7-公共API.html#GetModJsonConfigByName)，根据脚本根目录读取mod.json配置文件。<!--by xltang-->
3. 新增[NotifyToServiceNode](./4-SDK/8-服务器通信.html#NotifyToServiceNode)，客户端给service服务器发送事件。<!--by yfg-->
4. deploy.json中common层级下新增配置项`global_player_online_limit`，设置游戏的最大人数。该配置用于控制整个网络游戏的最大人数，避免在线人数过多超出承载能力，导致服务器响应变慢
5. 修复生存服地图膨胀问题
6. 领地插件Trace问题修复，具体参见领地插件readme中“1.0.10版本”更新说明
7. 好友插件补充代码注释并修复多个资源问题，具体参见好友插件readme中“1.0.7版本”更新说明
8. 宝石插件补充代码注释并修复多个资源问题，具体参见宝石插件readme中“1.0.5版本”更新说明

## 2021.01.21  1.21更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.21.0.release20210121 |
| proxy   | 1.21.0.release20210121 |
| master  | 1.21.0.release20210121 |
| service | 1.21.0.release20210121 |

## 2021.01.14  1.20更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.20.0.release20210114 |
| proxy   | 1.20.0.release20210114 |
| master  | 1.20.0.release20210114 |
| service | 1.20.0.release20210114 |
2. 公告插件新增收邮件回调，具体参见公告插件readme中“1.0.9版本”更新说明。
3. 好友插件新增同意、拒绝好友的回调，具体参见好友插件readme中“1.0.4版本”更新说明。
4. 新增问题反馈插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseFeedback目录。
5. 优化了任务、队伍、称号、排行榜、活动奖励、喇叭等插件的美术资源和注释

## 2020.12.31  1.20更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.20.0.release20201231 |
| proxy   | 1.20.0.release20201231 |
| master  | 1.20.0.release20201231 |
| service | 1.20.0.release20201231 |

2. 领地插件修复领地ID冲突问题，修复跨服传送问题，具体参见领地插件readme中“1.0.9版本”更新说明。
3. 新增累计消费活动插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseAddup、neteaseAddupMaster目录。
4. [AddServerPlayerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#AddServerPlayerEvent)新增proxyId参数
5. 新增[RemoteNotifyToClient](./4-SDK/8-服务器通信.html#RemoteNotifyToClient)，service发送事件到指定客户端。<!--by yfg-->
6. 新增[SyncInsert](./4-SDK/7-公共API.html#SyncInsert)，阻塞性执行sql语句，插入数据<!--by gmy-->

## 2020.12.17  1.20更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.20.0.release20201217 |
| proxy   | 1.20.0.release20201217 |
| master  | 1.20.0.release20201217 |
| service | 1.20.0.release20201217 |
2. 新增API注册玩家收到邮件的回调函数（客户端）、某UID玩家是否有未读邮件（服务端），具体参见公告插件readme中“1.0.8版本”更新说明。
3. 新增报名匹配插件, 从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseMatch、neteaseMatchMaster、neteaseMatchService目录。
4. 新增[IsServiceConnected](./4-SDK/6-大厅与游戏服API.html#IsServiceConnected)，检查服务器是否与某个service建立连接。<!--by yfg-->
5. 新增[BroadcastToServerByType](./4-SDK/8-服务器通信.html#BroadcastToServerByType)，service给某种类型服务器广播消息<!--by yfg-->
6. 调整[ServiceConnectEvent](./4-SDK/1-大厅与游戏服事件.html#ServiceConnectEvent)，与service建立连接事件，带一个功能服类型参数<!--by yfg-->
7. 领地插件新增关闭领地特效光圈的接口，新增修改创建领地与添加新玩家为指定领地所有者的接口，支持玩家不在线时也可以创建领地，具体参见领地插件readme中“1.0.8版本”更新说明。
8. 调整了宝石插件的界面命名，具体参见宝石插件readme中“1.0.4版本”更新说明。
9. 新增外观管理插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseAppear目录。
## 2020.12.03  1.20更新内容
1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.20.0.release20201203 |
| proxy   | 1.20.0.release20201203 |
| master  | 1.20.0.release20201203 |
| service | 1.20.0.release20201203 |
2. 去除了lobby引擎，以后大厅服、游戏服统一使用game的引擎。
3. 经济插件新增查询摊位API，具体参见经济插件readme中“2.0.6版本”更新说明。
4. 聊天插件新增关闭聊天大窗口是响应事件，具体参见聊天插件readme中“1.0.1版本”更新说明。
5. 新增面对面交易插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseTransaction目录。
6. 新增[IsInApollo](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.md#IsInApollo)，返回当前游戏Mod是否运行在Apollo网络服，当前版本仅Apollo网络服可用。<!--by xltang-->
## 2020.11.23  1.20更新内容
1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.20.0.release20201123 |
| lobby   | 1.20.0.release20201123 |
| proxy   | 1.20.0.release20201123 |
| master  | 1.20.0.release20201123 |
| service | 1.20.0.release20201123 |
## 2020.11.19  1.19更新内容
1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.19.0.release20201119 |
| lobby   | 1.19.0.release20201119 |
| proxy   | 1.19.0.release20201119 |
| master  | 1.19.0.release20201119 |
| service | 1.19.0.release20201119 |
2. 升级了战斗插件，具体参见战斗信息插件readme中“1.0.10版本”更新说明。
3. 对公会、弹幕、领地、pvp插件美术资源进行了优化和代码进行了注释。

## 2020.11.05  1.19更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.19.0.release20201105 |
| lobby   | 1.19.0.release20201105 |
| proxy   | 1.19.0.release20201105 |
| master  | 1.19.0.release20201105 |
| service | 1.19.0.release20201105 |
2. 新增[SetPlayerRespawnPos](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetPlayerRespawnPos)，设置玩家复活的位置，当前玩家的复活点仅支持主世界，当前版本仅Apollo网络服可用<!--by xltang-->
3. 新增云端信息插件在多个服务器中的使用功能，具体参见云端信息插件readme中“1.0.5版本”更新说明。
4. 升级了npc插件，具体参见npc信息插件readme中“1.0.4版本”更新说明。
5. 升级了副本插件，具体参见副本信息插件readme中“1.0.1版本”更新说明。
6. 升级了经济插件，具体参见经济插件readme中“2.0.5版本”更新说明。


## 2020.10.22  1.19更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.19.0.release20201022 |
| lobby   | 1.19.0.release20201022 |
| proxy   | 1.19.0.release20201022 |
| master  | 1.19.0.release20201022 |
| service | 1.19.0.release20201022

2. 新增[GetBedColor](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetBedColor)，获取床（方块）的颜色，仅Apollo网络服可用<!--by xltang-->
3. 新增[GetSignBlockText](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetSignBlockText)，获取告示牌（方块）的文本内容，仅Apollo网络服可用<!--by xltang-->
4. 新增[SetBedColor](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetBedColor)，设置床（方块）的颜色，仅Apollo网络服可用<!--by xltang-->
5. 新增[SetSignBlockText](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetSignBlockText)，设置告示牌（方块）的文本内容，仅Apollo网络服可用<!--by xltang-->
6. 新增[ChangeEntityDimension](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ChangeEntityDimension)，传送实体，仅Apollo网络服可用<!--by xltang-->
7. 新增[ShutdownServer](./4-SDK/6-大厅与游戏服API.html#ShutdownServer)，强制关机<!--by yfg-->
8. 新增聊天插件, 从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseChat、neteaseChatService目录。
9. 好友插件升级，具体参见好友插件readme中“1.0.3版本”更新说明。
10. 领地插件升级，具体参见领地插件readme中“1.0.5版本”更新说明。
11. 公告插件、战斗系统插件、每日登录奖励插件、主菜单插件进行了界面优化，公告插件、战斗系统插件、每日登录奖励插件、主菜单插件、好友插件增加了注释。

## 2020.9.29  1.19更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.19.0.release20200929 |
| lobby   | 1.19.0.release20200929 |
| proxy   | 1.19.0.release20200929 |
| master  | 1.19.0.release20200929 |
| service | 1.19.0.release20200929 |

2. 战斗插件升级，具体参见战斗插件readme中“1.0.7版本”更新说明
3. 宝石插件升级，具体参见宝石插件readme中“1.0.1版本”更新说明
4. 新增物品面板插件, 从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载。
5. 优化[ChangePerformanceSwitch](./4-SDK/6-大厅与游戏服API.html#ChangePerformanceSwitch)，用于提升服务器性能<!--by yfg-->
6. 新增[EntityChangeDimensionServerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#EntityChangeDimensionServerEvent)，实体维度改变时服务端触发<!--by txl-->

## 2020.9.17  1.19更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.19.0.release20200917 |
| lobby   | 1.19.0.release20200917 |
| proxy   | 1.19.0.release20200917 |
| master  | 1.19.0.release20200917 |
| service | 1.19.0.release20200917 |

2. 弹幕插件升级，新增少量UI交互，具体参见弹幕插件readme中“1.0.1版本”更新说明
3. 好友插件升级，具体参见好友插件readme中“1.0.3版本”更新说明
4. 经济插件升级，具体参见经济插件readme中“2.0.4版本”更新说明
5. 领地插件升级，新增领地转让接口，具体参见领地插件readme中“1.0.4版本”更新说明
6. 云端玩家信息插件升级，具体参见云端玩家信息插件readme中“1.0.4版本”更新说明
7. 新增飞行插件, 从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载。
8. 新增[PlayerLeftMessageServerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#PlayerLeftMessageServerEvent)，玩家即将离开时准备显示“xxx离开游戏”时触发事件<!--by gmy-->
9. 新增[ChangePlayerFlyState](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ChangePlayerFlyState)，改变玩家的飞行状态<!--by ld-->
10. 新增[IsPlayerFlying](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#IsPlayerFlying)，获取玩家是否在飞行<!--by ld-->
11. 新增[SetLoginStratege](./4-SDK/4-控制服API.html#SetLoginStratege)，支持设置玩家选服策略<!--by yfg-->

## 2020.9.3  1.18更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.18.0.release20200903|
| lobby   | 1.18.0.release20200903|
| proxy   | 1.18.0.release20200903 |
| master  | 1.18.0.release20200903 |
| service | 1.18.0.release20200903 |
2. [AsyncExecuteFunctionWithOrderKey](./4-SDK/7-公共API.html#AsyncExecuteFunctionWithOrderKey)支持mysql事务<!--by yfg-->
3. 领地插件升级，新建、修改领地时可以移动，旋转视角，具体参见领地插件readme中“1.0.3版本”更新说明
4. 权限插件升级，新增改变玩家op权限接口，具体参见权限插件readme中“1.0.1版本”更新说明

## 2020.8.20  1.18更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.18.0.release20200820|
| lobby   | 1.18.0.release20200820|
| proxy   | 1.18.0.release20200820 |
| master  | 1.18.0.release20200820 |
| service | 1.18.0.release20200820 |

2. 新增[ChangeDatabaseSlowLogLimit](./4-SDK/7-公共API.html#ChangeDatabaseSlowLogLimit)，修改数据库连接池慢请求报警日志限定时间<!--by xltang-->
3. 新增[CloseAsyncTaskSlowCheck](./4-SDK/7-公共API.html#CloseAsyncTaskSlowCheck)，停止每帧检查异步线程池中的任务<!--by xltang-->
4. 新增[DumpAsyncTaskPool](./4-SDK/7-公共API.html#DumpAsyncTaskPool)，打印当前异步线程池中的正在排队和执行中的任务信息<!--by xltang-->
5. 新增[OpenAsyncTaskSlowCheck](./4-SDK/7-公共API.html#OpenAsyncTaskSlowCheck)，启动每帧检查异步线程池中的任务，并且打印执行时间超过指定时间且尚未完成的任务<!--by xltang-->
6. 新增[StartDatabaseProfile](./4-SDK/7-公共API.html#StartDatabaseProfile)，开始记录数据库连接池请求信息统计<!--by xltang-->
7. 新增[StopDatabaseMysqlProfile](./4-SDK/7-公共API.html#StopDatabaseMysqlProfile)，停止记录数据库连接池请求信息并输出统计结果<!--by xltang-->
8. 新增弹幕插件, 从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseDanmu目录。
9. 调整了客户端无法登陆时的提示。
10. 修复了一些的bug。

## 2020.8.13  1.18更新内容

1. 领地插件升级，新增可视化操作UI，具体参见领地插件readme中“1.0.2版本”更新说明。

## 2020.8.6  1.18更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.18.0.release20200806|
| lobby   | 1.18.0.release20200806|
| proxy   | 1.18.0.release20200806 |
| master  | 1.18.0.release20200806 |
| service | 1.18.0.release20200806 |

2. 新增[StartRecordEvent](./4-SDK/5-功能服API.html#StartRecordEvent)，开始启动大厅服/游戏服与功能服之间的脚本事件收发包统计<!--by xltang-->
3. 新增[StopRecordEvent](./4-SDK/5-功能服API.html#StopRecordEvent)，停止大厅服/游戏服与功能服之间的脚本事件收发包统计并输出结果<!--by xltang-->
4. 新增[StartYappiProfile](./4-SDK/7-公共API.html#StartYappiProfile)，开始启动服务端脚本性能分析<!--by xltang-->
5. 新增[StopYappiProfile](./4-SDK/7-公共API.html#StopYappiProfile)，停止服务端脚本性能分析并生成火焰图<!--by xltang-->
6. 新增[StartRecordEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StartRecordEvent)，开始启动服务端与客户端之间的脚本事件收发包统计，当前仅Apollo网络服可用<!--by xltang-->
7. 新增[StopRecordEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StopRecordEvent)
，停止服务端与客户端之间的脚本事件收发包统计并输出结果，当前仅Apollo网络服可用<!--by xltang-->
8. 新增[StartRecordPacket](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StartRecordPacket)，开始启动服务端与客户端之间的引擎收发包统计，当前仅Apollo网络服可用<!--by xltang-->
9. 新增[StopRecordPacket](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StopRecordPacket)，停止服务端与客户端之间的引擎收发包统计并输出结果，当前仅Apollo网络服可用<!--by xltang-->
10. 新增[WillAddEffectServerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#WillAddEffectServerEvent)，实体即将获得状态效果<!--by xltang-->
11. 新增[SetEntityItem](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetEntityItem)，支持设置生物身上的物品，当前仅Apollo网络服可用<!--by lidi-->
12. 新增[GetEntityItem](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetEntityItem)，支持获取生物身上的物品，当前仅Apollo网络服可用<!--by lidi-->
13. 调整[GetEquItemDurability](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetEquItemDurability)，新增支持获取生物装备槽位中盔甲的耐久值，当前仅Apollo网络服可用<!--by lidi-->
14. 任务插件优化升级，支持关卡编辑器中任务组件的更多物品。
15. 新增PVP插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteasePeace目录。

## 2020.7.23  1.18更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.18.0.release20200723|
| lobby   | 1.18.0.release20200723|
| proxy   | 1.18.0.release20200723 |
| master  | 1.18.0.release20200723 |
| service | 1.18.0.release20200723 |

2. 新增[ChangeLevelUpCostServerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#ChangeLevelUpCostServerEvent)，获取玩家下一个等级升级经验事件，用于重载玩家的升级经验，每个等级在重置之前都只会触发一次，当前版本仅Apollo网络服可用<!--by xltang-->
3. 新增[HopperTryPullInServerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#HopperTryPullInServerEvent)，漏斗放在容器下方，尝试和容器交互物品时触发<!--by guanmingyu-->
4. 新增[HopperTryPullOutServerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#HopperTryPullOutServerEvent)，漏斗放在容器旁边，尝试往容器加物品时触发<!--by guanmingyu-->
5. 新增[CreateExperienceOrb](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#CreateExperienceOrb)，创建专属经验球<!--by guanmingyu-->
6. 新增[SetOrbExperience](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetOrbExperience)，修改经验球经验<!--by guanmingyu-->
7. 新增[UpgradeMapDimensionVersion](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#UpgradeMapDimensionVersion)，提升指定地图维度的版本号，版本号不符的维度，地图存档信息将被废弃，当前版本仅Apollo网络服可用<!--by xltang-->
8. 新增[GetDroppedItem](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetDroppedItem)，新增获取掉落在世界的指定entityid的物品信息<!--by why117-->
9. 新增[GetPlayerAllItems](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetPlayerAllItems)，获取制定槽位的批量物品信息，当前版本仅Apollo网络服可用<!--by why117-->
10. 新增[SetPlayerAllItems](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetPlayerAllItems)，设置玩家制定槽位物品信息，当前版本仅Apollo网络服可用<!--by xltang-->
11. 新增[ClearDefinedLevelUpCost](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ClearDefinedLevelUpCost)，清理自定义的升级经验，清理后才有会再次回调ChangeLevelUpCostServerEvent事件并再次设置新的升级经验值。当前版本仅Apollo网络服可用<!--by xltang-->
12. 调整[OnCarriedNewItemChangedServerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#OnCarriedNewItemChangedServerEvent)，新增关键字oldItemDict、newItemDict，当前版本仅Apollo网络服可用<!--by xltang-->
13. 调整[OnNewArmorExchangeServerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#OnNewArmorExchangeServerEvent)，新增关键字oldArmorDict、newArmorDict，当前版本仅Apollo网络服可用<!--by xltang-->
14. 调整[OnOffhandItemChangedServerEvent](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#OnOffhandItemChangedServerEvent)，新增关键字oldItemDict、newItemDict，当前版本仅Apollo网络服可用<!--by xltang-->
15. 调整[SetHurtByEntity](../2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetHurtByEntity)，新增参数knocked，可设置是否产生击退<!--by xltang-->
16. 新增称号插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseLabel、neteaseLabelMaster目录。
17. 新增排行榜插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseRank、neteaseRankMaster、neteaseRankService目录。
18. 箱子插件优化升级，具体参见箱子插件readme中“1.05版本”更新说明。
19. 战斗系统插件优化升级，具体参见战斗系统插件readme中“1.0.5版本”更新说明。

## 2020.7.17  1.18更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.18.0.release20200717|
| lobby   | 1.18.0.release20200717|
| proxy   | 1.18.0.release20200717 |
| master  | 1.18.0.release20200717 |
| service | 1.18.0.release20200717 |

2. 修正引擎自定义模块【http】与python常用库模块【http】重名导致的import错误问题

## 2020.7.9  1.18更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.18.0.release20200709|
| lobby   | 1.18.0.release20200709|
| proxy   | 1.18.0.release20200709 |
| master  | 1.18.0.release20200709 |
| service | 1.18.0.release20200709 |

2. 1.18引擎的首个release版本

## 2020.7.9  1.17更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.17.0.release20200709|
| lobby   | 1.17.0.release20200709|
| proxy   | 1.17.0.release20200709 |
| master  | 1.17.0.release20200709 |
| service | 1.17.0.release20200709 |

2. 控制服，功能服新增接口【commonNetgameApi.AddTimer】、【commonNetgameApi.AddRepeatedTimer】、【commonNetgameApi.CancelTimer】，支持触发定时器
3. 新增喇叭插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseShout、neteaseShoutMaster、neteaseShoutService目录。
4. 公会插件新增接口，具体参见公会插件readme中“1.0.2版本”更新说明。
5. 好友插件新增接口，具体参见好友插件readme中“1.0.1版本”更新说明。
6. 战斗系统插件新增接口，具体参见战斗系统插件readme中“1.0.4版本”更新说明。
7. 经济插件优化升级，具体参见经济插件readme中“2.0.2版本”更新说明。
8. 新增宝石插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseJewel目录。
9. 已发布插件界面适配优化，包括：活动奖励插件、每日登录奖励插件、经济插件界面优化、 队伍插件
10. 大厅服、游戏服新增接口【lobbyGame.netgameApi.GetUidIsSilent】，根据玩家uid获取该玩家是否被禁言
11. 新增弹窗提示插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseAlert目录。

## 2020.6.24  1.17更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.17.0.release20200624 |
| lobby   | 1.17.0.release20200624 |
| proxy   | 1.17.0.release20200624 |
| master  | 1.17.0.release20200624 |
| service | 1.17.0.release20200624 |

2. 已发布插件界面适配优化，包括：公告插件、战斗系统插件、任务插件、公会插件、私有箱子插件、NPC插件
3. 新增服务端事件【ChangeSwimStateServerEvent】，实体开始或者结束游泳时触发
4. 新增服务端接口【IsSwiming】，获取玩家是否处于游泳状态。
5. 新增服务端接口【SetCanBlockSetOnFireByLightning】，禁止/允许闪电点燃方块
6. 新增服务端接口【SetCanActorSetOnFireByLightning】，禁止/允许闪电点燃实体
7. 公告插件支持登录弹窗一次登录只显示1次
8. 新增维度地图修改插件，可以根据针对地图编辑器导出的地图文件替换游戏地图
9. 领地插件大规模升级，具体参见领地插件readme中“1.0.1版本”更新说明。

## 2020.6.11  1.17更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.17.0.release20200611 |
| lobby   | 1.17.0.release20200611 |
| proxy   | 1.17.0.release20200611 |
| master  | 1.17.0.release20200611 |
| service | 1.17.0.release20200611 |

2. 数据统计相关功能和文档完善。运营数据统计插件的readme.txt中，仔细说明支持的所有运营数据类型；介绍插件和grafana influxDB的关系
3. 新增服务端接口【CleanBlockTileEntityCustomData】，清空指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。 
4. 新增服务端接口【GetBlockTileEntityCustomData】，读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。
5. 新增服务端接口【GetBlockTileEntityWholeCustomData】，读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据字典。
6. 新增服务端接口【SetBlockTileEntityCustomData】，设置指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。
7. 私有箱子插件优化，增加持久存储箱子数据功能，修复上个版本遍历获取箱子数据的弊端
8. 好友插件优化，优化平台好友同步机制
9. 修正AsyncQueryWithOrderKey导致mysql死锁的问题
10. 新增服务端接口【GetChestPairedPosition】，获取与箱子A合并成一个大箱子的箱子B的坐标

## 2020.6.04  1.17更新内容
1. 新增好友插件，支持好友信息管理。
2. 修复了服务端事件【StoreBuySuccServerEvent】不能正常触发的问题。

## 2020.5.28  1.17更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.17.0.release20200528 |
| lobby   | 1.17.0.release20200528 |
| proxy   | 1.17.0.release20200528 |
| master  | 1.17.0.release20200528 |
| service | 1.17.0.release20200528 |

2. 新增服务端事件【StoreBuySuccServerEvent】, 当玩家在游戏内购买成功时触发。 
3. 服务端新增接口【GetWholeExtraData】, 获取完整的实体数据/全局数据字典，数据存放到leveldb。 
4. 服务端新增接口【CleanExtraData】，清理指定key的实体数据/全局数据，数据存放到leveldb。
5. 服务端mysql连接池新增【AsyncExecuteFunctionWithOrderKey】接口
6. 升级了云端信息插件，支持同步玩家的额外数据。
7. 升级了经济插件，支持摆摊功能

## 2020.5.14  1.17更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.17.0.release20200514 |
| lobby   | 1.17.0.release20200514 |
| proxy   | 1.17.0.release20200514 |
| master  | 1.17.0.release20200514 |
| service | 1.17.0.release20200514 |

2. 服务端接口【GetPlayerItem】，支持融合获取和设置装备耐久度，支持获取装备位附魔信息
3. 服务端新增接口【SpawnItemToArmor】，支持设置玩家装备
4. 服务端新增接口【ClearPlayerOffHand】，支持清除玩家左手物品
5. 升级了云端玩家信息插件，支持记录和设置装备附魔，可从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseCloud目录。
6. 升级了战斗系统插件，战斗系统插件新增获取物品属性接口，可从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseBattle目录。

## 2020.4.30  1.17更新内容


1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.17.0.release20200430 |
| lobby   | 1.17.0.release20200430 |
| proxy   | 1.17.0.release20200430 |
| master  | 1.17.0.release20200430 |
| service | 1.17.0.release20200430 |

2. 服务端新增【ChestBlockTryPairWithServerEvent】事件，当两个小箱子准备合成一个大箱子时触发
3. 服务端新增【OpenCityProtect】接口，用于开启城市保护
4. 服务端新增【ForbidLiquidFlow】接口，用于禁止/允许地图中的流体流动
5. 服务端新增【LookupItemByName】接口，用于判定指定identifier的物品是否存在
6. 服务端新增【IsSneaking】接口，用于判定当前玩家是否处于潜行状态
7. 服务端新增【ChangeSelectSlot】接口，用于设置玩家当前选中快捷栏物品的index
8. 队伍插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseSquad目录。
9. 任务插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseQuest目录。
10. 地图属性插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseMapAttrs目录。
11. 私有箱子插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseChest目录。
12. 云端玩家信息插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseCloud目录。

## 2020.4.24  1.17更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.17.0.release20200424 |
| lobby   | 1.17.0.release20200424 |
| proxy   | 1.17.0.release20200424 |
| master  | 1.17.0.release20200424 |
| service | 1.17.0.release20200424 |

2. 1.17引擎的首个release版本

## 2020.4.16  1.16更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.16.0.release20200416 |
| lobby   | 1.16.0.release20200416 |
| proxy   | 1.16.0.release20200416 |
| master  | 1.16.0.release20200416 |
| service | 1.16.0.release20200416 |

2. 运营数据统计插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseStatistics和neteaseStatisticsService目录。

3. 去除Apollo中提供的默认运营统计功能，提供功能更完整的运营数据统计插件。网络服中需添加【运营数据统计插件】才能查看运营统计数据。

## 2020.4.2  1.16更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.16.0.release20200402 |
| lobby   | 1.16.0.release20200402 |
| proxy   | 1.16.0.release20200402 |
| master  | 1.16.0.release20200402 |
| service | 1.16.0.release20200402 |

2. 主菜单插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseMenus目录。
3. 【PistonActionServerEvent】事件新增entityList参数，该参数表示活塞运动影响到产生被移动或被破坏效果的实体的ID列表。当前仅支持网络服使用。
4. 商城插件提供查询是否购买过某个商品的接口。商城插件从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseShop、neteaseShopMaster目录。
5. 修复 SetCommand 接口没有返回值的bug。
6. 修复经济插件商店按钮响应错误。经济插件从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseTrade、neteaseTradeMaster、neteaseTradeService目录。
## 2020.3.19  1.16更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.16.0.release20200319 |
| lobby   | 1.16.0.release20200319 |
| proxy   | 1.16.0.release20200319 |
| master  | 1.16.0.release20200319 |
| service | 1.16.0.release20200319 |

2. 新增领地插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseResidence、neteaseResidenceMaster目录。

3. 新增每日登录奖励插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseDaily、neteaseDailyMaster、neteaseDailyService目录。

4. 新增活动奖励插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseChill、neteaseChillMaster、neteaseChillService目录。

5. 新增经济插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseTrade、neteaseTradeMaster、neteaseTradeService目录。

6. 新增【StepOnBlockServerEvent】事件，生物脚踩压力板、踩红石矿、踩拌线钩事件。当前仅支持网络服使用。

7. 新增【MobGriefingBlockServerEvent】事件，生物与方块交互事件。当前仅支持网络服使用。

8. 新增【PlayerInteractServerEvent】事件，玩家和实体交互事件。当前仅支持网络服使用。

9. 新增【StartRidingServerEvent】事件，骑乘事件。当前仅支持网络服使用。

10. 新增【WillTeleportToServerEvent】事件，实体即将传送事件。当前仅支持网络服使用。

11. 新增【PistonActionServerEvent】事件，活塞影响方块的事件。当前仅支持网络服使用。

12. 【ride】组件新增函数IsEntityRiding、GetEntityRider、StopEntityRiding，可以修改实体的骑乘状态。当前仅支持网络服使用。

13. 【lobbyGame.netgameApi】新增SetForbidFlowField、DelForbidFlowField，可以限制流体流动。

14. 【lobbyGame.netgameApi】新增SetForbidDragonEggTeleportField、DelForbidDragonEggTeleportField，可以限制龙蛋传送。



## 2020.2.20  1.16更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.16.0.release20200220 |
| lobby   | 1.16.0.release20200220 |
| proxy   | 1.16.0.release20200220 |
| master  | 1.16.0.release20200220 |
| service | 1.16.0.release20200220 |

2. 新增组件【bulletAttributes】，可以通过函数GetSourceEntityId获取飞射物的发射者。

3. 【item】组件新增函数ChangePlayerItemTipsAndExtraId，可以修改物品的tips。

4. mysqlPool新增SyncFetchAll函数，阻塞性执行sql语句 查询全部数据 。

5. 新增公会插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载的neteaseGuildMaster. neteaseGuildService. neteaseGuildLobby. neteaseGuildGame目录。

6. 新增战斗系统插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载neteaseBattle目录。

7. 事件【ServerChatEvent】优化，可以指定给某些玩家发聊天消息。

8. CommonNetgameApi新增GetOnlineKey函数，返回redis中存储指定玩家在线状态信息的key。

9. CommonNetgameApi新增GetWeekOnlineKey函数，返回redis中存储指定玩家每周在线时间的key。

 

## 2020.1.15  1.16更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.16.0.release20200116 |
| lobby   | 1.16.0.release20200116 |
| proxy   | 1.16.0.release20200116 |
| master  | 1.16.0.release20200116 |
| service | 1.16.0.release20200116 |

2. 新增CheckChunkState接口：检查chunk是否已经加载

3. 新增CreateDimension接口：创建dimension

4. 外放GetSystem接口：获取已注册的system

5. DelServerPlayerEvent和AddServerPlayerEvent事件新增uid参数

6. Apollo event和api中uid参数统一使用int类型

7. event和gm指令传入参数统一使用驼峰格式，且兼容以前event和gm指令

8. 新增GetPlayerIdByUid接口：根据玩家uid获取玩家ID（也即playerId）

9. 新增SendMsgToPlayer接口：给某个玩家发送聊天消息

10. 新增OnCarriedNewItemChangedServerEvent事件：右手物品物品切换的服务端事件

11. 新增OnOffhandItemChangedServerEvent事件：左手物品切换服务端事件

12. 新增npc插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载的neteaseNpc目录。

 

## 2019.12.26  1.15更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.15.0.release20191226 |
| lobby   | 1.15.0.release20191226 |
| proxy   | 1.15.0.release20191226 |
| master  | 1.15.0.release20191226 |
| service | 1.15.0.release20191226 |

2. 新增CheckNameValid. CheckWordsValid接口：实现服务端敏感词检查功能

3. 运营数据支持用mysql存储

4. 添加PlayerJoinMessageEvent事件：准备显示“xxx加入游戏”的玩家登录提示文字时服务端抛出的事件。

5. 新增CheckChunkState接口：判断指定位置的chunk是否加载完成

6. mysqlpool连接池新增AsyncInsertOneWithOrderKey接口：向主键为AUTO INCREASEl类型的表格中插入一条记录，并且返回新建记录的主键。

7. 丰富DelServerPlayerEvent事件：可以判断玩家登出还是切服。

8. 丰富AddServerPlayerEvent事件：可以判断玩家登录还是切服。

9. Apollo接口规范化，兼容以前的api。

10. 新增GetModScriptRootDir接口：获取mod的当前目录

11. 连接池和线程池优化：

12. 连接池和线程池优化：屏蔽对外的Tick()接口，由引擎负责Tick；InitDB()接口取代Init()接口。优化后还兼容以前的接口。

13. 新增RegisterRpcMethodForMod接口：用于监听lobby/game发过来请求

14. 丰富TransferToOtherServer和TransferToOtherServerById接口：支持转服时带参数。

15. 新增运营指令 /profile：实现初级性能分析功能

16. 新增GetOnlineServerInfoOfPlayer和GetOnlineServerInfoOfMultiPlayers接口：获取玩家在线状态及所在服务器serverid

17. 新增ToPcUid和ToPeUid接口：提供PC uid与PE uid互相转换功能

18. 新增GetServerType接口：获取当前服务器的type

19. 新增GetServerId接口：获取service的服务器id

20. 新增公告插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载的neteaseAnnounce. 

neteaseAnnounceMaster. neteaseAnnounceService目录。

21. 新增权限插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载的neteaseAuth. 

neteaseAuthMaster目录。

22. 新增商场插件，从MC Studio的C++网络服的“网络服Mod”分页中的“公共Mod”处下载的neteaseShop. 

neteaseShopMaster目录。

 

 

## 2019.11.28  1.15更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.15.0.release20191128 |
| lobby   | 1.15.0.release20191128 |
| proxy   | 1.15.0.release20191128 |
| master  | 1.15.0.release20191128 |
| service | 1.15.0.release20191128 |

2. 多版本引擎支持。

3. 在线人数为负bug修复。

4. 皮肤验证功能。

5. 登录事件可以区分登录还是切服；登出事件可以区分登出还是切服。

 

## 2019.10.31  1.15更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.15.0.release20191031 |
| lobby   | 1.15.0.release20191031 |
| proxy   | 1.15.0.release20191031 |
| master  | 1.15.0.release20191031 |
| service | 1.15.0.release20191031 |

2. master和service间实现rpc通信。

3. 后台数据统计使用新数据库池。

4. 邮件Mod service端功能

5. 公共配置压缩优化

6. game/lobby 打印错误时出现trace问题修复

 

## 2019.9.27  1.15更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.15.0.release20190927 |
| lobby   | 1.15.0.release20190927 |
| proxy   | 1.15.0.release20190927 |
| master  | 1.14.release20190926   |
| service | 1.14.release20190926   |

 

## 2019.9.26  1.14更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion             |
| ------- | ---------------------- |
| game    | 1.14.release20190926   |
| lobby   | 1.14.release20190926   |
| proxy   | 1.14.0.release20190829 |
| master  | 1.14.release20190926   |
| service | 1.14.release20190926   |

2. 扩展mysql. redis. mongo连接池

3. lobby/game 脚本加载server.properties trace问题修复。

 

## 2019.9.12  1.14更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion           |
| ------- | -------------------- |
| game    | 1.14.release20190912 |
| lobby   | 1.14.release20190912 |
| proxy   | 1.14.release20190829 |
| master  | 1.14.release20190912 |
| service | 1.14.release20190829 |

2. 部分错误日志降级为INFO日志。

3. lobby新增功能开关，可以屏蔽红石相关逻辑。

4. lobby新增功能开关，可以屏蔽chunk存档相关逻辑。

5. 支持基础产品运营数据的记录和显示

6. lobby新增功能开关，可以屏蔽“xxx加入游戏”文字提示。

7. 登录切服核心步骤的关键日志完善

8. 玩家当前位置异常导致lobby dump问题修复。

 

 

## 2019.8.2  1.14更新内容

1. 引擎app_verion（deploy.json中需要配置引擎app_verion）分别是：

|         | app_verion           |
| ------- | -------------------- |
| game    | 1.14.release20190802 |
| lobby   | 1.14.release20190802 |
| proxy   | 1.14.release20190718 |
| master  | 1.14.release20190802 |
| service | 1.14.release20190718 |

2. 修复NPC消失问题

3. lobby性能优化

4. 线程池优化

5. 修复master心跳频率bug

6. mod patch优化，且默认关闭mod patch下载功能

7. 开服工具支持ipv6

8. 允许设置developer mods加载顺序。

 