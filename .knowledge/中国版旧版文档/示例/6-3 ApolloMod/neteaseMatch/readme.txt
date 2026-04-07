插件介绍：
报名匹配插件，该插件将报名玩家放入匹配池，然后根据一定算法匹配，产出匹配结果，功能概述如下：
（1）提供完整的报名、匹配流程。玩家从报名界面中报名，最终产出是匹配好的n个uid列表。
（2）服主可选择匹配算法，输入一个uid列表，产出匹配好的n个uid列表。
（3）报名与匹配可根据活动独立进行，也就是说，假如服务器里有A、B两个活动，每个活动可拥有自己独立的报名与匹配逻辑。

插件构成：
（1）neteaseMatch：部署大厅服或游戏服
（2）neteaseMatchMaster：部署控制服
（3）neteaseMatchService：部署功能服

使用步骤：
（1）配置lobby、game、service中mod.json，请按照文件mod.json中"_comment"注释配置对应内容。
（2）MCStudio把neteaseMatch添加到游戏服或大厅服，把neteaseMatchMaster添加到控制服，把neteaseMatchService添加到功能服。若不是MCStudio添加neteaseMatchService，则需要手动将字符串"neteaseMatch"添加到deploy.json中service下的module_names属性中。
（3）参照neteaseMatch中matchTestSystem.py实现，使用本插件提供的event和api完成游戏功能。

插件api：
（1）打开报名界面
适用服务器：client
函数：OpenMatchUI(activityId)
参数：
    activityId：int, 活动唯一id，具体参见mod.json中'activity_list'下'id'配置
示例：
    import client.extraClientApi as clientApi
    matchSystem = clientApi.GetSystem("neteaseMatch", "neteaseMatchClient")
    matchSystem.OpenMatchUI(3)

（2）申请报名
适用服务器：client
函数：ApplyToMatchActivity(activityId, uid, matchValue, isTeam, memberInfo, groupId)
参数：
	activityId：int, 活动唯一id
	uid：int, 报名玩家uid，若是组队报名则表示队长uid
	matchValue:int, 玩家的匹配值，分段匹配时会使用该值匹配，若未使用该值则设置为1
	isTeam:bool, 是否是组队匹配
	memberInfo:list(dict), 队员信息，它是个list，不包含队长信息，要求队员不能重复，每个元素是个dict，字段含义如下
		nickname:队员昵称
		match_value：队员匹配值
		uid：队员uid
	groupId:int, 阵营id，若为-1则表示申请任意阵营，阵营id对应mod.json配置中group_player_num的索引值。比如group_player_num配置为[1,2]，则需要两个阵营，若groupId为1，则报名第二个阵营，第二个阵营需要2个人；若groupId为-1，则报名任意阵营
示例：
    import client.extraClientApi as clientApi
    matchSystem = clientApi.GetSystem("neteaseMatch", "neteaseMatchClient")
    matchSystem.ApplyToMatchActivity(3, 123, 9, False, [], -1) #报名任意阵营
	member = {
		'nickname' : 'member1',
		'match_value' : 8,
		'uid' : 1
	}
	matchSystem.ApplyToMatchActivity(3, 123, 9, True, [member], 1) #组队报名，报名第二个阵营

（3）屏蔽某个活动默认报名逻辑
详细说明：默认报名逻辑，玩家执行报名后，执行下面申请报名请求
	ApplyToMatchActivity(activityId, uid, 1, False, [], -1)
	若需要自定义申请报名，则需要屏蔽活动默认报名逻辑，然后监听ApplyToMatchLocalEvent事件，事件回调中执行申请报名逻辑，具体参照matchTestSystem.py实现
适用服务器：client
函数：ShieldDefaultApplyMethod(activityId)
参数：
	activityId：int, 活动唯一id
示例：
    import client.extraClientApi as clientApi
    matchSystem = clientApi.GetSystem("neteaseMatch", "neteaseMatchClient")
    matchSystem.ShieldDefaultApplyMethod(3) #活动3要求实现自定义申请报名逻辑


