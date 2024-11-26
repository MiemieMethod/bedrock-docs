---
title: Minecraft Beta - 1.16.200.52 (Xbox One/Windows 10/Android)
date: 2020-10-28T15:41:45Z
updated: 2020-10-28T16:53:19Z
categories: Beta和预览信息及更新日志
tags:
  - beta
  - beta_changelog
link: https://feedback.minecraft.net/hc/en-us/articles/360051234492-Minecraft-Beta-1-16-200-52-Xbox-One-Windows-10-Android
---

请在参与Minecraft Beta之前阅读：

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的先前版本中打开，因此请务必备份世界以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参阅[ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![img_507.JPG](https://feedback.minecraft.net/hc/article_attachments/360074360472/img_507.JPG)

我们非常高兴在本周的基岩测试版中为您提前展示一些即将到来的洞穴与山崖特性！

我们希望了解您的想法，因此请通过[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)向我们反馈 - 我们将在稍后添加新主题，以便开始测试为未来的洞穴与山崖版本准备的新特性。和往常一样，如果您能在[bugs.mojang.com](https://bugs.mojang.com/)上搜索并报告任何漏洞，我们将非常感激 - 谢谢！

# 新特性：

### **新的实验性特性**

在本测试版中，我们将开始使用新的实验性特性开关来测试一些新特性！

这些选项允许我们向您展示我们正在为未来的大更新所做的工作！请注意，其中一些实验性特性在非测试版发布之前可能不可用，直到我们准备好发布完整更新。

请注意，使用实验性特性意味着您的世界在未来可能与其他测试版不兼容，因此请确保您保留世界的备份副本。

![img_506.JPG](https://feedback.minecraft.net/hc/article_attachments/360074360872/img_506.JPG)

### **山羊！**

我们很高兴在本周的测试版中介绍第一个*洞穴与山崖*特性 - 山羊！山羊将通过新的实验性特性开关启用 - 您需要启用此选项才能测试它们。

- 山羊目前将在极端丘陵生物群系中生成，直到我们为它们准备一个永久栖息地来练习它们的撞头技能
- 山羊是山脉之王。它们可以攀爬山脉和崎岖地形，并减少摔落伤害
- 它们喜欢跳跃 - 通常是在您最不期待的时候！
- 小心！它们顽皮，可能会把入侵者撞下山坡！
- 山羊如果撞到树木，可能会掉落角物品

### **细雪！**

- 添加了细雪块
  - 启用*洞穴与山崖*实验性开关以在本周的测试版中测试细雪！
  - 此块目前仅通过创造模式物品栏可用
- 皮革靴子使玩家在穿越细雪时更容易
- 实体可以进入细雪块，但在内部移动速度会减慢，并且摔落伤害会被忽略
- 山羊在路径规划时足够聪明，可以避免细雪块
- 细雪块的纹理与普通雪块略有不同
- 当相机在细雪块内部时，会渲染迷雾，并在其上渲染覆盖纹理

# 漏洞修复

### 性能和稳定性

- 修复了游戏过程中可能发生的多个崩溃
- 大量计划的即时更新不再导致游戏崩溃（[MCPE-94942](https://bugs.mojang.com/browse/MCPE-94942)）
- 修复了通过传送门或飞行时偶尔发生的崩溃
- 修复了在飞行或移动游戏世界时偶尔发生的崩溃

### 一般

- 在控制器上自动合成物品时，合成界面只会显示预览物品。这可以防止配方书的快速更新
- 修复了末地传送门块在末地传送门框架块被摧毁后未被移除的漏洞。除末地传送门块外的填充块将保持原位
- 修复了纸偶，使其在更衣室中始终可以用鼠标旋转（[MCPE-101210](https://bugs.mojang.com/browse/MCPE-101210)）

### 辅助功能

- 表情轮现在支持屏幕阅读器
- 修复了在邀请游戏屏幕上，UI屏幕阅读器未读取屏幕标题和快捷按钮的漏洞
- 修复了在某些设备上屏幕阅读器更新读取不够频繁的问题
- 修复了屏幕阅读器，使其能够正确读取聊天屏幕中带控制器图标的消息
- UI屏幕阅读器现在在关闭聊天的文本转语音时读取打开聊天消息

### 游戏玩法

- 双箱子在重新加载世界时不再丢失内容（[MCPE-102970](https://bugs.mojang.com/browse/MCPE-102970)）
- 在创造模式下，指南针在使用磁石时不再被消耗（[MCPE-96258](https://bugs.mojang.com/browse/MCPE-96258)）
- 丛林中生成的可可果现在会朝正确的方向生成（[MCPE-102399](https://bugs.mojang.com/browse/MCPE-102399)）
- 告示牌在尝试放置在与装饰相同的空间时不再替换装饰
- 用锹右键点击雪块不再破坏雪块
- 土径（以前称为草径）现在可以通过在泥土、灰化土、菌丝体或粗糙泥土（以及草）上使用锹来制作
- 更新了下界合金护腿的纹理（[MCPE-103016](https://bugs.mojang.com/browse/MCPE-103016)）
- 潮湿藤蔓在潜行时不再可以放置在堆肥桶上（[MCPE-78973](https://bugs.mojang.com/browse/MCPE-78973)）

### 生物

- 村民不再互相偷取工作台（[MCPE-43071](https://bugs.mojang.com/browse/MCPE-43071)）
- 生物不再随机停止攻击和跟随目标（[MCPE-48144](https://bugs.mojang.com/browse/MCPE-48144)）
- 靠近的猪灵不再可以捡起掉落在它们之间的相同物品
- 生物不再在凋灵玫瑰中生成（[MCPE-97331](https://bugs.mojang.com/browse/MCPE-97331)）
- 蜜蜂现在只在蜂巢和蜂巢前方出入

### 命令

- /playsound命令现在可以正确播放范围内所有玩家的声音
- /effect命令的持续时间现在限制为1,000,000秒（[MCPE-92916](https://bugs.mojang.com/browse/MCPE-92916)）
- 在同一刻执行的常加载区域命令不再允许添加同名区域两次
- /titleraw命令成功的占位符文本消息不再返回给玩家（[MCPE-63618](https://bugs.mojang.com/browse/MCPE-63618)）
- /title的times命令中的FadeOut参数不再被忽略  

### 图形、纹理和用户界面

- 更新僵尸猪灵的纹理以消除腰布的闪烁（[MCPE-96793](https://bugs.mojang.com/browse/MCPE-96793)）
- "经典控制 - 强烈"的字体颜色现在与VR控制菜单中的周围文本匹配
- 在使用控制器时，聊天设置中的\[X\]按钮不再出现
- 个人资料界面已改进，现在角色在加载时将可见并可以选择或修改
- 修复了在选项卡上悬停时视觉焦点指示器丢失的漏洞
- 荧光棒不再使用占位符纹理（教育功能）（[MCPE-45686](https://bugs.mojang.com/browse/MCPE-45686)）（[MCPE-68417](https://bugs.mojang.com/browse/MCPE-68417)）
- 加载屏幕提示将不再显示键“tips.game.62”
- 如果玩家取消“需要购买历史”对话框，则避免购买领域

### 脚本、附加包和技术更改

- 更改set_block和set_block_at_pos以使用BlockDescriptor指定block_type
- 带有物品锁组件的物品不再导致配方书显示无效的配方结果

### 方块

- 添加query.cardinal_facing_2d以获取不返回上下的地面方向
- 添加将方块模型放入models/blocks文件夹的能力
- 添加物品触发器向其交互的方块发送事件的能力（当有一个如on_use_on时）
- 添加查询交互面以便于与方块交互和在物品中使用minecraft:on_use_on。面可以通过query.block_face查询
- 修复数据驱动方块的面遮挡，以正确考虑单位立方体透明与单位立方体不透明
- 修复了由于实体碰撞和拾取碰撞组件导致的堆栈损坏引起的崩溃
- 数据驱动方块在携带或在物品栏中时不再将其顶部面旋转180度（[MCPE-63134](https://bugs.mojang.com/browse/MCPE-63134)）
- 如果没有足够的空间容纳多个实体，生物不再在固体物体外来回传送（[MCPE-101202](https://bugs.mojang.com/browse/MCPE-101202)）

### 事件响应

- "add_mob_effect"和"remove_mob_effect"在传入有效效果名称时不再抛出内容错误
- 为"remove_mob_effect"添加文档，以使创作者意识到他们可以使用值"all"来移除目标的所有生物效果
- 修复了物品无法放置在额外马具槽中的问题。并未修复所有可装备行为
- minecraft:inventory组件上的物品栏大小必须增加以匹配可装备槽，以便服务器接受物品放置
- 带有物品锁组件的物品的提示框在游戏规则showtags关闭时将不再显示