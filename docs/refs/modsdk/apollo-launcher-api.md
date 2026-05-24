# Apollo启动器信息接口<!-- md:flag china -->
本页汇总Apollo启动器信息相关接口，包括好友、评分、会员、实名状态和维护状态查询能力。
| 接口 | 可用环境 | 说明 |
| --- | --- | --- |
| `ApplyUserFriend` | Lobby/Game接口 | 申请添加为启动器中的好友 |
| `GetPcGameUserLike` | Master/Service/Lobby/Game接口 | 获取玩家是否点赞了当前网络服（仅支持PC玩家） |
| `GetPeGameUserStars` | Master/Service/Lobby/Game接口 | 获取玩家对本游戏的评分 |
| `GetUIDByNickname` | Master/Service/Lobby/Game接口 | 根据玩家昵称获取玩家uid |
| `GetUserAuthInfo` | Master/Service/Lobby/Game接口 | 获取在线玩家实名制、是否绑定信息 |
| `GetUserFriend` | Master/Service/Lobby/Game接口 | 获取启动器中玩家好友信息 |
| `GetUserGuest` | Master/Service/Lobby/Game接口 | 获取启动器中玩家是否游客的信息, 此接口已废弃 |
| `GetUsersVIP` | Master/Service/Lobby/Game接口 | 获取启动器中玩家会员信息 |
| `IsGameUnderMaintenance` | Master/Service/Lobby/Game接口 | 游戏是否在维护中 |
| `ShareApolloGame` | Lobby/Game接口 | 拉起网络游戏分享界面，界面包含游戏图标和描述 |