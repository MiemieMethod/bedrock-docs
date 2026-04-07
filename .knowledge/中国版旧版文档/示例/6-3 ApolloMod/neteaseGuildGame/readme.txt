公会插件介绍：
本插件用于对公会的管理，主要有公会的创建公会，申请，同意加入，任命成员，转让会长，退出公会，回到领地，解散公会，踢成员，活跃度管理等功能。服主使用该插件后：
（1）服主可以很方便的进行公会的管理，对于所有的操作成功或失败都有提示
（2）可以方便的在一个game服分配多个公会的领地（避免一个公会一个game服，很浪费）
（2）在公会的领地当中，玩家聊天只有同公会的玩家可见




插件构成：
（1）neteaseGuildGame: 部署于游戏服。
（2）neteaseGuildLobby: 部署于大厅服。
（3）neteaseGuildMaster: 部署于控制服。
（4）neteaseGuildService: 部署于功能服。


使用步骤：
（1）配置lobby、game、service中mod.json，请按照文件mod.json中"_comment"注释配置对应内容。使用过程中尽量保持各个服的mod.json关于公会配置的部分一致
（2）请在mysql中执行mod.sql（位于neteaseGuildService中）
（3）MCStudio把neteaseGuildGame添加到游戏服，把neteaseGuildLobby添加到大厅服，把neteaseGuildMaster添加到控制服，把neteaseGuildService添加到功能服。若不是MCStudio添加neteaseGuildService，则需要手动将字符串"neteaseGuild"添加到deploy.json中service下的module_names属性中。
（4）点击本插件提供的UI即可完成公会管理的功能

插件UI介绍：
（1）公会入口按钮：
如果玩家有公会，则显示玩家所在的公会信息的UI；如果玩家没有公会，则显示所有公会的简略信息的UI，玩家可以选择加入哪个公会
（2）申请加入公会按钮：
点击公会入口按钮后，如果玩家没有公会，则显示所有公会的简略信息，且服务器有其他公会时，每个公会的最后会带有“申请加入公会按钮”，点击就会把玩家加入到该公会的申请队列中
（3）创建公会按钮：
点击创建公会按钮时，会显示创建公会的UI，点击“创建”后，如果玩家钻石数量足够，且服务器公会数量没达上限，且名字通过敏感词检测，则创建公会成功
（4）公会信息的UI
点击公会入口按钮后，如果玩家有公会，会弹出玩家所在公会信息的UI，里面包括同公会玩家的列表，以及“退出公会”按钮，“申请列表”按钮，“回到领地”按钮。同时在每个玩家的后面都有对每个玩家操作的按钮，点开后有“升职”按钮，“降职”按钮，“踢出公会”按钮，“转让会长”按钮。
其中，“申请列表”按钮只有会长和长老点开才能看到申请列表，普通成员不能看到；“升职”，“降职”，“转让会长”只有会长点了才有权限；“踢出公会”只有会长和长老才有权限
（5）回到领地按钮
玩家点击后，会切到game服中公会领地对应的坐标位置（在mod.json中配置）
（6）申请列表界面
会长和长老点击“申请列表”按钮后，会弹出当前在公会申请列表里面的玩家，会长和长老则可以对他们进行“同意入会”和“拒绝入会”的操作


运营指令：
（1）解散某个公会
post url: http:masterip:masterport/dismiss-guild
post body:
{
	"guildId" : 1 #公会ID
}
response:
{
	"message": "公会解散",
	"code": 12,
	"entity": []
}

插件api
（1）通过公会id，获取该公会全体成员的uid列表。
函数：GetGuildUidsByGuilId
参数：
    guildId:公会Id
示例:
    import server.extraServiceApi as serviceApi
    neteaseGuildServiceSystem = serviceApi.GetSystem("neteaseGuild", "neteaseGuildService")
    mes = neteaseGuildServiceSystem.GetGuildUidsByGuilId(guildId)
    print mes # {"code":8, "message":"公会不存在！", "players":[]}

（2）获取玩家所在的公会id，没有则返回-1。
函数：GetPlayerAtGuild
参数：
    playerUid:玩家Uid
示例:
    import server.extraServiceApi as serviceApi
    neteaseGuildServiceSystem = serviceApi.GetSystem("neteaseGuild", "neteaseGuildService")
    mes = neteaseGuildServiceSystem.GetPlayerAtGuild(playerUid)
    print mes #{"code":10, "message":"玩家不在任何公会！", "guildId":-1}

更新列表
1.0.0：初始化版本
1.0.1：适配了UI，使手机端也能正常显示
1.0.2：新增接口GetGuildUidsByGuilId，GetPlayerAtGuild
1.0.3：新增PVP插件的支持
1.0.4：添加大量注释
