插件介绍：
该服务器Mod隶属于“弹幕”插件。
“弹幕”插件实现弹幕功能：
- 弹幕：定义并在游戏中生效弹幕（*lobby/game下的mod.json有非常详细的配置解释）

插件构成：
目前“弹幕”插件包含以下Mod：
- neteaseDanmu：部署于大厅服或游戏服
- neteaseDanmuMaster：部署于控制服

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseDanmu中）
（2）在部署配置中，将neteaseDanmu添加至需要的大厅服或者游戏服的mods列表中
（3）在部署配置中，将neteaseDanmuMaster添加至控制服的mods列表中

插件api：
（1）使一个玩家打开弹幕的操作界面
函数：OpenDanmuFrame(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    danmuSystem = serverApi.GetSystem("neteaseDanmu", "neteaseDanmuDev")
    danmuSystem.OpenDanmuFrame(uid)

支持的运营指令：
运营指令：
（1）增加或解除全员发弹幕限制
post url: http:masterip:masterport/forbid-all-danmu
post body:{
    "ban": 1  # 0为解除，1为限制
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {}
}
（2）解锁或上锁一个玩家的某个弹幕头像
post url: http:masterip:masterport/unlock-danmu-icon
post body:{
    "icon_id": "icon2",  # 对应mod.json中的icon_id
    "uid": 996,  # 玩家uid
    "lock": 0  # 0为解锁，1为上锁
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {}
}

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
新增少量UI交互
1.0.2版本：
优化贴图资源，增加部分代码注释
1.0.3版本：
添加大量注释
