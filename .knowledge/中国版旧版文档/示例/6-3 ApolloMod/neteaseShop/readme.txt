插件介绍：
该服务器Mod隶属于“商城”插件。
“商城”插件用于在服务器中实现商城的基本功能，有以下三点：
-查询订单信息
-通知发货成功
-查询订单信息并发货


插件构成：
目前“商城”插件包含以下Mod：
- neteaseShop: 部署于大厅服或游戏服。
- neteaseShopMaster: 部署于控制服。

使用步骤：
（1）该mod需配置mysql数据库，需手动执行mod.sql。
（2）在部署配置中，将该neteaseShop添加至需要的大厅服或者游戏服的mods列表中；将neteaseShopMaster添加至需要的控制服的mods列表中
（3）部署并启动服务器后，就能使用。插件api和event方法可以参看neteaseTestServerSystem.py中示例。
（4）测试时，需要在MCStudio中配置测试服的ID：基岩版服务器==>网络服开发==>鼠标悬浮在选中的网络服上==>更多==>服务器配置==>更多==>游戏ID。
（5）商城插件在开发阶段无法走完全部的商品发货流程

插件api：
(1)开始給玩家发货
函数：StartShipProcess(uid)
参数：
    data:int,玩家uid
返回：
    bool:是否开始查询订单（当玩家不在线的时候，不会开始查询订单，此时返回False）
示例：
    import server.extraServerApi as serverApi
    neteaseShopServerSystem = serverApi.GetSystem("neteaseShop", "neteaseShopDev")
    uid = 123456 #传入的参数是玩家的uid
    neteaseShopServerSystem.StartShipProcess(uid)
备注：调用本函数后，开发者会收到ServerShipItemsEvent服务端事件。开发者需要监听ServerShipItemsEvent事件，处理游戏中发货逻辑。

(2)发货成功
函数：ShipOrderSuccess(data)
参数：
    data:dict,包含玩家uid和订单信息
示例:
    import server.extraServerApi as serverApi
    neteaseShopServerSystem = serverApi.GetSystem("neteaseShop", "neteaseShopDev")
    data = {
        "uid":12343, #玩家uid
        "entities": [ #是个列表，包含多个未发货订单
        {
            "item_id": 90027446413343740,#商品id，仅记录用
            "item_num":1,#玩家购买的道具数量
            "orderid":"1234",#订单编号
            "cmd":"test",#实现指令。
            "buy_time":1230782400,#购买时间戳
            "group" : 1 #道具分类
        },
        {
            "item_id": 90027446413343740,
            "item_num":1,
            "orderid":"1234",
            "cmd":"test",
            "buy_time":1230782400,
            "group" : 1
        }
        ]
    } #传入的参数是玩家的id和发货成功的订单列表
    neteaseShopServerSystem.ShipOrderSuccess(data)
备注：ServerShipItemsEvent事件的监听函数在给玩家发货后，需要调用本api通知Apollo发货成功。

(3)查询玩家是否买过某个商品
函数CheckItem(data)
参数：
    data:dict,包含玩家uid和商品id
示例:
    import server.extraServerApi as serverApi
    neteaseShopServerSystem = serverApi.GetSystem("neteaseShop", "neteaseShopDev")
     data = {
        "uid":12343, #玩家uid
        "item_id": 90027446413343740,#商品id，仅记录用
        }
     neteaseShopServerSystem.CheckItem(data)
备注：函数执行完会触发CheckItemResultEvent事件，见“插件event”

插件event：
(1)ServerShipItemsEvent
namespace = 'neteaseShop',systemname = 'neteaseShopDev'
描述：当调用接口StartShipProcess后，插件会查询玩家还没发货的订单，然后触发此事件，服主可以根据事件携带的订单信息发货
备注：事件携带的参数如下所示，开发者可根据参数里面的订单信息发货
参数：
    uid:int,玩家uid
    entities:list,玩家订单列表
    code:int,返回码
    message:str,返回信息
