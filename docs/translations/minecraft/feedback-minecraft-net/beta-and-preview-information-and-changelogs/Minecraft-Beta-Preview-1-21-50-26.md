---
title: Minecraft Beta & 预览版 - 1.21.50.26
date: 2024-10-30T13:31:25Z
updated: 2024-11-06T13:50:26Z
categories: Beta 和预览版信息及更新日志
link: https://feedback.minecraft.net/hc/zh-cn/articles/31476211695501-Minecraft-Beta-Preview-1-21-50-26
hash:
  user-content-new-features-and-bug-fixes: 新功能和漏洞修复
  user-content-biomes: 生物群系
  user-content-pale-garden: 苍白之园
  user-content-blocks: 方块
  user-content-creaking-heart: 嘎枝之心
  user-content-resin-bricks: 树脂砖块
  user-content-resin-clump: 树脂团
  user-content-commands: 命令
  user-content-features: 地物
  user-content-gameplay: 游戏性
  user-content-graphics: 图形
  user-content-items: 物品
  user-content-mobs: 生物
  01JBES9M8RBW9AKYKK9KSQMWVA: 嘎枝
  user-content-realms: 领域
  user-content-stability-and-performance: 稳定性和性能
  user-content-structures: 结构
  user-content-jigsaw: 拼图
  user-content-technical: 技术
  user-content-trial-spawner: 试炼刷怪笼
  user-content-user-interface: 用户界面
  user-content-vanilla-parity: 原版趋同
  01JBES9M8R5GQJSS7V21Y0ZV6P: 方块-3
  user-content-technical-updates: 技术更新
  01JBES9M8S17RQ5054DJP6QB5R: 生物-1
  user-content-audio: 音频
  01JBES9M8RXQ7VHDS9QQ6FAFYW: 生物群系-1
  user-content-molang: molang
  user-content-editor: 编辑器
  user-content-entity-components: 实体组件
  user-content-scripting-api: 脚本API
  user-content-network-protocol: 网络协议
  user-content-recipes: 配方
  01JBES9M8S2FG813JWWA2E2Z85: 稳定性和性能-1
  user-content-experimental-technical-updates: 实验性技术更新
  user-content-api: API
  user-content-camera: 摄像头
  user-content-component: 组件
  user-content-scripting: 脚本
  user-content-server-ui: 服务器界面
  01JBES9M8STP9FXJ8CE96B5EJR: 结构-1
---

**发布时间:** 2024年10月30日

**关于Minecraft预览版和Beta的信息:**

