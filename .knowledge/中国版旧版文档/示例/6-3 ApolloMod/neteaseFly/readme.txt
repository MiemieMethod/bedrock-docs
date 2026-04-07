插件介绍：
该服务器Mod隶属于“飞行”插件。
该插件实现了玩家飞行区域的管理。具体包含以下功能：
（1）玩家在飞行区域点击开启飞行按钮可以进入飞行状态
（2）飞行区域的管理功能，包括黑名单或白名单
（3）飞行会消耗饥饿值

插件构成：
目前“飞行插件”包括以下mod：
（1）neteaseFly：部署大厅服或者游戏服

数据库：
-mysql

使用步骤：
（1）请在mysql中执行mod.sql
（2）在部署配置中，将neteaseFly添加至需要的大厅服或者游戏服的mods列表中
（3）在对应的mod.json中完善飞行插件的配置
（4）（可选）在flyPluginUI.json中修改changeFlyStateBtn控件（即开启/关闭飞行按钮）的位置使其放置于需要的位置
（5）部署并启动服务器之后即可使用飞行插件

插件API
（1）开启飞行
函数：OpenFly
参数：
    playerUid：int，玩家uid
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    playerUid = 12345
    neteaseFlyServerSystem.OpenFly(playerUid)
（2）关闭飞行
函数：CloseFly
参数：
    playerUid：int，玩家uid
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    playerUid = 12345
    neteaseFlyServerSystem.CloseFly(playerUid)
（3）获取玩家飞行状态
函数：GetFlyState
参数：
    args：dict，包括的字段有传入玩家ID(selfUid)，目标玩家ID(friendUid)
    callback:回调函数，参数是dict，返回本次操作成功或者失败的信息
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    playerUid = 12345
    neteaseFlyServerSystem.GetFlyState(playerUid)
（4）获取飞行时间间隔与饥饿值的消耗
函数：GetCostAndInterval
参数：
    无
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    neteaseFlyServerSystem.GetCostAndInterval()
（5）设置飞行时间间隔与饥饿值的消耗
函数：SetCostAndInterval
参数：
    cost int,每interval秒消耗cost饥饿度
    interval int,每interval秒消耗cost饥饿度
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    neteaseFlyServerSystem.SetCostAndInterval(2, 3) # 每3秒消耗2点饥饿度
（6）获取饥饿度要求
函数：GetHungerRequest
参数：
    无
示例:
    import server.extraServerApi as serverApi
    neteaseFlySystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    neteaseFlySystem.GetHungerRequest()
（7）设置饥饿度要求
函数：SetHungerRequest
参数：
    hungerLimit int 开启飞行的最低饥饿度要求，低于该值无法开启飞行
    phungerStopFly int 关闭飞行的饥饿度阈值，飞行状态下低于该值会自动关闭飞行
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    neteaseFlyServerSystem.SetHungerRequest(3, 3)

（8）获取飞行区域黑/白名单
函数：GetFlyAreaList
参数：
    无
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    neteaseFlyServerSystem.GetFlyAreaList()

（9）清空飞行区域黑/白名单
函数：ClearFlyAreaList
参数：
    无
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    neteaseFlyServerSystem.ClearFlyAreaList()

（10）获取黑/白名单模式
函数：GetBlackListMode
参数：
    无
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    neteaseFlyServerSystem.GetBlackListMode()

（11）设置黑/白名单模式
函数：SetBlackListMode
参数：
    isBlackListMode bool,True为黑名单模式，反之白名单模式
示例:
    import server.extraServerApi as serverApi
    neteaseFlyServerSystem = serverApi.GetSystem("neteaseFly", "neteaseFlyDev")
    neteaseFlyServerSystem.SetBlackListMode(True)
    
更新列表：

1.0.0版本：
初始版本

1.0.1版本：
修正mod.sql放置位置错误的问题

1.0.2版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题