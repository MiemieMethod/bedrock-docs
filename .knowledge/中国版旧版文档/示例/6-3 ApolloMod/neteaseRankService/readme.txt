插件介绍：
该服务器Mod隶属于“排行榜”插件。
该插件实现了排行榜的基本功能，具体包括以下功能：
（1）服主可以自己定义排行榜的类型，包括单服榜和全服榜，个人榜和公会榜
（2）服主可以自己定义排行榜的刷新频率，结算时间，排行榜奖励等
（3）本插件支持单个排行榜，多排行榜的用法可参考“MCStudio——基岩版网络服——排行榜模板
关于结算时间说明：
	年	月	日	周	时	分
格式	2020	10	1	1	4	0
	*	*	*	*		
	其中*表示不考虑具体的日期、星期、时间							
	举例说明:							
	年	月	日	周	时	分		
	2020	10	1	*	4	0	2020/10/1 4:00结算	
	*	*	*	1	4	0	每周一 4:00结算	
	*	*	*	*	4	0	每天 4:00结算


关于排行榜排序说明:
对应"dataType"是"int"的数据，根据"priority"的大小进行优先级排序，首先按"priority"值最小列的优先按数据从大到小排序，如果数据相同则按"priority"第二小的数据从大到小排序，以此类推。如果最后都相同，则按提交时间早排前面的原则排序。



插件构成：
目前“排行榜插件”包括以下mod
（1）neteaseRank:部署大厅服或者游戏服
（2）neteaseRankService:部署功能服
（3）neteaseRankMaster:控制服

数据库:
-mysql

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseRankService中）
（2）在部署配置中，将neteaseRank添加至需要的大厅服或者游戏服的mods列表中；
（3）在部署配置中，将neteaseRankService添加至功能服的mods列表中；
（4）部署并启动服务器后，即可使用排行榜插件

插件API：
（1）删除排行榜上某条数据。
函数：OnDelOneRankData
参数：
    rank：int，排名
示例:
    import server.extraServiceApi as serviceApi
    neteaseRankServiceSystem = serviceApi.GetSystem("neteaseRank", "neteaseRankService")
    neteaseRankServiceSystem.OnDelOneRankData(rank)

（2）向排行榜提交一条数据。
函数：OutCommitRankData
参数：
    fromId：int，玩家uid或者公会id
    oneRankData:list，一条排行数据，例如 [信息1,信息2,信息3,信息4,信息5,信息6]，顺序对应于mod.json的rankCol里面的顺序
示例:
    import server.extraServerApi as serverApi
    neteaseRankSystem = serverApi.GetSystem("neteaseRank", "neteaseRankDev")
    neteaseFriendServiceSystem.OutCommitRankData(fromId, oneRankData)
（3）结算排行榜。
函数：OnRankAward
参数：
    maxIndex：int，返回最大的排名，-1则代表所有人
示例:
    import server.extraServiceApi as serviceApi
    neteaseRankServiceSystem = serviceApi.GetSystem("neteaseRank", "neteaseRankService")
    neteaseRankServiceSystem.OnRankAward(10)
备注：
    调用这个接口后会触发下面的结算事件，maxIndex决定着返回排行榜数据的最大排名
（4）打开排行榜界面
函数：OpenRankUI
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    neteaseRankSystem = serverApi.GetSystem("neteaseRank", "neteaseRankDev")
    neteaseRankSystem.OpenRankUI(uid)
（5）获取排行榜数据。
函数：OnGetRankData
参数：
    无
返回值：
    rankData:dict 排行榜数据
示例:
    import server.extraServiceApi as serviceApi
    neteaseRankServiceSystem = serviceApi.GetSystem("neteaseRank", "neteaseRankService")
    rankData = neteaseRankServiceSystem.OnGetRankData()
（6）清除排行榜数据。
函数：OnCleareRankData
参数：
    无
示例:
    import server.extraServiceApi as serviceApi
    neteaseRankServiceSystem = serviceApi.GetSystem("neteaseRank", "neteaseRankService")
    neteaseRankServiceSystem.OnCleareRankData()

插件事件：
（1）功能服：排行榜结算事件
事件：neteaseRankAwardFromServiceEvent
namespace = 'neteaseRank',systemname = 'neteaseRankService'
描述：当排行榜刷新的时候触发，服主可以根据返回排行榜数据来给玩家做奖励
参数：
     rankData：list，排行榜的数据
示例
    self.ListenForEvent("neteaseRank", "neteaseRankService", "neteaseRankAwardFromServiceEvent", self, self.test)
    def test(self, args):
        rankData= args["rankData"]
        print rankData

支持的运营指令：
运营指令：
（1）提交一条排行榜数据
post url: http:masterip:masterport/commit-rank-data
post body:{
    "oneRankData": ["yfg", 39, 109, 56, 62, 37],#排行榜数据
    "fromId":1234, 玩家uid或者公会id
    "serverType":"gameA"
}
response:
{
    "code": 0,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {
    }
}
（2）删除一条排行榜数据
post url: http:masterip:masterport/delete-rank-data
post body:{
    "index": 2 #排名
}
response:
{
    "code": 0,  # 返回码，【1】代表成功，其他代表失败
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {
    }
}


更新列表：

1.0.0版本：
初始版本
1.0.1版本：
（1）修正了排行榜插件重启时没有从数据库读取数据的问题
（2）补充代码注释
1.0.2版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.3版本：
优化插件readme文档描述