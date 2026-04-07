插件介绍：
该服务器Mod隶属于“喇叭”插件。
“喇叭”插件实现喇叭功能：
- 喇叭：定义并在游戏中生效喇叭（*lobby/game下的mod.json与service下的mod.json均有配置项）

插件构成：
目前“喇叭”插件包含以下Mod：
- neteaseShout：部署于大厅服或游戏服
- neteaseShoutMaster：部署于控制服
- neteaseShoutService：部署于功能服

使用步骤：
（1）在部署配置中，将neteaseShout添加至需要的大厅服或者游戏服的mods列表中
（2）在部署配置中，将neteaseShoutMaster添加至控制服的mods列表中
（3）在部署配置中，将neteaseShoutService添加至某一个功能服的mods列表中

插件api：
（1）使一个玩家打开喇叭的输入界面
函数：OpenShoutBoard(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    shoutSystem = serverApi.GetSystem("neteaseShout", "neteaseShoutDev")
    shoutSystem.OpenShoutBoard(uid)

支持的运营指令：
运营指令：
（1）使用运营指令发送喇叭消息
post url: http:masterip:masterport/send-new-notice
post body:{
    "content": "准备停服",  # 内容
    "priority": 100,  # 优先级越高越先显示
    "name": "系统公告",  # 名字位置显示的字符
    "duration": 60,  # 显示持续时间，单位为秒，默认为10秒，即缺省，不得小于1
    "bg": 0  # 喇叭消息的背景资源序号，配置于mod.json中，默认为0，即缺省，错误的序号消息会返回操作成功，但依旧会无法显示，会报错
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
添加注释
1.0.2版本：
优化UI资源，补充代码注释
