---
title: Minecraft Beta & Preview - 1.21.60.21
date: 2024-11-19T11:23:54Z
updated: 2024-11-20T18:07:11Z
categories: Beta and Preview Information and Changelogs
link: https://feedback.minecraft.net/hc/en-us/articles/31998389834637-Minecraft-Beta-Preview-1-21-60-21
hash:
  user-content-features-and-bug-fixes: features-and-bug-fixes
  user-content-accessibility: accessibility
  user-content-blocks: blocks
  user-content-copper-bulb: copper-bulb
  user-content-gameplay: gameplay
  user-content-general: general
  user-content-mobs: mobs
  user-content-breeding: breeding
  user-content-realms: realms
  user-content-user-interface: user-interface
  user-content-vanilla-parity: vanilla-parity
  user-content-biomes: biomes
  01JD50VYJKXC2YAVE0D0G63EE9: blocks-2
  01JD50VYJKRAFCYSXVT95XDQ9B: mobs-1
  user-content-technical-updates: technical-updates
  user-content-api: api
  user-content-components: components
  user-content-editor: editor
  user-content-entity-components: entity-components
  user-content-entity-filters: entity-filters
  user-content-graphical: graphical
  user-content-items: items
  user-content-sounds: sounds
  user-content-technical-experimental-updates: technical-experimental-updates
  user-content-add-ons-and-script-engine: add-ons-and-script-engine
  user-content-commands: commands
  01JD50VYJKW731CK0B4E2JT4KV: gameplay-1
  01JD50VYJN8Z56ZKSNR2VZWT5R: components-1
  01JD50VYJN4E7RSF78D86VVZVE: graphical-1
  01JD50VYJMQ74QHPJAEHCHJ9RJ: user-interface-1
---

**发布时间：**2024 年 11 月 20 日

**Minecraft 预览版和测试版信息：**

- 这些开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft 预览版可在 Xbox、PlayStation、Windows 和 iOS 设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在 Android（Google Play）上使用。要加入或退出测试版，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 了解详细说明

