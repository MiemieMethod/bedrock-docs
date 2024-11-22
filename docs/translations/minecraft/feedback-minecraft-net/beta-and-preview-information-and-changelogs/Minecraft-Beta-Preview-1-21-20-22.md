---
title: Minecraft Beta & Preview - 1.21.20.22
date: 2024-07-10T12:02:41Z
updated: 2024-07-10T14:36:39Z
categories: Beta and Preview Information and Changelogs
link: https://feedback.minecraft.net/hc/en-us/articles/28289283945869-Minecraft-Beta-Preview-1-21-20-22
hash:
  h_01J2EGQQKSK41633S8SD8SVD5M: features-and-bug-fixes
  h_01J2EGQQKSCX0ZTMGP8Q3XDW1M: accessibility
  h_01J2EGQQKSG7EKZDE6B3YPQAAD: blocks
  h_01J2EGQQKTQZKA19B7G74Q7BZZ: game-tips
  h_01J2EGQQKT9TSTXAVN16GZ9CCD: gameplay
  h_01J2EGQQKTS133E0AFCW5QVM1A: split-screen
  h_01J2EGQQKTRM3BCAMCX9CKMVX7: general
  h_01J2EGQQKTA7TYKYGT95EDD9H6: graphical
  h_01J2EGQQKTR918WV1BKNDQ3558: maps
  h_01J2EGQQKTP7ZB9P5DEPW8JFT1: mobs
  h_01J2EGQQKTGSJCBFHTE8QSFDG7: ominous-vault
  h_01J2EGQQKTTJYFJJW9T90ZEYRR: realms-invite-links
  h_01J2EGQQKTN4GCGR0X3AMTFK2M: realms-stories
  h_01J2EGQQKTD7AH81MWENBPRSVK: user-interface
  h_01J2EGQQKTP67EA7F53DK5GQ7M: technical-updates
  h_01J2EGQQKTFWJJNHCMJQE4GBC6: api
  h_01J2EGQQKTZGM02TMDAQ5M67GV: blocks-1
  h_01J2EGQQKTJEJDYEFXFX52CTFE: commands
  h_01J2EGQQKT4D96RT3HB7X37TR1: editor
  h_01J2EGQQKT3Q0HSF2JH1VWFNPN: entity-components
  h_01J2EGQQKTG0ZDAKVE7HVSFTGY: entity-filters
  h_01J2EGQQKT4ZMMMRREPS9ACN59: gameplay-1
  h_01J2EGQQKTN6QETW8PRGGKEFQ2: general-1
  h_01J2EGQQKTZHCMK80FVCP7RMSS: items
  h_01J2EGQQKTK3E3AXK1H4XQ1DK8: technical-experimental-updates
  h_01J2EGQQKTA709524890NB50KJ: api-1
  h_01J2EGQQKT6NP0QXRQFGPVS0M5: graphical-1
---

**发布于:** 2024年7月10日

**关于Minecraft预览版和测试版的信息:**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 了解详细说明

