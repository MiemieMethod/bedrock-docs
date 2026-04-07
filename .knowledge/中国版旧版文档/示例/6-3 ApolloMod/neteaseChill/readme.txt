插件介绍：
该服务器Mod隶属于“活动奖励”插件。
“活动奖励”插件实现活动奖励功能：
- 活动奖励：定义并在游戏中生效活动奖励（配置于lobby/game下的mod.json）
- 当未达成活动奖励领取条件时，点击界面展示奖励下方的按钮将向Server发送NavigateToShopEvent事件，服主监听该事件可自定义该按钮点击后的操作
例（打开付费商城界面）：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseChill', 'neteaseChillBeh', 'NavigateToShopEvent', self, self.OnNavigateToShop)

    def OnNavigateToShop(self, data):
        print 'OnNavigateToShop', data
        playerId = data.get("playerId", "-1")
        uid = netgameApi.GetPlayerUid(playerId)
        if not uid:
            print 'can not get uid by playerId: %s' % playerId
            return
        netgameApi.NotifyClientToOpenShopUi(playerId)


插件构成：
目前“活动奖励”插件包含以下Mod：
- neteaseChill：部署于大厅服或游戏服
- neteaseChillMaster：部署于控制服
- neteaseChillService：部署于功能服。若不是MCStudio添加该mod，则需要手动将字符串"neteaseChill"添加到deploy.json中service下的module_names属性中

数据库：
- mysql

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseChillService中）
（2）在部署配置中，将neteaseChill添加至需要的大厅服或者游戏服的mods列表中
（3）在部署配置中，将neteaseChillMaster添加至控制服的mods列表中
（4）在部署配置中，将neteaseChillService添加至某一个功能服的mods列表中

插件api：
（1）使一个玩家打开活动奖励的界面
函数：OpenChillReward(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    chillSystem = serverApi.GetSystem("neteaseChill", "neteaseChillDev")
    chillSystem.OpenChillReward(uid)
（2）使一个玩家达成活动奖励的条件
函数：AchvChillReward(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    chillSystem = serverApi.GetSystem("neteaseChill", "neteaseChillDev")
    chillSystem.AchvChillReward(uid)

支持的运营指令：
运营指令：
（1）查询一个玩家是否拥有领取活动奖励资格
post url: http:masterip:masterport/query-player-chill
post body:{
    "uid": 996  # 玩家的uid
}
response:
{
    "code": 0,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {  # 返回该玩家活动奖励领取情况，查询失败则为空字典
        "qualified": 0,  # 是否具有领取资格，【1】代表拥有领取资格且未领取，【0】代表未拥有领取资格，【-1】代表已领取
        "achv": "1584093924.871",  # 达成活动奖励领取条件的时间戳，空字符串代表未拥有领取资格
        "recv": "1584094003.016"  # 领取活动奖励的时间戳，【"-1"】代表未领取，空字符串代表未拥有领取资格
    }
}

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
调整UI大小
1.0.2版本：
在配置了提示插件的场合使用提示插件弹出提示
1.0.3版本：
优化UI资源，补充代码注释
