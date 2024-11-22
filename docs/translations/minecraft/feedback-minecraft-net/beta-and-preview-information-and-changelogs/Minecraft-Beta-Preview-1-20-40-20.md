---
title: Minecraft 测试版与预览版 - 1.20.40.20
date: 2023-09-06T13:20:52Z
updated: 2023-09-07T15:41:59Z
categories: 测试版与预览版信息与更新日志
link: https://feedback.minecraft.net/hc/zh-cn/articles/19244682051341-Minecraft-Beta-Preview-1-20-40-20
hash:
  h_01H9QCWRGC7NSXFY3CFG8KQX3H: 实验性功能
  h_01H9QCWRGC2MEFKER6NTFNYN0F: 村民交易再平衡第2部分
  h_01H9QCZBYYWARZWB0TNGG8C9WM: 功能与漏洞修复
  h_01H9QCZT9HGCK007D4YQMSGQ5F: 辅助功能
  h_01H9QD21XE1NG9SRMNEM3Y2NFS: 音频
  h_01H9QD21XEJ9PJBW4T9ZV9P5V1: 游戏性
  h_01H9QD21XFWF3WWKY245TFPESF: 通用
  h_01H9QD21XFSX71RN0A6H2F6E0A: 图形
  h_01H9QD21XFA8QK6H26Y0KQHHT4: 生物
  h_01H9QD21XFEAPW8BAQP5XFJDRH: 原版趋同
  h_01H9QD21XFS1GS9CEY9ZDQBAK1: 用户界面
  h_01H9QD21XFQRPB88VTWWA0SH9R: 技术更新
  h_01H9QD21XF05WF7AQ53RXDCE0K: 附加包与脚本引擎
  h_01H9QD21XFM43QZ0CYYVZY9WXY: 命令
  h_01H9QD21XFSF222MJHYC8ZFRDR: 组件
  h_01H9QD21XF58NMJJK55V3GFKTE: molang
  h_01H9QD21XF97HF2TMFNKEQ6M5X: 交易表
  h_01H9QD21XF674ZEY6WPMTJ6F9T: 实验性技术更新
  h_01H9QD21XF54EHNCS5S1R7KHQV: 脚本API
  h_01H9QD3AADYNNJ1RBVP5KS6X2E: 图形-1
  h_01H9QD3AAE23Q6DNCA327550GN: 稳定性与性能
  h_01H9QD3AAEF8R54HX9CEA4KN8B: 用户界面-1
---

**发布日期：** 2023年9月7日

**关于Minecraft预览版与测试版的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明。

