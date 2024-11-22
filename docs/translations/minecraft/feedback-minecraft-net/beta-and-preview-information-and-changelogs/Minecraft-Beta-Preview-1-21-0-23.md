---
标题: Minecraft Beta & Preview - 1.21.0.23
日期: 2024-04-22T15:15:59Z
更新: 2024-04-24T15:22:22Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/26100457790093-Minecraft-Beta-Preview-1-21-0-23
哈希:
  h_01HW8AJJBAVMT77ZERWX8CQTP7: 特性与漏洞修复
  h_01HW8AJJBAKYK237CQD4ZZTKJJ: 试炼探险家地图
  h_01HW8AJJBA7AD8T3BJ6MPVZAVA: 方块
  h_01HW8AJJBAWAQ2EXFH6NZR2NQ3: 游戏玩法
  h_01HW8AJJBAWQBM7MEK9S5D6BCZ: 图形
  h_01HW8AJJBA1J8Z21PP1WM602D4: 重锤
  h_01HW8AJJBA79DKMQ33FD46GJSP: 生物效果
  h_01HW8AJJBAYPFHVMK3EJW8QC9P: 寄生
  h_01HW8AJJBAQA9PHGV1A2P8XVFF: 盘丝
  h_01HW8AJJBAC7YK4DTM29NZ7YVV: 不祥之瓶
  h_01HW8AJJBBPM392M1WS1QYJWF9: 不祥试炼刷怪笼
  h_01HW8AJJBBHJ59WAHG2K0GWBV5: 传送门
  h_01HW8AJJBBH1ZM5ARVAJEFDTYM: 声音
  h_01HW8AJJBB5BD117W4D62T589F: 试炼密室
  h_01HW8AJJBBEM2X7GVDYHZ9M2QE: 试炼刷怪笼
  h_01HW8AJJBBQK2DS8PC5E2W5KSK: 用户界面
  h_01HW8AJJBBSKHDGKYJWXWPQW0C: 原版趋同
  h_01HW8AJJBB12QKDXX8M4YRPNJV: 生物
  h_01HW8AJJBBWC4SAM0HCXYJDNDF: 宝库
  h_01HW8AJJBBJT1PH314WA8G7CT4: 风弹
  h_01HW8AJJBBTMX2PSY63NX6E9MF: 技术更新
  h_01HW8AJJBBVWWG57GSE956XD27: 接口
  h_01HW8AJJBBYRH36CEARN3DAGT3: 组件
  h_01HW8AJJBBG813TVNNXY4NP1NN: 编辑器
  h_01HW8AJJBB4D38NN1DGC6HCVTW: 技术实验性更新
  h_01HW8AJJBBWHPD7KZ0XHRDPTQX: api-1
  h_01HW8AJJBB1RBAFF8B6PSCNA7P: 图形-1
---

**发布:** 2024年4月24日

**关于Minecraft预览和Beta的信息:**

