---
title: Minecraft Beta & Preview - 1.21.10.20
date: 2024-05-21T12:59:47Z
updated: 2024-05-24T09:32:37Z
categories: Beta 和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/26899699762061-Minecraft-Beta-Preview-1-21-10-20
hash:
  h_01HYDM41B624607MHH5CAT6SPK: 功能与漏洞修复
  h_01HYDM41B6G9E2DRHDR1PR7WCM: 试炼刷怪笼
  h_01HYDM41B6Y7J3EHGBZQWQGCXS: 命令
  h_01HYDM41B6P6N422QQ57JS1328: 游戏技巧
  h_01HYDM41B6Y8WEZSZKAGHZ4BJ8: 游戏玩法
  h_01HYDM41B6XYNEZMDKNW9NARGN: 物品
  h_01HYDM41B6BGWJE38HGQ9BQ6CQ: 市场
  h_01HYDM41B62QWVXTTSD5G36JZP: 生物
  h_01HYDM41B631V68S5D0YENYYZD: 石化橡木台阶
  h_01HYDM41B7FNW5G89MQJ4F0J7P: 投射物
  h_01HYDM41B7JEETJNKKRVXHFFXC: 领域
  h_01HYDM41B7G9ZV6FH34JJG4JZF: 试炼密室
  h_01HYDM41B7GZSC6C4V9D4MCGHQ: 用户界面
  h_01HYDM41B7H98EWW0ER308DA1A: 宝库
  h_01HYDM41B7D9BSEMYP4F0KAB8Z: 技术更新
  h_01HYDM41B70ZVBN058FQH6YPZ6: 附加包与脚本引擎
  h_01HYDM41B72DX0E1MDFFBNMDV2: API
  h_01HYDM41B7A0942PFNG5DEJYGS: 方块
  h_01HYDM41B7R36W819FJY6DB6VH: 编辑器
  h_01HYDM41B7B3C1GBEAS7ADXGB9: 实体
  h_01HYDM41B7PFVC0PDQB4WM2VPK: 通用
  h_01HYDM41B7TZT5KWPAT1HF93AA: 图形
  h_01HYDM41B7SB3Y2F9WYM3P68Q6: 物品-1
  h_01HYDM41B7B8E3SJHCXD35JG4W: Molang
  h_01HYDM41B73M68A5XM6EGVQDJG: 技术实验性更新
  h_01HYDM41B715NZSCYPPCB9XQGG: API-1
  h_01HYDM41B76T8445T8QKZB0YYK: 组件
  h_01HYDM41B7PGX8RP8A429QF5X6: 通用-1
  h_01HYDM41B7SD3FENM4PHTTQKCD: 图形-1
---

**发布于：** 2024年5月22日

**Minecraft 预览版和测试版信息：**

- 这些开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft 预览版可在 Xbox、PlayStation 4、Windows 10/11 和 iOS 设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在 Android（Google Play）上获取。加入或退出测试版的详细说明请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

