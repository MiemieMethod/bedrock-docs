插件介绍：
该服务器Mod隶属于“称号”插件。
- 称号：定义并在游戏中生效称号（详见lobby/game下的mod.json配置项）
****称号属性配置：称号属性需配置于战斗插件物品属性相应的配置处，名称为"netease_label:"前缀加上称号唯一ID。例如："netease_label:headpic"

插件构成：
目前“称号”插件包含以下Mod：
- neteaseLabel：部署于大厅服或游戏服
- neteaseLabelMaster：部署于控制服

使用步骤：
（1）在部署配置中，将neteaseLabel添加至需要的大厅服或者游戏服的mods列表中
（2）在部署配置中，将neteaseLabelMaster添加至控制服的mods列表中
（3）请在mysql中执行mod.sql（位于neteaseLabel中）

插件api：
（1）使一个玩家打开称号界面
函数：OpenLabelBoard(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    labelSystem = serverApi.GetSystem("neteaseLabel", "neteaseLabelDev")
    labelSystem.OpenLabelBoard(uid)
（2）使一个玩家解锁一些称号
函数：UnlockLabelsForPlayer(uid, labelIdList)
参数：
    uid: 玩家的uid
    labelIdList: 称号ID列表
示例：
    import server.extraServerApi as serverApi
    labelSystem = serverApi.GetSystem("neteaseLabel", "neteaseLabelDev")
    labelSystem.UnlockLabelsForPlayer(uid, ["headpic", "headtext"])
（3）获得一个玩家已解锁的称号及信息，玩家不在线则返回空字典
函数：GetLabelInfoByPlayerId(playerId)
参数：
    playerId: 玩家的playerId
示例：
    import server.extraServerApi as serverApi
    labelSystem = serverApi.GetSystem("neteaseLabel", "neteaseLabelDev")
    print(labelSystem.GetLabelInfoByPlayerId(playerId))

支持的运营指令：
运营指令：
（1）使一个玩家获得一个称号，注意该指令只向数据库插入数据，请核对参数是否为生效的配置
post url: http:masterip:masterport/insert-one-label
post body:{
    "uid": 996,  # 玩家的uid
    "labelId": "headpic"  # 称号唯一ID
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {
        "rowcount": 1  # 数据库操作影响的行数
    }
}
（2）删除一个玩家的一个称号，注意该指令只向数据库删除数据，请核对参数是否为生效的配置，若该称号为玩家正在使用的称号，则玩家重新登录或重新打开称号界面后才会刷新
post url: http:masterip:masterport/delete-one-label
post body:{
    "uid": 996,  # 玩家的uid
    "labelId": "headpic"  # 称号唯一ID
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {
        "rowcount": 1  # 数据库操作影响的行数
    }
}

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
解决缩放问题
1.0.2版本：
优化UI资源，补充代码注释
1.0.3版本：
按照新的插件标准实现了界面，解决了以下问题：
（1）多个插件之间界面穿插、按钮点击响应问题
（2）多个插件之间资源文件重名问题
1.0.4版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.5版本：
1、提供UI工程