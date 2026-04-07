插件介绍：
该Mod隶属于“累积消费活动”插件；实现功能：
1、在规定的时间段内，消费钻石达到对应要求，可领取奖励，奖励有多档（此功能需要部署商店插件才能生效）
2、在活动结束之后，玩家再次重新登录时，会自动通过邮件补发达到领取条件但是尚未领取的奖励（此功能需要部署公告插件才能生效）
3、根据mod.json中的配置，活动结束之后，玩家的活动信息会保留一段时间，超过时限之后活动信息会在玩家再次上线时自动清理，并且这种情况下不会发送奖励补偿邮件（此功能需要部署公告插件才能生效）

插件构成：
目前“提示”插件包含以下Mod：
- neteaseAddup：部署于大厅服或游戏服
- neteaseAddupMaster：部署于控制服

数据库：
- mysql

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseAddup中）
（2）在部署配置中，将neteaseAddup添加至需要的大厅服或者游戏服的mods列表中；
（3）在部署配置中，将neteaseAddupMaster添加至控制服的mods列表中；

插件api：
（1）打开活动界面（服务端）
函数：OpenBonusUI(playerId)
参数：
    playerId:str, 需要打开界面的玩家的entityId
返回：
    无
示例：
    import server.extraServerApi as serverApi
    addupSystem = serverApi.GetSystem("neteaseAddup", "neteaseAddupDev")
    addupSystem.OpenBonusUI("1234")
（2）获取某玩家某次活动累计消费（服务端）
函数：GetAddupPayDiamonds(uid, addupKey)
参数：
    uid:int, 玩家的uid
    addupKey:str, 需要查询的活动的关键字
返回：
    int：玩家在目标活动中消费了多少钻石
示例：
    import server.extraServerApi as serverApi
    addupSystem = serverApi.GetSystem("neteaseAddup", "neteaseAddupDev")
    payDiamonds = addupSystem.GetAddupPayDiamonds(2147585444, "christmas2020")
（3）设置活动界面上【跳转】按钮的文字和回调函数（客户端）
函数：RegisterGotoButton(text, cbFunc)
参数：
    text:str, 活动界面上【跳转】按钮的文字，默认为【前往消费】
    cbFunc:function, 点击活动界面上【跳转】按钮时响应的回调函数，此函数没有参数，未设置时默认行为为打开商城界面（类似NotifyClientToOpenShopUi）
返回：
    无
示例：
    import client.extraClientApi as clientApi
    addupSystem = clientApi.GetSystem("neteaseAddup", "neteaseAddupBeh")
    def ClickCallback():
        print "ClickCallback"
    addupSystem.RegisterGotoButton("点击打印日志", ClickCallback)

支持的运营指令：
运营指令：
（1）查询某玩家某次累计消费
post url: http:masterip:masterport/addup/get-pay
post body:{
    "uid": 2147585444,    # int, 需要查询的玩家的uid
    "addupKey": "christmas2020"     # str, 需要查询的消费活动的关键字
}
response:
{
    "suc": true,  # bool, 是否成功
    "message": "",  # str, 失败的情况下，描述了失败原因
    "entity": {     # dict, 失败的情况下，entity为None
        "uid": 2147585444,  # int, 查询的玩家的uid
        "online": true,     # bool，此值为False的时候，说明此时目标uid的玩家不在线，查询出的可能是滞后的
        "payDiamonds": 160,     # int, 当前活动中，此玩家已经累积消费了多少钻石
        "alreadyGetBonusKeys": ["q01", "q02", "q03"]    # list(str), 当前活动中，此玩家已经领取了哪几个奖励条目
    }
}
（2）设置某玩家某个活动的累计消费（需要目标玩家在线）
post url: http:masterip:masterport/addup/set-pay
post body:{
    "uid": 2147585444,    # int, 需要修改累积消费钻石数的玩家的uid
    "addupKey": "christmas2020",     # str, 目标消费活动的关键字，允许缺损，缺损时默认为当前生效的活动
    "payDiamonds": 300     # int, 需要设置的消费钻石数
}
response:
{
    "suc": true,  # bool, 是否成功
    "message": "",  # str, 失败的情况下，描述了失败原因
    "entity": {     # dict, 失败的情况下，entity为None
        "uid": 2147585444,  # int, 玩家的uid
        "payDiamonds": 160,     # int, 设置成功之后，当前活动中，此玩家已经累积消费了多少钻石
        "alreadyGetBonusKeys": ["q01", "q02", "q03"]    # list(str),  设置成功之后，当前活动中，此玩家已经领取了哪几个奖励条目
    }
}
（3）将某玩家当前活动的某阶段的奖励设为已领取/未领取状态（需要目标玩家在线）
post url: http:masterip:masterport/addup/set-bonus-state
post body:{
    "uid": 2147585444,      # int, 需要修改奖励领取状态的玩家的uid
    "addupKey": "christmas2020",     # str, 目标消费活动的关键字，允许缺损，缺损时默认为当前生效的活动
    "bonusKey": "q01",      # str, 需要修改领取状态的奖励关键字
    "alreadyGet": 0,        # int，0代表需要设置为未领取状态，1代表需要设置为已领取状态
}
response:
{
    "suc": true,  # bool, 是否成功
    "message": "",  # str, 失败的情况下，描述了失败原因
    "entity": {     # dict, 失败的情况下，entity为None
        "uid": 2147585444,  # int, 玩家的uid
        "payDiamonds": 160,     # int, 设置成功之后，当前活动中，此玩家已经累积消费了多少钻石
        "alreadyGetBonusKeys": ["q02", "q03"]    # list(str),  设置成功之后，当前活动中，此玩家已经领取了哪几个奖励条目
    }
}

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
