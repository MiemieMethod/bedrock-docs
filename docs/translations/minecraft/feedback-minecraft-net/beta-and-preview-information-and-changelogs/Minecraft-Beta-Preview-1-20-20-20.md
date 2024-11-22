---
title: Minecraft Beta & Preview - 1.20.20.20
date: 2023-06-28T13:45:01Z
updated: 2023-06-28T14:13:05Z
categories: Beta和Preview信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/17151426531085-Minecraft-Beta-Preview-1-20-20-20
---

**发布日期：** 2023年6月28日

**关于Minecraft Preview和Beta的信息：**

- 这些开发中的版本可能不稳定，且可能不代表最终版本的质量。
- Minecraft Preview可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)。
- Beta版可在Android（Google Play）上获得。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)获取详细说明。

![Minecraft截图，展示了一名流浪商人、羊驼和一只婴儿山羊。商人站在堆叠的雪层上，场景中有一些饰纹柱子和一个物品展示框中的樱花树苗。](https://feedback.minecraft.net/hc/article_attachments/17151441004173)

是时候迎来新的Minecraft Preview和Beta了！以下是本次更新中的修复和地物列表。请继续向我们发送您的[反馈](https://aka.ms/MC120Feedback)和[漏洞报告](https://bugs.mojang.com/)，祝您游戏愉快！

# **实验性功能**

## **配方解锁**

- 为配方解锁添加了命令行自动补全。适用于您想查看可以解锁哪些配方时使用。([MCPE-171086](https://bugs.mojang.com/browse/MCPE-171086))
- 命令输入的顺序已更改，与Java版保持一致。([MCPE-171098](https://bugs.mojang.com/browse/MCPE-171098))
- 使用命令解锁配方时，您将收到确认消息。它会告知您命令是否成功执行。([MCPE-171065](https://bugs.mojang.com/browse/MCPE-171065))
- 基岩版的通知声音已更新。感谢您的反馈！您告诉我们Java版的*swoosh*声音更适合解锁通知。您是对的。因此，我们进行了更改。([MCPE-171116](https://bugs.mojang.com/browse/MCPE-171116))
- 配方通知的持续时间现在根据解锁的配方数量进行计算。

# **功能和漏洞修复**

## **方块**

- 修复了一个漏洞，导致玩家站在顶部雪层上时无法在台阶下爬行。([MCPE-170994](https://bugs.mojang.com/browse/MCPE-170994))
- 顶部雪层现在与Java版保持一致，每层具有不同的高度。

## **音频**

- 添加了缺失的荆棘伤害声音，并在适当时播放。([MCPE-37335](https://bugs.mojang.com/browse/MCPE-37335))
- 铁砧在被破坏、踩踏、坠落等时，现在会发出正确的声音。([MCPE-33286](https://bugs.mojang.com/browse/MCPE-33286))
- 骷髅和溺尸现在在射箭和投掷三叉戟时分别播放声音。([MCPE-50609](https://bugs.mojang.com/browse/MCPE-50609))
- 三叉戟引雷声音现在在击中实体时播放。([MCPE-43402](https://bugs.mojang.com/browse/MCPE-43402))
- 空地图在玩家绘制时现在会发出适当的声音。
- 下界传送门在其黑曜石框架被破坏时，现在会发出玻璃破裂的声音。([MCPE-94722](https://bugs.mojang.com/browse/MCPE-94722))
- 忠诚三叉戟返回玩家时，现在会在玩家位置播放其声音。([MCPE-43831](https://bugs.mojang.com/browse/MCPE-43831))
- 大型垂滴叶方块在其倾斜被重置时，现在会播放正确的声音。([MCPE-123488](https://bugs.mojang.com/browse/MCPE-123488))
- 潮涌核心在停用时，现在会播放其停用声音。([MCPE-128117](https://bugs.mojang.com/browse/MCPE-128117))
- 重生锚方块现在正确地播放其环境声音。([MCPE-136484](https://bugs.mojang.com/browse/MCPE-136484))

## **趋同**

- 下落的方块现在在坠落到船上时会破碎。
- 流浪商人现在也交易樱花树苗。([MCPE-171521](https://bugs.mojang.com/browse/MCPE-171521))
- 在爬行时更新了摄像机插值率，以匹配Java版。([MCPE-170841](https://bugs.mojang.com/browse/MCPE-170841))

## **命令**

- 实体在传送到玩家渲染距离边缘附近的已保存区块时，不再消失。

## **游戏玩法**

- 第三人称摄像机在靠近水或熔岩时，不再穿透地形。
- 修复了创造模式玩家站在火中时未被点燃的问题。
- 玩家在旁观模式下不再被强制进入潜行或爬行状态。([MCPE-170907](https://bugs.mojang.com/browse/MCPE-170907))
- 玩家在骑乘时现在会被强制退出潜行/爬行状态。([MCPE-170870](https://bugs.mojang.com/browse/MCPE-170870))
- 玩家在使用激流动画时不再被强制进入潜行或爬行状态。
- 玩家不应再在不应触发爬行时意外触发爬行。
- 修复了一些服务器上未正确触发爬行的情况。([MCPE-171225](https://bugs.mojang.com/browse/MCPE-171225))
- 在创造模式中进入飞行模式现在会正确取消鞘翅滑翔。([MCPE-171797](https://bugs.mojang.com/browse/MCPE-171797))
- 修复了进入包含损坏的已保存区块的世界时崩溃的问题。([MCPE-164634](https://bugs.mojang.com/browse/MCPE-164634))
- 在物品栏中点击装饰陶罐现在会显示正确的悬停提示。([MCPE-171800](https://bugs.mojang.com/browse/MCPE-171800))

## **图形**

- 透过末地传送门查看透明方块时，现在不再可见也不会闪烁。([MCPE-162061](https://bugs.mojang.com/browse/MCPE-162061))
- 修复了传送门效果的底部面，使其颜色和透明度与其他面匹配。
- 樱花叶方块现在会根据系统性能在较大距离处生成粒子效果。

## **物品**

- 谜之炖菜现在不再出现在创造物品栏中（近期意外更改导致其出现在那里）。

## **生物**

- 修复了使用鞘翅滑翔并切换到创造飞行模式的问题。([MCPE-171797](https://bugs.mojang.com/browse/MCPE-171797))
- 玩家杀死的村民现在不再掉落他们手中的物品。
- 被感染的僵尸村民现在显示正确的职业。([MCPE-80924](https://bugs.mojang.com/browse/MCPE-80924))

## **移动触控控制设置**

- 将摇杆可见性选项更改为下拉菜单。
- 将潜行选项更改为下拉菜单。

## **用户界面**

- 将“同步旧世界”按钮移动到设置/存储屏幕。

## **输入**

- 改进了鼠标输入，使其在Xbox上使用时更具响应性。([MCPE-163671](https://bugs.mojang.com/browse/MCPE-163671))

# **技术更新**

## **附加包和脚本引擎**

- 没有纹理的渲染控制器现在会导致内容错误并被忽略。
- 在世界模板清单中添加了对"*allow_random_seed*"选项的支持。
- 紫水晶簇方块使用状态"*minecraft:block_face*"代替"*facing_direction*"。"*minecraft:block_face*"使用字符串值("down", "up", "north", "south", "east", "west")。
- 台阶方块使用状态"*minecraft:vertical_half*"代替"*top_slot_bit*"。"*minecraft:vertical_half*"使用字符串值("bottom", "top")。

## **编辑器**

编辑器仍处于早期开发阶段，可在Windows PC基岩Preview版本上通过键盘/鼠标使用。了解[如何使用](https://aka.ms/LearnEditor)编辑器并加入[GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions)论坛，发布漏洞，查看更详细的发布说明。在社交渠道上用**#BedrockEditor**标签我们。

本周标志着**v0.4：编辑器API更新！**的发布！虽然仍处于早期开发阶段，但我们已发布以下支持：

- 编辑器扩展的[概述文章](https://learn.microsoft.com/en-us/minecraft/creator/documents/editorextensionsintroduction)和[API参考文档](https://aka.ms/EditorAPI)在learn.microsoft.com上。
- [入门套件](https://github.com/Mojang/minecraft-editor-extension-starter-kit)：包含编译工具和启动制作编辑器扩展所需的各种库。
- 我们团队创建的[示例](https://github.com/Mojang/minecraft-editor-extension-samples)，帮助您快速开始创建自己的扩展。

本周对编辑器体验的其他修复：

- 修复了工具面板中数字滑块滑块超出面板边界的漏洞。
- 修复了点击工具轨道中已选择工具未重新打开已关闭工具面板的漏洞。
- 修复了结构空位、光源方块和屏障方块仅在玩家持有时可见的问题——现在它们在编辑器中始终可见。
- 修复了在模拟暂停时，第三人称视角下玩家身体不旋转的问题。
- 改进了日志记录，并将操作聊天通知移至日志面板。
- 修复了当没有活动选择时选择小工具的可见性。之前，当没有选择体积时，选择箭头小工具会在世界原点(0,0,0)处渲染。
- 选定的主题现在将在快速启动面板的帮助标签中的外部链接上正确应用。
- 从快速面板标签中移除了无功能的汉堡菜单按钮。

## **物品**

- 在json格式1.20.20及更高版本中，将"*minecraft:hand_equipped*"物品组件从实验性功能中发布。
- 在json格式1.20.20及更高版本中，弃用"*minecraft:creative_category*"组件。
- 在json格式1.20.20及更高版本中，现在可以在"描述"字段中设置创造组和命令可见性。
- 将"*minecraft:foil*"物品组件重命名为"*minecraft:glint*"，并在json格式1.20.20及更高版本中从实验性功能中发布。
- 将用于投射物的火附魔持续时间从*ShooterItemComponent*更改，以匹配原版行为。
- 在json格式1.20.20及更高版本中，将"*minecraft:use_duration*"物品组件从实验性功能中发布。
- 在json格式1.20.20及更高版本中，将"*minecraft:stacked_by_data*"物品组件从实验性功能中发布。

## **网络**

- Linux专用服务器：Ubuntu 20.04 LTS（Focal Fossa）现已成为Ubuntu支持的最低版本。不再支持Ubuntu 18.04 LTS。

## **声音**

- 声音定义现在接受*min_distance*和*max_distance*的浮点数和整数值——请将sound_definitions.json的"*format_version*"参数设置为1.20.20或更高以使用此功能。([MCPE-154378](https://bugs.mojang.com/browse/MCPE-154378))

# **实验性技术功能**

## **API**

- 将"*set_block_property*"转换为用于自定义方块的"*set_block_state*"。
- 向*DynamicPropertiesDefinition*添加了*defineVector*。
- *EntityEquipmentInventoryComponent*
  - 实现了*setEquipment*的槽位验证，现在返回一个布尔值，指示物品是否可以装备到指定槽位。
  - *EntityEquipmentInventoryComponent*当前仅限于玩家。然而，我们希望在未来的更新中为生物重新引入此组件。
    - 将*getDay*移动到*1.4.0*。
    - 将*getTimeOfDay*移动到*1.4.0*。
    - 将*setTimeOfDay(timeOfDay: number | TimeOfDay)*移动到*1.4.0*。
    - 将*getAbsoluteTime*移动到*1.4.0*。
    - 将*setAbsoluteTime(absoluteTime: number)*移动到*1.4.0*。
  - 将*TimeOfDay*移动到*1.4.0*。
    - 向*setLore*添加了长度限制——最多20行，每行最多50个字符。
    - 将函数*setLore*移动到*1.4.0*。
    - 将函数*getLore*移动到*1.4.0*。
    - 将类*SystemAfterEvents*移动到*1.4.0*。
    - 将类*ScriptEventCommandMessageAfterEvent*移动到*1.4.0*。
  - 将玩家的*onScreenDisplay*移动到*1.4.0*。
  - 将*titleDisplayOptions*移动到*1.4.0*。
  - 将*screenDisplay*移动到*1.4.0*。

## **命令**

- 将命令*/scriptevent*从实验性功能中发布。

## **物品**

- 修复了在使用物品装备时，带有"*minecraft:wearable*"组件的物品会重复的漏洞。([MCPE-159736](https://bugs.mojang.com/browse/MCPE-159736))
- 带有"*minecraft:wearable*"组件且位于非武器槽位的物品现在无法堆叠。([MCPE-159736](https://bugs.mojang.com/browse/MCPE-159736))
- 移除了"*minecraft:ignores_permission*"组件。
- 移除了"*minecraft:mirrored_art*"组件。
- 在json格式1.20.20及更高版本中，将"*protection*"字段从"*minecraft:armor*"组件移动到"*minecraft:wearable*"组件。
- 在json格式1.20.20及更高版本中，弃用"*minecraft:armor*"组件。
- 从"*minecraft:wearable*"组件中移除了无功能和冗余的槽位选项，如mainhand、hotbar、inventory、enderchest和equippable。
- 使用"*weapon.offhand*"槽位的带有"*minecraft:wearable*"组件的物品在热键栏中使用时将不再装备。
- 装备自定义可穿戴物品时会触发通用装备声音。
- 可以通过点击和拖动物品栏中的物品或使用Shift键点击来装备带有"*minecraft:wearable*"组件的自定义物品。

## **用户界面**

- 当玩家按下摄像机视角切换按钮但已经设置了特定视角时，显示消息。