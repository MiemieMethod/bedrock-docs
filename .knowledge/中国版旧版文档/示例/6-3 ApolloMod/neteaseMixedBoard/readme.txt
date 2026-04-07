插件介绍：
该Mod隶属于“通用综合界面”插件
“通用综合界面”是含若干可拓展按钮的通用界面

插件构成：
目前“通用综合界面”插件包含以下Mod:
- neteaseMixedBoard: 部署于大厅服或游戏服

使用步骤：
（1）在部署配置中，将neteaseMixedBoard添加至需要的大厅服或者游戏服的mods列表中

插件api:
（1） 使一个玩家打开通用综合界面
函数：OpenMixedBoard(playerId, args)
参数：
    playerId: 需要打开界面的玩家的entityId
    args: 界面参数，说明如下
        title: 输入界面标题
        text: 文本区域内容，最多支持32行，超过阶段
        button_list: 按钮参数列表，最多支持16个按钮
            icon: 按钮图标，使用原生物品identify进行设置
            label: 按钮文本，最多两行，超过截断
            callback: 按钮回调，参数为playerId和args,playerId为点击按钮玩家的entityId，
                      args为客户端点击按钮时传递的参数，在发送ButtonCallbackEvent中进行设置，为参数中的callback_args，详见MixedBoardSystem.ButtonCallback
        
返回：
    board_id: 打开面板的id,每次打开的id都不一样
示例：
    playerId = '123456'
    def Demo(playerId, args):
        print 'Demo', playerId, args
    args = {
        'title': '标题',
        'text': '文本内容\n第二行',
        'button_list': [
            {
                'icon': 'minecraft:stone',
                'label': '第1个按钮',
                'callback': Demo
            },
            {
                'icon': 'minecraft:grass',
                'label': '§5第2个按钮\n§6下一行',
                'callback': Demo
            }
        ]
    }
    import server.extraServerApi as serverApi
    mixedBoardSystem = serverApi.GetSystem("neteaseMixedBoard", "neteaseMixedBoardDev")
    board_id = mixedBoardSystem.OpenMixedBoard(playerId,args)

（2） 使一个玩家关闭通用输入界面
CloseMixedBoard(playerId, board_id)
参数：
    playerId: 需要关闭界面的玩家的entityId
    board_id: 界面id,由打开界面接口返回，传None则关闭最新的界面
示例：
    import server.extraServerApi as serverApi
    mixedBoardSystem = serverApi.GetSystem("neteaseMixedBoard", "neteaseMixedBoardDev")
    mixedBoardSystem.CloseMixedBoard(playerId)

按钮回调运行原理：
1. 通过 OpenMixedBoard 设置按钮回调，详见OpenInputBoard函数说明
2. 服务端发送 OpenMixedBoardEvent 到客户端
3. 客户端监听 OpenMixedBoardEvent，设置并打开输入界面
4. 客户端监听按钮事件，获取按钮参数(board_id,button_id)，通过 ButtonCallbackEvent 发送到服务端
5. 服务端监听 ButtonCallbackEvent,调用按钮回调函数



更新列表：
1.0.0版本：
初始版本