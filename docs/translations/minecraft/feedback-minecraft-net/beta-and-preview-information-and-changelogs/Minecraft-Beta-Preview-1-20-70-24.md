---
title: Minecraft Beta & 预览 - 1.20.70.24
date: 2024-02-15T12:37:44Z
updated: 2024-02-16T09:35:27Z
categories: Beta 和 预览信息与更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/24139781551117-Minecraft-Beta-Preview-1-20-70-24
hash:
  h_01HPPG8XE6PEBHP6K6M5DGQMRH: 关于Minecraft预览和Beta的信息
  h_01HPPCAHC3Q1ST8CJJJYXBG7ZE: 实验性特性
  h_01HPPCAHC3B7B55KR84FZFRQGK: 风弹
  h_01HPPCAHC3J4FNWPJSB205TT7H: 沼骸
  h_01HPPCAHC321NAN6CT9ANBG6E2: 旋风人
  h_01HPPCAHC3SFZ2TH38H10ZE7DH: 试炼密室
  h_01HPPCAHC3G03ZW6E506XRJHT0: 漏洞修复
  h_01HPPCAHC3RD55EK4KNPW6P1T5: 特性与漏洞修复
  h_01HPPCAHC3JRE41EF2RKST6ETV: 方块
  h_01HPPCAHC3QMQ5ZDQT5TNHW9N1: 命令
  h_01HPPCAHC387625PRAHXH67H7C: 游戏提示
  h_01HPPCAHC3SKEGEBSQ68THWW05: 领域
  h_01HPPCAHC3RNKZ1VSQ363WY829: 稳定性与性能
  h_01HPPCAHC3MK5DA1FED2YSWAPB: 用户界面
  h_01HPPCAHC3TDXVYDM66PAZSY1A: 技术更新
  h_01HPPCAHC37W4Y2S2GEPJEMMT9: 附加包与脚本引擎
  h_01HPPCAHC3TH89E8ZZXV7FRCGP: 编辑器
  h_01HPPCAHC4YEQPM7B4MARGW7BQ: 市场服务器驱动布局SDL
  h_01HPPCAHC4W1A3H4J51TTDC59X: 角色创建器
  h_01HPPCAHC431AT9CTVQKH9DX4Z: 稳定性与性能1
  h_01HPPCAHC472ET87S60HTQFT4T: 实验性技术更新
  h_01HPPCAHC44TA8GHJ16JT5XEV4: API
---

**发布于：** 2024年2月15日

## **关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版可在Android（Google Play）上使用。要加入或退出Beta，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明

