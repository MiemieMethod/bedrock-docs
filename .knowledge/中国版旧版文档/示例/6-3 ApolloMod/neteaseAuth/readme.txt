插件介绍：
该服务器Mod隶属于“权限”插件。
“权限”插件用于在服务器中实现对玩家权限分组的基本功能，有以下两点：
-不同分组的玩家有不同的权限，分为normal，vip，op三组
-外部可通过运营指令修改权限分组

插件构成：
目前“权限”插件包含以下Mod：
- neteaseAuth: 部署于大厅服或游戏服。
- neteaseAuthMaster: 部署于控制服。

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseAuth中）。
（2）在neteaseAuth的develop_mods/neteaseAuthDev/mod.json中配置玩家的权限分组，具体配置参数的意义见文件中的注释；
    在neteaseAuthMaster的develop_mods/neteaseAuthDev/mod.json中配置玩家的权限分组，具体配置参数的意义见文件中的注释；
    以上两个json文件关于权限的部分需保持一致。新进来的玩家默认分组是0，即普通玩家，可通过运营指令修改其分组
（3）该neteaseAuth添加至大厅服或者游戏服的mods列表中；将neteaseAuthMaster添加至master服的mods列表中
（4）部署并启动服务器后，就能使用。



运营指令：
(1).改变分组指令
post url: http:masterip:masterport/change-player-group
post body:{
    "authGroup": 0, #权限分组
    "uid" : 123456789 #玩家uid
}

(2).改变玩家op权限
post url: http:masterip:masterport/op-player
post body:{
    "neteaseId": 1234, #玩家uid
    "opTime" : 123456789, #op权限持续时间，单位(s)（玩家在线过程中不会取消玩家的op权限，仅在玩家离线的时候取消）
    "opType": 1 #1是op，2是deop


短指令：
说明：在游戏聊天框中，admin分组的玩家在聊天框输入的指令，指令要求"op"开头。这些指令只能在审核阶段和上线阶段才生效
（1）op ban
描述：封禁某个玩家
参数：
    第一个参数：str，玩家昵称
    第二个参数：int，封禁时间，单位为秒，-1表示永封。可以不输入，默认-1
    第三个参数：str，封禁原因，使用utf8编码。可以不输入，默认“被超级管理员封禁”
示例:
    # 封禁玩家“我的昵称”，封禁3000秒，原因是“作弊”
    op silent 我的昵称 3000  作弊
    #封禁玩家“我的昵称”，永久封禁，原因“被超级管理员封禁”
    op silent 我的昵称
（2）op unban
描述：解除某个玩家的封禁
参数：
    第一个参数：str，玩家昵称
示例:
    #玩家“我的昵称”解禁
    op silent 我的昵称
（3）op silent
描述：禁言某个玩家
参数：
    第一个参数：str，玩家昵称
    第二个参数：int，禁言时间，单位为秒，-1表示永封。可以不输入，默认-1
    第三个参数：str，禁言原因，使用utf8编码。可以不输入，默认“被超级管理员禁言”
示例:
    #玩家“我的昵称”被禁言一天，原因”说了敏感话题“
    op silent 我的昵称 86400 说了敏感话题
    #玩家“我的昵称”被永久禁言，原因”被超级管理员禁言“
    op silent
（4）op unsilent
描述：解禁某个玩家
参数：
    第一个参数：str，玩家昵称
示例:
    #玩家“我的昵称”被解禁
    op unsilent 我的昵称

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
新增改变玩家op权限接口
1.0.2版本：
新增admin分组，新增禁言解禁、封禁解禁短指令