插件介绍：
该服务器Mod隶属于“每日登录奖励”插件。
“每日登录奖励”插件实现每日登录奖励功能：
- 每日登录奖励：定义并在游戏中生效每日登录奖励（配置于lobby/game下的mod.json）

插件构成：
目前“每日登录奖励”插件包含以下Mod：
- neteaseDaily：部署于大厅服或游戏服
- neteaseDailyMaster：部署于控制服
- neteaseDailyService：部署于功能服


数据库：
- mysql

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseDailyService中）
（2）在部署配置中，将neteaseDaily添加至需要的大厅服或者游戏服的mods列表中
（3）在部署配置中，将neteaseDailyMaster添加至控制服的mods列表中
（4）在部署配置中，将neteaseDailyService添加至某一个功能服的mods列表中。若不是MCStudio添加该mod，则需要手动将字符串"neteaseDaily"添加到deploy.json中service下的module_names属性中

插件api：
（1）使一个玩家打开每日登录奖励的界面
函数：OpenDailyReward(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    dailySystem = serverApi.GetSystem("neteaseDaily", "neteaseDailyDev")
    dailySystem.OpenDailyReward(uid)

支持的运营指令：
运营指令：
（1）查询一个玩家本周的每日登录奖励领取情况
post url: http:masterip:masterport/query-player-recv
post body:{
    "uid": 996  # 玩家的uid
}
response:
{
    "code": 0,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {  # 返回该玩家本周每日登录奖励领取情况，查询失败则为空字典
        "stamp": 1583322262.219,  # 查询时service的时间戳
        "recv": {
            0: 0,  # 周日奖励的领取情况，【1】代表已领取，【0】代表未领取
            1: 0,  # 周一奖励的领取情况，【1】代表已领取，【0】代表未领取
            2: 0,  # 周二奖励的领取情况，【1】代表已领取，【0】代表未领取
            3: 0,  # 周三奖励的领取情况，【1】代表已领取，【0】代表未领取
            4: 0,  # 周四奖励的领取情况，【1】代表已领取，【0】代表未领取
            5: 0,  # 周五奖励的领取情况，【1】代表已领取，【0】代表未领取
            6: 0  # 周六奖励的领取情况，【1】代表已领取，【0】代表未领取
        }
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
调整UI资源，增加注释
