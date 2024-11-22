---
标题: Minecraft Beta & Preview - 1.21.50.28
日期: 2024-11-07T16:40:42Z
更新于: 2024-11-07T16:40:47Z
分类: Beta 和 Preview 信息及更新日志
链接: https://feedback.minecraft.net/hc/zh-cn/articles/31693342053517-Minecraft-Beta-Preview-1-21-50-28
hash:
  user-content-features-and-bug-fixes: 功能和漏洞修复
  user-content-pale-garden: 苍白之园
  user-content-blocks: 方块
  user-content-copper-grate: 铜格栅
  user-content-creaking-heart: 嘎枝之心
  user-content-eyeblossom: 眼眸花
  user-content-pale-moss-carpet: 苍白覆地苔藓
  user-content-features: 功能
  user-content-gameplay: 游戏玩法
  user-content-items: 物品
  user-content-resin-bricks: 树脂砖块
  user-content-mobs: 生物
  user-content-magma-cube: 岩浆怪
  user-content-realms: Realms
  user-content-sound: 音效
  user-content-creaking: 嘎枝
  user-content-user-interface: 用户界面
  user-content-vanilla-parity: 原版趋同
  01JC3QNKBSW3E9ZXCNN14BEYXW: 方块-1
  user-content-weapons: 武器
  user-content-technical-updates: 技术更新
  user-content-add-ons-and-script-engine: 附加包和脚本引擎
  user-content-api: API
  user-content-editor: 编辑器
  user-content-entity-components: 实体组件
  user-content-experimental-technical-updates: 实验性技术更新
  01JC3QNKBS2QE3E1S7QMAXBECA: API-1
  user-content-block-components: 方块组件
  user-content-cameras: 相机
  user-content-ui: 用户界面
---

**Minecraft Preview 和 Beta 信息:**

