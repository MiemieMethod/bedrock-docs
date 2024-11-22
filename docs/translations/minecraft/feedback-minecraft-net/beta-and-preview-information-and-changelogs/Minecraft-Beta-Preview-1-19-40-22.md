---
title: Minecraft Beta & Preview - 1.19.40.22
date: 2022-09-21T14:33:13Z
updated: 2022-09-21T15:45:28Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/9329824511629-Minecraft-Beta-Preview-1-19-40-22
---

**发布时间：** 2022年9月21日

## **关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参阅[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)获取详细说明

![一张Minecraft截图，展示了村民、悦灵和一些脚手架。](https://feedback.minecraft.net/hc/article_attachments/9329732420877/R19U4_3_16x9.jpg)

以下是本周Minecraft预览版和测试版的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，欢迎您向我们发送[反馈](https://aka.ms/MinecraftBetaFeedback)。

# **新特性和漏洞修复**

## **原版趋同**

### **旁观模式（实验性）**

- 旁观玩家在进入/退出气泡柱时不再播放声音（[MCPE-161536](https://bugs.mojang.com/browse/MCPE-161536)）

# **新特性和漏洞修复**

## **方块**

- 脚手架现在以更正确的速度燃烧，1/4个物品（[MCPE-42949](https://bugs.mojang.com/browse/MCPE-42949)）
- 破坏覆盖在雪上的花后，花会掉落而不是雪层（[MCPE-61609](https://bugs.mojang.com/browse/MCPE-61609)）

## **命令**

- 使用/clone命令复制气泡柱不再导致水不可见（[MCPE-153903](https://bugs.mojang.com/browse/MCPE-153903)）

## **游戏玩法**

- 撤销导致箭和三叉戟停止移动的更改（[MCPE-162085](https://bugs.mojang.com/browse/MCPE-162085)）
- 修复了凋零效果伤害被盔甲减少的问题（[MCPE-159407](https://bugs.mojang.com/browse/MCPE-159407)）

## **图形**

- 修复了信标方块在远处观察时突然消失的问题

## **生物**

- 修复了溺尸在攻击时可以更换持有物品的问题（[MCPE-40288](https://bugs.mojang.com/browse/MCPE-40288)）

## **触控控制**

- 改进了触控设置菜单中三种控制方案的图像

## **用户界面**

- 修复了玩家无法从装备页面拖放或选择物品的问题
- 将“黑暗效果强度”和“通知持续时间”辅助功能选项的文本描述颜色更改为更浅的色调，以提高可读性（[MCPE-162047](https://bugs.mojang.com/browse/MCPE-162047)）
- 修复了用户无法使用触控控制交换不可堆叠物品的问题

# **技术更新**

## **实体文档**

- 移除了荒野更新实体行为和组件的实验性标记
- 添加了minecraft:heartbeat的文档，并重新措辞了一些文档内容

## **物品**

- 添加了支持直接使用物品标签而不是物品名称的配方
  - 添加了新的物品标签
  - 将多个配方从代码转换为自己的配方文件
  - 添加了多个使用新标签的配方，以覆盖许多旧的特定物品配方（这些仍然存在以保持向后兼容性）：
    - 木桶、蜂箱、书架、碗、酿造台、营火、制图台、箱子、堆肥桶、合成台、日光探测器、火焰弹、箭矢台、熔炉、砂轮、唱片机、讲台、织布机、音符盒、画、活塞、盾牌、锻造台、烟熏炉、灵魂营火、灵魂火把、木棍、石斧、石锄、石镐、石锹、石剑、火把、绊线钩、木斧、木锄、木镐、木锹、木剑

# **实验性技术特性**

## **附加包和脚本引擎**

- 实现了has_property、int_property、bool_property、float_property和enum_property活动对象行为过滤器

## **API**

- 更新了API。请参见下面的列表以获取具体更改：
  - 事件
    - 移除了每刻调用的事件tick
  - 系统
    - 添加了run() - 将回调排队以在下一个刻运行，每刻重新排队以获得类似于tick事件的行为
  - 方块
    - 将属性id重命名为typeId
  - 方块组件
    - 将属性id重命名为typeId
  - 实体
    - 将属性id重命名为typeId
    - 添加了只读属性id: string- 返回实体的唯一标识符。该标识符在世界加载之间保持一致。
  - 实体组件
    - 将属性id重命名为typeId
  - 物品组件
    - 将属性id重命名为typeId
  - 物品堆
    - 将属性id重命名为typeId

## **游戏测试框架**

- 修复了EntityHurtEvent在玩家死亡时未触发的漏洞
- 将实验性游戏测试框架重命名为Beta API
- 现在重命名的Beta API实验仍然需要访问所有测试版API，包括核心Minecraft API和游戏测试API