- 这些正在开发中的版本可能不稳定，并且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、PlayStation 4、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版可在Android（Google Play）上使用。要加入或退出Beta，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一位Minecraft制图师村民站在村庄的制图台旁，手中拿着试炼密室地图。](https://feedback.minecraft.net/hc/article_attachments/26100457788045)

以下是本周预览和Beta中的新内容！我们始终欢迎您的反馈，请通过 [feedback.minecraft.net](https://feedback.minecraft.net/) 告诉我们您的想法，并在 [bugs.mojang.com](http://bugs.mojang.com/) 报告任何漏洞。

# 特性与漏洞修复

## 试炼探险家地图

- 试炼密室地图物品已更名为试炼探险家地图

## 方块

- 在试炼密室中使用陶片制作的饰纹陶罐现在已正确定向 ([MCPE-180380](https://bugs.mojang.com/browse/MCPE-180380))
- “stone_block_slab”方块现在拆分为独特实例“smooth_stone_slab”、“sandstone_slab”、“oak_slab”、“cobblestone_slab”、“brick_slab”、“stone_brick_slab”、“quartz_slab”和“nether_brick_slab”。id“oak_slab”已从“wooden_slab”中拆分，因此任何“stone_block_slab:2”将转变为已存在的“oak_slab” id
- 铜活板门现在会随时间氧化
- 为以下方块添加了缺失的合成配方 ([MCPE-176613](https://bugs.mojang.com/browse/MCPE-176613))
  - 从斑驳的切制铜台阶 x 2 合成斑驳的雕纹铜块
  - 从涂蜡的切制铜台阶 x 2 合成涂蜡的雕纹铜块

## 游戏玩法

- 受到盘丝影响的实体现在可以以正常速度的50%穿过蜘蛛网，而不是25%
- 花丛森林现在生成所有预期的花卉类型 ([MCPE-180417](https://bugs.mojang.com/browse/MCPE-180417))
- 修复了在硬核世界中死亡后返回时旁观模式会禁用穿墙和飞行的问题 ([MCPE-180279](https://bugs.mojang.com/browse/MCPE-180279))
- 修复了一个配方漏洞，任何类型的石头台阶都可以用红色、红树或诡异木板合成砂轮。现在只能接受实际的普通石头台阶，其他类型的石头无效

## 图形

- 修复了火把图标在物品栏中垂直居中的问题 ([MCPE-180527](https://bugs.mojang.com/browse/MCPE-180527))

## 重锤

- 重锤现在也可以附魔耐久、亡灵杀手、火焰附加和节肢杀手 ([MCPE-179679](https://bugs.mojang.com/browse/MCPE-179679))
- 调整了在附魔台中应用重锤独占附魔的费用

## 生物效果

### 寄生

- 蠹虫现在将在寄生实体的边界框中心生成，并朝着实体面朝的方向飞出
- 现在有10%的几率生成1-2只蠹虫，而不是5%

### 盘丝

- 现在在死亡时更一致地生成2-3个蜘蛛网
- 如果“生物破坏”游戏规则关闭，则不再放置蜘蛛网

## 不祥之瓶

- 喝下不祥之瓶获得的不祥之兆将不再在玩家周围发出粒子

## 不祥试炼刷怪笼

- 玩家现在有50%的几率（而不是生物）被选中投掷投射物

## 传送门

- 使用触控控制时，下界传送门可以再次通过破坏传送门表面来摧毁

## 声音

- 更改了施加不祥之兆效果、使用后不祥之瓶破碎以及不祥之兆转变为袭击之兆时的声音
- 添加了4个新的环境洞穴声音

## 试炼密室

- 向密室添加了新的陷阱发射器样式
- 修复了走廊中各种破损的拼图连接
- 添加了新的交叉路口变体
- 重新制作了“密室6”，并将其更名为“组装”
- 密室喷发：
  - 向发射器添加缺失的水桶
- 添加了新的墙面发射器样式

## 试炼刷怪笼

- 试炼刷怪笼在变为不祥状态时现在会发出试炼之兆粒子，而不是幽匿灵魂粒子
- 调整了在不祥状态下投射物掉落的战利品表，以匹配Java版

## 用户界面

- 添加了一个新的HUD覆盖层，显示在世界中玩耍的天数。该覆盖层通过“显示玩耍天数”世界设置启用

## 原版趋同

- 喷溅药水的持续时间现在与可饮用药水相同

## 生物

- 从Bogged client_entity json中移除了不必要的“min_engine_version”，这导致资源包损坏 ([MCPE-178910](https://bugs.mojang.com/browse/MCPE-178910))
- 旋风人现在在朝玩家射击时略微提高瞄准
- 旋风风弹现在可以伤害在船和矿车中的生物
- 导致生物恐慌的伤害类型已被限制 ([MCPE-167513](https://bugs.mojang.com/browse/MCPE-167513))
  - 只有以下伤害会引起恐慌：
    - “营火”
    - “实体攻击”
    - “实体爆炸”
    - “火”
    - “火焰刻”
    - “烟花”
    - “冻结”
    - “熔岩”
    - “闪电”
    - “魔法”
    - “熔岩”
    - “投射物”
    - “冲撞攻击”
    - “音爆”
    - “灵魂营火”
    - “温度”
    - “凋零”
  - Java版也将调整以匹配这一新行为

## 宝库

- 更新了宝库和不祥宝库的战利品表，以匹配Java版 ([MCPE-180499](https://bugs.mojang.com/browse/MCPE-180499))
- 修复了无法使用试炼钥匙打开宝库的漏洞 ([MCPE-180291](https://bugs.mojang.com/browse/MCPE-180291))

## 风弹

- 修复了使用风弹后摔落到黏液块或细雪上时未能抵消摔落伤害的问题 ([MCPE-178878](https://bugs.mojang.com/browse/MCPE-178878)) ([MCPE-178891](https://bugs.mojang.com/browse/MCPE-178891))

# 技术更新

## API

- 修复了*GameRules*规则属性设置器，以便更改可以传播到客户端
- 将*startItemCooldown*和*player.getItemCooldown*从*beta*移动到*1.11.0*
- 将*playSound*从*beta*移动到*1.11.0*
- *playSound*现在已被弃用，将在未来的主要版本中移除。请使用*Dimension.playSound*作为替代
- 将*ListBlockVolume*从*beta*移动到*1.11.0*
- 将*BlockVolumeBase*从*beta*移动到*1.11.0*
- 将*BlockLocationIterator*从*beta*移动到*1.11.0*
- 将方法*getGameMode(): GameMode*从*beta*移动到*1.11.0*
- 将方法*setGameMode(gameMode?: GameMode): void*从*beta*移动到*1.11.0*
- 将成员*playerGameModeChange: PlayerGameModeChangeAfterEventSignal*从*beta*移动到*1.11.0*
- 将成员*playerGameModeChange: PlayerGameModeChangeBeforeEventSignal*从*beta*移动到*1.11.0*
- 将类*PlayerGameModeChangeAfterEvent*从*beta*移动到*1.11.0*
- 将类*PlayerGameModeChangeAfterEventSignal*从*beta*移动到*1.11.0*
- 将类*PlayerGameModeChangeBeforeEvent*从*beta*移动到*1.11.0*
- 将类*PlayerGameModeChangeBeforeEventSignal*从*beta*移动到*1.11.0*
- 为*beta*添加了*ItemComponentConsumeEvent*
- 将*waitTick(ticks?: number)*更改为*system.waitTicks(ticks: number);*
- 将属性*selectedSlot*重命名为*selectedSlotIndex*并将其从*beta*移动到*1.11.0*

## 组件

- “behavior.panic”的“damage_sources”字段的默认值已更新
  - 有关新默认值的完整列表，请参阅更新日志的“原版趋同”部分
  - 此更改仅影响格式版本为1.21.0或更高的实体
- 具有相同自定义组件的多个物品现在将正确触发自定义组件逻辑

## 编辑器

- 当选择体积超出世界高度限制时，将不再创建选择体积
- 在填充体积时，如果在填充操作中拖动体积，填充体积也会改变。现在填充操作发生在原始体积中
- 修复了相机碰撞导致第三人称视角在十字准星模式下显示在玩家头部内部的漏洞

# 技术实验性更新

## API

- EntityTameMountComponent
  - 添加了方法*tameToPlayer*
  - 添加了属性*isTamed*、*isTamedToPlayer*、*tamedToPlayer*和*tamedToPlayerId*
- GameRules
  - 向*beta*添加了属性*showDaysPlayed*
- 修复了*PlayerInputPermissions*输入锁定类别属性设置器，以便更改可以传播到客户端

## 图形

- 修复了延迟技术预览中的体积雾阴影漏洞，该漏洞导致雾比应有的亮得多。延迟技术预览中的体积雾现在与RTX中的体积雾外观更为接近。为延迟技术预览开发的资源包中的雾定义在此更改后需要更新。为了保持相似的外观，"max_density"或"scattering"的值应增加12倍。