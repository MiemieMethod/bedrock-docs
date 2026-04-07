插件介绍：
该服务器Mod隶属于“玩家意见反馈”插件。
该插件实现了玩家意见反馈的基本功能，具体包括以下功能：
（1）服主可以自己定义反馈的标签，玩家可以根据标签进行反馈


插件构成：
目前“玩家意见反馈插件”包括以下mod
（1）neteaseFeedback:部署大厅服或者游戏服

数据库:
-mysql

使用步骤：
（1）配置lobby、game中的mod.json，请按照mod.json中"_comment"注释配置对应内容。
（2）请在mysql中执行mod.sql（位于neteaseFeedback中）
（3）在部署配置中，将neteaseFeedback添加至需要的大厅服或者游戏服的mods列表中；
（4）部署并启动服务器后，即可使用玩家反馈意见插件

插件API：
（1）打开反馈界面。
函数：ShowFeedbackMainUI
参数：
    args：dict，包括:1.isShow True 是否显示
示例:
    import client.extraClientApi as clientApi
    neteaseFeedbackClientSystem = clientApi.GetSystem("neteaseFeedback", "neteaseFeedbackBehavior")
    neteaseFeedbackClientSystem.ShowFeedbackMainUI({"isShow":True})

（2）获取反馈的内容。
函数：ServerGetFeedbackByCond
参数：
    args：dict，包括tags list ["标签1","标签2"]；获取反馈标签获取反馈内容，
    cb:func，回调函数
示例:
    import server.extraServerApi as serverApi
    neteaseFeedbackSystem = serverApi.GetSystem("neteaseFeedback", "neteaseFeedbackDev")
    def cb(mes):
        print mes
    neteaseFeedbackSystem.ServerGetFeedbackByCond({"tags":["聊天", "黄色"]}, cb)


更新列表：

1.0.0版本：
初始版本
1.0.1版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.2版本：
1、替换废弃接口