插件介绍：
提供接口弹出通用的提示，经济插件，队伍插件，每日登录奖励插件，活动奖励插件，宝石插件均有使用该插件来进行操作反馈提示

插件构成：
目前“提示”插件包含以下Mod：
- neteaseAlert：部署于大厅服或游戏服

使用步骤：
（1）在部署配置中，将neteaseAlert添加至需要的大厅服或者游戏服的mods列表中

插件api：
（1）服务端向某一个玩家弹出一个提示，内容最多显示五行
函数：Alert(playerId, text, seconds, xratio, yratio, priority)
参数：
    playerId: 玩家的playerId
    text: 需要提示的内容
    seconds: 内容显示停留的秒数，不传则用mod.json的default_show_time设置
    xratio: 提示背景框中心与主屏横轴的位置比，0-1之间的小数，不传则用mod.json的default_xratio设置
    yratio: 提示背景框中心与主屏纵轴的位置比，0-1之间的小数，不传则用mod.json的default_yratio设置
    priority: 消息显示优先级，数值越大优先级越大。优先级大于0时消息按照优先级排序，顺序显示；优先级小于0时，覆盖显示当前消息，并清空之前保存的消息。默认优先级是-1
示例：
    import server.extraServerApi as serverApi
    alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
    alertSystem.Alert(playerId, '§c摊位方块只能放置于规定的摆摊区域。', 2, 0.5, 0.8, 50)  # 提示框中点位于(横屏水平方向大小*0.5, 横屏竖直方向大小*0.8)处
（2）客户端弹出一个提示，内容最多显示五行
函数：Alert(text, seconds, xratio, yratio, priority)
参数：
    text: 需要提示的内容
    seconds: 内容显示停留的秒数，不传则用mod.json的default_show_time设置
    xratio: 提示背景框中心与主屏横轴的位置比，0-1之间的小数，0-1之间的小数，不传则用mod.json的default_xratio设置
    yratio: 提示背景框中心与主屏纵轴的位置比，0-1之间的小数，0-1之间的小数，不传则用mod.json的default_yratio设置
    priority: 消息显示优先级，数值越大优先级越大。优先级大于0时消息按照优先级排序，顺序显示；优先级小于0时，覆盖显示当前消息，并清空之前保存的消息。默认优先级是-1
示例：
    import client.extraClientApi as clientApi
    alertSystem = clientApi.GetSystem("neteaseAlert", "neteaseAlertBeh")
    alertSystem.Alert('§c摊位方块只能放置于规定的摆摊区域。', 2, 0.5, 0.8, 50)  # 提示框中点位于(横屏水平方向大小*0.5, 横屏竖直方向大小*0.8)处

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
1. 多个消息同时到来时，根据优先级判断显示次序
2. 增加提示位置、显示时间的默认配置
3. 增加客户端API
4. 提示界面大小支持自适应，最多不超过5行。
