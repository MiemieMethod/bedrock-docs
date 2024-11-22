---
标题: Minecraft Beta & Preview - 1.19.70.21
日期: 2023-02-01T14:02:26Z
更新: 2023-02-01T15:34:27Z
分类: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/12739185905933-Minecraft-Beta-Preview-1-19-70-21
---

**发布于:** 2023年2月1日

**注意:** 本周的Android Beta版本可能会延迟。我们对此造成的不便表示歉意，并正在努力解决该问题。

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量。
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)。
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明。

![一张Minecraft的村庄截图，展示了一名村民站在两个音符方块旁，音符方块上方放着一个龙首和一个猪灵的头。场景中还有一个铁傀儡、两只骆驼和一只猫。](https://feedback.minecraft.net/hc/article_attachments/12738753624461)

 

以下是本周Minecraft预览和Beta中的新内容！关于盔甲装饰的说明：这些可以在[Java版快照](https://www.minecraft.net/en-us/article/minecraft-snapshot-23w04a)中进行测试，但它们还未完全准备好用于基岩版Beta和预览。我们会在它们准备好后立即通知您，以便您进行实验，请关注[Minecraft.net](https://www.minecraft.net/)以获取最新更新！

一如既往，您可以通过[aka.ms/MC120Feedback](http://aka.ms/MC120Feedback)向我们发送所有反馈和想法，并向[bugs.mojang.com](http://bugs.mojang.com/)报告任何漏洞。

# **实验性特性**

## **方块**

- 猪灵和龙首方块在快捷栏或物品栏中不再动画化（[MCPE-164535](https://bugs.mojang.com/browse/MCPE-164535)，[MCPE-32654](https://bugs.mojang.com/browse/MCPE-32654)）

# **特性和漏洞修复**

## **游戏玩法**

- 玩家现在可以在仅部分被实体阻挡的方块中放置顶部台阶（[MCPE-155016](https://bugs.mojang.com/browse/MCPE-155016)）
- 玩家在潜行或第三人称骑乘时不再能透视部分方块（[MCPE-156273](https://bugs.mojang.com/browse/MCPE-156273)）
- 当从某些角度与世界高度限制的方块交互时，不再出现关于在世界高度限制外建造的错误信息（[MCPE-152935](https://bugs.mojang.com/browse/MCPE-152935)）
- 玩家现在可以在潜行时与功能性方块交互，而无需按住潜行按钮

## **原版趋同**

- 修复了僵尸猪灵在光照等级高于11的下界生成的漏洞
- 矿车现在可以将生物弹出到液体方块中（[MCPE-120078](https://bugs.mojang.com/browse/MCPE-120078)）

## **触控控制**

- 允许在按下前进按钮时，左侧和右侧十字键按钮保持输入
- 当玩家从船上跌落时，添加了离开船的按钮
- 修复了一个问题，该问题阻止玩家通过点击创造模式物品栏中的物品或方块来移除装备的盔甲（[MCPE-165790](https://bugs.mojang.com/browse/MCPE-165790)）

## **性能和稳定性**

- 修复了在任何输入设备上同时按下“开采”和“放置”按钮时，目标为结构方块可能导致游戏崩溃的问题（[MCPE-155689](https://bugs.mojang.com/browse/MCPE-155689)）

## **市场**

- 使用控制器左摇杆在侧边栏向右导航现在会折叠侧边栏

## **命令**

- 移除了在命令 /clone、/execute、/fill、/setblock 和 /testforblock 中对字段 "data" 的支持，版本限制为1.19.70，例如 */setblock ~ ~ ~ minecraft:wool 1* 将仅支持其等效的 */setblock ~ ~ ~ minecraft:wool \["color":"orange"\]*
- 音量参数不再向下取整选择器的位置（[MCPE-162237](https://bugs.mojang.com/browse/MCPE-162237)）
- 按音量选择目标现在将选择所有与音量框碰撞的实体。这适用于1.19.70及更高版本（[MCPE-162237](https://bugs.mojang.com/browse/MCPE-162237)）
- 在版本低于1.19.70时，先前的行为按预期工作
- 选择器的音量参数（dx、dy、dz）现在支持浮点值（[MCPE-163863](https://bugs.mojang.com/browse/MCPE-163863)）

# **技术更新**

## **通用**

- 工作台组件不再在默认使用方块名称作为工作台标签时附加 "tile."

# **实验性技术更新**

## **API**

- 添加了 *function playAnimation(animationName: string, options?: PlayAnimationOptions)* - 为实体播放指定的动画
- **物品堆叠**
  - *ItemStack* 现在可以使用字符串标识符构造
  - 移除了构造函数参数数据
  - 移除了属性 *data*
  - 移除了函数 *clearLore* - 要清除描述，请调用 *setLore* 并传入空数组或 *undefined*
  - 将 *nameTag* 设置为空字符串现在将清除命名牌
  - 将 *nameTag* 设置为超过255个字符的字符串将导致异常
  - 将 *amount* 设置为超过最大堆叠数的值将被限制为最大堆叠数
  - 将 *amount* 设置为小于1的值将导致异常

<!-- -->

- **容器槽位**
  - 移除了函数 *clearItem* - 要清除物品，请调用 *setItem* 并传入 *undefined*
  - 移除了函数 *clearLore* - 要清除描述，请调用 *setLore* 并传入空数组或 *undefined*

## **GameTest框架**

- 测试
  - 为 *assertEntityPresent(entityTypeIdentifier: string, blockLocation: BlockLocation, searchDistance?: number, isPresent?: boolean)* 添加了可选的 *searchDistance* 参数
  - 添加了 *assertEntityInstancePresentInArea(entity: Entity, isPresent?: boolean)* 用于检查实体实例是否存在于测试区域
  - 在 *assertItemEntityPresent* 中将 *searchDistance* 参数设为可选

## **通用**

- 在1.19.70及更高版本的JSON格式中，如果方块变体中的 "condition" 字段不是有效的Molang字符串，则方块将无法加载