插件介绍：
该服务器Mod隶属于“唯一ID”插件。
“唯一ID”插件仅实现一个功能：
- 生成唯一ID：接受来自lobby/game/service的请求，返回全服务器进程，全生存周期唯一的正整数ID

插件构成：
目前“公告”插件包含以下Mod：
- neteaseUniqueIdService: 部署于功能服。

数据库：
- mysql


使用步骤：
（1）请在mysql中执行mod.sql
（2）在部署配置中，将neteaseUniqueIdService添加至某一个功能服的mods列表中。若不是MCStudio添加该mod，则需要手动将字符串"neteaseUniqueId"添加到deploy.json中service下的module_names属性中
（3）部署并启动服务器后，就可以在任意lobby/game/service进程中，通过下文描述的方法获取全服务器进程，全生存周期唯一的正整数ID（从1开始自增）

插件api：
（1）获取唯一ID
函数：system.RequestToService(module, event, eventData, callback, timeout=2.0)
参数：
    module:str, service的ModName，这里固定为"neteaseUniqueId"
    event:str, service提供的接口，这里固定为"UniqueIdAskNew"
    eventData:dict, event对应的参数，需要两个特定的关键字，
                    类似{"keyword":"hello", "requireNum":10}，
                    keyword是唯一ID所属的类别，需要一个str，keyword相同的唯一ID不会重复，
                    requireNum是申请发放多少个唯一ID，一旦发放之后，就无法回收，也不会重复发放。
    callback:function, 用于处理返回结果的回调函数。回调函数定义为function(suc, args)，
                        其中suc代表是否在timeout之前收到了返回结果，当suc=False的时候，args会是None，当suc=True的时候，args是一个字典，
                        类似{"code":0, "message":"", "keyword":"hello", "requireNum":10, "startId":1, "endId":10}，
                        当code不等于0时，args仅有message关键字，描述了失败的原因，
                        当code等于0时，keyword、requireNum就是请求中的对应参数，
                        从startId到endId就是返回的可用正整数ID，包括startId和endId
    timeout:float, 回应超时时间，单位秒，默认值为2.0秒
示例：
    #lobby mod
    class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
            ServerSystem.__init__(self, namespace, systemName)

        def OnUniqueIdCallback(self, suc, args):
            if not suc:
                logout.error("callUniqueId failed by 【请求超时】")
                return
            if args["code"] != 0:
                logout.error("callUniqueId failed by 【%s】"%args["message"])
                return
            logout.info("callUniqueId success, keyword=%s startId=%s endId=%s"%(args["keyword"], args["startId"], args["endId"]))

        def DoCallUniqueId(self, keyword, requireNum):
            eventData = {
                "keyword": keyword,
                "requireNum": requireNum,
            }
            self.RequestToService("neteaseUniqueId", "UniqueIdAskNew", eventData, self.OnUniqueIdCallback)

        def Destroy(self):
            pass
            
运营指令：
无

实现细节：
1、插件会在对应功能服进程的内存中预先生成keyword和对应的可用ID的最小值和最大值，生成方式是更新数据库对应主键为keyword的记录，
2、预先生成的ID数量，会取mod.json的配置中的"DefaultPlusSize"属性和每次申请的requireNum*10中较大的那个。
3、每次申请新的可用ID，会先检查内存中可用的ID是否足够，假如足够，就直接返回结果
4、假如不够，会把对应的申请放入任务队列，然后开始更新数据库（或者新建）对应keyword主键的记录，预生成一批新的ID
5、数据库记录修改（新建）成功之后，从任务队列中，按照时间顺序依次返回可以结果，假如ID又不够用了，那就重复第4步
6、预生成的可用ID，假如没有发放出去，会在功能服关闭时被丢弃，所以不能保证唯一ID是连续的
7、需要关注的细节：请根据实际需要，调整每次申请ID的数量（尽量每次都一样），这样可以减少唯一ID的浪费，又不至于有太过频繁的数据库操作影响性能。

更新列表：
1.0.0版本：
初始版本
