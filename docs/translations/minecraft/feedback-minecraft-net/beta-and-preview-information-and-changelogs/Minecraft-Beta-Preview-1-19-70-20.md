---
title: Minecraft Beta & Preview - 1.19.70.20
date: 2023-01-26T14:32:12Z
updated: 2023-01-26T17:40:19Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/zh-cn/articles/12571216557709-Minecraft-Beta-Preview-1-19-70-20
---

**发布于：** 2023年1月26日

**注意：** 本周的Android Beta版本可能会延迟。对于带来的不便，我们深表歉意，正在努力解决该问题。

**Minecraft预览和Beta信息：**

- 这些正在开发中的版本可能不稳定，且可能不代表最终版本的质量
- Minecraft预览适用于Xbox、Windows 10/11和iOS设备。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta版本适用于Android（Google Play）。加入或退出Beta，请参阅[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)了解详细说明

![一个Minecraft的区块截图，显示一个穿着Steve皮肤的玩家在1.5区块的空间中潜行。](https://feedback.minecraft.net/hc/article_attachments/12571212293261)

这是本周Minecraft预览和Beta的新内容列表！关于盔甲修饰的说明：这些可以在最新的[Java Edition快照](https://www.minecraft.net/en-us/article/minecraft-snapshot-23w04a)中进行测试，但它们尚未*完全*准备好用于基岩版Beta和预览，我们会在它们准备好后立即通知您，以便您进行试验，请关注[minecraft.net](http://minecraft.net/)获取最新更新！

一如既往，您可以通过[aka.ms/MC120Feedback](http://aka.ms/MC120Feedback)向我们发送所有反馈和想法，并在[bugs.mojang.com](http://bugs.mojang.com/)报告任何漏洞。

# **实验性功能**

- 热键栏或物品栏中渲染的猪灵的头块的耳朵不再与头的其余部分重叠 ([MCPE-164605](https://bugs.mojang.com/browse/MCPE-164605))
- 玩家在骑乘骆驼时跌落现在会受到伤害

# **功能和漏洞修复**

## **玩家潜行**

- 玩家击中箱高度在潜行时现在减少到1.5区块
  - 在小于1.8区块的缝隙中卡住时，将自动启动潜行
  - 潜行将相应地降低玩家摄像头高度
  - 退出潜行现在需要足够的站立空间
  - 如果玩家无法站立但可以潜行，将从游泳过渡到潜行
- 已知问题，我们希望尽快解决：
  - 第三人称视角下潜行时摄像头可能被区块遮挡
  - 在缝隙中潜行时与某些区块交互可能不起作用
  - 在缝隙中潜行时跳下区块边缘可能无法按预期工作

## **原版趋同**

- 连接到多个区块的钟在破坏一个区块时不再掉落
- 繁殖马现在可以产生随机变种 ([MCPE-129071](https://bugs.mojang.com/browse/MCPE-129071))
- 修复了一个问题，死亡玩家阻止其他玩家跳过夜晚
- 吃喝动画现在将始终居中，无论屏幕纵横比如何
- 音符盒的声音衰减距离现在是线性的 ([MCPE-164935](https://bugs.mojang.com/browse/MCPE-164935))

## **游戏玩法**

- 玩家在触碰有伤害的区块时不再受到快速伤害 ([MCPE-165347](https://bugs.mojang.com/browse/MCPE-165347))
- 修复了在1.8或更高版本中进入1.7.1.0世界时可能发生的崩溃 ([MCPE-165564](https://bugs.mojang.com/browse/MCPE-165564))
- 在游泳/滑翔时射出的投射物不再从玩家位置上方生成 ([MCPE-31896](https://bugs.mojang.com/browse/MCPE-31896))
- 在游泳/滑翔时掉落的物品，无论是手动还是死亡，都不再从玩家位置上方生成 ([MCPE-31896](https://bugs.mojang.com/browse/MCPE-31896))
- 玩家在游泳/滑翔时的十字准星现在正确地挖掘/与前方的物品互动，而不是在其位置上方1区块处 ([MCPE-57257](https://bugs.mojang.com/browse/MCPE-57257))
- 即使玩家拥有相同的成书，也可以在物品栏中移动成书
- 双击熔炉输出槽现在不再掉落物品 ([MCPE-165079](https://bugs.mojang.com/browse/MCPE-165079))
- 修复了一个错误，导致侦测器由于数据损坏而无法检测变化 ([MCPE-150506](https://bugs.mojang.com/browse/MCPE-150506))
- 漏斗现在通过所有比完整区块低高度的区块从上方拉取物品 ([MCPE-55824](https://bugs.mojang.com/browse/MCPE-55824))

## **区块**

- 破坏红树原木或红树木现在会正确导致树叶腐烂
- 占据与某个区块相同空间的末地水晶将不再导致该区块消失

## **图形**

- 修复了在创造模式下用三叉戟瞄准区块时“采矿”提示框出现的问题 ([MCPE-44846](https://bugs.mojang.com/browse/MCPE-44846))

## **生物**

- 鹦鹉在骑乘正在转向中的马时不再摇晃
- 修复了一个错误，导致全局实体（例如末影龙和投射物）在超出正常实体渲染距离时停止渲染 ([MCPE-161136](https://bugs.mojang.com/browse/MCPE-161136))

## **触控控制**

- 更新了“如何玩”屏幕，包含有关新触控控制的信息
- 在物品被选中时从游戏手柄切换到触控模式将返回物品到物品栏或掉落物品
- 修复了熔炉屏幕上的一个问题，双击输出窗口会导致其他槽位变得无法选择
- 修复了一个错误，打开小箱子时逐步选择会自动在第一个槽位启动

## **移动端**

- 在口袋UI中开始新世界时，移除了“按打开聊天以打开聊天”消息，适用于关闭文本转语音的玩家

## **用户界面**

- 海洋探险家、森林探险家和藏宝图现在在物品栏中显示正确的图标 ([MCPE-163464](https://bugs.mojang.com/browse/MCPE-163464))
- 修复了朋友选项下拉菜单鼠标滚动无法滚动下拉内容的错误
- 解决了登录/注册屏幕的图形元素可能超出对话框容器边界的问题

## **命令**

- 替换物品和替换区块的战利品命令不再在炼药锅中放置物品 ([MCPE-129472](https://bugs.mojang.com/browse/MCPE-129472))
- 传送命令中的旋转现在相对于命令执行者而不是目标。命令中旋转的旧用法将保持相对于目标生物，以保持向后兼容性

 

# **技术更新**

## **生物**

- 热带鱼的生成规则.json文件现在位于正确的文件夹中 ([MCPE-165963](https://bugs.mojang.com/browse/MCPE-165963))
- 女巫的药水饮用和远程攻击行为现在在其.json文件中定义

## **创造模式**

- 使用蜜蜂刷怪蛋在刷怪机上时，游戏将不再创建内容错误
- 带有脚本的行为包现在可以从世界中移除

# **实验性技术更新**

## **命令**

- 修复了在执行者在执行前被移除时的延迟命令执行崩溃问题

## **API**

- **重要的破坏性更改：** Beta脚本API中*Location*和*BlockLocation*类不再存在。所有这些类的用法已更改为使用*Vector3*接口（即{x: 1, y: 2, z: 3}对象）。
- 此外，请注意，为了使调用结构更一致，对象的属性和获取/设置方法进行了多项更改（见下文）。
- ItemStack
  - 现在可以通过调用*setLore(undefined)*或*setLore([])*清除物品说明
  - 添加了*clearLore*函数 - 清除物品说明
- ItemStack
  - 修复了一个错误，调用*getComponent*或*ItemStack.getComponents*函数在*EntityItemComponent.itemStack*返回的*ItemStacks*上会失败
- BeforeChatEvent
  - 将函数tell重命名为*sendMessage*
- Block
  - 添加了*isAir*函数 - 返回该区块是否为空气区块（即空旷空间）
  - 添加了*isLiquid*函数 - 返回该区块是否为液体（例如，水区块和熔岩区块是液体，而空气区块和石头区块不是）。
  - 添加了*isSolid*函数 - 返回该区块是否为固体（例如，圆石区块和钻石区块是固体，而梯子区块和栅栏区块不是）。
  - 以下区块现在具有*inventory*组件：
    - 木桶
    - 信标
    - 高炉
    - 酿造台
    - 发射器
    - 投掷器
    - 熔炉
    - 漏斗
    - 唱片机
    - 讲台
    - 烟熏炉
  - 世界事件
    - 添加了*entityDie*事件 - 当一个实体死亡时触发。
    - 将*projectileHit*修改为事件类上的只读属性
  - Player
    - 添加了方法 'getSpawnPosition'：获取出生点位置
    - 添加了属性 'spawnDimension'：获取出生点维度
    - 添加了方法 'setSpawn'(spawnPosition : Vec3, spawnDimension : Dimension) ：设置带有位置和维度的出生点
    - 添加了方法 'clearSpawn'：将出生点位置和维度设置为未定义
  - World
    - 将函数*say*重命名为*sendMessage*
    - 添加了方法 'getDefaultSpawnPosition'：获取默认出生点位置
    - 添加了方法 'setDefaultSpawn'(spawnPosition : Vec3) ：在主世界维度内设置默认出生点位置
  - BeforeChatEvent
    - 添加了*getTargets(): Player[]*函数 - 获取聊天玩家目标
    - 添加了*setTargets(players: Player[])*函数 - 设置聊天玩家目标
    - 移除了*targets*属性
  - BeforeDataDrivenEntityTriggerEvent
    - 添加了*getModifiers(): DefinitionModifier[]*函数 - 获取实体定义修饰符
    - 添加了*setModifiers(modifiers: DefinitionModifier[])*函数 - 设置实体定义修饰符
    - 移除了*modifiers*属性
  - BoolBlockProperty
    - 添加了*getValidValues(): boolean[]*函数 - 获取BoolBlockProperty的所有有效布尔值
    - 移除了*validValues*属性
  - 将*BlockHitInformation*转换为接口
  - ChatEvent
    - 添加了*getTargets(): Player[]*函数 - 获取聊天玩家目标
    - 移除了*targets*属性
  - 将*Color*转换为接口
  - DataDrivenEntityTriggerEvent
    - 添加了*getModifiers(): DefinitionModifier[]*函数 - 获取实体定义修饰符
    - 移除了*modifiers*属性
  - DefinitionModifier
    - 添加了*getComponentGroupsToAdd(): string[]*函数 - 获取将与DefinitionModifier一起添加的组件组
    - 添加了*setComponentGroupsToAdd(newGroups: string[]): void*函数 - 设置将与DefinitionModifier一起添加的组件组
    - 添加了*getComponentGroupsToRemove(): string[]*函数 - 获取将与DefinitionModifier一起移除的组件组
    - 添加了*setComponentGroupsToRemove(removedGroups: string[]): void*函数 - 设置将与DefinitionModifier一起移除的组件组
    - 添加了*getTriggers(): Trigger[]*函数 - 获取DefinitionModifier的事件触发器
    - 添加了*setTriggers(newTriggers: Trigger[]): void*函数 - 设置DefinitionModifier的事件触发器
    - 移除了*componentGroupsToAdd*属性
    - 移除了*componentGroupsToRemove*属性
    - 移除了*triggers*属性
  - DirectionBlockProperty
    - 添加了*getValidValues(): Direction[]*函数 - 获取DirectionBlockProperty的所有有效方向枚举值
    - 移除了*validValues*属性
  - Entity
    - 添加了*getViewDirection(): Vector3*函数 - 获取实体的视方向
    - 添加了*getRotation(): XYRotation*函数 - 获取实体的旋转
    - 添加了*getVelocity(): Vector*函数 - 获取实体的速度
    - 移除了*viewDirection*属性
    - 移除了*rotation*属性
    - 移除了*velocity*属性
  - EntityAgeableComponent
    - 添加了*getDropItems(): string[]*函数 - 获取实体成长时掉落的物品
    - 添加了*getFeedItems(): EntityDefinitionFeedItem[]*函数 - 获取可以喂给实体的物品
    - 移除了*dropItems*属性
    - 移除了*feedItems*属性
  - EntityBreathableComponent
    - 添加了*getBreatheBlocks(): BlockPermutation[]*函数 - 获取实体可以呼吸的区块
    - 添加了*getNonBreatheBlocks(): BlockPermutation[]*函数 - 获取实体不能呼吸的区块
    - 移除了*breatheBlocks*属性
    - 移除了*nonBreatheBlocks*属性
  - EntityHealableComponent
    - 添加了*getFeedItems(): FeedItem[]*函数 - 获取EntityHealableComponent的治疗物品
    - 移除了*items*属性
  - 将*EntityHitInformation*转换为接口
  - EntityRideableComponent
    - 添加了*getFamilyTypes(): string[]*函数 - 获取支持的骑乘实体类型
    - 添加了*getSeats(): Seat[]*函数 - 获取每个座位的骑乘者信息
    - 移除了*familyTypes*属性
    - 移除了*seats*属性
  - EntityTameableComponent
    - 添加了*getTameItems(): string[]*函数 - 获取EntityTameableComponent的驯服物品
    - 移除了*tameItems*属性
  - FeedItem
    - 添加了*getEffects(): FeedItemEffect[]*函数 - 获取FeedItem的效果
    - 移除了*effects*属性
  - IntBlockProperty
    - 添加了*getValidValues(): number[]*函数 - 获取IntBlockProperty的所有有效整数值
    - 移除了*validValues*属性
  - ItemDurabilityComponent
    - 添加了*getDamageRange(): NumberRange*函数 - 获取描述物品失去耐久度几率的数字范围
    - 移除了*damageRange*属性
  - 将*NumberRange*转换为接口
  - ProjectileHitEvent
    - 添加了*getBlockHit(): BlockHitInformation*函数 - 从ProjectileHitEvent获取击中区块的信息
    - 添加了*getEntityHit(): EntityHitInformation*函数 - 从ProjectileHitEvent获取击中实体的信息
    - 移除了*blockHit*属性
    - 移除了*entityHit*属性
  - StringBlockProperty
    - 添加了*getValidValues(): string[]*函数 - 获取StringBlockProperty的所有有效字符串值
    - 移除了*validValues*属性