示例:
    self.ListenForEvent("neteaseShop", "neteaseShopDev", "ServerShipItemsEvent", self, self.test)
    def test(self, args):
        uid = args["uid"]
        entities = args["entities"]
        print entities
        #print的结果如下：
        #[{
        # 	"item_id": 90027446413343740, #商品id，仅记录用
        # 	"uuid": "8a0886b5-eeb5-41f0-b517-f65691a2ce3b",# 玩家的唯一编号
        # 	"item_num":1,#玩家购买的道具数量
        # 	"orderid":"1234", #订单id
        # 	"cmd":"test",#实现指令
        # 	"buy_time":1230782400,#购买时间戳
        # 	"group" : 1#道具分类
        # },
        # {
        # 	"item_id": 90027446413343740,
        # 	"uuid": "8a0886b5-eeb5-41f0-b517-f65691a2ce3b",
        # 	"item_num":1,
        # 	"orderid":"1235",
        # 	"cmd":"test",
        # 	"buy_time":1230782400,
        # 	"group" : 1
        # }
        # ]
	    #根据 entities 执行发货逻辑
	    #具体可以参考neteaseTestServerSystem.py中示例代码

(2)CheckItemResultEvent
namespace = 'neteaseShop',systemname = 'neteaseShopDev'
描述：当调用接口函数CheckItem后，插件会查询玩家是否购买过传进来的商品，然后触发此事件
备注：事件携带的参数如下所示，开发者可根据参数里面的订单信息发货
参数：
    uid:int,玩家uid
    item_id:int,商品id
    has_buy:bool,是否购买商品
示例:
    self.ListenForEvent("neteaseShop", "neteaseShopDev", "CheckItemResultEvent", self, self.test)
    def test(self, args):
        uid = args["uid"]
        item_id = args["item_id"]
        has_buy = args["has_buy"]
        print uid, item_id, has_buy
        #print的结果如下：
        # 1234, 90027446413343740, False

运营指令：
(1).查询订单信息指令
post url: http:masterip:masterport/check-single-order
post body:{
    "orderid" : "1234",#订单id
    "uid" : 123456789 #玩家uid
}
response:
{
    "code": 0,
    "entity": [
    {
        "item_id": 90027446413343740, #商品id，仅记录用
        "uuid": "8a0886b5-eeb5-41f0-b517-f65691a2ce3b",# 玩家的唯一编号
        "item_num":1,#玩家购买的道具数量
        "orderid":"1234", #订单id
        "cmd":"test",#实现指令
        "buy_time":1230782400,#购买时间戳
        "group" : 1#道具分类
    }
    ],
    "message": "正常返回"
} 
(2).查询订单列表指令
post url: http:masterip:masterport/check-orders-list
post body:{
    "uid" : 123456789 #玩家uid
}
response:
{
    "code": 0,
    "entity": [
    {
       "item_id": 90027446413343740, #商品id，仅记录用
       "uuid": "8a0886b5-eeb5-41f0-b517-f65691a2ce3b",# 玩家的唯一编号
       "item_num":1,#玩家购买的道具数量
       "orderid":"1234", #订单id
       "cmd":"test",#实现指令
       "buy_time":1230782400,#购买时间戳
       "group" : 1#道具分类
    },
    {
       "item_id": 90027446413343740,
       "uuid": "8a0886b5-eeb5-41f0-b517-f65691a2ce3b",
       "item_num":1,
       "orderid":"1235",
       "cmd":"test",
       "buy_time":1230782400,
       "group" : 1
    }
    ],
    "message": "正常返回"
} 
(3).通知发货成功指令
post url: http:masterip:masterport/ship-orders-success
post body:{
    "orderid" : "1234",#订单id
    "uid":123456789 #玩家uid
}
response:
{
    "code": 0,
    "entity": None,
    "message": "正常返回"
} 

版本更新内容：

1.0.0版本：
初始版本

1.0.1版本：
1、优化了订单发货的速度
2、新增了配置，可以选择自动查询订单/手动查询订单两种模式
3、优化了配置功能，已经可以直接根据环境配置获取需要的信息，审核服/正式服的切换不再需要调整配置了
4、API【StartShipProcess】增加了返回值

1.0.2版本：
1、去掉了mod.json中的配置项：【isTestServer】、【gameId】、【gameKey】，使用环境配置代替
2、修正由于配置文件编码格式问题可能导致获取订单出错的问题

1.0.3版本：
修正一个会导致插件无法正常卸载的Traceback