![在延迟技术预览中，带有更新的水和反射效果的Minecraft截图](https://feedback.minecraft.net/hc/article_attachments/28289283931661)

Minecraft预览版和测试版正在推出，带来了更多的调整和漏洞修复！以下是本周的新内容列表：

# 功能和漏洞修复

## 辅助功能

- 修复了屏幕朗读在Android和iOS上无法描述如何接受游戏邀请的问题
- 用户界面中的文本转语音现在可以通过悬停、点击或导航到各自的标题和段落来朗读如何进行游戏的屏幕

## 方块

- 活板门和栅栏门在被红石激活时不再推动玩家或生物
- 添加了VanillaBlockTag "one_way_collidable"，可用于模拟门、活板门和栅栏门的单向碰撞，当生物在其碰撞箱内时不会被推开
- 缠根泥土方块现在具有独特的声音，以更好地匹配Java版 ([MCPE-121664](https://bugs.mojang.com/browse/MCPE-121664))
- 铜门的“开启”声音现在调整了音调
- 损坏的铁砧方块现在可能会在古迹废墟中生成，就像在Java版中一样
- “铁砧”方块现在分为独立的实例：“铁砧”、“有缺口的铁砧”、“损坏的铁砧”、“废弃的铁砧”
- “石英块”现在分为独立的实例“石英块”、“雕刻石英块”、“石英柱”和“平滑石英块”
- 平滑石英块的破坏时间已调整以匹配Java版 ([MCPE-101893](https://bugs.mojang.com/browse/MCPE-101893))
- 石英柱方块已重命名为石英柱
- “红砂岩”方块现在分为独立的实例“红砂岩”、“雕刻红砂岩”、“切割红砂岩”和“平滑红砂岩”
  - “平滑红砂岩”的破坏时间从0.8更改为2.0
- “泥土”方块现在分为独立的实例：“泥土”和“粗糙泥土”
- “沙子”方块现在分为独立的实例“沙子”和“红沙”

## 游戏提示

- 添加了一个游戏提示，告知触摸设备上的玩家正在潜行，以避免新玩家卡在蹲伏状态
- 对现有游戏提示进行了一些小的提示中断改进

## 游戏玩法

- 修复了在快速移动时将火把物品从物品栏转移到快捷栏时图标暂时错位的问题 ([MCPE-180913](https://bugs.mojang.com/browse/MCPE-180913))
- 在卸载时，骑乘的坐骑和载具不再获得轻微的速度

## 分屏

- 修复了分屏时卸载的生物动画未播放的问题

## 通用

- 修复了一个问题，确保在创建或开始世界之前正确导入Marketplace内容
- 传统世界在世界边缘不再有未渲染的区块

## 图形

- 修复了迷雾JSON验证，允许max_density_height和zero_density_height值的范围从(-64,320)

## 地图

- 修复了结构图标或其他地图装饰在无限跟踪的地图边缘上不可见的问题，例如试炼探险家地图 ([MCPE-182681](https://bugs.mojang.com/browse/MCPE-182681))

## 生物

- 沼骸在骑乘船、筏或矿车时不再漂浮 ([MCPE-178876](https://bugs.mojang.com/browse/MCPE-178876))

## 不祥宝库

- 不祥宝库中的稀有战利品掉落概率现为80% ([MCPE-180654](https://bugs.mojang.com/browse/MCPE-180654))

## Realms邀请链接

我们正在对Realms邀请链接的工作方式进行一些更改，以使邀请朋友变得比以往任何时候都更容易，并保持您的Realms免受不受欢迎的加入者的侵害：

- 每个Realms现在最多可以创建5个邀请链接
- 邀请链接可以随时启用或禁用，或设置为将来的某个过期日期
- 邀请链接可以被完全删除
- 新创建的邀请链接代码将为15个字符长（从11个字符增加）
- 现有的预览Realms将保留其现有的邀请链接，但所有新的预览Realms将默认从0个邀请链接开始

**Realms漏洞修复**

- 修复了Realms按钮在不应存在时仍然存在或在应出现时未显示的问题
- 修复了一个错误，在取消加入最近声称的预览Realm的过程后，会将玩家锁定在无限循环中
- 修复了一个错误，导致刚安装Minecraft的玩家需要重新启动才能看到Realms故事

## Realms故事

- 清理了在分屏模式下作为第二个用户玩游戏时暂停屏幕上禁用的Realms故事按钮界面

## 用户界面

- 从2人Realms订阅中移除了不必要的警告
- 修正了在新播放屏幕上按“加入Realm”不会进入空虚的问题
- 新的就寝屏幕现在在按下键盘的ESC键时取消睡眠 ([MCPE-183434](https://bugs.mojang.com/browse/MCPE-183434))

# 技术更新

## API

- 修复了在Air方块物品上调用*getTags*方法时导致*Item Stack*崩溃的问题
- 维度
  - 将方法*getTopmostBlock*从*beta*发布到*1.13.0*
  - 将接口*VectorXZ*从*beta*发布到*1.13.0*

## 方块

- 资源包中找到的“blocks.json”文件现在有版本控制
  - 使用1.20.50或更高的format_version覆盖“石头”方块时，将假定terrain_texture.json中的纹理数据已被展平，不使用数组
  - 使用1.21.10或更高的format_version覆盖“海晶石”方块时，将假定terrain_texture.json中的纹理数据已被展平，不使用数组
  - 使用1.21.20或更高的format_version覆盖“铁砧”、“石英块”、“红砂岩”、“沙子”和“砂岩”方块时，将假定terrain_texture.json中的纹理数据已被展平，不使用数组
- “寄生石头”及其衍生物现在定义了它们的方块声音 ([MCPE-182290](https://bugs.mojang.com/browse/MCPE-182290))

## 命令

- /locate structure命令现在使用命名空间结构名称。未提供命名空间的结构名称将假定为“minecraft”命名空间 ([MCPE-151807)](https://bugs.mojang.com/browse/MCPE-151807)

## 编辑器

编辑器及其相应的API处于早期开发阶段，可在Windows PC基岩预览版构建的键盘/鼠标上使用。在社交媒体上使用**#BedrockEditor**标签与我们互动。

了解[如何使用](https://aka.ms/LearnEditor)编辑器，加入[GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions)论坛与团队交流，并通过[启动套件](https://github.com/Mojang/minecraft-editor-extension-starter-kit)和[示例](https://github.com/Mojang/minecraft-editor-extension-samples)开始构建扩展。

本周更新：

- 更新了编辑器选择器中出现的方块和实体集
- 添加了“附加调试器”ActionBarItem快捷方式，用于附加到脚本调试器
- 实现了用于实体删除/创建的单实体事务负载
- 实现了单实体创建和删除的撤销/重做
- 添加了*isFloat*以支持*addNumber*编辑器属性窗格API中的浮点值
- 为日志面板消息添加了复制到剪贴板按钮
- 在延迟照明属性编辑器下拉菜单中添加了本地化的字段名称
- 向延迟照明属性编辑器添加了全局照明设置
- 修复了在编辑器中启用延迟照明时导致视觉伪影的问题
- 从API中移除了备用显示文本属性，改为使用单一本地化属性
  - 向*IDropdownItem* API添加了*label*属性，移除了*displayAltText*和*displayStringId*属性
  - 向*IMenuCreationParams* API添加了*label*属性，移除了*name*和*displayStringId*属性
  - 向*IPropertyItemOptions*和*IPropertyItem* APIs添加了*title*属性，移除了*titleAltText*和*titleStringId*属性
  - 向*ModalToolCreationParameters* API添加了*title*和*tooltip*属性，移除了*titleAltText*、*titleStringId*、*tooltipAltText*和*tooltipStringId*属性

## 实体组件

- 添加了“behavior.teleport_to_owner”目标，允许实体传送到其所有者
  - 该目标旨在紧急情况下使用，当“behavior.follow_owner”速度过慢或优先级过低时
  - “filters”字段允许使用实体过滤器定义传送的条件
  - “cooldown”字段允许定义实体尝试传送的频率
- *minecraft:behavior.move_away_from_target*已重命名为*minecraft:behavior.move_around_target*，以更好地描述该目标的作用，因为它既可以用于远离目标移动，也可以用于向目标周围的随机位置移动

## 实体过滤器

- 添加了新的实体过滤器“owner_distance”，用于检查实体与其所有者的距离

## 游戏玩法

- 通过添加*Trigger Type*修改了*ItemUseInventoryTransaction*数据包。这个新值告诉我们数据包是来自直接的玩家输入还是按钮被按住时的模拟刻

## 通用

- 由于缺少内容而无法加载的实体现在将保留在存档内。这些实体将在缺少的内容可用时重新出现（例如移除并重新应用附加包）

## 物品

- 在“slot.weapon.offhand”槽位中使用“minecraft:wearable”并将“minecraft:allow_off_hand”设置为false，现在将导致内容错误

# 技术实验性更新

## API

- 摄像机
  - 在beta中向*setCamera*函数的选项中添加了`CameraFixedBoomOptions`.

CameraFixedBoomOptions

- 新接口已添加到beta
- 仅在启用第三人称摄像机预设切换时，允许自定义*minecraft:follow_orbit*摄像机
- 引入了`viewOffset?: Vector2`。此属性允许您更改摄像机相对于玩家的偏移，以创建肩膀后方的效果

## 图形

- 扩展了TextureSet的功能，以支持Deferred Technical Preview中的物品。详情请参阅创建者门户上的更新文档。
- 为Deferred Technical Preview中的水添加了新的生物光学照明模型。自定义和数据驱动水的能力将在未来的更新中提供
  - 已知问题：水面下8个区块处存在体积边界，当摄像机穿过时会产生强烈的照明过渡
  - 已知问题：瀑布或狭窄的水体可能难以看到
- 为Deferred Technical Preview添加了屏幕空间反射。这些反射作为Deferred图形设置菜单中反射质量滑块的一部分包含。在移动设备上，屏幕空间反射仅在运行超高设置时可用。详情请参阅创建者门户上的更新文档。
- 修复了iOS上的一个错误，导致Deferred Technical Preview中的图形行为未定义（例如无点光源或照明过度）
- 修复了一个伽玛校正错误，导致蜡烛、玻璃、冰、蜂蜜、史莱姆、信标、炼药锅和传送门的纹理在Deferred Technical Preview中过于明亮