插件介绍：
该服务器Mod隶属于“随机传送”插件。
“随机传送”插件实现探索地图常用的功能，玩家可以随机传送到本维度、跨纬度、跨服符合一定条件的安全坐标。


插件构成：
目前“随机传送”插件包含以下Mod：
- neteaseRandomTp: 部署于大厅服或游戏服。
- neteaseRandomTpService：部署于功能服。


使用步骤：
（1）在部署配置中，将neteaseRandomTp添加至需要的大厅服或者游戏服的mods列表中；
（2）在部署配置中，将neteaseRandomTpService添加至某一个功能服的mods列表中。若不是MCStudio添加该mod，则需要手动将字符串"neteaseRandomTp"添加到deploy.json中service下的module_names属性中


插件api：
（1）本维度传送
适用范围：大厅服/游戏服
函数：TpInDimension(playerId, targetPos=None, randomRange=None, coolingTime=None, readingTime=None, interruptType=None, isCoolingAfterInterrupt=None)
参数：
    playerId: str, 玩家的entityId
    targetPos: tuple(int, int, int), 目标中心点坐标(x,y,z)，若不传则为玩家当前坐标
    randomRange: tuple(int, int, int, int), 随机范围(Xmin, Zmin, Xmax, Zmax)
    coolingTime: float, 冷却时间，单位秒
    readingTime: float, 读秒时间，单位秒
    interruptType: int, 打断机制(0 不能被打断；1 移动打断；2 受伤害打断；3 移动或受伤害都打断)
    isCoolingAfterInterrupt: int, 打断后是否进入冷却(0 不进入冷却；1 进入冷却)
返回：
    无
示例：
    import server.extraServerApi as serverApi
    randomTpSystem = serverApi.GetSystem("neteaseRandomTp", "neteaseRandomTpDev")
    randomTpSystem.TpInDimension(playerId, (10, 5, 20), (-100, -200, 100, 200), 10, 3, 1, 0)

（2）跨维度传送
适用范围：大厅服/游戏服
函数：TpCrossDimension(playerId, targetPos, tpParams=[], randomRange=None, coolingTime=None, readingTime=None, interruptType=None, isCoolingAfterInterrupt=None)
参数：
    playerId: str, 玩家的entityId
    targetPos: tuple(int, int, int), 目标中心点坐标(x,y,z)，不能传None
    tpParams: list(int), 传送参数[dimensionId,]，如果为空列表则表示默认当前维度
    randomRange: tuple(int, int, int, int), 随机范围(Xmin, Zmin, Xmax, Zmax)
    coolingTime: float, 冷却时间，单位秒
    readingTime: float, 读秒时间，单位秒
    interruptType: int, 打断机制(0 不能被打断；1 移动打断；2 受伤害打断；3 移动或受伤害都打断)
    isCoolingAfterInterrupt: int, 打断后是否进入冷却(0 不进入冷却；1 进入冷却)
返回：
    无
示例：
    import server.extraServerApi as serverApi
    randomTpSystem = serverApi.GetSystem("neteaseRandomTp", "neteaseRandomTpDev")
    randomTpSystem.TpCrossDimension(playerId, (10, 5, 20), [0, 1, 2], (-100, -200, 100, 200), 10, 3, 1, 0)

（3）跨服务器传送
适用范围：大厅服/游戏服
函数：TpCrossServer(playerId, targetPos, tpParams={}, randomRange=None, coolingTime=None, readingTime=None, interruptType=None, isCoolingAfterInterrupt=None)
参数：
    playerId: str, 玩家的entityId
    targetPos: tuple(int, int, int), 目标中心点坐标(x,y,z)，不能传None
    tpParams: dict, 传送参数{"gameType": [dimensionId,]}，如果为空则表示默认当前服务器当前维度
    randomRange: tuple(int, int, int, int), 随机范围(Xmin, Zmin, Xmax, Zmax)
    coolingTime: float, 冷却时间，单位秒
    readingTime: float, 读秒时间，单位秒
    interruptType: int, 打断机制(0 不能被打断；1 移动打断；2 受伤害打断；3 移动或受伤害都打断)
    isCoolingAfterInterrupt: int, 打断后是否进入冷却(0 不进入冷却；1 进入冷却)
返回：
    无
示例：
    import server.extraServerApi as serverApi
    randomTpSystem = serverApi.GetSystem("neteaseRandomTp", "neteaseRandomTpDev")
    randomTpSystem.TpCrossServer(playerId, (10, 5, 20), {"lobby": [0, 1, 2], "gameA": [0,]}, (-100, -200, 100, 200), 10, 3, 1, 0)