*![凯在红树林沼泽中使用风弹对抗沼骸。他们在主世界的传送门遗迹附近战斗。](https://feedback.minecraft.net/hc/article_attachments/24141679587853)*

*呼啸*! 你听到那个声音了吗？不，那不是毒箭的声音（稍后会详细介绍）——那是风弹的声音，今天将加入基岩版预览和Beta。风弹是一种物品，让你能够利用旋风人的一些力量——比如能够跳得更高，并向敌人发射风的冲击波，造成冲击伤害 *和* 击退。风弹由被击败的旋风人掉落，我将使用我的风弹直接跳向：沼骸！沼骸是一种新的敌对生物，可以在试炼密室中生成，使用毒药药箭进行攻击。沼骸的生命值可能略低于它们的骷髅表亲，但它们在伤害上可不容小觑！面对沼骸，测试新的风弹以及更多内容，尽在今天的Minecraft：基岩版预览和Beta中。

以下是新内容的列表。我们始终欢迎你的反馈，请在[这里](https://aka.ms/mcvaultsfeedback)告诉我们你的想法，并在[bugs.mojang.com](https://bugs.mojang.com/)报告你可能遇到的任何漏洞。

# 实验性特性

## 风弹

- 成为旋风人！使用风弹将发射出类似于旋风人发射的风弹投射物
- 玩家发射的风弹将比旋风人发射的风弹多10%的击退效果
- 就像旋风人发射的投射物一样，玩家发射的风弹如果直接击中实体也会造成伤害
- 击败旋风人时会掉落4-6个风弹
- 风弹的最大堆叠数量为64
- 每次使用后有半秒的冷却时间
- 风弹可以从发射器中发射
- 玩家使用风弹发射时，只有在与风爆碰撞的y轴以下才会累积掉落伤害

## 沼骸

- 一种新的骷髅变种，发射毒药箭
  - 生命值为16，比20的骷髅更容易击败
  - 攻击间隔为3.5秒，而不是2秒，攻击速度较慢
- 被玩家击杀时有机会掉落毒药箭
- 这些覆盖着苔藓和蘑菇的骷髅自然生成于沼泽和红树林沼泽
  - 也可以在某些试炼密室中从试炼刷怪笼中生成

## 旋风人

- 为风弹投射物添加了缺失的翻译字符串 ([MCPE-176968](https://bugs.mojang.com/browse/MCPE-176968))
- 旋风人在被风弹投射物击中时现在会受到伤害

## 试炼密室

- 试炼密室现在在与Java版相同的世界位置生成

## 漏洞修复

- 骷髅、僵尸、尸壳、蜘蛛、洞穴蜘蛛和流浪者再次会对彼此的攻击进行反击 ([MCPE-178560](https://bugs.mojang.com/browse/MCPE-178560))
  - 此外，当被旋风人发射的风弹击中时，它们会正确地不进行反击

# 特性与漏洞修复

## 方块

- 从创造模式物品栏中取出的无图案旗帜在首次放置时将不再重置 ([MCPE-178327](https://bugs.mojang.com/browse/MCPE-178327))
- 高大的花朵不再受到时运的影响 ([MCPE-18880](https://bugs.mojang.com/browse/MCPE-18880))
- 大型蕨现在有机会掉落小麦种子 ([MCPE-126947](https://bugs.mojang.com/browse/MCPE-126947))
- 调整了西瓜、红石矿石、荧石和下界疣的时运附魔掉落分布，以更好地匹配Java版

## 命令

- 命令方块的界面现在将在成功编译命令后移除最后一条错误消息 ([MCPE-114029](https://bugs.mojang.com/browse/MCPE-114029))

## 游戏提示

- 添加了逐步推出的上下文初学者游戏提示

## 领域

- 修复了在触发领域事件后访问领域故事时可能导致的随机崩溃，原因是添加新的故事状态条目与俱乐部动态排序之间的竞争条件
- 为领域故事添加了新的加载屏幕提示
  - 已知问题：新提示在Android Beta上无法使用
- 更改了Xbox平台上领域故事隐私和在线安全模态，以显示二维码而不是链接

## 稳定性与性能

- 修复了在某些平台上更改语言时可能导致游戏冻结的问题

## 用户界面

- 当资源包应用于世界时，新死亡屏幕现在已启用（仅限预览）
- 修复了在显示“加载资源包”模态时游戏可能出现软锁定的问题

# 技术更新

## 附加包与脚本引擎

- 使用“minecraft:material_instances”组件且“render_method” = “alpha_test_single_sided”的方块在玩家手中正确显示

## 编辑器

编辑器及其相应的API处于早期开发阶段，并可在Windows PC基岩预览版构建中使用键盘/鼠标。请在社交渠道上标记我们 **\#BedrockEditor.**

了解[如何使用](https://aka.ms/LearnEditor)编辑器，加入[GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions)论坛与团队互动，并通过[入门工具包](https://github.com/Mojang/minecraft-editor-extension-starter-kit)和[示例](https://github.com/Mojang/minecraft-editor-extension-samples)开始构建扩展。

本周更新：

- 修复了状态栏中光标增量显示的负号错误
- 为编辑器远程面板的TextComponent添加了'border: true\|false'选项
- 在Playtest对话框的信息部分添加了文本组件
- 在扩展上下文中创建了一个“blockPalette”服务，包含“getSelectedBlockType”和“setSelectedBlockType”。这将用于存储将要涂抹到世界中的方块类型。选择、立方体刷和线条工具已更新为使用此服务！
- 添加了一个有状态菜单以在世界选项中切换主世界天气。

## 市场服务器驱动布局（SDL）

- 添加了SDL屏幕具有不可滚动布局的能力
- 添加了布局包含垂直填充边距的能力
- 修复了用户界面中垂直工厂内的垂直填充对象无法正常工作的问题

## 角色创建器

- 添加了一个新模型以包含角色创建动画逻辑
- 更新了触发更新绑定的逻辑，以便在动画状态更新时不会出现每帧更新绑定导致的重大帧率下降问题

## 稳定性与性能

- 实施了针对“单块天空岛”市场地图在客户端生成平坦世界的问题修复，如果地图是在领域上传的
  - 连接到专用服务器或领域的客户端将不再错误生成LevelChunks，如果以下任一条件为真：
    - 地图是平坦世界
    - 它是市场地图
  - 这将覆盖专用服务器的server.properties设置client-side-chunk-generation-enabled

# 实验性技术更新

## API

- 添加函数 *createEmpty(identifier: string, size: Vector3, saveMode?: StructureSaveMode): StructureTemplate* - 创建一个新的空结构
- 添加函数 *createFromWorld(identifier: string, dimension: Dimension, blockVolume: BlockVolume, options?: StructureCreateOptions): StructureTemplate* - 从世界中的方块创建一个新结构
- 添加函数 *delete(structure: string \| StructureTemplate): boolean* - 删除结构
- 添加函数 *get(identifier: string): StructureTemplate \| undefined* - 获取具有指定标识符的结构
- 添加函数 *place(structure: string \| StructureTemplate, dimension: Dimension, location: Vector3, options?: StructurePlaceOptions)* - 在世界中放置结构