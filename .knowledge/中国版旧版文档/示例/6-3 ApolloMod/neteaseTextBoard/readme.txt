插件介绍：
该Mod隶属于“通用显示界面”插件
“通用显示界面”是通用分行显示文本界面。

插件构成：
目前“通用显示界面”插件包含以下Mod:
- neteaseTextBoard: 部署于大厅服或游戏服

使用步骤：
（1）在部署配置中，将neteaseTextBoard添加至需要的大厅服或者游戏服的mods列表中

插件api:
（1） 使一个玩家打开通用显示界面
OpenTextBoard(playerId)
参数：
    playerId: 需要打开界面的玩家的entityId
示例：
    import server.extraServerApi as serverApi
    textBoardSystem = serverApi.GetSystem("neteaseTextBoard", "neteaseTextBoardDev")
    textBoardSystem.OpenTextBoard(playerId)

（2）使一个玩家关闭通用显示界面
CloseTextBoard(playerId)
参数：
    playerId: 需要关闭界面的玩家的entityId
示例：
    import server.extraServerApi as serverApi
    textBoardSystem = serverApi.GetSystem("neteaseTextBoard", "neteaseTextBoardDev")
    textBoardSystem.CloseTextBoard(playerId)

（3）清空显示内容
ClearTextBoard(playerId)
参数：
    playerId: 需要清空显示内容的玩家的entityId
示例：
    import server.extraServerApi as serverApi
    textBoardSystem = serverApi.GetSystem("neteaseTextBoard", "neteaseTextBoardDev")
    textBoardSystem.ClearTextBoard(playerId)

（4）设置显示内容
SetTextBoard(playerId, content)
参数：
    playerId: 需要设置的玩家的entityId
    content: 显示的内容
示例：
    import server.extraServerApi as serverApi
    textBoardSystem = serverApi.GetSystem("neteaseTextBoard", "neteaseTextBoardDev")
    textBoardSystem.SetTextBoard(playerId, '§1第一行深蓝色\n§2第二行深绿色')

（5）获取显示内容
GetTextBoard(playerId)
参数：
    playerId: 需要获取显示内容的玩家的entityId
返回：
    content: 显示内容
示例：
    import server.extraServerApi as serverApi
    textBoardSystem = serverApi.GetSystem("neteaseTextBoard", "neteaseTextBoardDev")
    content = textBoardSystem.GetTextBoard(playerId)

更新列表：
1.0.0版本：
初始版本