插件介绍：
该服务器Mod隶属于“面对面交易”插件。
“交易”插件实现2个主要功能，1个是交易货币，1个是交易物品：
- 交易货币：弱依赖经济插件，需要配置对应的货币类型和货币贴图。也可以自行进行管理，只需要在transactionServerSystem.py中搜索“经济插件”，并把对应的获取货币和更新货币的地方换成自己的接口管理即可
- 交易物品：玩家可以通过选择背包中的物品及数量进行交易

注：
- 该插件目前与聊天插件进行了联动，当开发者同时部署了聊天插件和交易插件时，可直接点击聊天插件中其他玩家名字弹出发起交易的入口
- 货币显示规则：最高显示5位，超过99999例如123456会显示123k，超过999999例如12345678会显示12m。超过10位可能因为显示框限制而超出显示框（应该也没有那么大数量的货币了吧）

插件构成：
目前“交易”插件包含以下Mod：
- neteaseTransaction：部署于大厅服或游戏服

数据库：
- mysql

使用步骤：
（1）请在mysql中执行mod.sql（位于developer_mods/neteaseTransactionDev中）
（2）在部署配置中，将neteaseTransaction添加至需要的大厅服或者游戏服的mods列表中

插件api：
（1）A玩家向B玩家发起交易申请
函数：RequestTransaction(fromPlayerId, toPlayerId)
参数：
    fromPlayerId: 发起交易玩家的id
    toPlayerId: 收到交易请求的玩家id
示例：
    import server.extraServerApi as serverApi
    transactionServerSystem = serverApi.GetSystem("NeteaseTransaction", "NeteaseTransactionServerSystem")
    transactionServerSystem.RequestTransaction(fromPlayerId, toPlayerId)
（2）查询玩家今日剩余交易次数
函数：QueryPlayerRemainTransactionTimes(uid)
参数：
    uid: 玩家的uid
返回：
    int：玩家剩余交易次数，如果为负数表示不限制交易次数，如果为None表示该玩家不在线
示例：
    import server.extraServerApi as serverApi
    transactionServerSystem = serverApi.GetSystem("NeteaseTransaction", "NeteaseTransactionServerSystem")
    transactionServerSystem.QueryPlayerRemainTransactionTimes(uid)

更新列表：
1.0.0版本：
初始版本

1.0.1版本：
按照新的插件标准实现了界面，解决了以下问题：
（1）多个插件之间界面穿插、按钮点击响应问题
（2）多个插件之间资源文件重名问题

1.0.2版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
