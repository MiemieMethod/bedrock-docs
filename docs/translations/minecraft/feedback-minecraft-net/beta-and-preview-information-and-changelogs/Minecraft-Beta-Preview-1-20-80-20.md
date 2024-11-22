---
title: Minecraft 测试版与预览版 - 1.20.80.20
date: 2024-02-27T21:03:06Z
updated: 2024-02-29T16:59:31Z
categories: 测试版与预览版信息及更新日志
link: https://feedback.minecraft.net/hc/zh-cn/articles/24509955193229-Minecraft-Beta-Preview-1-20-80-20
hash:
  h_01HQSPSHHCPXMEFPRX1KW1CZGR: experimental-features
  h_01HQSPSHHCF0QBS5RPTHTXSW1R: vault
  h_01HQSPSHHCZ7FNT1BXQ22BCCX9: trial-chambers
  h_01HQSPSHHCSB81QE441P4P1M8C: coming-soon-hardcore-mode
  01HQTWSQVF9W23M0A63RBXJBW9: features-and-bug-fixes
  h_01HQSPSHHCPZ30ZMHC5TE91QVJ: wolf-armor
  h_01HQSPSHHC62AQPE16850YFP1A: wolves
  h_01HQSPSHHCCFP3ANEQSBAYE4ZD: armadillo
  h_01HQSPSHHCQABC4A3W0CZW236S: blocks
  h_01HQSPSHHCVVASWD9A46SVC3B3: gameplay
  h_01HQSPSHHCCY1R9S0YVTKW42YE: realms-stories
  h_01HQSPSHHDESNM5WV6CTSH7P9N: user-interface
  h_01HQSPSHHD7CET4AV34GCEPG7Z: technical-updates
  h_01HQSPSHHD3JVE61YHXDF66QB0: api
  h_01HQSPSHHDHAH7QEFQCP4G3VNT: blocks-1
  h_01HQSPSHHDDBG80PED3GXA1161: cameras
  h_01HQSPSHHD7WBP99WJX4F7KRFG: components
  h_01HQSPSHHDNQZ4HXEDHY85WWTT: editor
  h_01HQSPSHHDXWM2AP0Z6FYDXRW9: entity-filters
  h_01HQSPSHHD74N5HWFC1N4JXFSS: molang
  h_01HQSPSHHDX72PTWFJQ2YQ8RBT: stability-and-performance
  h_01HQSPSHHDK9YBBEJNNZMRE8WF: experimental-technical-updates
  h_01HQSPSHHD4Y509Q0238JE1RDF: blocks-2
  h_01HQSPSHHDZGGCE7FDCE69575K: commands
  h_01HQSPSHHD56839ABXJDQ7BFVK: graphical
  h_01HQSPSHHDS9F8RD202A4RCEB0: api-1
---

**发布于：** 2024年2月29日  
    
    
**Minecraft 预览版与测试版信息：**
    
- 这些开发中版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft 预览版可在 Xbox、PlayStation 4、Windows 10/11 和 iOS 设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在 Android（Google Play）上使用。加入或退出测试版，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明
    
