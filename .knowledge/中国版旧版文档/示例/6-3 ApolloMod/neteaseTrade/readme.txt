插件介绍：
该服务器Mod隶属于“经济”插件。
“经济”插件实现3个功能，1个是定义货币，1个是定义商店，1个是摆摊：
- 定义货币：定义并在游戏中生效交易货币（配置于Service下的mod.json）****货币的贴图资源必须为正方形，例如现在预设的金币贴图为40x40
- 定义商店：定义并在游戏中生效可用交易货币购买商品的商店（配置于Service下的mod.json）
- 摆摊（2.0.0新增）：玩家可以在游戏中设置自己的摊位，上架自己背包中的道具出售，其他玩家可以通过摊位购买上架的商品（一些摆摊限制配置于Service下的mod.json）
- 摆摊附加说明：插件实现了简易的自定义摊位方块，该方块限制了不得放置其他方块于其顶部与底部，玩家可与该方块交互打开摊位相关操作界面，插件同时提供了打开摊位界面的api，可结合api自行实现摊位于游戏中存在的形式

插件构成：
目前“经济”插件包含以下Mod：
- neteaseTrade：部署于大厅服或游戏服
- neteaseTradeMaster：部署于控制服
- neteaseTradeService：部署于功能服

数据库：
- mysql

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseTradeService中）
（2）在部署配置中，将neteaseTrade添加至需要的大厅服或者游戏服的mods列表中
（3）在部署配置中，将neteaseTradeMaster添加至控制服的mods列表中
（4）在部署配置中，将neteaseTradeService添加至某一个功能服的mods列表中。若不是MCStudio添加该mod，则需要手动将字符串"neteaseTrade"添加到deploy.json中service下的module_names属性中

插件api：
（1）使一个玩家打开某种商店的界面
函数：OpenGrocery(uid, groceryId)
参数：
    uid: 玩家的uid
    groceryId: mod.json中配置的商店唯一字符串ID
示例：
    import server.extraServerApi as serverApi
    tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
    tradeSystem.OpenGrocery(uid, 'DRUGS')
（2）为一个玩家添加/减少货币（参数：玩家id、货币类型、货币数量，货币数量可为负数）
函数：UpdatePlayerDoughs(uid, mod)
参数：
    uid: 玩家的uid
    mod: 修改货币数据的字典
示例：
    mod = {
        'RMB': 996,  # 货币类型 RMB 增加996（不超过上限值）
        'USD': -996  # 货币类型 USD 减少996（持有值可以小于0）
    }
    import server.extraServerApi as serverApi
    tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
    tradeSystem.UpdatePlayerDoughs(uid, mod)
（3）打开摊位界面（2.0.0新增）
函数：DisplayStall(uid, owner)
参数：
    uid: 玩家的uid
    owner: 摊主玩家的uid，若uid与owner相等，则打开摊位管理界面（无需正在摆摊），反之则打开owner对应玩家摊位的购买界面
示例：
    import server.extraServerApi as serverApi
    tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
    # tradeSystem.DisplayStall(666, 666)  # 使uid为666的玩家打开摊位管理界面
    tradeSystem.DisplayStall(666, 777)  # 使uid为666的玩家打开uid为777的玩家摊位的购买界面
（4）关闭一个玩家正在开张的摊位（2.0.0新增）
函数：CloseStall(uid, cb)
参数：
    uid: 要关闭摊位的摊主玩家的uid
    cb: 返回后调用的cb函数
示例：
    import server.extraServerApi as serverApi
    tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
    tradeSystem.CloseStall(uid, self.do_something)

    ...

    def do_something(self, success, data):
        if not success:
            print('请求超时')
            print('返回数据为 data: {}'.format(data))
        else:
            if data['code'] == 1:
                print('操作成功')
            else:
                print('操作失败')
                print('失败信息为 message: {}'.format(data['message']))
