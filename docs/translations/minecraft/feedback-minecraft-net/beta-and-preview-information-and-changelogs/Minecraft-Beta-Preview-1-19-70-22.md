---
标题: Minecraft Beta & Preview - 1.19.70.22
日期: 2023-02-08T14:58:17Z
更新: 2023-02-08T15:21:29Z
类别: Beta 和预览信息及更改日志
链接: https://feedback.minecraft.net/hc/en-us/articles/12940778804877-Minecraft-Beta-Preview-1-19-70-22
---

**发布于:** 2023年2月8日

**注意:** 本周的Android Beta版本可能会延迟。我们对此造成的不便表示歉意，并正在努力解决该问题。

**关于Minecraft预览和Beta的信息:**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一张Minecraft村庄和生物的截图。](https://feedback.minecraft.net/hc/article_attachments/12940611585293)

以下是本周Minecraft预览和Beta中的新内容！我们仍在努力添加盔甲修饰到基岩版Beta和预览中。一旦准备好，我们会及时通知您，以便您进行实验。请关注 [Minecraft.net](https://minecraft.net/) 获取最新更新！

如往常一样，您可以通过 [aka.ms/MC120Feedback](https://aka.ms/MC120Feedback) 向我们发送所有反馈和想法，并向 [bugs.mojang.com](https://bugs.mojang.com/) 报告任何漏洞。

# **实验性特性**

## **方块**

- 移除了竹栅栏和竹栅栏门边缘的黑线 ([MCPE-163360](https://bugs.mojang.com/browse/MCPE-163360))
- 使用结构方块将实验性方块导入非实验性世界时，现在会正确放置不可交互的未知方块

## **骆驼**

- 骆驼现在可以再次跨越高达一个半区块的障碍 ([MCPE-166452](https://bugs.mojang.com/browse/MCPE-166452))

## **用户界面**

- 红树和悬挂式竹告示牌现在在创造模式物品栏中正确放置 ([MCPE-163340](https://bugs.mojang.com/browse/MCPE-163340))

# **特性和漏洞修复**

### **原版趋同**

- 投射物在紫水晶方块和簇上的撞击声现在可听见
- 枯萎的灌木在用任何工具（除了剪刀）破坏时现在会掉落木棍，即使是带有精准采集魔咒的工具。在同样情况下，藤蔓不会掉落任何物品 ([MCPE-163246](https://bugs.mojang.com/browse/MCPE-163246))
- 当方块放置在钟的下方或上方时，钟不再破坏 ([MCPE-166742](https://bugs.mojang.com/browse/MCPE-166742))

### **旁观模式**

- 在第三人称视角中穿透方块不再使相机向玩家的头部缩放 ([MCPE-160467](https://bugs.mojang.com/browse/MCPE-160467))
- 末地折跃门在旁观模式中不再可用 ([MCPE-165689](https://bugs.mojang.com/browse/MCPE-165689))

## **游戏玩法**

- 红石源现在可以同时从不同侧面为单个方块供电 ([MCPE-163651](https://bugs.mojang.com/browse/MCPE-163651))
- 玩家在没有空间站立的情况下不再能够开始飞行 ([MCPE-166413](https://bugs.mojang.com/browse/MCPE-166413))
- 玩家在潜行时如果不按住潜行按钮，现在可以从边缘掉落

### **方块**

- 堆肥桶现在在变满时总是会消耗一个物品 ([MCPE-162020](https://bugs.mojang.com/browse/MCPE-162020))

### **生物**

- 女巫在营火上站立时会饮用抗火药水

## **物品**

- 弩在充能箭时现在会摇晃 ([MCPE-152952](https://bugs.mojang.com/browse/MCPE-152952))
- 在函数内部使用时，战利品表条件不再被忽略 ([MCPE-164582](https://bugs.mojang.com/browse/MCPE-164582))
- 雪傀儡、凋零和行商羊驼的刷怪蛋现在在物品栏和快捷栏中正确显示

## **市场**

- 在市场屏幕侧边栏添加了一个新的“市场”图标

## **用户界面**

- 胡萝卜在 *can_place_on* 和 *can_destroy* 物品组件中使用时，现在显示正确的名称 ([MCPE-160838](https://bugs.mojang.com/browse/MCPE-160838))
- 调整了Android设备上文本输入字段的键盘交互

## **命令**

- 召唤命令不再导致某些实体以角度生成

# **技术更新**

## **实体属性**

- 修复了一个问题，即如果通过事件触发的活动行为被移除，实体属性值的更改可能会被丢弃

# **实验性技术特性**

## **API**

用方法替换了通用的 *setVelocity* 调用，以对实体应用冲击：

- 添加函数 *clearVelocity(): void* - 将实体的当前速度设置为零
- 添加函数 *applyImpulse(vector: Vector3): void* - 将冲击向量应用于实体的当前速度
- 添加函数 *applyKnockback(directionX: number, directionZ: number, horizontalStrength: number, verticalStrength: number): void* - 根据垂直和水平力量对实体施加击退
- 移除函数 *setVelocity*

对简单数据对象与属性的处理进行了更一致的更改：

- BeforeExplosionEvent
  - 添加函数 *getImpactedBlocks(): Vector3\[*] - 获取受爆炸影响的方块位置
  - 添加函数 *setImpactedBlocks(blocks: Vector3\[*]): void* - 设置受爆炸影响的方块位置
  - 移除属性 *impactedBlocks*
- BeforeItemUseOnEvent
  - 添加函数 *getBlockLocation(): Vector3* - 获取受影响方块的位置
  - 移除属性 *blockLocation*
- BlockInventoryComponent
  - 移除属性 *location*
- BlockLavaContainerComponent
  - 移除属性 *location*
- BlockPistonComponent
  - 添加函数 *getAttachedBlocks(): Vector3\[*] - 获取受此活塞激活影响的方块位置
  - 移除属性 *attachedBlocks*
  - 移除属性 *location*
- BlockPotionContainerComponent
  - 移除属性 *location*
- BlockRecordPlayerComponent
  - 移除属性 *location*
- BlockSignComponent
  - 移除属性 *location*
- BlockSnowContainerComponent
  - 移除属性 *location*
- BlockWaterContainerComponent
  - 移除属性 *location*
  - 添加函数 *getHeadLocation(): Vector3* - 获取实体的头部位置
  - 移除属性 *headLocation*
- ExplosionEvent
  - 添加函数 *getImpactedBlocks(): Vector3\[*] - 获取受爆炸影响的方块位置
  - 移除属性 *impactedBlocks*
- ItemStartUseOnEvent
  - 添加函数 *getBlockLocation(): Vector3* - 获取受影响方块的位置
  - 添加函数 *getBuildBlockLocation(): Vector3* - 获取生成方块的位置
  - 移除属性 *blockLocation*
  - 移除属性 *buildBlockLocation*
- ItemStopUseOnEvent
  - 添加函数 *getBlockLocation(): Vector3* - 获取受影响方块的位置
  - 移除属性 *blockLocation*
- ItemUseOnEvent
  - 添加函数 *getBlockLocation(): Vector3* - 获取受影响方块的位置
  - 移除属性 *blockLocation*
- NavigationResult
  - 添加函数 *getPath(): Vector3\[*] - 获取构成导航路线的方块位置
  - 移除属性 *path*
- Player
  - 添加函数 *getHeadLocation(): Vector3* - 获取玩家的头部位置
  - 移除属性 *headLocation*

ItemStack API改进：

- 添加只读属性 *getMaxAmount: number* - 返回物品的最大堆叠数量
- 添加只读属性 *isStackable: bool* - 返回物品是否可堆叠
- 添加函数 *isStackableWith(itemStack: ItemStack): bool* - 返回物品是否可以与给定物品堆叠
- 添加只读属性 *type: ItemType* - 返回物品的类型
- 添加函数 *clone(): ItemStack* - 返回物品堆叠的副本
- 添加属性 *keepOnDeath: bool* - 设置物品在死亡时是否保留
- 添加属性 *lockMode: ItemLockMode* - 设置物品是否可以移动或丢弃
- 添加函数 *setCanPlaceOn(blockIdentifiers?: string\[\])* - 设置物品可以放置的方块
- 添加函数 *setCanDestroy(blockIdentifiers?: string\[\])* - 设置此物品可以破坏的方块