- 这些开发中的版本可能不稳定，且可能不代表最终版本的质量
- Minecraft预览版可在Xbox、PlayStation、Windows和iOS设备上获得。更多信息请访问[aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版可在Android（Google Play）上获得。要加入或退出Beta，请参阅[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)获取详细说明

![苍白橡树叶.jpg](https://feedback.minecraft.net/hc/article_attachments/31476211693453)

是时候发布新的预览版和Beta版了！本周我们在苍白之园增强了氛围。当眼眸花开放时会喷出橙色粒子——苍白橡树的树叶也会从苍白之园的苍白橡树上落下，为这个新的、诡异的生物群系增添了氛围。像往常一样，我们非常希望在[feedback.mojang.net](http://feedback.mojang.net/)上收到您对这些新功能的反馈，您也可以在[bugs.mojang.com](http://bugs.mojang.com/)报告任何漏洞！以下是本周的新内容：

# 新功能和漏洞修复

## 生物群系

- 进入苍白之园时音乐音量会逐渐降低至零，离开时音量会逐渐恢复

### 苍白之园

- 将苍白橡树树苗、眼眸花、苍白苔藓块和苍白垂须添加到流浪商人中 ([MCPE-187456](https://bugs.mojang.com/browse/MCPE-187456))

## 方块

- 调整了苍白苔藓、苍白覆地苔藓和苍白垂须的易燃性  
  - 现在它们燃烧得更快，但更难着火
  - 现在可以被熔岩点燃
- 苍白垂须和嘎枝之心的环境声音衰减率现为线性，使其在更远的距离内可听见 ([MCPE-187326](https://bugs.mojang.com/browse/MCPE-187326))
- 眼眸花在开放和闭合时现在会播放声音
- 放置在苍白苔藓块上的开放眼眸花现在会发出环境声音
- 藤蔓、洞穴藤蔓、缠怨藤和垂泪藤现在会播放正确的声音，而不是下界疣的声音
- 苍白垂须现在与Java版本使用相同的模型 ([MCPE-187397](https://bugs.mojang.com/browse/MCPE-187397))
- 在世界中和花盆中放置的眼眸花在开放/闭合时现在会发出粒子
- 苍白橡树叶现在会发出落叶粒子

### 嘎枝之心

- 将嘎枝之心传播树脂团的距离减少了一个方块
- 树脂团现在只能传播到苍白橡木原木、去皮苍白橡木原木、苍白橡木和去皮苍白橡木

### 树脂砖块

- 树脂砖台阶、楼梯和墙壁的配方现在与下界砖的配方提供相同数量的方块 ([MCPE-187707](https://bugs.mojang.com/browse/MCPE-187707), [MCPE-187795](https://bugs.mojang.com/browse/MCPE-187795), [MCPE-187796](https://bugs.mojang.com/browse/MCPE-187796))

> **开发者注:** *计数很难。*

### 树脂团

- 生物现在可以正确地在树脂团上方路径寻找 ([MCPE-187778](https://bugs.mojang.com/browse/MCPE-187778))

## 命令

- 含有额外百分号的rawtexts在数字形式（"%%%%1"）中不再与非数字形式（"%%%%s"）不一致地展开 ([MCPE-171001](https://bugs.mojang.com/browse/MCPE-171001))
- 效果命令在添加效果后现在在显示消息中正确显示持续时间为秒 ([MCPE-186963](https://bugs.mojang.com/browse/MCPE-186963))

## 地物

- 标准化了树木在生长时可以替换的方块，带有一些例外情况 ([MCPE-187302](https://bugs.mojang.com/browse/MCPE-187302)) ([MCPE-187301](https://bugs.mojang.com/browse/MCPE-187301))
  - 除樱花树不能穿过它们自己的树叶外，所有树木现在都可以穿过树叶生长 ([MCPE-168029](https://bugs.mojang.com/browse/MCPE-168029))
  - 所有树木都可以在泥土类方块上生长 ([MCPE-187739](https://bugs.mojang.com/browse/MCPE-187739))
- 高草在苍白之园生物群系中其顶部部分现在正确生成 ([MCPE-187308](https://bugs.mojang.com/browse/MCPE-187308))
- 高草在繁茂洞穴生物群系中其顶部部分现在正确生成 ([MCPE-125799](https://bugs.mojang.com/browse/MCPE-125799))

## 游戏性

- 在史莱姆块上坠落时按住跳跃键不再取消弹跳 ([MCPE-185354](https://bugs.mojang.com/browse/MCPE-185354))
- 在史莱姆块上着陆时潜行不再导致坠落伤害

> **开发者注:** 现在停止在史莱姆块上弹跳的预期方法是潜行。  
> 之前玩家可以通过按住跳跃键停止弹跳，但这是一个无意的疏忽，因为跳跃键实际上取消了来自方块的运动。
>
> 这导致了其他类型的漏洞，例如当玩家在按住跳跃键时用带有风弹附魔的重锤攻击生物。  
> 新的玩家跳跃行为是始终选择现有垂直速度和跳跃速度中的较高者。

- 修复了一个案例，在玩家放置方块后更改选定槽位但服务器尚未处理方块放置时，方块放置失败的问题。这会因为服务器未预料到槽位更改而拒绝方块放置 ([MCPE-112420](https://bugs.mojang.com/browse/MCPE-112420))

## 图形

- 天空颜色在不同生物群系之间旅行时现在逐渐过渡，而不是突然变化 ([MCPE-90625](https://bugs.mojang.com/browse/MCPE-90625))

## 物品

- 树脂团和树脂砖块物品在第三人称视角下不再在玩家手中漂浮
- 开放和闭合的眼眸花现在可以在哞菇上使用以获取各自的谜之炖菜，当进行挤奶时 ([MCPE-187754](https://bugs.mojang.com/browse/MCPE-187754))
- 黑石现在可以用来修复石质工具和石质武器 ([MCPE-71859](https://bugs.mojang.com/browse/MCPE-71859))

## 生物

### 嘎枝

- 减缓了非敌对嘎枝的速度
- 被驯服的狼的攻击不再阻止嘎枝攻击玩家
- 当嘎枝的脚被观察到且其脚在灵魂沙或泥巴中时，嘎枝不再能移动
- 嘎枝现在可以接近向下看的玩家，只有在进入玩家视野范围内时才停止
- 嘎枝在被投射物击中时现在会摇晃
- 嘎枝的攻击动画已被平滑，以实现更自然的动作
- 调整了嘎枝步行动声音的音量和音调
- 嘎枝部分声音的衰减率现在为线性，使其在更远的距离内可听见

## 领域

- 修复了在加载领域时加载屏幕未显示领域UI元素的漏洞

## 稳定性和性能

- 改善了游戏加载的稳定性

## 结构

### 拼图

- 放置拼图结构的起始部分时现在考虑了维度填充

## 技术

- 原版试炼刷怪笼NBT `normalConfig` 和 `ominousConfig` 标签值现在支持引用常见配置，作为内联配置的替代

## 试炼刷怪笼

- 一些试炼刷怪笼在Ominous状态下不会同时发出额外的旋风人

## 用户界面

- 在跨平台关闭时，允许在“加入朋友”菜单中选择已禁用的按钮
- Dualsense游戏手柄现在在移动设备上具有正确的提示图标
- 修正了领域故事和时间线页面的间距问题
- 触控控制: 修复了在控制自定义期间船只可交互的漏洞 ([MCPE-184404](https://bugs.mojang.com/browse/MCPE-184404))
- 修复了在使用资源包时死亡屏幕和新床屏幕有时会应用不正确纹理的漏洞 ([MCPE-178701](https://bugs.mojang.com/browse/MCPE-178701), [MCPE-184050](https://bugs.mojang.com/browse/MCPE-184050))
- *为创造模式的触控控制添加了选择方块功能*

  > ***开发者注:*** 选择方块功能允许您将物品添加到快捷栏，而无需打开物品栏。使用选择方块，您可以在世界中选择您想要的方块，它将被添加到您的快捷栏中。

## 原版趋同

### 方块

- 树脂团和发光地衣现在在活动对象行走的方块上方播放它们的步行动声音

# 技术更新

### 生物

- 红树林沼泽现在不再生成其他生物群系的生物 ([MCPE-187514](https://bugs.mojang.com/browse/MCPE-187514))

### 方块

- 添加了“minecraft:liquid_detection”方块组件，该组件控制方块的基本液体检测属性，如液体记录、液体阻挡，以及被液体扩散破坏或弹出。当前组件仅支持水
- 使用“minecraft:block_placer”物品组件渲染引用的方块作为物品图标不再需要“即将到来的创作者功能”切换
- 樱花树叶现在不再计为自定义方块 ([MCPE-180725](https://bugs.mojang.com/browse/MCPE-180725))

## 音频

- 每个生物群系的环境声音现在在client_biome JSON组件中定义  
  - 这使用了新的“minecraft:ambient_sounds”组件
  - 命名的声音必须在sounds.json文件中的“individual_named_sounds”中定义

## 生物群系

- 客户端生物群系JSON文件现在支持带有“volume_multiplier”字段的“minecraft:biome_music”组件，当音频监听器位于对应生物群系内时，将逐渐影响音乐音量  
  - 逐渐的音量变化大约需要十秒，并将线性增加但指数减少

## Molang

- 将 `query.client_memory_tier` 移至稳定版本。
  - 移除了“未确定”。它返回一个表示客户端RAM内存层级的数字，0 = 'SuperLow'，1 = 'Low'，2 = 'Mid'，3 = 'High'，或4 = 'SuperHigh'。仅在客户端（资源包）可用。
- 将 `query.server_memory_tier` 移至稳定版本。
  - 移除了“未确定”。它返回一个表示服务器RAM内存层级的数字，0 = 'SuperLow'，1 = 'Low'，2 = 'Mid'，3 = 'High'，或4 = 'SuperHigh'。仅在服务器端（行为包）可用。
- 将 `query.client_max_render_distance` 移至稳定版本。

## 编辑器

- 向客户端窗口系统添加了新的 `ClipboardWidgetComponent`，允许创作者将剪贴板项目添加到窗口中，并以“全息图”形式显示
- 向 `Widget` 和 `WidgetBaseComponent` 添加了一个标志，允许根据XZ位置锁定Y位置到表面
- 向 `Widget` 添加了一个标志，以将窗口的位置绑定到3D方块光标的位置
- 向选择工具添加了快速操作按钮栏（取消选择和填充）
- 向主菜单和操作栏项目添加了复制和剪切功能
- 为核心编辑器窗格添加了信息提示框链接
- 向块选择模式中添加了中键选择方块
- 更新了选择工具的大小输入框，使其在选择方块时启用
- 更新了 `IModalToolContainer.addTool` API函数，要求传入唯一的工具ID作为必要参数。移除了创建参数中的 `inputContextId` 和 `inputContextLabel`。
- 更新了抓钩移动  
  - 向光标服务API添加了 'getRay()'
  - 摄像头现在在飞行期间旋转向抓钩目标，且旋转不再那么突然
  - 如果没有附近的方块可抓钩，抓钩现在允许创作者飞行100个方块距离朝鼠标指针方向
  - 将抓钩到选择的热键从F更改为CTRL+SHIFT+F
- 移除了所有与 `CursorAttachment` 相关的类型、属性和方法
- 从 `IModalTool` API中移除了 `hide`、`show`、`dispose` 函数
- 为了更清晰，将 `ClipboardWriteOptions` 中的 `anchor` 重命名为 `normalizedOrigin`
- 修复了柱状和立方刷子高度为1时尺寸不正确的问题
- 修复了线条工具中的取消选择问题（实际上是客户端窗口未正确跟踪脚本中的选中状态的问题）
- 修复了选择上下移动中的键绑定不正确
- 修复了“下一个导航位置”键盘快捷键不再与“上一个导航位置”冲突的问题
- 修复了刷子绘画工具仅在起始维度（通常是主世界）中工作的问题，并且在切换维度时不工作
- 修复了交互式提示框链接的键盘导航
- 修复了当滚动条缺失时选择工具面板项的填充问题
- 修复了抓钩时摄像头闪到玩家生物头部内部的问题

## 实体组件

- “minecraft:looked_at”组件的“look_at_locations”字段现在接受一个对象列表作为参数，每个对象包含两个字段  
  - “location”，必须可见的实体的位置
    - 有效值: “头部”， “身体”， “脚部”
  - “vertical_offset”，应用于实体位置的可选垂直偏移

## 脚本API

- 将 `ClientSystemInfo` 从 `beta` 移至 `1.16.0`。
- 将 `MemoryTier` 从 `beta` 移至 `1.16.0`。
- 将 `PlatformType` 从 `beta` 移至 `1.16.0`。
- 将 `SystemInfo` 从 `beta` 移至 `1.16.0`。
- 枚举 `MemoryTier`。
  - 移除了 `Undetermined` 条目。

## 网络协议

- 新增的级别声音事件: Open, OpenLong, Close, 和 CloseLong
- 新增粒子类型: EyeblossomOpen
- 新增粒子类型: EyeblossomClose
- 新增粒子类型: PaleOakLeaves

## 配方

- 如果有序配方的图案包含未定义的键，解析时将添加内容错误，并修复打开有此类格式错误配方的合成界面时的崩溃问题 ([MCPE-178520](https://bugs.mojang.com/browse/MCPE-178520))

## 稳定性和性能

- 启动时发现的包的一些统计信息存储在本地，以便在某些平台上实现更快的未来启动

# 实验性技术更新

## 方块

- 添加了“minecraft:item_visual”方块组件。该组件采用嵌套的“minecraft:geometry”和“minecraft:material_instances”组件来配置方块的物品表示
  - “geometry”和“material_instances”字段为必需。它们使用与“minecraft:geometry”和“minecraft:material_instances”相同的字段/要求
  - 方块必须同时包含“minecraft:geometry”和“minecraft:material_instances”组件以及“minecraft:item_visual”组件
  - 需要“即将到来的创作者功能”切换
- 蜘蛛网现在遵守在blocks.json中设置的 'blockshape' 和 'textures' 属性
  - 需要“即将到来的创作者功能”切换

## API

- 通过ItemStack API新增了对现有原版物品的堆肥几率的访问
- 通过物品组件API新增了对具有CompostableItemComponent的物品的堆肥几率的访问

## 摄像头

- 为fixed_boom摄像头命令新增了旋转功能

## 组件

- 向即将到来的创作者功能实验性切换添加了“minecraft:compostable”物品组件

## 脚本

### 服务器界面

- 新增了对服务器表单 (`ActionFormData`, `MessageFormData`, 和 `ModalFormData`) 的输入字形替换的支持

## 结构

- 向创作者公开“数据驱动拼图结构”实验性切换
  - 创作者将能够修改结构生成规则，涉及放置（位置和频率）、布局（结构部件之间的放置方式）和自定义（如何修改或替换结构部件内的方块）。
  - 拼图结构数据包含4个新的JSON文件：
    - 拼图结构: 这些结构可以通过各种结构部件在世界中构建。连接方块是拼图方块。
    - 处理器: 处理器可以为结构添加自定义行为，影响其外观。
    - 结构集: 结构集合是指示结构在世界中放置位置和方式的JSON。
    - 模板池: 模板池包含构成结构的结构部件。