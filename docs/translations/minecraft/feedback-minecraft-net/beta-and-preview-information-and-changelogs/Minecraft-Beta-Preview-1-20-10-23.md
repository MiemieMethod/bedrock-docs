---
title: Minecraft Beta & Preview - 1.20.10.23
date: 2023-06-14T14:06:49Z
updated: 2023-06-14T17:13:00Z
categories: Beta and Preview Information and Changelogs
link: https://feedback.minecraft.net/hc/en-us/articles/16744110942349-Minecraft-Beta-Preview-1-20-10-23
---

**发布日期：**2023年6月14日

**Minecraft预览版和测试版信息：**

- 这些正在开发中的版本可能不稳定，且可能不代表最终版本的质量
- Minecraft Preview可在Xbox、Windows 10/11和iOS设备上使用。更多信息请参见[aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。加入或退出测试版的详细说明请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

![一张Minecraft的截图，显示一个村民在森林中，旁边有一棵倒下的白桦树，上面有一朵蘑菇。背景中还有一只被栅栏拴住的骆驼，附近有一个营火和一些木桶。](https://feedback.minecraft.net/hc/article_attachments/16744150904333)

新的Minecraft预览版和测试版更新已发布，更多调整和更改以改善您的游戏体验！请继续向我们发送您的[反馈](https://aka.ms/MC120Feedback)和[漏洞报告](https://bugs.mojang.com/)，我们非常感激！以下是此次更新的概览：

# **实验性功能**

## **配方解锁**

- 我们测试了在您已经解锁的配方创建新方式时提供通知。感觉并没有帮助。你知道制作木棍有多少种方法吗？！是的，很多。我们将移除此版本的解锁通知
- 旁观模式是用于旁观，不是解锁配方！通过此修复，当您在旁观模式时不会解锁配方（[MCPE-171073](https://bugs.mojang.com/browse/MCPE-171073)）
- 解锁新配方不再将物品栏切换选项设置为“全部”。可制作切换现在将可靠地保持您离开的方式

## **潜行与爬行**

- 修复了玩家在梯子上时自动潜行的问题（[MCPE-166569](https://bugs.mojang.com/browse/MCPE-166569)）
- 修复了潜行时玩家在梯子顶部卡住的漏洞（[MCPE-171022](https://bugs.mojang.com/browse/MCPE-171022)）
- 爬行时的头部旋转不再直接跟随摄像头旋转（[MCPE-170838](https://bugs.mojang.com/browse/MCPE-170838)）
- 修复了Swift Sneak（迅捷潜行）未增加爬行速度的问题（[MCPE-170885](https://bugs.mojang.com/browse/MCPE-170885)）
- 修复了在关闭潜行与爬行切换时，遗留的爬行功能不能正常工作的问题
- 修复了生成时怪物没有正确碰撞箱的问题（[MCPE-170983](https://bugs.mojang.com/browse/MCPE-170983)）
- 短暂潜行现已“去实验化”，并可在正常游戏过程中使用
- 修复了在方块下滑翔时不应触发爬行动画的问题（[MCPE-170889](https://bugs.mojang.com/browse/MCPE-170889)）
- 现在可以在飞行时强制玩家进入潜行/爬行状态

# **功能与漏洞修复**

## **通用**

- 修复了玩家的披风在前进移动但侧视时未正确摆动的问题（这次真正修复了！）（[MCPE-153446](https://bugs.mojang.com/browse/MCPE-153446)）
- 减少因“发现信息过期认证”导致玩家可能看到“无法连接”错误的情况（[MCPE-170814](https://bugs.mojang.com/browse/MCPE-170814)）
- 修复了在使用鼠标和控制器一起时输入无响应或卡顿的问题（[MCPE-167447](https://bugs.mojang.com/browse/MCPE-167447)）

## **鼠标输入**

- 改善了同时鼠标点击的处理，触发每个单独关联的动作/响应

## **辅助功能**

- 当在聊天屏幕悬停在“/”按钮上时，文本转语音复述功能现在会说“斜杠按钮”
- 默认聊天持续时间现在设置为10秒，而默认吐司通知持续时间保持为3秒
- 文本转语音复述功能现在会在热栏选择物品时朗读物品名称

## **活动对象**

- 修复了无法在不先手动卸下坐骑的情况下切换坐骑的问题（[MCPE-170894](https://bugs.mojang.com/browse/MCPE-170894)）

## **方块**

- 南瓜、雕刻南瓜和点燃南瓜的“minecraft:cardinal_direction”状态字符串现在在世界更新期间被接受
- 蘑菇现在能够在倒下的树干上生成（[MCPE-138333](https://bugs.mojang.com/browse/MCPE-138333)）
- 潮涌核心放置在地面上时现在拥有正确的光照（[MCPE-169732](https://bugs.mojang.com/browse/MCPE-169732)）

## **游戏玩法**

- 移除了使用木棍合成木桶的配方（[MCPE-170848](https://bugs.mojang.com/browse/MCPE-170848)）
- 实体在Powder Snow（细雪）块附近时不会继续冻结（[MCPE-169453](https://bugs.mojang.com/browse/MCPE-169453)）

## **雕纹书架**

- 从雕纹书架中移除附魔书时现在播放了正确的音效（[MCPE-168119](https://bugs.mojang.com/browse/MCPE-168119)）
- 雕纹书架槽位的交互现在是对称的（[MCPE-164801](https://bugs.mojang.com/browse/MCPE-164801)）

## **船**

- 升级到Trails and Tales后，船仍能携带乘客（[MCPE-169772](https://bugs.mojang.com/browse/MCPE-169772)）
  - 受此错误影响的船再次可以携带乘客

## **用户界面**

- 使用控制器时，光标不再随机跳到物品栏的一个槽位（[MCPE-171203](https://bugs.mojang.com/browse/MCPE-171203)）
- 马和驴的跳跃栏以及骆驼的冲刺栏，现在可以正确地与经验栏同步缩放（[MCPE-156444](https://bugs.mojang.com/browse/MCPE-156444)）

## **命令**

- */time query* 命令现在将在绝对时间为负时返回正确的日和时间

# **技术更新**

## **专用服务器**

- 修复了allowlist.json中无效条目导致崩溃的问题（[BDS-18133](https://bugs.mojang.com/browse/BDS-18133)）

## **附加包和脚本引擎**

- 实际修复了导致玩家披风在前进移动但侧视时停止摆动的错误，通过将使用的旋转从玩家的视线旋转切换到玩家的身体旋转（[MCPE-153446](https://bugs.mojang.com/browse/MCPE-153446)）
- 侦测器方块使用状态“minecraft:facing_direction”而非“facing_direction”。“minecraft:facing_direction”使用字符串值（“down”、“up”、“north”、“south”、“east”、“west”）

## **实体**

- 自定义实体不再仅限于覆盖1.20之前发布的原版实体。所有原版实体都可以在“identifier”或“runtime_identifier”字段中使用，包括骆驼和嗅探兽

## **物品**

- 在1.20.10及更高的JSON格式中，将“minecraft:shooter”物品组件从实验性中释放
- 在1.20.10及更高的JSON格式中，将“minecraft:throwable”物品组件从实验性中释放
- 在1.20.10及更高的JSON格式中，将“minecraft:projectile”物品组件从实验性中释放
- 在1.20.10及更高的JSON格式中，将“minecraft:can_destroy_in_creative”物品组件从实验性中释放
- 在1.20.10及更高的JSON格式中，将“minecraft:hover_text_color”物品组件从实验性中释放

## **编辑器**

编辑器处于早期开发阶段，并可在Windows PC Bedrock Preview构建版上通过键盘/鼠标使用。了解[如何使用](https://aka.ms/LearnEditor)编辑器并加入[GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions)论坛，发布错误，查看更详细的发布说明。在社交渠道上用#BedrockEditor标签标记我们。

- 修复了与初始脚本加载相关的错误消息未在日志面板中显示的错误
- /scriptEvent 命令现在可以在编辑器中使用，无需启用测试版API实验
- 修复了在使用D3D11的设备上视口缩放无法正常工作的问题

# **实验性技术更新**

## **API**

- 动态属性标识符现在限制为1024个字符。
- 移除了在*@minecraft/server中定义的MinecraftEffectTypes。请参见@minecraft/vanilla-data NPM包获取等效内容。

*将几个API迁移到稳定的1.3.0版本：*

- 将*tryTeleport(location: Vector3, duration: number, options: ScriptTeleportOptions)*迁移到*1.3.0*
- 将*teleport(location: Vector3, options: ScriptTeleportOptions)*迁移到*1.3.0*
- 将函数*getComponent*迁移到*1.3.0*
- 将世界事件*PlayerJoinAfterEvent*迁移到*1.3.0*
- 将世界事件*PlayerLeaveAfterEvent*迁移到*1.3.0*
- 将世界事件*PlayerSpawnAfterEvent*迁移到*1.3.0*
- 将实体组件*EntityHealableComponent*迁移到*1.3.0*
- 将实体组件*EntityHealthComponent*迁移到*1.3.0*
- 将类*FeedItem*迁移到*1.3.0*
- 将类*FeedItemEffect*迁移到*1.3.0*
- 将*addEffect(effectType: string | EffectType, duration: number, options: EntityEffectOptions)*迁移到*1.3.0*
- 将*getEffect(effectType: string | EffectType)*迁移到*1.3.0*
- 将*getEffects*迁移到*1.3.0*
- 将*removeEffect(effectType: string | EffectType)*迁移到*1.3.0*
- AfterEvents
  - 将*ButtonPushEvent*迁移到*1.3.0*
  - 将*LeverActivateEvent*迁移到*1.3.0*
- 将函数*spawnEntity*迁移到*1.3.0*
- 将函数*spawnItem*迁移到*1.3.0*

*生成点更新：*

- 移除了函数*clearSpawn*
- 移除了属性*spawnDimension*
- 新增函数*getSpawnPoint: DimensionLocation | undefined* - 返回玩家的生成点
- 新增函数*setSpawnPoint(spawnPoint?: DimensionLocation): void* - 设置玩家的生成点，若*spawnPoint*为*undefined*则清除
- 将函数*getDefaultSpawnPosition*重命名为*getDefaultSpawnLocation*
- 将函数*setDefaultSpawn*重命名为*setDefaultSpawnLocation*
- DimensionLocation
  - 新增接口*DimensionLocation* - 表示一个维度中的位置
- 为*ScoreboardObjective*新增*hasParticipant*函数
- 以下*ScoreboardObjective*中的函数现在可以接受*Entity*或*string*类型作为*participants*参数：
  - *getScore*
  - *setScore*
  - *removeParticipant*
- 移除了*ScoreboardIdentity*和*Scoreboard*中的*getScore*、*setScore*
- 从*ScoreboardIdentity*中移除了*removeFromObjective*函数
- 修复了当从脚本更新记分板值时，客户端不会更新的问题
- 射线投射
  - 更改函数*getBlockFromRay*
    - 将返回类型从*Block*更改为*BlockRaycastHit | undefined*
  - 更改函数*getEntitiesFromRay*
    - 将返回类型从*Entity[]*更改为*EntityRaycastHit[]*
  - 更改函数*getBlockFromViewDirection*
    - 将返回类型从*Block*更改为*BlockRaycastHit | undefined*
  - 更改函数*getEntitiesFromViewDirection*
    - 将返回类型从*Entity[]*更改为*EntityRaycastHit[]*
  - 新增接口*BlockRaycastHit*
  - 新增接口*EntityRaycastHit*
- 将leverActivate after event重命名为leverAction
  - 移除了类*EntityHitAfterEvent*。
  - 新增类*EntityHitBlockAfterEvent*
  - 新增类*EntityHitEntityAfterEvent*
  - 类*WorldAfterEvents*
    - 移除了属性*entityHit*
    - 新增属性*entityHitBlock*
    - 新增属性*entityHitEntity*
  - 为多个类新增辅助函数*isValid*，以检查对象是否有效。这可以在访问或使用对象之前安全地用于检查本地对象的句柄，以确保底层对象仍然存在且有效。
    - Block（检查块位置是否在边界内且包含的区块已加载且正在刻）
    - Container（检查相关的容器物品栏是否存在且有效）
    - Effect（检查拥有的实体是否有效且效果存在于该实体上）
    - ScreenDisplay（检查拥有的玩家是否有效）
    - ScoreboardObjective（检查目标条目是否存在且附加到有效的记分板）
    - Entity（检查实体是否存在于世界中。如果实体已死，将返回true）
      - Player
      - SimulatedPlayer（注意，模拟玩家不会自动从世界中移除，因此*isValid*将在它们死亡后仍长时间返回true）
    - ContainerSlot（检查物品上下文是否有效：容器存在于世界中，如拥有的实体，且槽位在容器范围内）
      - 之前作为只读属性存在，现更改为方法以保持一致
    - Component
      - EntityAttributeComponent（检查拥有的实体是否有效且属性存在于实体上）
      - BlockLiquidContainerComponent（检查方块是否存在且为有效的炼药锅类型）
        - 新增只读方法*isValidLiquid*，用于检查炼药锅中的液体是否与相关组件匹配（例如，BlockLavaContainerComponent检查是否为熔岩）
      - EntityComponent（检查拥有的实体是否存在）
      - ItemComponent（检查拥有的物品是否存在）

<!-- -->

- World
- 将*getTime*重命名为*getTimeOfDay*。
- 将*setTime*重命名为*setTimeOfDay*。
- *setTimeOfDay*现在接受*TimeOfDay*枚举作为参数。
- *setTime*的*timeOfDay*参数现在必须在0-23999之间（含）
- 新增*getDay*

更新了以下枚举的值，使其为PascalCase而非camelCase：

- *ClipboardMirrorAxis*
- *ClipboardRotation*
- *HttpRequestMethod*
- *FormCancelationReason*
- *Direction*
- *DisplaySlotId*
- *EntityLifetimeState*
- *FluidType*
- *ObjectiveSortOrder*
- *ScoreboardIdentityType*
- *ScriptEventSource*
- *SignSide*
- *WatchdogTerminateReason*
- *WeatherType *

## **实验性摄像机**

- 摄像机预设JSON现在支持一个可选的布尔值‘player_effects’，当此预设激活时会使用玩家效果状态（例如夜视）进行游戏渲染。新增“example:example_player_effects”预设以展示此功能
- 摄像机命令现在可以接受‘facing’选项，而不是使用带有目标实体或位置的‘rot’选项
- 修复了自定义摄像机在玩家头部位于方块内时不使用“方块内部”效果的问题（[MCPE-170206](https://bugs.mojang.com/browse/MCPE-170206)）

## **物品**

- 在1.20.10及更高的JSON格式中弃用了“minecraft:render_offsets”组件
- 更改了“minecraft:shooter”中的充能动作行为以匹配原版弩，更改了“minecraft:shooter”充能后在物品栏/副手为空时的射击行为，使其成功射出充能弹药