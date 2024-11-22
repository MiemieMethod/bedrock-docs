---
标题：Minecraft Beta & 预览 - 1.21.40.20
日期：2024-09-04T13:52:17Z
更新：2024-09-04T21:22:39Z
类别：Beta 和预览信息及更新日志
链接：[https://feedback.minecraft.net/hc/en-us/articles/29937458432397-Minecraft-Beta-Preview-1-21-40-20](https://feedback.minecraft.net/hc/en-us/articles/29937458432397-Minecraft-Beta-Preview-1-21-40-20)
哈希：
  用户内容-实验性特性：experimental-features
  用户内容-附加包：bundles
  用户内容-特性和漏洞修复：features-and-bug-fixes
  用户内容-方块：blocks
  用户内容-命令：commands
  用户内容-游戏玩法：gameplay
  用户内容-图形：graphical
  用户内容-生物：mobs
  用户内容-领域：realms
  用户内容-用户界面：user-interface
  用户内容-原版趋同：vanilla-parity
  01J6YGVDFH2GGV7N6RF98FNEDV：mobs-1
  用户内容-技术更新：technical-updates
  用户内容-附加包和脚本引擎：add-ons-and-script-engine
  用户内容-API：api
  01J6YGVDFGHD8K1Z26TBC2HNND：commands-1
  用户内容-组件：components
  用户内容-编辑器：editor
  用户内容-实体组件：entity-components
  用户内容-实体事件响应：entity-event-responses
  用户内容-通用：general
  01J6YGVDFG1M0EV1N6TS8WJRPA：graphical-2
  用户内容-Molang：molang
  用户内容-资源和行为包：resource-and-behavior-packs
  用户内容-稳定性和性能：stability-and-performance
  用户内容-实验性技术更新：experimental-technical-updates
  01J6YGVDFH75W9YRM4VYPK4VQM：api-1
  用户内容-相机：cameras
---

**发布：** 2024年9月4日

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能与最终版本的质量不符。
- Minecraft预览可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)。
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)获取详细说明。