插件event：
（1）TpStartedOutputEvent
适用范围：大厅服/游戏服
命名空间：namespace = 'neteaseRandomTp', systemname = 'neteaseRandomTpDev'
描述：玩家开始发起传送请求时广播
参数：
    uid: int, 玩家的uid
    cancel: bool, 是否取消传送，设置为True则可取消传送
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseRandomTp', 'neteaseRandomTpDev', 'TpStartedOutputEvent', self, self.OnTpStarted)

    def OnTpStarted(self, data):
        uid = data['uid']
        cancel = data['cancel']

（2）ReadingInterruptedOutputEvent
适用范围：大厅服/游戏服
命名空间：namespace = 'neteaseRandomTp', systemname = 'neteaseRandomTpDev'
描述：玩家随机传送时读秒被打断时广播
参数：
    uid: int, 玩家的uid
    interruptType: int, 玩家被打断的原因，对应打断机制的定义（1 移动打断；2 受伤害打断）
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseRandomTp', 'neteaseRandomTpDev', 'ReadingInterruptedOutputEvent', self, self.OnReadingInterrupted)

    def OnReadingInterrupted(self, data):
        uid = data['uid']
        interruptType = data['interruptType']

（3）ReadingFinishedOutputEvent
适用范围：大厅服/游戏服
命名空间：namespace = 'neteaseRandomTp', systemname = 'neteaseRandomTpDev'
描述：玩家随机传送时读秒完成时广播
参数：
    uid: int, 玩家的uid
    cancel: bool, 是否取消传送，设置为True则可取消传送
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseRandomTp', 'neteaseRandomTpDev', 'ReadingFinishedOutputEvent', self, self.OnReadingFinished)

    def OnReadingFinished(self, data):
        uid = data['uid']
        cancel = data['cancel']

（4）TpFinishedOutputEvent
适用范围：大厅服/游戏服
命名空间：namespace = 'neteaseRandomTp', systemname = 'neteaseRandomTpDev'
描述：玩家随机传送完成时广播
参数：
    uid: int, 玩家的uid
    originServerType: str, 传送者原来所在服务器类型
    originDimensionId: int, 传送者原来所在服务器维度
    originPos: tuple(int, int, int), 传送者原来所在服务器坐标
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseRandomTp', 'neteaseRandomTpDev', 'TpFinishedOutputEvent', self, self.OnTpFinished)

    def OnTpFinished(self, data):
        uid = data['uid']
        originServerType = data['originServerType']
        originDimensionId = data['originDimensionId']
        originPos = data['originPos']

（5）ReadingStartedToClientEvent
适用范围：客户端
命名空间：namespace = 'neteaseRandomTp', systemname = 'neteaseRandomTpDev'
描述：玩家开始读秒
参数：
    readingTime: int, 读秒时间
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseRandomTp', 'neteaseRandomTpDev', 'ReadingStartedToClientEvent', self, self.OnReadingStarted)

    def OnReadingStarted(self, data):
        readingTime = data['readingTime']
        # 可以展示读秒特效

（6）ReadingInterruptedToClientEvent
适用范围：客户端
命名空间：namespace = 'neteaseRandomTp', systemname = 'neteaseRandomTpDev'
描述：玩家读秒被打断
参数：
    无
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseRandomTp', 'neteaseRandomTpDev', 'ReadingInterruptedToClientEvent', self, self.OnReadingInterrupted)

    def OnReadingInterrupted(self, data):
        # 中断读秒特效
        pass

（7）TpFinishedToClientEvent
适用范围：客户端
命名空间：namespace = 'neteaseRandomTp', systemname = 'neteaseRandomTpDev'
描述：玩家传送完成
参数：
    uid: int, 玩家的uid
    originServerType: str, 传送者原来所在服务器类型
    originDimensionId: int, 传送者原来所在服务器维度
    originPos: tuple(int, int, int), 传送者原来所在服务器坐标
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseRandomTp', 'neteaseRandomTpDev', 'TpFinishedToClientEvent', self, self.OnTpFinished)

    def OnTpFinished(self, data):
        uid = data['uid']
        originServerType = data['originServerType']
        originDimensionId = data['originDimensionId']
        originPos = data['originPos']
        # 播放传送完毕特效

更新列表：
1.0.0版本：
初始版本