- 这些进行中的版本可能不稳定，且可能不代表最终版本的质量
- Minecraft Preview 可在 Xbox、PlayStation、Windows 和 iOS 设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta 版本可在 Android（Google Play）上获得。要加入或退出 Beta，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![sildfjsldfkjv.jpeg](https://feedback.minecraft.net/hc/article_attachments/31693342049421)

是时候推出新的 Preview 和 Beta 了！一如既往，我们希望在 [aka.ms/mcgamedropfeedback](https://aka.ms/mcgamedropfeedback) 上获得您对这些新功能的反馈，您也可以在 [bugs.mojang.com](https://bugs.mojang.com/) 报告任何漏洞！本周新内容包括：

# 功能和漏洞修复

## 苍白之园

- 在苍白之园生物群系下雨时，地平线上天空现在呈现更暗的色调 ([MCPE-187539](https://bugs.mojang.com/browse/MCPE-187539))

## 方块

- 使用刷怪蛋设置生物的试炼刷怪笼在冷却结束后不再回到空状态 ([MCPE-185960](https://bugs.mojang.com/browse/MCPE-185960))
- 杜鹃树、盛开的杜鹃花丛、红树、樱花和苍白橡树树叶在远处不再显示黑色像素 ([MCPE-156469](https://bugs.mojang.com/browse/MCPE-156469))
- 当“华丽树叶”被禁用时，红树树叶现在有专用的纹理 ([MCPE-170516](https://bugs.mojang.com/browse/MCPE-170516))
- 苍白橡树树叶纹理的方向不再为每个方块随机化
- 苔藓块现在有更安静的行走和着陆声音 ([MCPE-176933](https://bugs.mojang.com/browse/MCPE-176933))
- 饰纹陶罐在世界加载时不再激活侦测器
- 幽匿感测体现在能够检测眼眸花的开合
- 修复了所有头颅方块变为skeleton_skull的问题，当打开版本锁定低于1.21.40的世界模板或结构时。请注意，此修复不会应用于已被覆盖的区块
- 红砖块、下界砖块、红色下界砖块、树脂砖块及相关方块的纹理已更新，与所有其他砖块横向对齐 ([MCPE-187806](https://bugs.mojang.com/browse/MCPE-187806))
- 闭合的眼眸花不再使蜜蜂中毒
- 开放的眼眸花的中毒效果现在在蜜蜂位于方块内时也会造成伤害，而不仅仅是在蜜蜂退出时
- 减少了开放的眼眸花施加的中毒效果的持续时间
- 调整了眼眸花、嘎枝之心和苍白垂须发出的环境声音频率，以更好地与Java版本对齐

### 铜格栅

- 液体如静止水和静止熔岩在铜格栅覆盖时不再错误地贴图 ([MCPE-178719](https://bugs.mojang.com/browse/MCPE-178719))

### 嘎枝之心

- 使用时运破坏嘎枝之心时掉落更多树脂团 ([MCPE-187697](https://bugs.mojang.com/browse/MCPE-187697))

### 眼眸花

- 即使被雪覆盖，眼眸花现在也会开合 ([MCPE-187759](https://bugs.mojang.com/browse/MCPE-187759))

### 苍白覆地苔藓

- 苍白覆地苔藓的侧面现在阴影正确显示 ([MCPE-187373](https://bugs.mojang.com/browse/MCPE-187373))
- 矿采时苍白覆地苔藓的侧面现在正确显示裂缝 ([MCPE-187566](https://bugs.mojang.com/browse/MCPE-187566))

## 功能

- 以下功能类型现在无法放置仅内部使用的地物
  - `minecraft:aggregate_feature`
  - `minecraft:snap_to_surface_feature`
  - `minecraft:surface_relative_threshold_feature`
  - `minecraft:weighted_random_feature`

## 游戏玩法

- 修复客户端有时与服务器的雨/雪天气状态不匹配的问题 ([MCPE-131325](https://bugs.mojang.com/browse/MCPE-131325))

## 物品

- Slate 不再出现在教育版以外的创造模式物品栏中 ([MCPE-187696](https://bugs.mojang.com/browse/MCPE-187696))
- 谜之炖菜的效果持续时间已调整为各版本一致
- 开放的眼眸花产生的谜之炖菜现在赋予相同的失明持续时间，和蓝花美耳草产生的谜之炖菜相同 ([MCPE-187802](https://bugs.mojang.com/browse/MCPE-187802))

## 树脂砖块

- 树脂砖块现在用于应用树脂盔甲饰条，而不是树脂团

## 生物

- 嘎枝不再在远距离观察时有时会穿透方块
- 劫掠兽现在可以破坏所有类型的树叶方块，而不仅限于部分选择 ([MCPE-169375](https://bugs.mojang.com/browse/MCPE-169375))
- 蜜蜂无法在闭合的眼眸花内被诱惑或进行授粉
- 喂食蜜蜂开放的眼眸花现在会施加中毒效果
- 喂食蜜蜂凋灵玫瑰现在会施加凋零效果

### 岩浆怪

- 岩浆怪模型部分的UV不再彼此重叠

## Realms

- 修复在几个平台上，当在管理成员屏幕邀请玩家后返回Realms故事时导致崩溃的问题

## 音效

- 海绵、湿海绵、嘎枝之心、树脂砖块和树脂块的坠落和行走声音事件改为“player”
- 为嘎枝之心、树脂砖块和树脂块新增跳跃和着陆声音事件 ([MCPE-187713](https://bugs.mojang.com/browse/MCPE-187713) , [MCPE-188088](https://bugs.mojang.com/browse/MCPE-188088))
- 嘎枝之心的破坏和放置声音现在更安静
- 为树脂新增更多破坏声音

### 嘎枝

- 嘎枝现在播放4种不同的摇动声音
- 嘎枝现在播放新的攻击声音

## 用户界面

- 收纳袋提示框中的物品现在有灰色背景
- 触控控制：修复离开船后相机有时会卡住的错误 ([MCPE-184406](https://bugs.mojang.com/browse/MCPE-184406))
- 收纳袋提示框在从光标放置后正确显示
- 游戏手柄在物品栏屏幕和工作台屏幕上将鼠标悬停在收纳袋上时，合成输出提示框现在正确显示
- 截图：新增功能和展示截图的能力，供他人访问您的个人资料时查看。新增从截图设置自定义世界缩略图的能力。

## 原版趋同

- 一击击杀狼、蜜蜂或蠹虫不再激怒附近同类型的生物
- 一击击杀僵尸猪灵不再激怒附近的僵尸猪灵 ([MCPE-68327](https://bugs.mojang.com/browse/MCPE-68327))

### 方块

- 头颅方块现在可以放置在方块的侧面，即使它们下方缺少支撑方块

## 武器

- 如果生物在攻击过程中使用会破损的物品，游戏不再崩溃

# 技术更新

## 附加包和脚本引擎

- 修复了一个错误，即带有“minecraft:block_placer”组件的原版物品在分屏客户端上显示错误的图标。

## API

- 修复了一个API脚本处理错误，可能导致无限循环

## 编辑器

编辑器及其相应的API处于早期开发阶段，可在Windows PC Bedrock Preview版本的键盘/鼠标上使用。在社交平台上使用 **#BedrockEditor** 标签与我们互动。了解 [如何使用](https://learn.microsoft.com/zh-cn/minecraft/creator/documents/editoroverview?view=minecraft-bedrock-stable) 编辑器，加入 [GitHub 讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛与团队互动，并通过 [starter kit](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [samples](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

本周我们发布了编辑器 V0.8！此版本包含大量新功能和改进，包括：

- 平整工具
- 填充工具
- 平滑工具
- 快速挤出
- 重复工具
- 农场工具
- 2D 方向 XZ 指南针
- 自定义方块
- 方块选择器更新
- 使用刷子选择
- 使用刷子雕刻
- 刷子偏移
- 定位生物群系工具
- 抓钩/运动更新
- 中键选择方块
- 自定义小部件改进

在 [GitHub 讨论](https://github.com/Mojang/minecraft-editor/discussions) 页面查看带有演示的完整更新日志。
本周更新内容：

- 新增平整刷：将此刷在方块上拖动，将其上方的方块变为空气。此刷具有可自定义的高度和半径。
- 新增填充工具，允许创作者快速更改方块组
- 新增平滑工具，轻松平滑地形
- 新增快速挤出工具，允许创作者挤出方块组
- 新增重复工具，可沿X、Y和Z轴重复选择体积
- 新增农场工具，可快速在世界中放置农场
- 方块选择器中新增友好名称
- 新增2D方向XZ指南针到游戏视口以辅助建筑
  - 新增点击指南针以对齐最近的基本方向的功能
- 新增可配置的飞行速度倍数
  - 新增速度设置
  - 视图 -> 视图设置中的新滑块，可将飞行速度倍数配置在1到10之间
  - 飞行速度倍数仅在工具/编辑器模式下生效
- 新增选择::删除的快速操作
- 在小部件 Gizmo 组件创建选项中新增新的轴和面限制选项。创作者可以限制其小部件允许的移动轴
- 新增方块过滤器禁用状态
- 新增 M 键切换掩码模式和禁用状态
- 新增 R 键切换替换模式和禁用状态
- 新增热键栏方块调色板的持久性支持
- 新增热键栏旁选项按钮的上下文菜单，用于创建和管理新调色板
- 新增新的 `session.extensionContext.blockUtilities` 对象，提供多种高性能常见方块操作。新增的第一个功能是 `fillVolume` 函数，用于执行大型填充操作，遵循编辑器不同的方块调色板类型
- 更新默认过滤器为空气（当未加载前一状态时）
- 更新选择::取消选择的图标
- 更新用户界面中的方块ID以使用本地化名称
- 更新复选框标签为可点击
- 更新属性窗格信息提示图标以提高可见性
- 更新视图 -> 日志面板菜单项，现在可展开面板抽屉
- 修复导致下拉菜单在窗口边缘被截断的错误

## 实体组件

- 新增 `minecraft:ignore_cannot_be_attacked` 组件，并将过滤器从 `minecraft:cannot_be_attacked` 移至此组件。这允许内容拥有自定义生物绕过 `cannot_be_attacked` 组件（例如恶魂上的组件），而无需修改被攻击生物的设置。

# 实验性技术更新

## API

- 将 `BlockFillOptions` 从 Beta 移至 `v1.16.0`
- 将 `UnloadedChunksError` 从 Beta 移至 `v1.16.0`
- 修复当 `ignoreChunkBoundErrors` 设置为 true 时，`Dimension.fillBlocks` 会在常加载区域外设置方块的错误
- 维度
  - 将 `containsBlock(volume: BlockVolumeBase, filter: BlockFilter, allowUnloadedChunks?: boolean): boolean` 从 Beta 移至 `v1.16.0`
  - 将 `getBlocks(volume: BlockVolumeBase, filter: BlockFilter, allowUnloadedChunks?: boolean): ListBlockVolume` 从 Beta 移至 `v1.16.0`
  - 将 `fillBlocks(volume: BlockVolumeBase, block: BlockPermutation | BlockType | string, options?: BlockFillOptions): ListBlockVolume;` 从 Beta 移至 `v1.16.0`
- ItemUseOnBeforeEvent
  - 将属性 `readonly isFirstEvent: boolean` 从 Beta 移至 `v1.16.0`
- ItemUseOnAfterEvent
  - 将属性 `readonly isFirstEvent: boolean` 从 Beta 移至 `v1.16.0`
- CameraFixedBoomOptions
  - 新增属性 `entityOffset?: Vector3`
- 在 `setCamera` 中新增 `CameraTargetOptions` 参数，适用于 `beta`。如果启用了焦点目标实验性相机切换，可以用来修改 `minecraft:free` 预设

## 方块组件

- 修改 `"ambient_occlusion"` 字段为 `"minecraft:material_instances"` 组件的浮点值，需开启 **UpcomingCreatorFeatures** 实验

## 相机

- 使用自由相机预设跟踪目标：可选的 "tracking_radius" 浮点值，用于设置目标实体的监听半径
- 尝试在非自由相机模式下目标实体时新增内容错误

## 用户界面

- 新增对签名书输入字形替换的支持。例如，使用输入字符串 ":_input_key.jump:" 在使用键盘时将替换为 "JUMP"，或在使用游戏手柄时替换为表情符号。

# 完