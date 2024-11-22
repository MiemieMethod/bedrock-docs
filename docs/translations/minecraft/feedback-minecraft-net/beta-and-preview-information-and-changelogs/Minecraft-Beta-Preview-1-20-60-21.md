---
标题: Minecraft Beta & Preview - 1.20.60.21
日期: 2023-11-28T19:24:04Z
更新: 2023-12-06T09:04:13Z
分类: Beta 和 Preview 信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/21754158247437-Minecraft-Beta-Preview-1-20-60-21
哈希:
  h_01HBVR6KM8JCTEG8SDY8V3WBB3: 关于Minecraft预览和Beta的信息
  h_01HGBQ7QA8B4JR55SJJJ5HC9DX: 实验性特性
  h_01HGBQ7QA8J9X8C7D0GQ0HP8DX: 雕纹铜块
  h_01HGBQ7QA8BFQ55NFMBP57V88R: 铜格栅
  h_01HGBQ7QA8X0KFWHYVD73PX41Y: 特性和漏洞修复
  h_01HGBQ7QA91AJM24Q29N3T4T9F: 方块
  h_01HGBQ7QA9CTEM7PCN5TNJDVHZ: 可自定义触控控制
  h_01HGBQ7QA9W152GQ1RNYDYN7BX: 游戏玩法
  h_01HGBQ7QA9WCBZKDT05WQKQ0TR: 原版趋同
  h_01HGBQ7QA9GSEC7006WTFEE0A7: 图形
  h_01HGBQ7QA90GKEGJT05FK0C5S3: 输入
  h_01HGBQ7QA9JE7ATJZTYRPCR8S1: 用户界面
  h_01HGBQ7QA9GK4TV7RDNH52EMYF: 加载屏幕
  h_01HGBQB43B1H1C0ZWSJ2Z8PGRF: 技术更新
  h_01HGBQB43BJT3FXTF5H0WFSTHM: 附加包和脚本引擎
  h_01HGBQB43BR3X36EY7P26DA9G7: AI意向
  h_01HGBQB43B4YERC9E2DBB96QYQ: API
  h_01HGBQB43B86BN6FH9EGYRCHVF: 生物群系
  h_01HGBQB43BTNSHD9N582R1QED8: 组件
  h_01HGBQB43BWBM9YV67TFYRESMT: 编辑器
  h_01HGBQB43BV35GSG8FWB9B44F0: 实体过滤器
  h_01HGBQB43B0R39CZQPM683YAEB: 一般
  h_01HGBQB43BHFT9TX3Q34WXRD7R: Molang
  h_01HGBQB43BA075GNY7PP3CBP14: 性能和稳定性
  h_01HGBQCRRC05YEAKV3DAKS5TMG: 实验性技术特性
  h_01HGBT13MQ92FQN38FAB4B4Z1S: picture2jpg
  h_01HGBQK5RXPZTV5SAW8QRYD114: 图形-1
  01HGBQPKS4J09GWZ0DC9ED1E3X: api-1
---

**发布:** 2023年11月29日

## **关于Minecraft预览和Beta的信息:**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![Picture1.jpg](https://feedback.minecraft.net/hc/article_attachments/21754860127885)

