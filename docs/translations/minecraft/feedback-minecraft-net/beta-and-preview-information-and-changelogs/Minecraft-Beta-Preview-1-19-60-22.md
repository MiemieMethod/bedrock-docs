---
标题: Minecraft Beta & Preview - 1.19.60.22
日期: 2022-12-01T14:44:06Z
更新: 2022-12-01T16:33:23Z
类别: Beta 和 Preview 信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/11062311640333-Minecraft-Beta-Preview-1-19-60-22
---

**发布于:** 2022年12月1日

**注意:** 本周的预览版本在iOS上不可用。我们对此带来的不便表示歉意，并正在努力解决该问题。

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明

![一张Minecraft截图，展示了雕纹书架、装备鞍的骆驼和放置在音符盒上的生物头颅。](https://feedback.minecraft.net/hc/article_attachments/11061416160141)

以下是本周Minecraft预览和Beta中的新内容！请记得将您的反馈发送至 [aka.ms/MC120Feedback](https://aka.ms/MC120Feedback)，并将任何漏洞报告至 [bugs.mojang.com](http://bugs.mojang.com/)。  
  

# **实验性特性**

## **竹木类型**

- 竹板和竹台阶现在可以在所有需要任何木材类型木板的配方中使用 ([MCPE-163365](https://bugs.mojang.com/browse/MCPE-163365), [MCPE-163367](https://bugs.mojang.com/browse/MCPE-163367))
- 竹马赛克（木板和台阶）不能作为一般木板在合成配方中使用
- 将“去皮竹块”重命名为“去皮竹块”，因为之前命名不正确
- 竹块和去皮竹块现在在创造模式物品栏中正确分类为“木材”，而不是“原木”
- 更新了竹块和去皮竹块的纹理，因为它们的光照与其他方块不一致

## **骆驼**

- 在成年骆驼上使用鞍现在会正确装备 ([MCPE-163333](https://bugs.mojang.com/browse/MCPE-163333))
- 发射器现在可以为驯服的骆驼装备鞍

## **游戏玩法**

- 玩家音效滑块现在可以正确调整竹块、悬挂式告示牌、下界木材类型和雕纹书架的步伐和跌落音效
- 方块音效滑块现在可以正确调整雕纹书架的音效 ([MCPE-164700](https://bugs.mojang.com/browse/MCPE-164700))
- 当末影龙放置在音符盒上时，降低了其音量
- 唱片机滑块现在可以正确调整放置在音符盒上的生物头颅的音量

### **雕纹书架**

- 书籍现在可以从雕纹书架的特定槽位中移除和添加
- 你现在可以在手中持有书籍的情况下，从雕纹书架上移除一本书

# **特性和漏洞修复**

## **游戏玩法**

- 修复了一个问题，导致玩家在被向上推动时可能会掉出移动方块 ([MCPE-163725](https://bugs.mojang.com/browse/MCPE-163725))
- 修复了一个问题，如果游戏中的最后一名玩家在下界或末地，夜晚会被错误跳过
- 玩家进入下界或末地时，如果主世界中剩余的所有玩家都在睡觉，将触发夜晚跳过
- 修复了一个漏洞，导致同时掉落物品和睡觉时服务器会挂起 ([MCPE-162989](https://bugs.mojang.com/browse/MCPE-162989))
- 在同一方块内生成的经验球将合并并组合经验值，直到达到经验球限制 ([REALMS-10706](https://bugs.mojang.com/browse/REALMS-10706))

## **通用**

- 修复了一个问题，导致文本字段在使用游戏手柄取消选择后无法重新获得焦点 ([MCPE-153842](https://bugs.mojang.com/browse/MCPE-153842))
- 修复了一个问题，导致成就屏幕和新建世界屏幕上的用户界面元素未能正确触发音效 ([MCPE-163722](https://bugs.mojang.com/browse/MCPE-163722))

## **物品**

- 修复了一个问题，导致在与制箭师村民交易时某些绊线钩无效 ([MCPE-108195](https://bugs.mojang.com/browse/MCPE-108195))

## **移动控制**

- 修复了一个漏洞，导致玩家无法与摇杆和十字准星触控控制中的吐司通知进行交互

## **生物**

- 修复了恼鬼在黑暗环境中被错误照亮的问题
- 修复了恼鬼在基岩版和Java版之间的纹理差异 ([MCPE-164227](https://bugs.mojang.com/browse/MCPE-164227))
- 末影人、骷髅和凋灵骷髅现在仅在下界的光照等级7及以下生成（而不是11及以下） ([MCPE-163701](https://bugs.mojang.com/browse/MCPE-163701))

## **玩家**

- 修复了一个漏洞，导致玩家的击中箱和姓名标签在死亡后重新加入世界并返回菜单而未重生时未对齐 ([MCPE-162630](https://bugs.mojang.com/browse/MCPE-162630))

## **触控控制**

- 如果玩家使用第二种输入方法并悬停在另一个标签上，物品栏标签现在将重置其悬停状态

## **原版趋同**

### **生物**

- 在驯服的马、驴或骡上使用鞍现在会导致其被装备 ([MCPE-83815](https://bugs.mojang.com/browse/MCPE-83815))
- 在未装备盔甲的驯服马上使用马铠现在会导致其被装备 ([MCPE-163336](https://bugs.mojang.com/browse/MCPE-163336))
- 在驯服的羊驼上使用地毯现在会导致其被装备 ([MCPE-163336](https://bugs.mojang.com/browse/MCPE-163336))
- 发射器现在可以为驯服的马装备鞍和马铠
- 发射器现在可以为驯服的骡和驴装备鞍和箱子
- 发射器现在可以为驯服的羊驼装备地毯和箱子
- 发射器现在可以为猪和炽足兽装备鞍
- 发射器中的剪刀现在每次只会剪一只绵羊
- 发射器中的剪刀现在可以剪雪傀儡和哞菇

### **流浪商人**

- 流浪商人将不再有机会提供重复的种子交易 ([MCPE-161780](https://bugs.mojang.com/browse/MCPE-161780))

### **用户界面**

- 修复了在游戏中播放屏幕、设置屏幕选择语言、设置屏幕选择控制和邀请朋友屏幕中，当列表中有大量项目时，文本到语音的枚举问题

# **技术更新**

## **组件**

- 添加了“inventory”作为“has_equipment”过滤器的可能“domain”值，允许检查存储在活动对象库存中的物品
- 向“interact”组件添加了“equip_item_slot”字段
  - 如果设置，将在成功交互时将玩家持有的物品装备到指定槽位
  - 如果指定槽位中已经存在物品，则该物品将移至玩家的库存
  - 装备物品将从玩家的库存中移除，除非玩家处于创造模式

# **技术实验性特性**

## **API**

- 方块
  - 添加函数 *getRedstonePower(): number* - 获取方块的红石信号强度，如果它是电路的一部分，则返回该值，否则返回未定义
- 添加/scriptevent命令作为Beta API实验的一部分。这将触发system.events.scriptEventReceive事件（见下文）  
    
  - 用法: /scriptevent \<messsageId: string\> \[message: ???\]
  - messageId必须是命名空间，使用minecraft命名空间无效（例如“/scriptevent give:coal”，“/scriptevent my_scripts:spawn_sheep”）
  - message是可选的，最大长度为256个字符  
      
- events.scriptEventReceive
  - 添加系统事件 *events.scriptEventReceive*
  - 添加只读属性 *id: String* - 事件的命名空间ID
  - 添加只读属性 message: String - 事件发送的消息内容
  - 添加只读属性 *sourceBlock: Block* - 触发/执行命令调用的命令方块（如果适用），否则为未定义
  - 添加只读属性 *sourceEntity: Entity* - 执行命令调用的玩家/实体（如果适用），否则为未定义
  - 添加只读属性 *initiator: Entity* - 导致NPC执行命令调用的玩家（如果适用），否则为未定义
  - 添加只读属性 *sourceType: MessageSourceType* - 触发事件的源类型
  - *subscribe()*可以使用 *ScriptEventMessageFilterOptions* 类过滤有效的命名空间字符串  
      
- ScriptEventMessageFilterOptions
  - 添加 *ScriptEventMessageFilterOptions* 类
  - 添加属性 *namespaces: string\[*\]* - 要过滤的命名空间数组
- 模拟玩家
  - 添加属性 *isSprinting* - 用于获取或设置模拟玩家的疾跑状态是否设置为true

## **通用**

- 确保方块排列条件不能有副作用（即“math.random”，“math.random_integer”和变量赋值）