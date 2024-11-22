---
标题：Minecraft Beta 和预览 - 1.20.40.22
日期：2023-09-19T20:35:32Z
更新：2023-09-19T20:55:28Z
类别：Beta 和预览信息及变更日志
链接：https://feedback.minecraft.net/hc/en-us/articles/19648957981965-Minecraft-Beta-Preview-1-20-40-22
哈希：
  h_01HAQJSX6DBW59BBY4TCS3M9KZ: 特性和漏洞修复
  h_01HAQK1SVQTG342KDF0EH9D39G: 方块
  h_01HAQK1HGDQ7YVTEMFW9X1CPMW: 教育切换
  h_01HAQK3PB5N5EAJWTW574VSXGR: 游戏规则
  h_01HAQK1HGDXZSHDEQK52D85EH1: 游戏玩法
  h_01HAQK1HGD8QHX1CSKTQ9R9B7M: 生物
  h_01HAQK1HGDQ790RNBX8XXTWJHC: 用户界面
  h_01HAQK1HGD1YNEMQH73V6CPQKC: 原版趋同
  h_01HAQK7PQRNMVH5MR9XPCX8GPS: 技术更新
  h_01HAQK80AY07QZMENXXGCWGJ2C: API
  h_01HAQK7PQRR7BKHQD00DP02WAG: 编辑器
  h_01HAQK7PQRZ2H7JGJ3DXY8K249: 实体组件
  h_01HAQK7PQRTAW87JHFCMWHVX0E: 生物-1
  h_01HAQK7PQRDH9R921K67T19CA5: 稳定性和性能
  h_01HAQK7PQRDQEPBECCB3ZG2B96: 实验性技术
  h_01HAQK7PQRES2CTV6MCF1QS7FF: API-1
  h_01HAQK7PQRRDXZHHZ8AVAKN5YQ: 稳定性和性能-1
---

**发布于：** 2023年9月20日

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明。

