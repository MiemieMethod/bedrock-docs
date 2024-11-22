**发布日期：**2024年1月24日

# **Minecraft 预览版和测试版信息：**

- 这些正在进行中的版本可能不稳定，可能不代表最终版本的质量
- Minecraft 预览版可在 Xbox、Windows 10/11 和 iOS 设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在 Android（Google Play）上使用。加入或退出测试版的详细说明请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

![u7-1 preview.png](https://feedback.minecraft.net/hc/article_attachments/23458261139725)

以下是最新 Minecraft 预览版和测试版的新功能列表。我们一如既往地欢迎您的反馈，请在 [这里](https://aka.ms/MinecraftArmadilloFeedback) 告诉我们您的想法，并在 [bugs.mojang.com](https://bugs.mojang.com/) 报告您可能遇到的任何漏洞。

# **实验性功能：**

## **犰狳**

- 更新了犰狳、犰狳刷怪蛋和犰狳鳞甲的纹理
- 犰狳在扫描潜在威胁时的垂直范围已减少
- 犰狳现在也可以在恶地生物群系变种中找到
- 犰狳现在会驱赶蜘蛛和洞穴蜘蛛，但仅在它们未卷起来时
- 犰狳在水中漂浮更好，并产生更多的水花粒子
- 幼犰狳现在追上父母的速度更快
- 犰狳的卷起行为已增强，以加强其防御能力：
  - 犰狳在卷起时对伤害的抵抗力更强
  - 犰狳在被玩家或生物攻击时会卷起，而不是惊慌
  - 犰狳现在会记录最后攻击它的玩家，将其视为威胁20秒

## **磨制凝灰岩**

- 磨制凝灰岩在实体掉落到其上时现在会播放落下声音（[MCPE-176939](https://bugs.mojang.com/browse/MCPE-176939)）

## **图形**

- 修复了在延迟技术预览中手持物品时物品未在物品栏中显示的问题（[MCPE-177578](https://bugs.mojang.com/browse/MCPE-177578)）
- 修复了延迟技术预览中更多“光线泄漏”的情况（[MCPE-177189](https://bugs.mojang.com/browse/MCPE-177189)）
- 修复了在延迟技术预览中Android设备挂起/恢复后可能出现的光照伪影
- 玩家在第三人称视角下手持的物品现在会投影阴影（延迟技术预览）
- 生物手持的物品现在会投影阴影（延迟技术预览）
- 修复了延迟技术预览中装备在手中的旗帜杆未渲染的问题
- 改进了延迟技术预览中的点光源颜色混合
- 修复了延迟技术预览中摄像机后方的点光源闪现问题

## **旋风人**

- 更新了风弹投射物的模型、纹理和动画，使其看起来更具动态感

## **狼**

- 驯服狼的项圈尺寸已增大，不仅从前方可见，其他角度也可见

## **狼铠**

- 更新了狼铠和狼铠物品的纹理

## **API**

- ItemComponents
  - 在 *ItemCooldownComponent* 中添加了 *isCooldownCategory(cooldownCategory: string) : boolean*
  - 在 *ItemCooldownComponent* 中添加了 *getCooldownTimeRemaining(player: Player) : number*
  - 在 *@minecraft/vanilla-data* 中添加了 *MinecraftCooldownCategoryTypes*
    - 添加了 *getHiddenHudElements(): HudElements[]*
    - 添加了 *isForcedHidden(hudElement: HudElements): Boolean*
    - 添加了 *resetHudElements(): void*
    - 添加了 *setHudVisibility(visible: HudVisibility, hudElements?: HudElements[]): void*
    - 添加了 *hideAllExcept(hudElements?: HudElements[])*
  - 添加了接口 *BlockFilter*。用于按标签、类型和排列组合包含/排除区块
  - BlockRaycastOptions
    - 添加了可选成员 *BlockFilter*
    - 更新了 *getBlockFromRay(location: Vector3, direction: Vector3, options?: BlockRaycastOptions): BlockRaycastHit | undefined*，如果在 *BlockRaycastOptions* 中无法解析 *BlockFilter* 的包含/排除类型，将抛出异常
    - 将 *ItemDurabilityComponent* 从 *beta* 移至 *1.9.0*
  - 调试工具
    - 开始发布调试工具类型信息
    - 添加了一个 *disableWatchdog* 方法，允许在脚本中禁用和启用脚本看门狗
    - 添加了函数 *playSound(soundId: string, location: Vector3, soundOptions?: WorldSoundOptions): void* - 在指定位置为维度内所有玩家播放声音
    - 将 *getAllStates* API 从 *beta* 移至 *stable*
      - *clearJob(jobId: number)* - 现在将清除当前刻中的迭代以及未来刻中计划的迭代。以前仅清除未来刻中的迭代
    - @minecraft/server.WeatherChangeAfterEvent
      - 将 *WeatherChangeAfterEvent* 从 *beta* 移至 *stable*
      - 将 *setOnFire* 从 *beta* 移至 *1.9.0*
      - 将 *extinguishFire* 从 *beta* 移至 *1.9.0*
    - 将 *EntityOnFireComponent* 从 *beta* 移至 *1.9.0*
      - 将 *getEquipmentSlot* 从 *beta* 移至 *1.9.0*
    - 将 *BlockStateType* 从 *beta* 移至 *1.9.0*
    - 将 *BlockStates* 从 *beta* 移至 *1.9.0*
    - 将 *BlockSignComponent* 从 *beta* 移至 *1.9.0*
    - 将 *DyeColor* 从 *beta* 移至 *1.9.0*
    - 将 *SignSide* 从 *beta* 移至 *1.9.0*
    - 将 *ContainerSlot* 从 *beta* 移至 *1.9.0*
    - 将 *InvalidContainerSlotError* 从 *beta* 移至 *1.9.0*
      - 将 *getSlot* 从 *beta* 移至 *1.9.0*
    - 将 *EffectTypes* 从 *beta* 移至 *1.9.0*
    - 将 *RawText* 从 *beta* 移至 *1.9.0*
      - 将 *createExplosion* 从 *beta* 移至 *1.9.0*
    - 将 *ExplosionOptions* 从 *beta* 移至 *1.9.0*
    - 将 *DimensionType* 从 *beta* 移至 *1.9.0*
    - 将 *DimensionTypes* 从 *beta* 移至 *1.9.0*

# **功能和漏洞修复：**

## **Android**

- 如果在启动游戏之前通过应用设置授予了存储权限，新安装时存储位置将自动切换到外部存储，适用于运行 Android 12 或更早版本的设备（[MCPE-177269](https://bugs.mojang.com/browse/MCPE-177269)）
- 当通过游戏内设置将存储位置设置为外部存储时，下一次启动将在外部存储中生成某些文件和目录，适用于运行 Android 12 或更早版本的设备（[MCPE-176675](https://bugs.mojang.com/browse/MCPE-176675)）

## **区块**

- 修复了一个错误，使玩家在移动时无法放置多个物品，如船或烟花（[MCPE-178063](https://bugs.mojang.com/browse/MCPE-178063)，[MCPE-178077](https://bugs.mojang.com/browse/MCPE-178077)）
  - 由于此修复，我们不得不撤销对台阶和楼梯在持续建造时放置不一致的修复（[MCPE-54855](https://bugs.mojang.com/browse/MCPE-54855)）。我们将在即将更新中重新引入此修复
- 在 Realms 中，在创造模式下从物品展示框中移除物品不再销毁物品展示框（[REALMS-10464](https://bugs.mojang.com/browse/REALMS-10464)）
- 在 Realms 中，在创造模式下从讲台中移除书籍不再销毁讲台（[REALMS-10536](https://bugs.mojang.com/browse/REALMS-10536)）
- “leaves” 区块现在分为独特名称，“oak_leaves”、“spruce_leaves”、“birch_leaves”和“jungle_leaves”
- “leaves2” 区块现在分为 “acacia_leaves” 和 “dark_oak_leaves”
  - 命令仍然可以使用 “leaves” 和 “leaves2”，但在命令提示中仅建议新的叶子名称
- “minecraft:grass” 区块已重命名为 “minecraft:grass_block”，旧名称仍在命令和数据中被理解
- “double_wooden_slab” 区块现在分为独特实例 “double_oak_slab”、“double_spruce_slab”、“double_birch_slab”、“double_jungle_slab”、“double_acacia_slab”、“double_dark_oak_slab”
  - 命令仍然可以使用 “double_wooden_slab”，但不会建议 “double_wooden_slab” 区块
- “wooden_slab” 区块现在分为独特实例 “oak_slab”、“spruce_slab”、“birch_slab”、“jungle_slab”、“acacia_slab”、“dark_oak_slab”
  - 命令仍然可以使用 “wooden_slab”，但不会建议 “wooden_slab” 区块

## **命令**

- 为实体目标选择器添加了 “has_property” 过滤器。这将允许用户根据实体拥有或不拥有的属性来选择目标实体

## **触控控制**

- 玩家死亡时无法再进入自定义触控控制（[MCPE-178037](https://bugs.mojang.com/browse/MCPE-178037)）

## **游戏玩法**

- 甜浆果丛树苗现在在被行走穿过时会减慢玩家的速度（[MCPE-46152](https://bugs.mojang.com/browse/MCPE-46152)）
- 修复了当天花板和地板之间存在大片空气时天空光未正确更新的问题
- 玩家现在可以在水面上搭桥（[MCPE-163165](https://bugs.mojang.com/browse/MCPE-163165)）
- 向上的玩家运动现在会重置跌落距离，允许激流三叉戟帮助阻止跌落（[MCPE-126454](https://bugs.mojang.com/browse/MCPE-126454)）

## **Realms**

- 修复了在 Realms Stories Feed 页面删除最后一个故事时，在某些情况下不会重定向回上一页的问题
- Realms Stories 在发布功能后不再需要重新启动游戏
- 更新了 Realms Plus 登陆页面，使 Realms 订阅工作方式更加清晰

## **盾牌地球图案**

- 更新了盾牌上的地球图案，使其与 Java 版匹配（[MCPE-169595](https://bugs.mojang.com/browse/MCPE-169595)）

## **区块声音**

- 许多区块在实体掉落到其上时现在会播放适当的声音。具体区块如下：（[MCPE-176939](https://bugs.mojang.com/browse/MCPE-176939)）
  - 紫水晶块
  - 紫水晶簇变种
  - 远古残骸块
  - 铁砧块
  - 杜鹃树块
  - 杜鹃树叶
  - 竹子块
  - 竹子木
  - 玄武岩块
  - 大型垂滴叶
  - 骨块
  - 方解石块
  - 蜡烛
  - 洞穴藤蔓
  - 锁链块
  - 樱花树叶
  - 樱花木
  - 雕纹书架
  - 铜块变种
  - 珊瑚块
  - 绯红菌岩块
  - 深板岩块
  - 深板岩砖
  - 滴水石块
  - 青蛙刷怪蛋
  - 蛙明灯
  - 玻璃块
  - 草方块
  - 沙砾块
  - 垂根
  - 悬挂式告示牌
  - 蜂蜜块
  - 梯子块
  - 灯笼块
  - 磁石块
  - 红树根
  - 苔藓块
  - 覆地苔藓
  - 泥巴块
  - 泥砖
  - 沾泥的红树根
  - 下界砖块
  - 下界金矿石块
  - 下界苗
  - 下界疣
  - 下界岩块
  - 灵魂沙块
  - 灵魂土块
  - 孢子花
  - 石块
  - 可疑的沙砾
  - 可疑的沙子
  - 凝灰岩块
  - 海龟蛋块
  - 藤蔓块
  - 诡异菌岩块
  - 诡异疣
  - 木头块
  - 羊毛块

## **Realms 文字转语音**

- 文字转语音叙述器现在将在成员标签页折叠时读取过滤器下拉菜单
- 文字转语音叙述器现在将在成员标签页折叠时读取排序下拉菜单
- 修复了 Realms 插槽屏幕上主面板文本和 Realms Feed 按钮的叙述问题
- 为故事和评论中的时间戳添加了完整的叙述
- 移除了 Realms 设置菜单中“选择退出”按钮的双重叙述

## **用户界面**

- 更新了举报朋友警告模态窗口和举报限制警告模态窗口的设计
- 修复了一个错误，导致清除的文本在物品栏搜索栏中重新出现（[MCPE-174590](https://bugs.mojang.com/browse/MCPE-174590)）

# **原版一致性：**

## **生物**

- 狼现在可以承受与 Java 版相同数量的伤害（[MCPE-177613](https://bugs.mojang.com/browse/MCPE-177613)）
  - 不再像 Java 版那样将对驯服狼的所有伤害减半，而是将驯服狼的最大生命值从20增加到40
  - 预先存在的驯服狼需要通过喂食来达到新的最大生命值
  - 为确保治疗速率保持一致，喂食狼恢复的生命值已加倍
  - Java 版将调整以匹配新的基岩版实现

# **技术更新：**

## **API**

- 添加了 *ScriptGameRules* 和 *gameRules* 以访问和修改游戏规则

## **组件**

- “entity_sensor” 组件的 “range” 字段现在支持两个值，第一个用于水平范围，第二个用于垂直范围
- 这需要 “format_version” 为 1.20.70 或更高

## **编辑器**

编辑器及其相应的 API 处于早期开发阶段，适用于 Windows PC 基岩预览版本的键盘/鼠标。请在社交渠道上使用 **#BedrockEditor** 标记我们。

了解 [如何使用](https://aka.ms/LearnEditor) 编辑器，加入 [GitHub 讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛与团队互动，并通过 [起始套件](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [示例](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

本周更新：

- PropertyPane.addDropdown 函数现在返回一个 IDropdownPropertyItem，可以用于调用新的 “updateDropdownItems” 方法，以更改现有下拉菜单中的下拉项，并可选择设置新的当前选择索引。“updateDropdownItems” 调用相应的 “onChange” 函数，但将旧值传递为 -1，因为列表正在更改条目
- 在玩家位置状态栏条目中添加了相对于玩家位置的光标增量和光标位置处区块的名称
- Vector3 面板现在具有默认的 “minX/Y/Z” 为 “MIN_SAFE_INTEGER”，允许使用负值
  - 当在测试世界属性面板中选中 “在当前地点生成” 选项时，玩家现在将正确地在当前位置生成
- 编辑器中的视口在启用延迟图形的世界中不再错误地偏移

## **实体过滤器**

- 添加了新的实体过滤器 “was_last_hurt_by”，用于检查主体是否是最近攻击实体的最后一个玩家或生物

## **Molang**

- 移除了实验性的 Molang 查询
  - biome_has_any_tag
  - biome_has_all_tags
  - self
  - target
  - client_input_type
  - get_nearby_entities
  - get_nearby_entities_except_self
- 添加了新的 Molang API，允许读取乘骑者身体和头部的旋转
  - rider_body_x_rotation(riderIndex) ⇒ float
  - rider_body_y_rotation(riderIndex) ⇒ float
  - rider_head_x_rotation(riderIndex) ⇒ float
  - rider_head_y_rotation(riderIndex, clampRotation?) ⇒ float
  - ride_body_x_rotation ⇒ float
  - ride_body_y_rotation ⇒ float
  - ride_head_x_rotation ⇒ float
  - ride_head_y_rotation(clampRotation?) ⇒ float

## **NBT 解析**

- NBT 数据的加载现在更加严格。负长度数组、无效的标签 ID 以及有效负载中的字节不足现在都被视为错误，将阻止标签加载，而以前这些情况有时会被忽略

## **预览 Realms**

- 修复了在选择订阅页面按下返回按钮时，在某些情况下会出现 “预览 Realms 无法加载” 消息的错误

## **生成规则**

- “minecraft:spawns_on_block_filter” 现在支持区块描述符
- “minecraft:spawns_on_block_prevented_filter” 现在支持区块描述符
- “minecraft:spawns_above_block_filter” 现在支持区块描述符