![一个盔甲匠村民站在门口。村庄中还可以看到其他村民、一个铁傀儡和一只猫。靠近箱子的地板上有掉落的绿宝石。](https://feedback.minecraft.net/hc/article_attachments/19244724805773)

哦！我没想到会在这里见到你，我正在找我的基地！相反，我似乎偶然发现了这个预览版；其中包括一些调整以帮助方向感不佳的探险者，以及趋同调整、游戏性修复和音频调整（流浪猫现在在乞讨食物时会发出声音！）村庄中的制图师现在也会出售七张新地图，随着村民交易再平衡实验的继续，使得寻找村庄和其他结构更容易。当探索时，这将派上用场，因为某些附魔书也更有可能出现在特定结构中。不久我拥有的一切都将是耐久的！只要我能重新找到我的基地……如往常一样，我们真的希望听到你对这些实验的看法，请将你的反馈和想法发送至 [aka.ms/MC120Feedback](http://aka.ms/MC120Feedback) 并在 [bugs.mojang.com](http://bugs.mojang.com/) 报告任何漏洞。

# 实验性功能

## 村民交易再平衡第2部分

此预发布更新了村民交易再平衡实验。此实验对普通世界没有影响。如果你想尝试这些更改，必须在创建新世界时在实验菜单中开启功能切换。

感谢所有提供建议和反馈的玩家！我们正在尝试这些更改以重新平衡村民交易系统，使其对每个人更公平和有趣。然而，这些更改尚未最终确定，它们将作为实验性功能保留，同时我们继续完善。感谢你对这些更改的反馈。请访问 [此链接](https://aka.ms/VillagerTradingFeedback) 分享你的想法！我们一直在关注之前图书管理员和流浪商人更新的讨论，期待看到讨论的继续。

**制图师**

以前，制图师只出售海底神殿和林地府邸的地图。在此实验中，制图师还可以出售七张新地图。这些新地图各指向不同的村庄或结构，并可用于找到七种不同的生物群系。这将帮助那些希望快速找到特定位置的玩家，而无需等待偶然遇见。

来自不同生物群系的制图师将出售不同种类的地图。从一个村庄开始，玩家可以通过一个村庄的地图找到所有其他类型的村庄。

![cartographer.png](https://feedback.minecraft.net/hc/article_attachments/19276192204301)

制图师现在出售七张新地图：沙漠村庄地图、丛林探险家地图、平原村庄地图、热带草原村庄地图、雪村庄地图、沼泽探险家地图和针叶林村庄地图。

**盔甲匠**

盔甲匠的交易已进行了多项更新。

最大的变化是，购买钻石盔甲现在需要支付少量钻石和绿宝石。这旨在使盔甲匠的钻石盔甲交易在游戏初期玩家没有钻石时不那么有用，同时仍然为已经收集了一些钻石的高级玩家提供强大的优势。

早期玩家会发现盔甲匠是铁盔甲、盾牌和绿宝石的极好来源。

其他更改包括：

- 大多数大师级盔甲匠购买铁块（并支付高价）
- 链甲盔甲只由秘密的丛林和沼泽盔甲匠出售
- 热带草原盔甲匠以较低价格出售诅咒钻石盔甲
- 针叶林盔甲匠可以将一件钻石盔甲交换为另一件

![armorer.png](https://feedback.minecraft.net/hc/article_attachments/19276175921549)

**结构战利品**

某些附魔书现在在部分结构中有较高的生成几率：

- 远古城市：修补
- 废弃矿井：效率（I到V）
- 掠夺者前哨站：快速装填（I到III）
- 沙漠神庙：耐久（I到III）
- 丛林神庙：耐久（I到III）

# 功能与漏洞修复

## 辅助功能

- 修复了文本转语音未能说明如何打开聊天或表情的问题
- 弹出窗口标题/描述的文本转语音消息现已正确播放

## 音频

- 守卫者和远古守卫者在陆地上再次发出扑通声 ([MCPE-26929](https://bugs.mojang.com/browse/MCPE-26929))
- 凋灵骷髅现在有自己的独特声音
- 更新了在音符盒上放置凋灵骷髅头颅时播放的声音
- 使用‘/give’命令时拾取物品的声音现已播放
- 流浪猫在乞讨食物时现在会播放声音
- 瓶子的更改 ([MCPE-157918](https://bugs.mojang.com/browse/MCPE-157918))
  - 从水块装满时瓶子会发出声音
  - 将水或药水从玻璃瓶倒入炼药锅时会发出适当的声音
  - 从炼药锅使用水或药水填满玻璃瓶时会发出适当的声音
  - 从玻璃瓶饮用时会发出适当的声音

## 游戏性

- 使用精准采集时，幽匿块不再掉落经验
- 僵尸村民的治疗时间现在在3到5分钟之间随机，以匹配Java版
- 修复了在灵魂沙上缓慢移动时有时导致玩家无法获得灵魂疾行移动速度的问题 ([MCPE-173155](https://bugs.mojang.com/browse/MCPE-173155))
- 玩家在创造模式下飞行并频繁按潜行键时，不再有时会穿透方块的问题 ([MCPE-172785](https://bugs.mojang.com/browse/MCPE-172785))
- 玩家使用鞘翅滑翔进入方块时，不再有时会穿透方块的问题 ([MCPE-73307](https://bugs.mojang.com/browse/MCPE-73307))
- 钢桶放置后几刻内无法再次拾取液体 ([MCPE-100598](https://bugs.mojang.com/browse/MCPE-100598))
  - 这应有助于使快速放置和取回液体更加一致，并帮助使用水桶的玩家快速避免坠落伤害
- 从高处坠落时乘坐船只不会再造成坠落伤害 ([MCPE-152753](https://bugs.mojang.com/browse/MCPE-152753))
- 坠落伤害现在由落地的实体吸收，并在坐骑死亡时传递给乘客

## 通用

- 对角线旗帜图案在应用于盾牌时不再被反转 ([MCPE-169577](https://bugs.mojang.com/browse/MCPE-169577))
- 更新了制图师出售的探险家地图上的结构图标
- 箱子方块使用状态 "minecraft:cardinal_direction" 代替 "facing_direction"，此状态使用字符串值 \["south", "west", "north", "east"\] 代替 \[0, 1, 2, 3, 5, 6\]
- 陷阱箱方块使用状态 "minecraft:cardinal_direction" 代替 "facing_direction"，此状态使用字符串值 \["south", "west", "north", "east"\] 代替 \[0, 1, 2, 3, 5, 6\]
- 末影箱方块使用状态 "minecraft:cardinal_direction" 代替 "facing_direction"，此状态使用字符串值 \["south", "west", "north", "east"\] 代替 \[0, 1, 2, 3, 5, 6\]
- 切石机方块使用状态 "minecraft:cardinal_direction" 代替 "facing_direction"，此状态使用字符串值 \["south", "west", "north", "east"\] 代替 \[0, 1, 2, 3, 5, 6\]

## 图形

- 装备的附魔盔甲现在具有整体较弱的闪光，但其强度随时间的增加和减少更为明显

## 生物

- 生物在落入1块深的水池时不再受到坠落伤害 ([MCPE-173094](https://bugs.mojang.com/browse/MCPE-173094))
- 兔子现在可以再次食用部分和完全成熟的胡萝卜作物 ([MCPE-131980](https://bugs.mojang.com/browse/MCPE-131980))

## 原版趋同

- 曾被剪羊毛且之后长回羊毛的绵羊在死亡时现在会掉落羊毛 ([MCPE-99972](https://bugs.mojang.com/browse/MCPE-99972))
- 狐狸现在可以捡起可装备的物品 ([MCPE-173898](https://bugs.mojang.com/browse/MCPE-173898))
- 关闭船、筏或运输矿车的物品栏时现在会发出振动
- 制图师在非主世界时不再作为交易物品提供探险地图
- 僵尸村民现在拥有正确的生物群系覆盖效果 ([MCPE-172377](https://bugs.mojang.com/browse/MCPE-172377))
- 将高级设置中的重生半径默认值更改为10

## 用户界面

- 点击游戏窗口外不会取消选择朋友。这也不会在重新选择朋友时为当前选中的朋友添加新的邀请
- 锻造台不再为某些槽位显示双重重叠的提示框 ([MCPE-168369](https://bugs.mojang.com/browse/MCPE-168369))
- 物品名称不再与伤害吸收生命条重叠 ([MCPE-152131](https://bugs.mojang.com/browse/MCPE-152131))
- 物品名称不再与坐骑生命条重叠 ([MCPE-152130](https://bugs.mojang.com/browse/MCPE-152130))
- 物品名称不再与氧气条重叠 ([MCPE-152129](https://bugs.mojang.com/browse/MCPE-152129))
- 更新酿造台界面，在缩放时始终保持在其背景内 ([MCPE-154385](https://bugs.mojang.com/browse/MCPE-154385))
- 修复了v-sync设置的提示框在未悬停时显示的问题

# 技术更新

## 附加包与脚本引擎

- 更改了 *CameraSetOptions* 选项的名称，以不包含“Script”一词

## 命令

- 重新进入世界后，不再在使用 "@e[type=item]" 的命令后破坏命令自动完成 ([MCPE-164734](https://bugs.mojang.com/browse/MCPE-164734))
- 带有 "override" 原因的 /damage 命令现在通过后击无敌造成伤害 ([MCPE-160290](https://bugs.mojang.com/browse/MCPE-160290))
- recipe 命令的颜色已从蓝色更改为白色 ([MCPE-173362](https://bugs.mojang.com/browse/MCPE-173362))

## 组件

- 尝试加载具有无效 "cause" 值的伤害传感器时添加内容错误
- 允许对 "minecraft:icon" 物品组件进行单值解析
- 骆驼生物的冲刺组件现在可以应用于除马、驴和骡之外的可骑乘生物，使用 “minecraft:dash”

## Molang

- Molang 更新至1.20.40版本，替换 "block_property" 和 "has_block_property" 为 "block_state" 和 "has_block_state"
  - 这是一个Molang版本变更，仅对使用最低引擎版本1.20.40或更高的附加包中的Molang表达式生效

## 交易表

- 交易物品现在有一个 "filters" 属性来决定是否应考虑该交易
- 交易物品不再支持 "biome" 属性来检查村民的生物群系类型，可以在 "filters" 属性中使用 "is_mark_variant" 过滤器来检查村民的生物群系类型

# 实验性技术更新

## 脚本API

- 添加了 *chat(message: string)* 方法
- 更改 *get* 返回类型为 *ItemType | undefined*
- 更改 *ItemDefinitionTriggeredAfterEvent* 上的 *source* 为可选项
- 向 *Player* 添加了以下方法
  - *above(steps?: number): Block | undefined;*
  - *below(steps?: number): Block | undefined;*
  - *north(steps?: number): Block | undefined;*
  - *east(steps?: number): Block | undefined;*
  - *south(steps?: number): Block | undefined;*
  - *west(steps?: number): Block | undefined;*
  - *offset(offset: Vector3): Block | undefined;*
  - *center(): Vector3;*
  - *bottomCenter(): Vector3;*
  - 使 getItemStack 函数返回 ItemStack 或 undefined
- 方块状态
  - 使 get 函数返回 BlockStateType 或 undefined
- 更新了 *ExplosionAfterEvent* 和 *ExplosionBeforeEvent*
  - *getUpdatedBlocks()* 现在将返回 *Block[]*
  - *setUpdatesBlocks(blocks: Block[])* 现在接受一个 *Block[]*
- 向 *Player* 添加了以下方法 playMusic(trackId: string, musicOptions?: MusicOptions): void; queueMusic(trackId: string, musicOptions?: MusicOptions): void; stopMusic(): void;
- 动态属性
  - 不再需要属性注册，且 *propertyRegistry* 已从 *worldInitialize* 事件中移除
  - 移除了实体或世界上可以设置的属性数量和大小的限制
  - 移除了默认值。*getProperty* 现在对于未设置的属性总是返回 undefined
  - 字符串动态属性值现在限制为32767字节长度
- 动态属性
  - 移除了函数 *removeDynamicProperty* —— 请使用 *setDynamicProperty* 并将值设为 *undefined* 来移除属性
  - 添加了函数 *getDynamicPropertyIds* —— 返回此行为包使用的实体/世界上的所有动态属性id的数组
  - 添加了函数 *getDynamicPropertyTotalByteCount* —— 返回行为包在实体/世界上所有动态属性使用的总字节数
  - 添加了函数 *clearDynamicProperties* —— 从实体/世界中移除此行为包添加的所有动态属性
- 动态属性
  - 动态属性数字现在以双精度（64位）存储
- 添加 PlayerInteractWithBlock 和 PlayerInteractWithEntity 前后事件
- 在测试版中添加 PlayerDimensionChangeBeforeEvent 和 PlayerDimensionChangeAfterEvent

## 图形

- 灵魂火把现在在延迟技术预览中被视为点光源
- 允许通过资源包在延迟技术预览中驱动任何方块的点光源及其颜色

## 稳定性与性能

- 在延迟技术预览中改善了区块渲染性能

## 用户界面

- 修复了在使用延迟技术预览时，“PBR”未包含在HUD中的错误

# 结语

感谢您参与Minecraft的测试版与预览版！您的反馈对于我们改进游戏至关重要。请继续分享您的意见和建议，让我们一起打造更好的Minecraft世界！