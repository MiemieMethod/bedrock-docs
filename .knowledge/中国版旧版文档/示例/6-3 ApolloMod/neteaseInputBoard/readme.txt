插件介绍：
该Mod隶属于“通用输入界面”插件
“通用输入界面”是含一个输入框以及两个按钮的通用界面。

插件构成：
目前“通用输入界面”插件包含以下Mod:
- neteaseInputBoard: 部署于大厅服或游戏服

使用步骤：
（1）在部署配置中，将neteaseInputBoard添加至需要的大厅服或者游戏服的mods列表中

插件api:
（1） 使一个玩家打开通用输入界面
函数：OpenInputBoard(playerId, args)
参数：
    playerId: 需要打开界面的玩家的entityId
    args: 界面参数，说明如下
        title: 输入界面标题
        text: 文本区域内容
        input_text: 输入框内容
        button_list: 按钮参数列表，一共有两个按钮
            label: 按钮文本，最多两行，超过截断
            callback: 按钮回调，参数为playerId和args,playerId为点击按钮玩家的entityId，
                      args为客户端点击按钮时传递的参数，在发送ButtonCallbackEvent中进行设置，为参数中的callback_args，详见InputBoardSystem.ButtonCallback，
                      文本内容可通过args['input_text']获取
        
返回：
    board_id: 打开面板的id,每次打开的id都不一样
示例：
    playerId = '123456'
    def Demo(playerId, args):
        print 'Demo', playerId, args
        print '文本内容:',args['input_text']
    args = {
        'title': '标题'，
        'text': '文本内容\n第二行',
        'input_text': '输入框内容',
        'button_list': [
            {
                'label': '第1个按钮',
                'callback': Demo
            },
            {
                'label': '§5第2个按钮\n§6下一行',
                'callback': Demo
            }
        ]
    }
    import server.extraServerApi as serverApi
    inputBoardSystem = serverApi.GetSystem("neteaseInputBoard", "neteaseInputBoardDev")
    board_id = inputBoardSystem.OpenInputBoard(playerId,args)

（2） 使一个玩家关闭通用输入界面
CloseInputBoard(playerId, board_id)
参数：
    playerId: 需要关闭界面的玩家的entityId
    board_id: 界面id,由打开界面接口返回，传None则关闭最新的界面
示例：
    import server.extraServerApi as serverApi
    inputBoardSystem = serverApi.GetSystem("neteaseInputBoard", "neteaseInputBoardDev")
    inputBoardSystem.CloseInputBoard(playerId)

（3）设置输入框内容
SetInputText(playerId, text, board_id)
参数：
    playerId: 需要关闭界面的玩家的entityId
    text: 输入框内容
    board_id: 界面id,由打开界面接口返回，传None则设置最新的界面
示例：
    import server.extraServerApi as serverApi
    inputBoardSystem = serverApi.GetSystem("neteaseInputBoard", "neteaseInputBoardDev")
    inputBoardSystem.SetInputText(playerId, '输入内容')

按钮回调运行原理：
1. 通过OpenInputBoard设置按钮回调，详见OpenInputBoard函数说明
2. 服务端发送 OpenInputBoardEvent 到客户端
3. 客户端监听 OpenInputBoardEvent，设置并打开输入界面
4. 客户端监听按钮事件，获取按钮参数(board_id,button_id,text)，通过 ButtonCallbackEvent 发送到服务端
5. 服务端监听 ButtonCallbackEvent,调用按钮回调函数



更新列表：
1.0.0版本：
初始版本