（5）查询一个玩家身上的货币剩余数量（2.0.4新增，该玩家需在线）
函数：QueryPlayerDoughs(uid, cb)
参数：
    uid: 玩家的uid
    cb: 返回后调用的cb函数
示例：
    import server.extraServerApi as serverApi
    tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
    tradeSystem.QueryPlayerDoughs(uid, self.do_something)

    ...

    def do_something(self, success, data):
        if not success:
            print('请求超时')
            print('返回数据为 data: {}'.format(data))
        else:
            if data['code'] == 1:
                print(data)  # 与指令查询返回结构一致
            else:
                print('失败')
                print('失败信息为 message: {}'.format(data['message']))
（6）货币变动事件（2.0.4新增）
事件名：PlayerDoughsUpdateEvent
说明：该事件为“服务端”事件，可于“服务端”监听此事件，有玩家货币发生变动时“服务端”会广播此事件
响应参数：
    uid: 玩家的uid
    k: 货币的唯一id
    dt: 变化量，负数为消耗量，正数为获得量
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseTrade', 'neteaseTradeDev', 'PlayerDoughsUpdateEvent', self, self.OnSomeoneUpdateDoughs)

    def OnSomeoneUpdateDoughs(self, data):
        print 'OnSomeoneUpdateDoughs', data
（7）查询当前总共有多少个出售摊位，返回结构等同指令查询（2.0.6新增）
函数：CountStalls(cb)
参数：
    cb: 返回后调用的cb函数
示例：
    import server.extraServerApi as serverApi
    tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
    def cb(success, data):
        print success, data
    tradeSystem.CountStalls(cb)

支持的运营指令：
运营指令：
（1）查询一个玩家身上的货币剩余数量（该玩家需在线）
post url: http:masterip:masterport/query-player-doughs
post body:{
    "uid": 996  # 玩家的uid
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {  # 返回该玩家身上货币剩余数量信息，查询失败则为空字典
        "RMB": 996,
        "USD": -996
    }
}
（2）为一个玩家添加/减少货币（参数：玩家id、货币类型、货币数量，货币数量可为负数）
post url: http:masterip:masterport/update-player-doughs
post body:{
    "uid": 996,  # 玩家的uid
    "mod": {  # 修改货币数据的字典
        "RMB": 996,
        "USD": -996
    }
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {  # 返回该玩家身上货币剩余数量信息，操作失败则为空字典
        "RMB": 1992,
        "USD": -1992
    }
}
（3）查询当前总共有多少个出售摊位（2.0.0新增）
post url: http:masterip:masterport/count-stalls
post body:{}
response:
{
    "code": 1,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {
        "stalls": {
            "996": {
                "duration": 12,  # 摆摊总时长
                "deadline": 1590462263,  # 摆摊自动收摊时间戳
                "ver": 0,  # 无用
                "label": "好货不便宜",  # 摊位名称
                "deals": [...]  # 该摊位的出售记录
            }
        }
    }
}

更新列表：
1.0.0版本：
初始版本
2.0.0版本：
新增出售摊位功能，支持玩家摆摊上架商品交易
2.0.1版本：
调整UI大小
2.0.2版本：
增加半小时不摆摊自动销毁摆摊方块逻辑
增加摆摊方块名字显示
在配置了提示插件的场合使用提示插件弹出提示
2.0.3版本：
增加对领地插件的支持
2.0.4版本：
增加货币查询接口，货币变动事件
2.0.5版本：
商店界面全新改版，商品支持复数购买（详见游戏内UI）及使用组合货币购买（详见service中的mod.json）
2.0.6版本：
新增查询当前总共有多少个出售摊位接口
2.0.7版本：
修复1.21富文本显示的bug
2.0.8版本：
优化UI资源
2.0.9版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
2.0.10版本：
1、修改可摆摊区域相关的配置方式，以服务器类型为一级的Key，支持基于服务器类型分别配置摆摊区域的限制