是时候发布新的预览版和测试版了！一如既往，我们非常期待您对即将推出的游戏更新功能提供反馈，您可以通过 [aka.ms/mcgamedropfeedback](https://aka.ms/mcgamedropfeedback) 提供反馈，并且您可以在 [bugs.mojang.com](https://bugs.mojang.com/) 报告任何漏洞！以下是本周的新内容：

# 功能和漏洞修复

## 辅助功能

- 在 Realms 计划选择屏幕中添加了旁白，告知玩家他们可以在“购买”按钮下方导航，以获取有关特定计划的更多信息

## 方块

- 在某些情况下稍微改进了移动方块与生物之间的碰撞检测
- 幽匿感测体现在可以检测到通过嘎枝之心放置的树脂团 ([MCPE-188260](https://bugs.mojang.com/browse/MCPE-188260))
- 修复了各种植物方块在渲染时与 Java 版不同的问题 ([MCPE-40646](https://bugs.mojang.com/browse/MCPE-40646))
  - 所有树苗
  - 矮草丛
  - 枯萎的灌木
  - 绯红菌索
  - 诡异菌索
  - 虞美人
  - 兰花
  - 绒球葱
  - 蓝花美耳草
  - 所有郁金香
  - 滨菊
  - 矢车菊
  - 铃兰
  - 蒲公英
  - 红色和棕色蘑菇
  - 胡萝卜
  - 凋灵玫瑰
  - 张开的眼眸花和闭合的眼眸花
  - 火把花
  - 甜浆果丛
  - 丁香
  - 高草丛
  - 大蕨
  - 玫瑰丛
  - 牡丹
- 红树树叶在“高级树叶”选项禁用时，玩家手持时不再显示黑色像素 ([MCPE-156469](https://bugs.mojang.com/browse/MCPE-156469))
- 火把花、瓶子草、张开的眼眸花和闭合的眼眸花现在增加了附近树苗生长为带有蜂箱的树木的概率

### 铜灯

- 更新了斑驳的铜灯的发光纹理 ([MCPE-177105](https://bugs.mojang.com/browse/MCPE-177105))

## 游戏玩法

- 添加了在单人世界中进入暂停屏幕后暂停游戏的功能，该功能可在“常规”设置中打开或关闭。
  - 我们很想知道您对这一新增功能的看法，请在 [aka.ms/mcbedrockpausefeedback](https://aka.ms/mcbedrockpausefeedback) 提供反馈

## 一般

- 改进了世界生成点算法，因此优质生物群系但远离世界原点的位置比靠近原点但地形很差的位置更受青睐 ([MCPE-120237](https://bugs.mojang.com/browse/MCPE-120237))
- 滤净不当言论切换。我们在 Windows 上引入了一个新的“滤净不当言论”设置。开启时，所有文本内容包括聊天内容将按常规处理；不当言论将为您和他人过滤。关闭时，大多数不当言论（部分可能有害的内容除外）将为您和同样关闭该选项的其他人显示未过滤内容。对于所有玩家，该设置默认开启，并且对未登录或儿童账户无法更改。您可以在“常规”设置中关闭此选项。

## 生物

- 如果嘎枝之心通过命令被强制禁用，则嘎枝会崩塌
- 嘎枝现在像其他敌对生物一样持久，意味着它们在保存/加载时不会消失 ([MCPE-188352](https://bugs.mojang.com/browse/MCPE-188352))
- 嘎枝在被激怒时不再播放环境音，仅在闲置时播放

### 繁殖

- 用兼容的羊毛颜色繁殖绵羊现在会使小绵羊拥有混合颜色 ([MCPE-19862](https://bugs.mojang.com/browse/MCPE-19862))
- 繁殖狼现在会产生拥有父母其中一个的项圈颜色，或者如果颜色兼容，则产下混合父母颜色的后代
- 用兼容的项圈颜色繁殖猫现在会使小猫戴有混合颜色项圈 ([MCPE-188187](https://bugs.mojang.com/browse/MCPE-188187))

## 领域

- Realms 故事中的玩家头像现在加载更可靠
- 修复了用户有时无法通过使用邀请代码重新加入他们离开的领域的问题
- 移除了对 Realms API 的不必要重复调用
- 在领域世界选择屏幕中，当选择一个世界槽时，如果存在“编辑世界”按钮，焦点将切换到该按钮，否则切换到“激活世界”
- 在向玩家展示领域试用优惠之前，新增了检查领域试用优惠可用性的逻辑，基于客户端的试用资格

## 用户界面

- 通过故事设置屏幕禁用领域故事徽章通知，现在在故事提要和游戏屏幕中都隐藏徽章
- 触控控制：D 方向键中间的空白区域在飞行或游泳时不再作为前进按钮 ([MCPE-183944](https://bugs.mojang.com/browse/MCPE-183944))
- 修复了玩家需要在编辑世界屏幕上跳过夜晚滑块才能达到 0% 的问题
- 更改了跳过夜晚所需最低玩家睡眠人数的措辞
- 为了回应玩家对药水瓶含义的困惑反馈，我们更新了多个屏幕上的成就位置、标签和图标使用
- 对于成就百分比计数器，新的书籍资产替换了药水瓶，并支持多级视觉状态以庆祝进度，包括 100% 完成时的令人愉快的动画
- 将高级图形切换和光线追踪切换合并到一个图形模式下拉菜单中。高级和光线追踪模式等同于启用之前的高级和光线追踪切换，简单模式等同于未启用之前的任何切换

## 原版趋同

### 生物群系

- 在红树林沼泽生物群系中生成的僵尸村民现在应用正确的皮肤 ([MCPE-158736](https://bugs.mojang.com/browse/MCPE-158736))
- 通常在主世界生成的怪物（僵尸、末影人、蜘蛛、苦力怕等，骷髅除外）现在可以在红树林沼泽生物群系中生成 ([MCPE-170183](https://bugs.mojang.com/browse/MCPE-170183))

### 方块

- 睡莲方块的击中箱已更新，与 Java 版趋同 ([MCPE-60826](https://bugs.mojang.com/browse/MCPE-60826))
- 甘蔗方块的击中箱已更新，与 Java 版趋同 ([MCPE-60827](https://bugs.mojang.com/browse/MCPE-60827))
- TNT 方块在爆炸时不再以纯白色闪烁 ([MCPE-51809](https://bugs.mojang.com/browse/MCPE-51809))
- 蜡烛和蜡烛蛋糕方块现在正确播放环境音 ([MCPE-130585](https://bugs.mojang.com/browse/MCPE-130585))
- 剪刀现在可以用于洞穴藤蔓、海带、缠怨藤和垂泪藤，以防止进一步生长 ([MCPE-141497](https://bugs.mojang.com/browse/MCPE-141497))

### 生物

- 马、骷髅马、僵尸马、驴和骡现在按预期播放其环境音 ([MCPE-178313](https://bugs.mojang.com/browse/MCPE-178313))
- 狐狸在保护玩家时现在会周期性地播放它们的“怒”声音
- 小溺尸现在移动速度与其僵尸和僵尸村民对应生物一致 ([MCPE-34574](https://bugs.mojang.com/browse/MCPE-34574))
- 猪灵和僵尸猪灵掉落的金剑现在具有随机耐久度，与 Java 版趋同 ([MCPE-75292](https://bugs.mojang.com/browse/MCPE-75292))
- 猪灵蛮兵掉落的斧头现在具有随机耐久度，与 Java 版趋同 ([MCPE-95543](https://bugs.mojang.com/browse/MCPE-95543))
- 苦力怕在爆炸时不再以纯白色闪烁 ([MCPE-51809](https://bugs.mojang.com/browse/MCPE-51809))
- 中立生物在玩家或其他生物扔出对它们有正面效果的滞留药水时不再变得具有攻击性 ([MCPE-105343](https://bugs.mojang.com/browse/MCPE-105343))

# 技术更新

## API

- 更新了数值 JavaScript 枚举，现在可以正确处理和支持反向值映射
- 修复了调用 `Player.hideAllExcept` 可能导致服务器崩溃的漏洞
- 输入权限
  - 将以下 `InputPermissionCategory` 枚举值移动到 1.17.0 版本：`LateralMovement`、`Sneak`、`Jump`、`Mount`、`Dismount`、`MoveForward`、`MoveBackward`、`MoveLeft` 和 `MoveRight`
  - 将以下 `PlayerInputPermissions` 方法移动到 1.17.0 版本：
    - `isPermissionCategoryEnabled(permissionCategory: InputPermissionCategory): boolean;`
    - `setPermissionCategory(permissionCategory: InputPermissionCategory, isEnabled: boolean): void;`
- 移除了 ItemStack API 中可用的 "compostingChance"。原版物品的堆肥几率现在可以通过 Item Component API 中单一的 CompostableItemComponent->compostingChance 访问
- 修复了在打开 UI 时 `ModalFormData` 滚动到最底部的边缘情况

## 方块

- 移除了 `minecraft:item_visual` 组件的“即将公开的创作者功能”切换需求
- 更新了 `"minecraft:material_instances"` 组件
  - 移除了 `"ambient_occlusion"` 字段的 **UpcomingCreatorFeatures** 实验需求，以将其类型改为浮点数
- 重新添加了新字段 `"ambient_occlusion_exponent"` 到资源包的 **blocks.json** 文件架构，替代损坏的 `"brightness_gamma"` 字段 ([MCPE-188216](https://bugs.mojang.com/browse/MCPE-188216), [MCPE-188221](https://bugs.mojang.com/browse/MCPE-188221))

## 组件

- 炽足兽现在使用 `minecraft:movement_sound_distance_offset` 组件来设置其移动声音距离偏移

## 编辑器

- 向地形工具添加了“粗糙”刷子
- 添加了颜色选择器色相渐变选择器，适用于单色值
- 更新了编辑器指南针主体，单击时在 NSEW 方向和轴向方向（Z、-Z、X、-X）之间切换
- 将方块选择器更新为漂浮窗口，并使其后面的视口在中键点击时更清晰
- 将平整刷子更新为原生刷子，增加了最大高度和半径
- 将导出和游戏测试面板更新，现在包括床的工作和所需的睡眠玩家作为导出选项
- 更新了热栏物品，当快捷键按下且方块已选择时打开方块选择器
- 修复了 block:// 图像资源的一些缺失方块图标缩略图的问题
- 修复了按下数字 9 键时触发的错误音效

## 实体组件

- "minecraft:breedable" 组件现在有一个字段，允许后代的 "minecraft:color" 属性成为父母颜色的混合
  - "combine_parent_colors"，如果颜色突变不会发生，宝宝会获得父母颜色的组合（如果颜色兼容）。颜色组合遵循染料物品的组合规则。如果颜色不兼容，宝宝会随机获得父母中的一个颜色
    - 有效值： "true"、"false"

## 实体过滤

- 新增了实体过滤器 "home_distance"，用于检查实体与其家的距离
  - 要求主题实体具有 "minecraft:home" 组件
  - 如果主题没有家，或家在不同的维度，则返回 false
- 新增了实体过滤器 "is_bound_to_creaking_heart"，用于检查生成主题嘎枝的嘎枝之心是否仍然存在

## 图形

- 改进了处理图集中非常大纹理的逻辑。确保会超出最大图集尺寸的纹理现在会单独丢弃 mipmap，而不是强制整个图集丢弃 mipmap

## 物品

- 当为 "minecraft:durability_sensor" 物品组件的 "particle_type" 提供无效值时，添加了内容警告

## 声音

- 为方块声音添加了 "base" 参数，指定如果方块自身未定义声音时应使用的其他方块声音

# 技术实验性更新

## 附加包和脚本引擎

- 更新了瞄准辅助，现在它只能在第三人称摄像视角中使用。切换到不支持的摄像类型将禁用瞄准辅助

## 命令

- 为 `/me` 和 `/tell` 命令添加了输入字符替换的支持。例如，使用输入字符串 ":\_input_key.jump:" 在使用键盘时将替换为 "JUMP"，在使用游戏手柄时将替换为表情符号

## 游戏玩法

- 当启用“创作者摄像：新第三人称预设”实验时，新增了两个移动摄像头之间的缓动效果

### 组件

- 使用 `minecraft:liquid_detection` 组件移除含水的自定义方块，并启用了 `stopsLiquidFlowingFromDirection` 对所有方向，现在将产生流动的水，而不是静止的水块

## 图形

- 修复了在使用延迟技术预览时，某些基于 PowerVR 的 Android 设备出现黑屏的漏洞。一些 PowerVR 设备仍已知存在问题
- 修复了在启用延迟技术预览时，被活塞移动的方块闪烁的问题
- 次表面散射现在受延迟技术预览中的点光源影响
- 修复了在延迟技术预览中，某些立方体贴图边缘会在天空反射中可见的漏洞

## 用户界面

- 添加了一个新的单选按钮，允许玩家选择是否希望延迟视频设置偏向性能或视觉
- 为告示牌、签名书和 NPC 对话新增了输入字符替换的支持。例如，使用输入字符串 ":\_input_key.jump:" 在使用键盘时将替换为 "JUMP"，在使用游戏手柄时将替换为表情符号