（4）获得某玩家的报名某活动的开始报名时间
适用服务器：service
函数：GetPlayerApplyTime(uid, activityId)
参数：
	uid：int, 玩家id
	activityId：int, 活动唯一id
返回：
	int，返回玩家开始报名时间。具体含义如下：
	a、若玩家已经报名且在等待匹配中，则返回玩家开始报名时间
	b、若玩家匹配超时了，则返回玩家开始报名时间
	c、若玩家超时后继续报名，则返回玩家第一次报名时间
	d、若玩家没有报名活动或取消了报名，则返回-1
示例：
    import server.extraServiceApi as serviceApi
    matchSystem = serviceApi.GetSystem("neteaseMatch", "neteaseMatchServiceSystem")
    startApplyTime = matchSystem.GetPlayerApplyTime(123, 3)

（5）获得某活动的匹配队列
适用服务器：service
函数：GetAppliedUIDs(activityId)
参数：
	activityId：int, 活动唯一id
返回：
	list(int)，玩家uid列表，比如[123, 456]
示例：
    import server.extraServiceApi as serviceApi
    matchSystem = serviceApi.GetSystem("neteaseMatch", "neteaseMatchServiceSystem")
    playerUIDs = matchSystem.GetAppliedUIDs(3)

（6）获得某玩家报名的活动
适用服务器：service
函数：GetApppliedActivityList(uid)
参数：
	uid：int，玩家uid
返回：
	list(int)，活动id列表，比如[1,2,3]
示例：
    import server.extraServiceApi as serviceApi
    matchSystem = serviceApi.GetSystem("neteaseMatch", "neteaseMatchServiceSystem")
    activityIds = matchSystem.GetApppliedActivityList(123)

插件event：
（1）ApplyToMatchLocalEvent
适用服务器：client
命名空间：namespace = 'neteaseMatch',systemname = 'neteaseMatchClient'
描述：玩家申请报名事件，玩家点击“报名”按钮后才会触发，注意只有屏蔽默认报名逻辑的活动（执行【ShieldDefaultApplyMethod】）才会触发本事件
参数：
    activity_id：int，活动id

（2）ApplyToMatchResultEvent
适用服务器：client
命名空间：namespace = 'neteaseMatch',systemname = 'neteaseMatchClient'
描述：申请报名结果事件，该事件会告知报名成功或失败的状态。玩家点击“报名”按钮后会触发本事件。
参数：
    activity_id：int，活动id,
    code:int，状态码，状态码含义如下：
    	0，申请报名成功，玩家会放入匹配队列中
    	1，组队匹配下，某个玩家不满足分段匹配条件
    	2，阵营不存在
    	3，组队匹配下，组队人员过多，超过一次匹配需要的人数
    	4，不满足报名方式，比如活动要求单人报名，玩家却用组队方式申请报名
    	5，活动不存在
    	6，重复报名，表示以前已经报名成功，玩家已经在匹配队列中
    	7，组队匹配下，某个玩家已报名
    	200，匹配超时后弹出ui提示，玩家点击“继续等待”，继续申请报名，但是玩家却不在匹配队列中

（3）MatchResultEvent
适用服务器：client
命名空间：namespace = 'neteaseMatch',systemname = 'neteaseMatchClient'
描述：匹配结果事件，只有申请报名成功（ApplyToMatchResultEvent参数code为0）后才触发，在ApplyToMatchResultEvent后触发
参数：
    activity_id：int，活动id,
    group_uids, list(list(int))，匹配结果，格式为[[uid1,uid2],[uid3,uid4,uid5],…,]
    code:int，状态码，状态码含义如下：
    	0，匹配成功
    	100，匹配超时，自动取消报名，组队报名匹配超时后会提示这个错误
    	101，匹配超时，然后弹出超时ui，允许玩家继续报名
    	102，取消报名，匹配超时出现超时ui后，长时间没有点击“继续等待”按钮后，系统自动取消报名
    	103，组队匹配下，某个玩家取消报名
    	104，玩家自己点击取消报名

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
删除neteaseMatch中无用的server.properties文件
