插件介绍：
该服务器Mod隶属于“云端玩家信息”插件。
该插件用于管理玩家存在地图中的数据，支持在不同服务器之间同步玩家持有物品、装备、背包、状态效果信息。具体包含下面功能：
（1）支持进入服务器时清空本地信息（比如持有物品、装备、背包、状态效果），离开服务器时将特定类型的物品通过邮件发送给玩家，邮件不包含物品的耐久度信息；
（2）使用云端玩家信息，可配置要使用的云端信息类型（比如持有物品、装备、背包、状态效果），进入服务器（包括登录和切换）时会同步云端信息到本地，而且信息变化时会同步到云端。
（3）查询和管理玩家云端玩家信息
可以用于解决以下问题：
（1）背包/装备/左手物品/右手物品/状态等跨地图同步（RPG中必需）；
（2）重新部署后，仍维持玩家信息不变（和生存服不一样，RPG不保存地图，但须保存玩家信息）；
（3）部分玩法设计中，希望能够带出一部分物品到其他服务器（比如，希望玩家从生存服回到大厅服时，能够将部分物品带过来）；


插件构成：
目前“云端玩家信息”插件包含以下Mod：
- neteaseCloud: 部署于大厅服或游戏服。
- neteaseCloudMaster：部署于控制服。


数据库：
- mysql

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseCloud中）
（2）在部署配置中，将neteaseCloud添加至需要的大厅服或者游戏服的mods列表中；特别注意下面几点
        - 若将process_type配置为1，则对应大厅服或游戏服一定要部署"公告"插件。公告插件具体部署方式参见"公告"插件使用说明。
        - 使用云端玩家信息时，如果碰到自定义物品/装备在服务器中不存在的情况，那么会自动禁用，请服主避免这种情况！
（3）在部署配置中，将neteaseCloudMaster添加至控制服的mods列表中；
（4）部署并启动服务器后，可以管理玩家存在地图中的数据

插件api：
 无

 插件event：
（1）FinishSyncCloudItemEvent
适用服务器：lobby/game
命名空间：namespace = 'neteaseCloud',systemname = 'neteaseCloudDev'
描述：完成云端玩家信息同步事件。mod.json中配置服务器信息处理方式为云端玩家信息，玩家从云端同步完信息后触发本事件
参数：
    uid：int，玩家uid
示例:
    self.ListenForEvent("neteaseCloud", "neteaseCloudDev", "FinishSyncCloudItemEvent", self, self.test)
    def test(self, args):
        uid = args["uid"]
        apply_tag = args["apply_tag"]

支持的运营指令：
运营指令：
（1）查询玩家云端信息
post url: http:masterip:masterport/cloud/query-user-cloud-items
post body:{
    "uid" :1357471387 #玩家uid
    "apply_tag" :tag0 #数据适用的tag，当云端插件用于不同服务器类型是生效。tag相同的云端插件数据共通
}

response:
{
    "entity": {
        "armor": {
            "0": [
                "minecraft:leather_helmet", #装备itemName
                0, #装备auxValue
                "" #装备extraId
            ]
        },
        "hands": {#玩家手上持有物品信息
            "right": 1, #获取当前手持的快捷栏的槽id
            "left": {#左手持有物品，是个物品信息字典 itemDict，各个元素含义参见"GetPlayerItem(posType, slotPos)" ModApi中描述
                "count": 1,
                "enchantData": [],
                "customTips": "",
                "extraId": "",
                "modId": "",
                "modItemId": "",
                "itemName": "minecraft:shield",
                "auxValue": 0,
                "showInHand": true
            }
        },
        "inventory": {#所有背包物品，key是槽位id，，value物品信息字典 itemDict，字典各个元素含义参见"GetPlayerItem(posType, slotPos)" ModApi中描述
            "29": {
                "count": 64,
                "enchantData": [],
                "customTips": "",
                "extraId": "",
                "modId": "",
                "modItemId": "",
                "itemName": "minecraft:painting",
                "auxValue": 0,
                "showInHand": true
            },
        },
        "armor": {#玩家所有装备，key是ArmorSlotType GetMinecraftEnum().ArmorSlotType.*， value是装备信息
            "0": [
                "minecraft:leather_helmet",  #装备itemName
                0,  #装备auxValue
                "" #装备extraId
            ]
        },
        "effect": [#实体当前所有状态效果
            {
                "duration": 439,#状态效果剩余持续时间，单位秒
                "effectName": "speed",#状态效果名称
                "amplifier": 0#状态效果额外等级
            }
        ],
        "extraData":{#玩家额外数据（SetExtraData API设置的玩家数据）
            "name":"test_name",
            "level":123
        }
    },
    "code": 0,
    "message": ""
}
（2）设置云端背包槽位物品
post url: http:masterip:masterport/cloud/set-inventory-items
post body:{
    "uid":1357471387,#玩家id
    "slot":0,#背包槽位id
    "inventory":{#物品信息字典 itemDict，字典各个元素含义参见"GetPlayerItem(posType, slotPos)" ModApi中描述
    "count": 0,#0表示删除物品；否则设置物品数量
    "enchantData": [],
    "customTips": "",
    "extraId": "",
    "modId": "",
    "modItemId": "",
    "itemName": "minecraft:leather_chestplate",
    "auxValue": 0,
    "showInHand": true,
    "durability": 70,#耐久度，可选参数，若不配置则表示没有损耗,
    "apply_tag" :tag0 #数据适用的tag，当云端插件用于不同服务器类型是生效。tag相同的云端插件数据共通
    }
}
response:
{
    "message": "",
    "code": 0,
    "entity": ""
}

更新列表：

1.0.0版本：
初始版本

1.0.1版本：
邮件发送物品支持附魔属性
云端保存物品耐久度信息和附魔信息

1.0.2版本：
云端支持保存额外数据（SetExtraData API设置的玩家数据）

1.0.3版本：
修复切维度时不能保存extraData bug

1.0.4版本：
新增事件FinishSyncCloudItemEvent事件，具体参见上面事件描述

1.0.5版本：
新增apply_tag配置，详情见mod.json