![screenshot_1.20.40.22.png](https://feedback.minecraft.net/hc/article_attachments/19649108664589)

以下是本周Minecraft预览和Beta的新内容！一如既往，我们非常希望听到您对这些实验的想法，因此请将您的反馈和想法发送至 [aka.ms/MC120Feedback](http://aka.ms/MC120Feedback)，并将任何漏洞报告至 [bugs.mojang.com](http://bugs.mojang.com/)。

 

# **特性和漏洞修复**

## **方块**

- 修复了一个漏洞，导致告示牌的错误面有时会被编辑（[MCPE-169067](https://bugs.mojang.com/browse/MCPE-169067)）
- 修复了一个极其罕见的漏洞（约0.000003%的几率），可能导致物品展示框在被击打或摧毁时不掉落其物品

## **教育切换**

- 修复了一个漏洞，导致在打开作品集时关闭游戏会导致崩溃

## **游戏规则**

- 将重生半径的默认游戏规则值更改为10

## **游戏玩法**

- 山羊角现在可以在256个区块外听到（[MCPE-153254](https://bugs.mojang.com/browse/MCPE-153254)）

## **生物**

- 骆驼在行走时不再看起来像是在滑动（[MCPE-169666](https://bugs.mojang.com/browse/MCPE-169666)）
- 骆驼在静止时不再移动其腿（[MCPE-172846](https://bugs.mojang.com/browse/MCPE-172846)）
- 骆驼在熔岩中不再无限冲刺（[MCPE-172369](https://bugs.mojang.com/browse/MCPE-172369)）

## **用户界面**

- 自动补全文本现在将光标移动到行末

## **原版趋同**

- 铁傀儡和雪傀儡在创建时现在具有类似崩溃的粒子效果
- 流动的熔岩和水混合机制现在与Java版相匹配（[MCPE-41103](https://bugs.mojang.com/browse/MCPE-41103)）
- 女巫现在会在16个区块的范围内瞄准玩家  
    

# **技术更新**

## **API**

- 相机API从Beta版本移至1.6.0
  - 将Entity.is\* API从“beta”发布至“1.6.0”
    - *isSleeping*
    - *isSneaking*
    - *isSprinting*
    - *isSwimming*
    - *isClimbing*
    - *isOnGround*
    - *isInWater*
    - *isFalling*
  - 将玩家等级和经验API从“beta”发布至“1.6.0”
    - *addLevels*
    - *addExperience*
    - *level*
    - *getTotalXP*
    - *xpEarnedAtCurrentLevel*
    - *totalXpNeededForNextLevel*
    - *resetLevel*
  - 将Player.is\* API从“beta”发布至“1.6.0”
    - *isEmoting*
    - *isGliding*
    - *isJumping*
    - *isFlying*
  - 更新所有方法，除了ActionFormData、MessageFormData和ModalFormData上的show方法，以便在只读模式下调用
  - BlockInventoryComponent
    - 容器成员变量现在正确反映它可以是容器或未定义
  - 修复了一个版本控制漏洞，导致@minecraft/server-ui模块无法与@minecraft/server版本1.2.0以上的版本一起使用
  - WeatherType移至1.6.0
    - 将函数 *setWeather* 移至1.6.0
    - 将事件/属性 *entityRemove* 从Beta移至1.6.0
    - 将事件/属性 *entityRemove* 从Beta移至1.6.0
  - 将类EntityRemovedAfterEvent从Beta移至1.6.0
  - 将类EntityRemoveAfterEventSignal从Beta移至1.6.0
  - 将类EntityRemovedBeforeEvent从Beta移至1.6.0
  - 将类EntityRemoveBeforeEventSignal从Beta移至1.6.0
    - 将事件/属性 *entityLoad* 从Beta移至1.6.0
  - 将类EntityLoadAfterEvent从Beta移至1.6.0
  - 将类EntityLoadAfterEventSignal从Beta移至1.6.0
    - 将事件/属性 *entitySpawn* 从Beta移至1.6.0
  - 将枚举EntityInitializationCause从Beta移至1.6.0
  - 将类EntitySpawnAfterEvent从Beta移至1.6.0
  - 将类EntitySpawnAfterEventSignal从Beta移至1.6.0
    - 将事件/属性 *playerBreakBlock* 从Beta移至1.6.0
    - 将事件/属性 *playerBreakBlock* 从Beta移至1.6.0
  - 将类PlayerBreakBlockAfterEvent从Beta移至1.6.0
  - 将类PlayerBreakBlockAfterEventSignal从Beta移至1.6.0
  - 将类PlayerBreakBlockBeforeEvent从Beta移至1.6.0
  - 将类PlayerBreakBlockBeforeEventSignal从Beta移至1.6.0
    - 将事件/属性 *playerPlaceBlock* 从Beta移至1.6.0
  - 将类PlayerPlaceBlockAfterEvent从Beta移至1.6.0
  - 将类PlayerPlaceBlockAfterEventSignal从Beta移至1.6.0
  - 将类BlockEventSignalOptions从Beta移至1.6.0
    - 将 *isAir(): boolean* 从Beta移至1.6.0
    - 将 *isLiquid(): boolean* 从Beta移至1.6.0
    - 将 *amount* 从Beta移至1.6.0
    - 将 *keepOnDeath: boolean* 从Beta移至1.6.0
    - 将 *lockMode: ItemLockMode* 从Beta移至1.6.0
    - 将 *nameTag?: string* 从Beta移至1.6.0
    - 将 *clone(): ItemStack* 从Beta移至1.6.0
    - 将 *getTags(): string\[\]* 从Beta移至1.6.0
    - 将 *hasTag(tag: string): boolean* 从Beta移至1.6.0
    - 将 *setCanDestroy(blockIdentifiers?: string\[\]): void* 从Beta移至1.6.0
    - 将 *getCanDestroy(): string\[\]* 从Beta移至1.6.0
    - 将 *setCanPlaceOn(blockIdentifiers?: string\[\]): void* 从Beta移至1.6.0
    - 将 *getCanPlaceOn(): string\[\]* 从Beta移至1.6.0
    - 将函数 *getProperty* 移至1.6.0
    - 将函数 *resetProperty* 移至1.6.0
    - 将函数 *setProperty* 移至1.6.0

## **编辑器**

编辑器及其相应的API仍在早期开发中，适用于Windows PC的基岩预览构建的键盘/鼠标操作。请在社交渠道上标记我们，使用 **\#BedrockEditor**。

了解 [如何使用](https://aka.ms/LearnEditor) 编辑器，加入 [GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛与团队互动，并通过 [入门工具包](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [示例](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

**本周介绍**... *第一个* 向我们的v0.5版本：编辑/测试轻量版发布的迭代！以下是您需要知道的内容 - 请在 [GitHub Release 0.4.5说明](https://github.com/Mojang/minecraft-editor/discussions/categories/announcements) 中阅读更多信息：

- 在编辑器上下文中进行完整的往返编辑 --> （游戏）测试体验
- 自定义您的世界条件以进行测试
- 您在测试会话中所做的更改将不会被保存
- 市场和角色在测试体验中被禁用，这在编辑器中也是标准
- 目前仅在单人游戏中可用（*暂时* 😊）

本周的其他修复：

- 修复了选择工具中的一个漏洞，其中Vector3原点的Y轴超出了维度高度范围
- 修复了一个漏洞，导致在撤销后无法在最后放置的方块位置放置方块

## **实体组件**

- “behavior.random_look_around_and_sit”现在公开了字段“continue_sitting_on_reload”供创作者使用。这就是骆驼在重载时保持坐姿的方式
- “behavior.is_scenting”重命名为通用的“behavior.timer_flag_1”并发布给创作者
- “behavior.is_rising”重命名为通用的“behavior.timer_flag_2”并发布给创作者
- “behavior.is_feeling_happy”重命名为通用的“behavior.timer_flag_3”并发布给创作者
- “behavior.timer_flag 1”：当该行为开始时触发事件，然后等待一段时间后停止。当由于超时或被其他行为中断而停止时，触发另一个事件。query.timer_flag_1在该行为运行时将在客户端和服务器上返回1.0，否则返回0.0
- “behavior.timer_flag 2”：当该行为开始时触发事件，然后等待一段时间后停止。当由于超时或被其他行为中断而停止时，触发另一个事件。query.timer_flag_2在该行为运行时将在客户端和服务器上返回1.0，否则返回0.0
- “behavior.timer_flag 3”：当该行为开始时触发事件，然后等待一段时间后停止。当由于超时或被其他行为中断而停止时，触发另一个事件。query.timer_flag_3在该行为运行时将在客户端和服务器上返回1.0，否则返回0.0

## **生物**

- 为Molang添加了一个新的“query.is_in_lava”查询函数，以了解生物当前是否在熔岩中

## **稳定性和性能**

- 声音定义文件sound_definitions.json如果使用了错误的json类型进行特定声音定义将不再导致游戏崩溃（[MCPE-168913](https://bugs.mojang.com/browse/MCPE-168913)）  
    

# **实验性技术**

## **API**

- 添加了函数 *getWeather*

## **稳定性和性能**

- 修复了在某些Android设备（例如Mali GPU）上加载启用延迟技术预览的世界时的崩溃（[MCPE-173934](https://bugs.mojang.com/browse/MCPE-173934)）
- 在一些不支持我们当前计算着色器要求的Android设备上禁用了延迟技术预览（GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS >= 256）