![一名村民站在村庄中，身后有一只鸡，背景中可以看到繁花森林。](https://feedback.minecraft.net/hc/article_attachments/29937458426637)

是时候进行新的Minecraft预览和Beta了！我们希望您能对附加包提供反馈，请在 <https://aka.ms/mcbundlesfeedback> 告诉我们您的想法，并在 [bugs.mojang.com](http://bugs.mojang.com/) 报告任何漏洞。

**已知问题：** 在此Beta和预览版本中，您可能会发现一些图形渲染问题。我们的团队正在处理此问题，我们希望尽快解决。感谢您的耐心等待！

# 实验性特性

## 附加包

- 当在快捷栏中选择附加包并使用游戏控制器输入时，现已显示“使用”按钮提示（[MCPE-185504](https://bugs.mojang.com/browse/MCPE-185504)）。
  - 使用此按钮会将物品从附加包中扔出。
- 附加包现在在放置于快捷栏时显示其满度的条。
- 从快捷栏使用附加包时，清空物品时会播放声音并触发动画（[MCPE-185460](https://bugs.mojang.com/browse/MCPE-185460)）。
- 附加包的提示框位置现在考虑了屏幕安全区域。
- 在快捷栏中使用附加包时，一次只会清空一组物品，而不是全部一次清空。
- 当将光标悬停在附加包上时，现已显示“清空快捷栏”按钮提示，并启用“清空快捷栏”切换，使用游戏控制器（[MCPE-185504](https://bugs.mojang.com/browse/MCPE-185504)）。
- 当使用游戏控制器将一个物品悬停在另一个物品上时，现已显示“交换”按钮提示。
- 当用游戏控制器将物品悬停在光标上时，现已在所有屏幕上显示“放置”按钮提示。

# 特性和漏洞修复

- 在Nintendo Switch上进行了更改，可能帮助相邻区块在玩家设置最大帧率时更快加载（[MCPE-120971](https://bugs.mojang.com/browse/MCPE-120971)）。

## 方块

- 使用命令放置的藤蔓现在可见（[MCPE-131854](https://bugs.mojang.com/browse/MCPE-131854)）。
- “蘑菇柄”现在是独立的方块，不再是“红蘑菇方块”和“棕蘑菇方块”的变种。
- “头颅”已分为7个独特的实例：“骷髅头”、“凋零骷髅头”、“僵尸头”、“玩家头”、“苦力怕头”、“龙头”、“猪灵头”。

## 命令

- 游戏规则ShowRecipeMessages不再被视为作弊（[MCPE-177299](https://bugs.mojang.com/browse/MCPE-177299)）。
- 向相机命令添加了'entity_offset'参数。

## 游戏玩法

- 风弹在投掷后短时间内无法被击中和重定向。
- 与床互动现在会将其设置为重生点，无论附近是否有敌人（[MCPE-152134](https://bugs.mojang.com/browse/MCPE-152134)）。
- 玩家在生成世界的边缘碰撞时将保持其速度。例如：在使用鞘翅飞行时，玩家将保持漂浮状态，而不是瞬间失去所有速度。

## 图形

- 解决了在iOS上使用大缩放时游戏显示粉色的问题（[MCPE-174398](https://bugs.mojang.com/browse/MCPE-174398)）（[MCPE-185373](https://bugs.mojang.com/browse/MCPE-185373)）。

## 生物

- 北极熊被火或熔岩杀死时现在掉落熟鱼（[MCPE-122488](https://bugs.mojang.com/browse/MCPE-122488)）。
- 掠夺者的“celebrate3”声音现在有效（[MCPE-121058](https://bugs.mojang.com/browse/MCPE-121058)）。
- 狼、猫和鹦鹉在试图追赶主人时，在瞬移后会无缝恢复导航。
- 狼、猫和鹦鹉在惊慌时会瞬移到主人身边，且距离足够远。
- 狼在战斗中与主人距离足够远时会瞬移到主人身边，防止被落下（[MCPE-151765](https://bugs.mojang.com/browse/MCPE-151765)）。

## 领域

- 添加了一个新的领域事件。你能发现它吗？
- 修复了一个通过市场激活领域附加包的漏洞。

## 用户界面

- 在更改维度并重新进入世界时，不再出现关于下马实体的提示（[MCPE-182876](https://bugs.mojang.com/browse/MCPE-182876)）。
- 盔甲HUD在玩家装备的盔甲破损时现在更新正常（[MCPE-103592](https://bugs.mojang.com/browse/MCPE-103592)）。
- 修复了在使用控制器时切石机面板中的关闭按钮子面板为空而不是隐藏的漏洞。
- 添加了新消息以解释当市场模板在特定平台上不可用时的情况。
- 在移动设备的经典用户界面中，饥饿和生命条与经验条对齐（[MCPE-177192](https://bugs.mojang.com/browse/MCPE-177192)）。
- 空气泡现在与饥饿条正确对齐（[MCPE-185268](https://bugs.mojang.com/browse/MCPE-185268)）。
- 玩家纸娃娃在用户界面中的位置在经典和口袋用户界面设置之间保持一致（[MCPE-57498](https://bugs.mojang.com/browse/MCPE-57498)）。
- 具有基于百分比效果的药水在其提示框上正确显示百分号（在移动设备上）（[MCPE-28531](https://bugs.mojang.com/browse/MCPE-28531)）。
- 当被守卫的荆棘杀死时，死亡信息现在显示“‘玩家’因试图伤害‘生物’而被杀”（[MCPE-114752](https://bugs.mojang.com/browse/MCPE-114752)）。
- 聊天消息不再重叠一个像素（[MCPE-119761](https://bugs.mojang.com/browse/MCPE-119761)）。
- 当看向不可交互实体时，物品文本不再跳动（[MCPE-161140](https://bugs.mojang.com/browse/MCPE-161140)）。
- 切石机和织布机的关闭和帮助按钮视觉效果更改为与制图台的视觉效果一致（[MCPE-166008](https://bugs.mojang.com/browse/MCPE-166008)）。
- “隐藏控制器提示”现在在村民交易菜单中正确隐藏所有控制提示（[MCPE-167134](https://bugs.mojang.com/browse/MCPE-167134)）。

## 原版趋同

- 苦力怕被沼骸杀死后现在掉落音乐唱片（[MCPE-179008](https://bugs.mojang.com/browse/MCPE-179008)）。
- 沼骸被玩家驯服的生物杀死后现在掉落毒箭。
- 给绵羊和猫、狗的项圈染色时，现在会播放与Java版相同的染色声音（[MCPE-150684](https://bugs.mojang.com/browse/MCPE-150684)）。
- 用于堆肥桶的蘑菇柄的填充几率已从85%调整为65%。
- 所有面孔的孔蘑菇方块已从创造模式物品栏中移除。
- 附魔金苹果现在提供生命恢复II，而不是生命恢复V，与Java版一致（[MCPE-103061](https://bugs.mojang.com/browse/MCPE-103061)）。
- 向效果命令添加了无限持续时间选项。`/effect <player: target> <effect: Effect> infinite [amplifier: int] [hideParticles: Boolean]`
- 向效果命令添加了特定效果移除选项。`/effect <player: target> clear <effect: Effect>`
- 放置可可豆时现在会播放声音（[MCPE-49126](https://bugs.mojang.com/browse/MCPE-49126)）。
- 蜂箱和蜂巢不再可以作为熔炉的燃料（[MCPE-128393](https://bugs.mojang.com/browse/MCPE-128393)）。

### 生物

- 猪灵将不再捡起并仰慕动力铁轨物品（[MCPE-91187](https://bugs.mojang.com/browse/MCPE-91187)）。

# 技术更新

## 附加包和脚本引擎

- 修复了使用“bone_visibility”作为方块几何体时，导致“item_display_transforms”未正确应用的漏洞（[MCPE-185868](https://bugs.mojang.com/browse/MCPE-185868)）。
- 修复了阻止新1.21.30交易表格式在游戏中加载的问题。

## API

- ItemStack
  - 修复了方法 `ItemStack.getComponents` 返回当前 `@minecraft/server`版本中不支持的组件的问题。
- 修复了无效的ModalFormData从不拒绝或解决其承诺的问题（[MCPE-178148](https://bugs.mojang.com/browse/MCPE-178148)）。
- `BlockLiquidContainerComponents` API（水、熔岩、药水、雪）已从Beta中移除。
- `BlockFluidContainerComponent` API已添加到Beta，替换了 `BlockLiquidContainerComponents`。
- 将 `isHardcore` 从Beta移动到1.15.0。

## 命令

- 为 `schedule` 命令添加了新的重载，允许您清除排队的函数。
  - `/schedule clear <function name>` - 清除所有与给定名称匹配的排队函数。
  - `/schedule on_area_loaded clear function <function name>` - 清除所有按名称排队的`on_area_load`函数。
  - `/schedule on_area_loaded clear tickingarea <tickingarea name> [function name]` - 清除所有按计时区域名称排队的`on_area_load`函数（可选地也检查函数名称）。

## 组件

- “restriction_type”字段已添加到“minecraft:home”组件，允许定义实体如何限制其在家位置的移动：
  - 其值为：
    - “none”，无任何限制。
    - “random_movement”，限制在家位置周围的随机移动。
    - “all_movement”，限制在家位置周围的任何移动。
  - “all_movement”值当前处于\[Beta\]阶段，计划稍后完全发布。
  - 移动过远的实体始终可以在提示下更靠近家位置。
  - 限制的半径仍通过“restriction_radius”指定。
  - 具有1.21.40之前格式版本的实体将以保留其现有行为的方式升级以使用新字段。
- 添加了“minecraft:dimension_bound”组件，防止实体通过传送门改变维度。
  - 在原版内容中，这被末影龙、鱼钩和一些投射物使用。
- 添加了“minecraft:transient”组件，具有此组件的实体将永远不会被保存。在原版内容中，这目前用于鱼钩。

## 编辑器

- 添加了在中间鼠标点击时为当前方块调色板选择方块的功能。
- 添加了自定义方块纹理，现在支持方块图像。
- 添加了资源访问协议“block://\<block_name\>”以检索方块图像。
- 添加了新的API接口 `IStatusBar` 以管理 `IStatusBarItem` 对象。可以通过 `IPlayerUISession`中的 `statusBar` 属性访问。
  - 添加了 `IStatusBarItemCreationParams` 用于状态栏项目初始化。
  - 从 `IStatusBarItem` 中移除了 `text` 属性，改为使用 `getText` 和 `setText` 函数。添加了文本内容的本地化支持。
  - 将 `EditorStatusBarAlignment` 重命名为 `StatusBarAlignment`。
- 将“输入映射”重命名为“键盘设置”操作栏项目，并改进了模态面板的视觉效果。
- 修复了在应用程序挂起/恢复之间，简单方块在快捷栏中丢失方块调色板设置的漏洞。
- 修复了快速开始面板可见性未正确保留的漏洞。
- 修复了创建新编辑器世界时，快捷栏填充默认方块列表而不是全部空气的漏洞。

## 实体组件

- 如果缺少投射物定义，“behavior.fire_at_target”将不再可用，并将在这种情况下抛出内容错误。

## 实体事件响应

- 添加了“execute_event_on_home_block”实体事件响应，允许实体在其家位置的方块上执行事件。
  - “event”字段允许指定要执行的事件。
  - 为使其正常工作，该实体必须具有设置了家位置的“minecraft:home”组件。

## 通用

- 对“minecraft:single_block_feature”进行了以下更改：
  - “places_block”现在支持加权方块说明符列表。
  - 新的“randomize_rotation”属性。
  - 新的“may_not_attach_to”放置条件。
  - 添加了“diagonal”作为“may_attach_to”条件的新选项。
  - 文件格式版本增加到1.21.40。

## 图形

- 修复了红石粉的镶嵌与以下方块的供电状态不匹配的漏洞：
  - minecraft:\*\_slab
  - minecraft:chain
  - minecraft:chorus_flower
  - minecraft:chorus_plant
  - minecraft:farmland
  - minecraft:grass_path
  - minecraft:heavy_core
  - minecraft:jigsaw
  - minecraft:sea_lantern
  - minecraft:sniffer_egg
  - minecraft:structure_block。

## Molang

- Molang查询“wing_flap_position”和“wing_flap_speed”现在适用于鸡。

## 资源和行为包

- 内置包现在包括归档文件，以提高某些平台的加载性能。

## 稳定性和性能

- 将保存的区块数据中的生物群系ID大小从8位增加到16位。
- 修复了极快移动的实体会导致游戏崩溃的问题。实体现在无法在单个刻中移动超过16个方块。（作为参考，速度255的实体在单个刻中将移动约11个方块。）
- 在加载靠近末地城的世界时，游戏将不再崩溃。

# 实验性技术更新

## API

- 将 `EntityBreathableComponent` 从 `beta` 移动到 `1.15.0`。
  - 将 `breathesAir` 从 `beta` 移动到 `1.15.0`。
  - 将 `breathesLava` 从 `beta` 移动到 `1.15.0`。
  - 将 `breathesSolids` 从 `beta` 移动到 `1.15.0`。
  - 将 `breathesWater` 从 `beta` 移动到 `1.15.0`。
  - 将 `generatesBubbles` 从 `beta` 移动到 `1.15.0`。
  - 将 `inhaleTime` 从 `beta` 移动到 `1.15.0`。
  - 将 `suffocateTime` 从 `beta` 移动到 `1.15.0`。
  - 将 `totalSupply` 从 `beta` 移动到 `1.15.0`。
  - 将 `componentId` 从 `beta` 移动到 `1.15.0`。
  - 将 `getBreatheBlocks()` 从 `beta` 移动到 `1.15.0`。
  - 将 `getNonBreatheBlocks()` 从 `beta` 移动到 `1.15.0`。
- 将类 `BlockLocationIterator` 从 `beta` 移动到 `1.15.0`。
- 将类 `InvalidIteratorError` 从 `beta` 移动到 `1.15.0`。
- 将属性 `BlockVolumeBase.getBlockLocationIterator` 从 `beta` 移动到 `1.15.0`。
- 将枚举 `BlockVolumeIntersection` 从 `beta` 移动到 `1.15.0`。
- 将类 `BlockVolume` 从 `beta` 移动到 `1.15.0`。
- 添加了 `DyeableItemComponent` 到 `beta`。

## 相机

- 修复了在使用 `minecraft:follow_orbit` 相机时，`minecraft:rideable`的 `rider_rotation_lock` 没有效果的问题。
- 添加了 `minecraft:camera_attach_to_player` 到 `minecraft:follow_orbit`。
- 添加了相机预设行为包JSON中的 `align_target_and_camera_forward`选项，可在启用第三人称相机预设实验时使用。
- 第三人称相机实验 - 创作者相机的半径属性现在限制在0.1到100之间的值。
- 当在相机命令中传递“默认”参数时，第三人称Boom相机将重置为JSON中指定的起始旋转值。

## 图形

- 移除了延迟技术预览中月亮周围的黑暗光环。