我们带来了另一个令人兴奋的Minecraft Beta和预览更新，包含许多调整和修复，我们相信你会喜欢！和往常一样，我们希望听到你对这些特性的反馈，请在 [这里](https://aka.ms/Minecraft121Feedback) 发送你的想法和建议，并在 [bugs.mojang.com](https://bugs.mojang.com/) 报告任何漏洞！

**注意:** 该版本现在也可在Android设备上使用！感谢你的耐心。

# 实验性特性

## 雕纹铜块

- 雕纹铜块及其变种现在可以在切石机中使用切制铜块进行合成 ([MCPE-176595](https://bugs.mojang.com/browse/MCPE-176595))

## 铜格栅

- 铜格栅及其变种现在可以含水 ([MCPE-176379](https://bugs.mojang.com/browse/MCPE-176379))
- 铜格栅在被打蜡时不再变成打蜡铜块 ([MCPE-176373](https://bugs.mojang.com/browse/MCPE-176373))

# 特性和漏洞修复

## 方块

- 霜冰方块在用精准采集工具开采时不再在世界中留下水
- 海龟蛋、青蛙卵、珊瑚和珊瑚扇在被开采时不再生成双倍粒子
- 蜂箱和蜂巢不再可以通过附魔书的精准采集进行采集
- 从底部方块破坏床时现在会正确清除出生点
- 冰、浮冰、霜冰和顶雪在被开采时现在会发送振动
- 营火在被玩家破坏时现在正确掉落2个木炭而不是4个 ([MCPE-159894](https://bugs.mojang.com/browse/MCPE-159894))

## 可自定义触控控制

- 修复了一个漏洞，当使用非触控控制器输入退出自定义触控控制屏幕时，快捷栏消失

## 游戏玩法

- 台阶和楼梯在持续建造时不再随机从底部开始放置 ([MCPE-54855](https://bugs.mojang.com/browse/MCPE-54855))
- 马、驴和骡在被玩家控制时现在会受到跌落伤害，除非是针对1.20.60之前的基础游戏版本的世界 ([MCPE-107031](https://bugs.mojang.com/browse/MCPE-107031))

## 原版趋同

- 下界金矿石在用未附魔工具开采时现在可以掉落最多6个金粒（之前为5个），或在使用时运等级3时掉落最多24个（之前为20个）
- 青金石矿石在用未附魔工具开采时现在可以掉落最多9个青金石（之前为8个），或在使用时运等级3时掉落最多36个（之前为32个）

## 图形

- 修复了在启用“改进输入响应”选项后，出水时方块照明不正确的问题 ([MCPE-175727](https://bugs.mojang.com/browse/MCPE-175727))

## 输入

- 修复了在移动设备上仅使用键盘时无法导航物品栏的问题
- 修复了在触控模式下使用键盘时无法进行堆叠分割的问题

## 用户界面

- 修复了资源包中“技术细节”按钮未能链接到技术细节屏幕的漏洞
- 修复了信标用户界面按钮在较小分辨率下超出窗口的问题 ([MCPE-173649](https://bugs.mojang.com/browse/MCPE-173649))
- 物品栏中的物品耐久条已调整，以匹配快捷栏中的耐久条 ([MCPE-128532](https://bugs.mojang.com/browse/MCPE-128532))
- 调整了口袋铁砧用户界面中的成本文本，以匹配经典版本 ([MCPE-101740](https://bugs.mojang.com/browse/MCPE-101740))
- 音乐唱片名称文本现在与附魔物品的颜色相同 ([MCPE-109471](https://bugs.mojang.com/browse/MCPE-109471))
- 添加了新朋友抽屉功能的首次迭代（在线/离线朋友以列表形式显示，添加朋友按钮重命名为搜索玩家，您没有朋友的空状态和改进的文本转语音）

## 加载屏幕

- 加载屏幕现在根据玩家进度显示3类提示  

# 技术更新

## 附加包和脚本引擎

- 为3D方块光标添加了*Project Through Liquid*属性
- 添加了*CursorPropertiesChangeAfterEvent*以在光标属性更改时通知编辑器脚本
- 流浪商人现在可以在其交易菜单中正确显示自定义实体刷怪蛋 ([MCPE-170184](https://bugs.mojang.com/browse/MCPE-170184))

## AI意向

- "behavior.breed"现在会在停止时中断导航，适用于使用引擎版本1.20.60或更高版本的内容

## API

- 将*DataDrivenEntityTriggerAfterEvent*从*beta*发布到*1.8.0*
- 将*DataDrivenEntityTriggerAfterEventSignal*从*beta*发布到*1.8.0*
- 将*DataDrivenEntityTriggerAfterEventSignalOptions*从*beta*发布到*1.8.0*
- 将*DefinitionModifier*从*beta*发布到*1.8.0*
- 将*WorldAfterEvents*.dataDrivenEntityTrigger从*beta*发布到*1.8.0*
- 将*EffectAddBeforeEvent*从*beta*发布到*1.8.0*
- 将*EffectAddAfterEvent*从*beta*发布到*1.8.0*
- 将*EffectAddAfterEvent*从*beta*发布到*1.8.0*
- 将*getTags*从*beta*发布到*1.8.0*
- 将*hasTag*从*beta*发布到*1.8.0*
- *RGBA*接口现在继承自*RGB*

## 生物群系

- 生物群系JSON文件不再支持从其他生物群系JSON文件继承字段。如果这影响到任何内容，则应通过手动复制所需的JSON文本来更新这些文件

## 组件

- "entity_sensor"组件现在支持多个"subsensors":
- "event"、"require_all"、"minimum_count"、"maximum_count"、"range"和"event_filter"现在是每个子传感器的单独可配置字段
- 子传感器还具有新的"cooldown"字段，定义每个子传感器感知实体的频率
- 所有这些更改需要"format_version"为1.20.60或更高

## 编辑器

- 修复了*CompoundBlockVolumeIterator*中的问题，去除了在某些*CompoundBlockVolume*配置中添加额外方块位置的情况
- 在世界选项菜单中使用状态菜单更新暂停活动对象
- 为工具轨道添加了工具分组支持
- 为*ExtensionOptionalParameters* API添加了*toolGroupId*属性，以组织在扩展中创建的工具
- 为*Extension* API添加了*name*、*description*、*notes*和*defaultToolGroupId*属性
- 为*ExtensionContext* API添加了*extensionInfo: Extension*属性，并移除了*extensionName*属性

## 实体过滤器

- 添加了新的实体过滤器"is_panicking"，检查实体是否正在执行"behavior.panic"
- 添加了新的实体过滤器"is_sprinting"，检查实体是否正在疾跑

## 一般

- 将*water_spash_manual.json*重命名为*water_splash_manual.json*在*resource_packs\vanilla\particles*中 ([MCPE-176784](https://bugs.mojang.com/browse/MCPE-176784))

## Molang

- 改进了当评估的Molang表达式结果出现错误时内容日志的上下文

## 性能和稳定性

- 在StartGamePacket的blockProperties中要求每个方块的block_id

# 实验性技术特性

## ![Picture2.jpg](https://feedback.minecraft.net/hc/article_attachments/21755225955725)

## 图形

- 修复了延迟技术预览中的纹理Z-fighting问题
- 为延迟技术预览添加了体积雾和光束。此新特性通过近似光线穿过空气时发生的散射来工作，从而产生更真实的雾和更强的场景深度感。它还连接到资源包中现有的数据驱动能力，以便创作者可以在各种条件下自定义雾的外观和感觉；有关更多信息，请参见Minecraft创作者门户上更新的[开始使用延迟照明](https://learn.microsoft.com/en-us/minecraft/creator/documents/deferredlighting?view=minecraft-bedrock-stable)文章

## API

- 修复了一个漏洞，在不可恢复的脚本监视器错误期间，世界有时无法正确关闭并断开客户端连接
- 更新了*SimulatedPlayer*，使其可以持续建造
- 更新了*SimulatedPlayer*，使其可以移动并朝不同方向查看
- ChatSendAfter & ChatSendBeforeEvent
  - 将*message*和*sender*更改为只读属性
  - 移除了*setTargets*、*getTargets*、*sendToTargets*，并替换为可选的玩家列表属性*targets*
- 类ItemDurabilityComponent
  - 将*unbreaking*重命名为*unbreakingEnchantmentLevel*
  - 将*getDamageRange*重命名为*getDamageChanceRange*
- EntityTypes
  - 将*getAll*返回类型从*EntityTypeIterator*更改为*EntityType\[\]*
- EntityEquippableComponent
  - 修复了在“before”事件处理程序中无法调用*getEquipment*和*getEquipmentSlot*函数的问题
- 修复了一个漏洞，导致在清除其背景故事后无法堆叠ItemStack