![patchnotes_u8-1.png](https://feedback.minecraft.net/hc/article_attachments/24554985642253)
    
本周的预览版和测试版更新内容繁多，我需要一个代码来记住所有内容。如何使用“狼铠-犰狳”呢？因为在本周的预览版和测试版中，你不仅会发现更新后的狼铠（更强大！可修复！且非常酷！），还可以将其染成任何你想要的颜色。如果这还不够，犰狳已经取消实验化（确实是一个词），我们也已迈出了朝着令人兴奋的方向工作的第一步（下文会详细说明）。这就是所有内容吗？也许我应该列一个清单，而不是使用代码。无论如何！一如既往，我们希望听到你的想法和反馈，请在[这里](https://feedback.minecraft.net/)告诉我们你的意见，并在[bugs.mojang.com](https://bugs.mojang.com/)报告你遇到的任何漏洞。  
    
**已知问题：** 在此版本中，玩家无法连接到 Xbox One 和 PlayStation 4 上的预览版宝库（Realms）。
    
# 实验性功能
    
## Vault
    
- Vault 的击中声音音调已修正，以匹配 Java 版
- 更新了 Vault 的视觉效果
    
## 试炼密室
    
- 试炼密室现在将与 Java 版在相同的位置和配置中生成
    
## 即将推出：极限模式
    
我们很高兴地宣布，我们正在为基岩版开发极限模式，并希望在春季某个时候可以进行测试。极限模式是生存模式的一个子类别，玩家只有一次生命，且没有重生的机会。不仅如此，在极限模式中，难度被锁定为最高设置！
    
在如此高的风险下，我们希望在将极限模式发布到基岩版的零售版之前，确保其正确无误，因此一旦进入测试阶段，它将保留在预览版中，直到我们对玩家和创造者的体验顺畅感到信心。你将能够通过在 [bugs.mojang.com](https://bugs.mojang.com/) 提交漏洞，并在 [Discord](https://discord.com/invite/minecraft) 或 [feedback.minecraft.net](http://feedback.minecraft.net/) 提供反馈来帮助我们测试极限模式！
    
我们也很高兴地宣布，当准备就绪时，极限模式将同时在 Java 和基岩版的宝库（Realms）中提供。
    
# 功能与漏洞修复
    
## 狼铠
    
自狼铠初次发布以来，我们一直致力于改进其保护性、可用性并增加定制功能。为了保护，采用了一种新的铠甲方法，考虑到玩家需要快速查看铠甲状态而无需使用 UI 元素，并能在需要时快速帮助它们的宠物狼。
    
- 狼铠已取消实验化，现在可在正常游戏中使用
- 狼铠现在可以染色
- 狼铠现在充当盾牌，吸收大部分针对狼的伤害：
  - 狼铠现在具有 64 点耐久
  - 狼铠在受到更多伤害时会出现更多裂缝
  - 如果狼铠受到超过 0 耐久的伤害，它将破损
  - 但不用担心，狼铠现在可以使用犰狳鳞甲在坐着的狼上修复
- **已知问题：**
  - 装备狼铠的狼不会触发伤害后无敌时间，导致狼铠因持续伤害来源（如熔岩、史莱姆和岩浆怪）迅速破损
    
## 狼
    
- 驯服狼的项圈现在正确阴影显示 ([MCPE-178351](https://bugs.mojang.com/browse/MCPE-178351))
- 狼的尾巴在坐着时现在正确定位 ([MCPE-31121](https://bugs.mojang.com/browse/MCPE-31121))
    
## 犰狳
    
- 犰狳已取消实验化，现在可在正常游戏中使用
- 繁殖冷却时间在卷起后不再重置
- 即使在实验开启时，蜘蛛和洞穴蜘蛛现在也会害怕犰狳 ([MCPE-178887](https://bugs.mojang.com/browse/MCPE-178887))
    
## 方块
    
- 甜浆果丛在使用附有时运的工具开采时现在最多掉落 6 颗甜浆果 ([MCPE-172622](https://bugs.mojang.com/browse/MCPE-172622))
- 成熟的可可豆荚现在稳定掉落 3 颗可可豆
- 当堆叠两个相同的台阶时，现在可以再次创建双台阶 ([MCPE-179187](https://bugs.mojang.com/browse/MCPE-179187))
    
## 游戏玩法
    
- 修复了驯服的生物在传送到其主人后，从客户端/来宾的视角看其垂直位置的问题 ([MCPE-139168](https://bugs.mojang.com/browse/MCPE-139168))
- 骑乘或下船时，马和船不再滑向意外的先前位置
    
## 宝库故事
    
- 修复了宝库故事按钮在游戏屏幕上失去焦点的问题
- 成员和时间线标签现在限制最多渲染 300 名宝库玩家，以避免大型宝库的性能问题。所有玩家仍然可以在成员标签中搜索
- 添加新故事时，玩家离开添加故事屏幕时文本框不再被清空。实质上，玩家可以保存他们的故事草稿
- 发布宝库故事时，只有当前在由宝库托管的游戏中游玩的玩家头像才会显示在线徽章
- 修复了宝库故事“选择加入”屏幕有时显示破损的视觉效果的问题
- 修复了再次选择同一截图时会取消选择截图而不是保持选中状态的错误
- 为宝库故事“选择加入”屏幕添加了屏幕阅读器旁白
- 为时间线标签添加了信息按钮
- 更新了某些宝库故事设置的描述文本
- 在故事提要标签上添加了未读故事指示器
- 在 Minecraft 的“如何游玩”部分添加了宝库故事页面
    
## 用户界面
    
- 反馈按钮已从主菜单移动到设置屏幕的常规标签下，标签为“帮助中心”
- 在常规部分的设置中添加了启用/禁用游戏提示的切换按钮和重启提示的按钮
- 增加了显示标准加载提示的时间间隔
- 在设置/存储屏幕中添加“导入零售世界”按钮
- 增加了“上移”按钮的范围，现在你可以慢慢滑动到附近的按钮而不会停止移动 ([MCPE-178399](https://bugs.mojang.com/browse/MCPE-178399))
- 在新的游玩屏幕中导入的世界现在在“（导入）”后缀前有一个空格（仅预览）
- 在触摸设备上，当交换物品时，图标现在会朝正确的方向移动
- 合成器输出槽中现在正确渲染自定义饰纹陶罐和染色旗帜
- 在触摸设备上，所选物品现在在所有屏幕上都有蓝色背景
- 蜂巢、制图台和锻造台屏幕的触摸屏版本中飞行动画不再缺失  
    
# 技术更新
    
## API
    
- 移除了*EntityHealableComponent.filters*，因为它们目前没有后端实现
- 修复了一些组件*isValid*方法，这些方法在组件从实体中移除时未能正确返回false
- 在*beta*中添加了*PaletteColor*枚举，用于*ItemColorComponent/ItemColor2Component*
- 在*beta*中添加了*ItemColor2Component*，用于读取*minecraft:color2*
- 使用大于32kb键设置动态属性现在将导致异常
    
## 方块
    
- “sapling”方块现在分为独特的实例：“oak_sapling”、“spruce_sapling”、“birch_sapling”、“jungle_sapling”、“acacia_sapling”和“dark_oak_sapling”。
- “coral_fan”方块现在分为独特的实例：“tube_coral_fan”、“brain_coral_fan”、“bubble_coral_fan”、“fire_coral_fan”和“horn_coral_fan”
    
## 摄像机
    
- 添加了“extend_player_rendering”摄像机组件，允许玩家（及通过骑乘和牵引连接的任何实体）即使在超出最大实体渲染距离时也进行渲染
- 将“extend_player_rendering”组件添加到“minecraft:free”摄像机
  - 此组件旨在增强和改进当前功能，因此默认设置为“true”
  - 将此组件设置为false将移除新增的渲染能力。文档将在发布前更新
- 服务器现在会向客户端发送摄像机周围的区块和活动对象（如果这些信息已存在于服务器上），即使摄像机放置在远离玩家的位置
    
## 组件
    
- “interact”组件的字段“equip_item_slot”和“drop_item_slot”现在支持铠甲槽和物品栏槽：
  - 铠甲槽指定为‘slot.armor.head’、‘slot.armor.chest’、‘slot.armor.legs’和‘slot.armor.feet’
  - 物品栏槽指定为正数，现在以字符串形式表示
  - 此更改需要世界版本为1.20.80或更高
- 在“interact”组件中添加了“repair_entity_item”字段，允许修复实体的物品栏或铠甲槽中的物品
    
## 编辑器
    
- 在属性窗格中添加了addImage支持
- 为IPropertyItemOptionsButton API添加了图标属性，以在按钮中显示图标
- 添加了WidgetManager和CustomWidget的概念——允许服务器实例化世界内的小部件，这应有助于操作世界工具。我们目前仅支持CustomWidgets（由服务器驱动的自定义实体）
- 调整了默认编辑器 UI 缩放，以优化屏幕空间
    
## 实体过滤器
    
- 添加了新的实体过滤器“is_sitting”，用于检查实体是否在坐着
- 添加了新的实体过滤器“has_damaged_equipment”，用于检查实体在指定槽位中是否有某个损坏的装备
    
## Molang
    
- 添加了新的查询“query.armor_slot_damage”，返回指定槽位中的铠甲物品的损坏值
    
## 稳定性与性能
    
- 移除了*FilterTextPacket*  
    
# 实验性技术更新
    
## 方块
    
- 在测试版 API 功能标志下添加了‘minecraft:custom_components’方块组件
    
## 命令
    
- 修复了/hud 命令，使更改仅影响目标玩家
    
## 图形
    
- 部分修复了在延迟技术预览中在资源包中标记为点光源的全块形状（例如红石灯、蛙明灯、荧石等）。它们仍然可以被转化为点光源，但不会有遮挡/阴影
- 在延迟视频设置菜单中为点光源阴影添加了专用的质量滑块
- 在延迟技术预览的照明模型中添加了新功能：次表面散射。此效果模拟光线穿过半透明表面的情况。目前，此功能仅影响树叶
- 增加了延迟技术预览中世界的对比度和饱和度
    
## API
    
- 方块自定义组件 – 见 [https://learn.microsoft.com/minecraft/creator/Documents/CustomComponents](https://learn.microsoft.com/minecraft/creator/Documents/CustomComponents)
  - 在*beta*中添加了*BlockComponentStepOnEvent*
  - 在*beta*中添加了*BlockRegistry*
  - 添加了*WorldInitializeBeforeEvent*
  - 添加了*BlockCustomComponent*
- 创作者设置菜单新增了一个选项，可在世界加载（或/reload）时自动连接调试器。这将使设置（和捕捉）加载时的断点更加容易，并避免输入调试器斜杠命令的麻烦
- 添加了类*ListBlockVolume*，扩展自*BaseBlockVolume*——一个存储多个方块位置的体积
- 结构
  - 将类*StructureTemplate*重命名为*Structure*
  - 添加了只读属性*size: Vector3*——返回结构在区块中的大小
  - 添加了函数*getBlockPermutation(location: Vector3): BlockPermutation | undefined;*——返回结构中给定位置的方块排列
  - 添加了函数*isValid(): boolean*——如果结构已被删除，则返回false
  - 添加了函数*getIsWaterlogged(location: Vector3): boolean;*——返回给定位置的方块是否含水