![丛林生物群系边缘的传送门废墟，丘陵上的丛林神庙](https://feedback.minecraft.net/hc/article_attachments/26900163666957)

这是最新的 Minecraft 基岩版测试版和预览版更新的新增内容！请继续在 [feedback.minecraft.net](https://feedback.minecraft.net/) 提交您的建议，并在 [bugs.mojang.com](https://bugs.mojang.com/) 报告并点赞您发现的任何漏洞！

# 功能与漏洞修复

## 试炼刷怪笼

- 修复了一些试炼刷怪笼的纹理不一致问题 ([MCPE-181455](https://bugs.mojang.com/browse/MCPE-181455))

## 命令

- '/stopsound' 命令不再停止音乐

## 游戏技巧

- 为触屏设备添加了游泳提示
- 现在在使用 D 键盘控制方案的触屏设备上教玩家如何移动

有时不是学习新游戏技能的好时机。例如，当你刚发现地板是熔岩时，打开物品栏不是一个相关技能。因此，以下是游戏提示不显示时的额外限制：

- 游泳游戏提示只在你在水中时显示
- 当你在细雪中冻结时，“破坏方块”提示是最相关的提示。其他提示不会显示
- 当附近有敌对生物时，你仍然可以学习有助于逃跑的技能（移动、跳跃和摄像机移动），但其他提示不会打扰你

## 游戏玩法

- 台阶和楼梯不再在连续建造时随机开始摆放在底部 ([MCPE-54855](https://bugs.mojang.com/browse/MCPE-54855))
- 修复了一个导致在生成点数千块远的地方环境显著变化的漏洞 ([REALMS-11625](https://bugs.mojang.com/browse/REALMS-11625))
- 在破坏树叶时生成的粒子现在与被破坏树叶的颜色匹配 ([MCPE-179726](https://bugs.mojang.com/browse/MCPE-179726))
- 定位地图现在只渲染头颅和头颅附着物 ([MCPE-61891](https://bugs.mojang.com/browse/MCPE-61891))
- 当玩家在沉重核心区块上行走时发出的声音现在由音频偏好设置中的相应滑块控制

## 物品

- 旋风棒现在在第三人称视角中正确显示 ([MCPE-179661](https://bugs.mojang.com/browse/MCPE-179661))
- 重锤不再像剑和其他锋利物品那样快速破坏蜘蛛网和竹子 ([MCPE-179754](https://bugs.mojang.com/browse/MCPE-179754))
- 钓鱼竿钩子不再粘在具有投射物反射组件的活动对象上 ([MCPE-180337](https://bugs.mojang.com/browse/MCPE-180337))
- 重锤的猛击攻击不再击退被玩家驯服的生物 ([MCPE-180962](https://bugs.mojang.com/browse/MCPE-180962))
- 使用带有风爆魔咒的重锤攻击实体不再抵消坠落伤害 ([MCPE-181496](https://bugs.mojang.com/browse/MCPE-181496))

## 市场

- 修复了与下载内容卡住相关的多个漏洞，包括“下载全部停留在0%”和内容更新失败的错误 ([MCPE-177684](https://bugs.mojang.com/browse/MCPE-177684))

## 生物

- 沼骸的水下近战攻击不再对受害者施加缓慢效果 ([MCPE-178884](https://bugs.mojang.com/browse/MCPE-178884))
- 鹦鹉现在在附近时正确模仿沼骸
- 女巫现在在死亡时总会掉落4-8红石粉
  - 这旨在提高利用女巫小屋获取红石粉的农场的可行性

## 石化橡木台阶

- “stone_block_slab” 的橡木台阶变体（附加值2）现在被平铺为新的方块 "minecraft:petrified_oak_slab" ([MCPE-180964](https://bugs.mojang.com/browse/MCPE-180964))
  - 行为类似于其他石头台阶，例如不可被火毁坏，但看起来像普通的橡木台阶
  - "minecraft:petrified_oak_slab" 只能通过命令获得和摆放
- “double_stone_block_slab” 的橡木台阶变体（附加值2）现在被平铺为新的方块 "minecraft:petrified_oak_double_slab" ([MCPE-180964](https://bugs.mojang.com/browse/MCPE-180964))
  - 行为类似于其他石头双台阶，例如不可被火毁坏，但看起来像普通的橡木双台阶
  - "minecraft:petrified_oak_double_slab" 只能通过命令摆放

## 投射物

- 风弹投射物现在可以通过 /summon 命令召唤 ([MCPE-178937](https://bugs.mojang.com/browse/MCPE-178937))

## 领域

- 领域购买界面上的所有物品现在都可以聚焦，并且可以通过游戏手柄输入进行导航
- 移除了 Minecraft 百科中的领域部分多余的 “the”

## 试炼密室

- 试炼密室现在在深暗之域生物群系中生成的频率大大降低

## 用户界面

- 我们已经在预览版中测试了修复后的 D 键盘调整几周，欢迎在这里提供您的反馈：<https://aka.ms/newdpadfeedback>
- 当生命恢复效果激活时，HUD 上的心脏不再移动过快 ([MCPE-180864](https://bugs.mojang.com/browse/MCPE-180864))
- Shift+点击物品栏物品不再导致物品堆叠计数在堆叠上方短暂出现
- 在玩家可达范围之外与方块互动不再导致方块界面短暂出现
- 在创建新世界和编辑世界时为极限模式添加了新的视觉元素，并在切换极限模式开关时添加了音效（仅预览版）
- 快速移动时，物品不再在堆叠数量前方显示 ([MCPE-180712](https://bugs.mojang.com/browse/MCPE-180712))
- 村民交易菜单中，物品堆叠上的数字不再与物品悬停文本重叠 ([MCPE-181338](https://bugs.mojang.com/browse/MCPE-181338))
- 快速移动到铁砧后，物品不再在槽位中略微移动 ([MCPE-180275](https://bugs.mojang.com/browse/MCPE-180275))
- 切换创造模式物品栏标签时，触屏设备上的物品不再保持选中状态 ([MCPE-173506](https://bugs.mojang.com/browse/MCPE-173506))
- 现在可以通过在移动设备的创造模式物品栏中点击其他物品来移除副手槽和合成网格中的物品 ([MCPE-168757](https://bugs.mojang.com/browse/MCPE-168757))

## 宝库

- 试炼密室中从宝库中弹出的战利品现在依赖于等级、位置和玩家种子

# 技术更新

## 附加包与脚本引擎

- 当生物群系 JSON 中的 ‘snow_accumulation’ 数组的最小值设置高于最大值时，添加内容错误
- 修复了摄像机在非缓动摄像机设置命令后有时出现可见平滑运动的问题 ([MCPE-181364](https://bugs.mojang.com/browse/MCPE-181364))
- 修复了在上传到领域时导致侧载 .mcpack 文件无法应用的问题

## API

- 修复了一个漏洞，阻止 *get* 和 *StructureManager.place* 从结构目录根目录加载结构
- *MinecraftItemTypes* 不再包含旧的物品名称
- 修复了在从 *runCommand()* 和 *Dimension.runCommandAsync()* 脚本 API 执行运行命令时导致游戏崩溃的漏洞
- 药水
  - 添加了包含用于检索与药水相关类型的句柄的 *Potions* 类
  - 添加了与 *MinecraftPotionEffectTypes* 相关联的药水效果类型句柄 *PotionEffectType* 类
  - 添加了与 *MinecraftPotionModifierTypes* 相关联的药水修饰类型句柄 *PotionModifierType* 类
  - 添加了与 *MinecraftPotionLiquidTypes* 相关联的药水类型句柄 *PotionLiquidType* 类
  - 添加了可以从有效药水 *ItemStack* 获取的 *ItemPotionComponent* 类
  - 为 *createPotion* 添加了用于的接口 *PotionOptions*
  - 添加了用于创建有效药水物品的函数 *createPotion*
- 原版数据
  - 添加了包含药水液体 ID 的枚举 *MinecraftPotionLiquidTypes*
  - 添加了包含药水效果 ID 的枚举 *MinecraftPotionEffectTypes*
  - 添加了包含药水修饰 ID 的枚举 *MinecraftPotionModifierTypes*
- BlockExplodeAfterEvent
  - 将 *BlockExplodeAfterEvent* 从 *beta* 发布到 *1.12.0*
  - 将 *BlockExplodeAfterEventSignal* 从 *beta* 发布到 *1.12.0*
  - 将 *blockExplode* 从 *beta* 发布到 *1.12.0*
- 将 *ItemTypes* 从 *beta* 发布到 *1.12.0*
- 将 *InputPermissionCategory* 从 *beta* 发布到 *1.12.0*
- 将 *PlayerInputPermissions* 和 *inputPermissions* 从 *beta* 发布到 *1.12.0*
- 将 *PlayerInputPermissionCategoryChangeAfterEvent* 和 *afterEvents.playerInputPermissionCategoryChanged* 从 *beta* 发布到 *1.12.0*
- 为 *setCurrentValue* 添加了边界检查。提供的值将被限制在此属性的范围内
- 游戏规则
  - 将 *ShowDaysPlayed* 从 *beta* 发布到 *1.12.0*
  - 将 *showDaysPlayed* 从 *beta* 发布到 *1.12.0*
- EnchantmentTypes
  - 将 *getAll(): EnchantmentType[]* 从 *beta* 发布到 *1.12.0*
- EntityRaycastOptions
  - 将 *ignoreBlockCollision* 从 *beta* 发布到 *1.12.0*
  - 将 *includeLiquidBlocks* 从 *beta* 发布到 *1.12.0*
  - 将 *includePassableBlocks* 从 *beta* 发布到 *1.12.0*
  - 将 *hitBlockPermutation* 从 *EntityHitBlockAfterEvent* 发布到 *beta* 到 *1.12.0*
- 将 *addEffect* 方法在 *Entity* 上的 *beta* 版本发布到 *3.0*，为新创建的效果添加了返回类型（如果未添加任何效果，则为未定义）

## 方块

- 修复了在潜行时与命令块、拼图块和结构块互动可能导致 UI 多次打开/关闭的漏洞
- 脚手架方块在远距离移动时不再闪烁 ([MCPE-120910](https://bugs.mojang.com/browse/MCPE-120910))
- 当使用 /setblock 命令放置时，顶部雪/雪层方块现在会坠落
- “double_stone_block_slab” 方块现在分裂为独特实例 “smooth_stone_double_slab”、“sandstone_double_slab”、“oak_double_slab”、“cobblestone_double_slab”、“brick_double_slab”、“stone_brick_double_slab”、“quartz_double_slab” 和 “nether_brick_double_slab”
  - ID “oak_double_slab” 已经从 “double_wooden_slab” 分离，因此任何 “double_stone_block_slab:2” 将被转换为已存在的 “oak_double_slab” ID
- “monster_egg” 方块现在分裂为独特实例：“infested_stone”、“infested_cobblestone”、“infested_stone_bricks”、“infested_mossy_stone_bricks”、“infested_cracked_stone_bricks” 和 “infested_chiseled_stone_bricks”
- “infested_cobblestone” 方块的破坏时间已更改为符合 Java 版
- “stonebrick” 方块现在分裂为独特实例：“stone_bricks”、“mossy_stone_bricks”、“cracked_stone_bricks” 和 “chiseled_stone_bricks”
- “平滑石砖” 方块现在不能通过命令获得，现有的 “平滑石砖” 将被转换为 “石砖”
- “stone_block_slab3” 方块现在分裂为独特实例 “end_stone_brick_slab”、“smooth_red_sandstone_slab”、“polished_andesite_slab”、“andesite_slab”、“diorite_slab”、“polished_diorite_slab”、“granite_slab” 和 “polished_granite_slab”
- “prismarine_slab”、“dark_prismarine_slab”、“prismarine_brick_slab”、“andesite_slab”、“polished_andesite_slab”、“diorite_slab”、“polished_diorite_slab”、“granite_slab” 和 “polished_granite_slab” 的破坏时间现在为1.5
- “end_stone_brick_slab” 的破坏时间现在为3.0
- “stone_block_slab2” 方块现在分裂为独特实例 “red_sandstone_slab”、“purpur_slab”、“prismarine_slab”、“dark_prismarine_slab”、“prismarine_brick_slab”、“mossy_cobblestone_slab”、“smooth_sandstone_slab” 和 “red_nether_brick_slab”

## 编辑器

编辑器及其对应的 API 处于早期开发阶段，适用于 Windows PC 基岩预览版本的键盘/鼠标。请在社交渠道上使用 **#BedrockEditor** 标签与我们互动。

学习 [如何使用](https://aka.ms/LearnEditor) 编辑器，加入 [GitHub 讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛与团队交流，并通过 [starter kit](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [samples](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

本周更新：

- 添加了一个新的粘贴预览工具，支持剪贴板内容的预览可视化，并启用了旋转和镜像。键盘绑定也添加了额外功能
  - SHIFT+CTRL+V - 激活粘贴预览模式（如果剪贴板中有内容）
  - CTRL+C - 将选择内容复制到剪贴板
  - CTRL+V - 立即粘贴到光标位置（无预览）
  - 箭头键/Pg UP/Pg DN - 手动将3D方块光标在相机相对方向上轻微移动
  - CTRL + 箭头键/Pg UP/Pg DN - 手动在剪贴板物品的范围内将轴心位置在相机相对方向上轻微移动
  - SHIFT+CTRL + 箭头键/Pg UP/Pg DN - 手动在相机相对方向上轻微移动放置偏移
  - CTRL+D 或 ESC - 取消选择预览模式
  - 左键点击、ENTER 或 CTRL+F - 将粘贴预览放置在3D方块光标位置的世界中
  - CTRL + 鼠标点击 - 以剪贴板物品的形状移除方块（注意：当前实现仅使用边界框...复杂形状的移除仍在开发中）
  - B - 光标方块模式
  - F - 光标相邻（面）模式
  - R - 围绕轴心点顺时针旋转循环（0, 90, 180, 270）绕 Y 轴
  - SHIFT+R - 围绕轴心点逆时针旋转循环（270, 180, 90, 0）绕 Y 轴
  - X - 围绕轴心点镜像 X 轴
  - Z - 围绕轴心点镜像 Z 轴
  - C - 在“键盘与鼠标”或“仅键盘”之间切换光标控制模式
  - D - 将光标控制模式更改为“固定距离”
  - 滚轮 - 调整固定光标距离（仅在启用固定距离时）
- 修复了反复点击刷子工具设置中的 “Uniform” 复选框可能导致崩溃的漏洞
- 为 *IMenu* 和 *IMenuCreationParams* 添加了 *enabled* 属性
- 为动作栏添加了自定义和分页支持。动作选择器可以通过加号按钮打开以添加新项目，或通过现有项目的右下角箭头打开以修改它们
- 更新了 SimpleTool 类的文档
- 雪层现在在使用刷子放置时会坠落

## 实体

- 装备到 "minecraft:equippable" 第二槽的盔甲现在应用于 "slot.armor.body" 而不是 "slot.armor.torso"
  - 要检索有关信息，应现在使用 "query.armor_texture_slot"、"query.armor_color_slot" 和 "query.armor_damage_slot" 并赋值为4
  - 此更改仅影响格式版本等于或大于 *21.10* 的实体

## 通用

- 更新了地物规则模式的架构文档

## 图形

- 存档截图缩略图现在支持 RTX 和延迟技术预览世界
- 使用 "minecraft:particle_appearance_lighting" 组件的粒子发射器现在使用正确的光照级别，而不是世界原点的光照级别

## 物品

- 当物品图标纹理名称包含命名空间或不匹配物品名称时，修剪过的自定义盔甲物品图标现在正确显示
- \[BETA\] 引入 "slot.armor.body" 作为马等实体的额外盔甲槽，仅限于单个盔甲物品但需要完整盔甲套装的效果
  - "slot.armor.body" 支持：
    - 命令（即使当前没有适合操作的物品）
    - "minecraft:attachable"
    - "minecraft:interact"
    - "query.armor_texture_slot"（值为4）
    - "query.armor_color_slot"（值为4）
    - "query.armor_damage_slot"（值为4）
    - "query.equipment_count"
    - "has_equipment" 实体过滤器（域为 "body"）
    - "all_slots_empty" 实体过滤器（域为 "body"）
    - "any_slot_empty" 实体过滤器（域为 "body"）
  - "slot.armor.body" 不支持：
    - "minecraft:wearable"
  - 未来的调整可能会改变装备到 "slot.armor.body" 上的物品如何影响实体的可见性（意图为实体被其他实体检测到的容易程度）、附魔和盔甲保护

## Molang

- 发布了不再需要“即将推出的创作者功能”切换的 *state_time*

# 技术实验性更新

## API

- BlockRecordPlayerComponent
- 添加了 *UIManager* 类和 *uiManager* 对象到 *@minecraft/server-ui* 测试版
  - 为一致性将 componentId 重命名为 *minecraft:record_player*
  - 添加了方法 *getRecord*、*ejectRecord*、*pauseRecord* 和 *playRecord*
  - 移除了方法 *clearRecord*，现在应传递 undefined 给 *setRecord* 以重置
  - 从 *beta* 中移除了属性 *readonly getLifetimeState: EntityLifetimeState*
- 从测试版中移除了枚举 *EntityLifetimeState*
  - 将 *setBlockPermutation(location: Vector3, permutation: BlockPermutation): void* 从测试版移动到 *12.0*
  - 将 *setBlockType(location: Vector3, blockType: BlockType | string): void* 从测试版移动到 *12.0*
  - 将 *getTags(): string[]* 从 *beta* 移动到 *12.0*
  - 将 *hasTag(tag: string): boolean* 从 *beta* 移动到 *12.0*
  - 从测试版中移除了属性 *readonly fallDistance: number*

## 组件

- EntityLeashableComponent
  - 添加了属性 *canBeStolen: boolean*
  - 添加了属性 *hardDistance: number*
  - 添加了属性 *leashHolder: Entity*
  - 添加了属性 *leashHolderEntityId: string*
  - 添加了属性 *maxDistance: number*
  - 添加了属性 *isLeashed: boolean*
  - 将函数 *leash(leashHolder: Entity): void* 重命名为 *leashTo(leashHolder: Entity): void*

## 通用

- 更新了 Chromebook 默认隐藏纸娃娃的切换为 false
- 添加了 'Creator Cameras: 新的第三人称预设' 实验和切换，包括：
  - 新的 'minecraft:follow_orbit' 预设，可通过 /camera 命令访问并可有视图偏移

## 图形

- 在延迟技术预览中移除了大气散射中的多余10倍乘数
  - 这预计会导致现有包中的天空变暗，并将需要内容创建者将 Rayleigh Strength、Mie Sun Strength 和 Mie Moon Strength 各乘以10倍，以实现与之前相同的视觉效果
- 修正了延迟技术预览中 Android 平台的 ACES 色调映射问题。ACES 色调映射现在应在 Android 上提供预期的结果。这不应对其他平台造成任何变化
- 当在延迟技术预览中指定 format_version 为1.21.0或更高时，现在支持天气的体积雾密度设置

# 版本

这是完整的翻译内容，所有专用术语和技术术语均按照指导原则准确翻译。如有进一步需求，请随时提供。