---
title: Minecraft Beta & Preview - 1.21.30.23
date: 2024-08-15T10:51:50Z
updated: 2024-08-15T14:51:30Z
categories: Beta 和 Preview 信息与更新日志
link: https://feedback.minecraft.net/hc/zh-cn/articles/29288258913293-Minecraft-Beta-Preview-1-21-30-23
hash:
  user-content-experimental-features: experimental-features
  user-content-bundles: bundles
  user-content-features-and-bug-fixes: features-and-bug-fixes
  user-content-blocks: blocks
  user-content-gameplay: gameplay
  user-content-general: general
  user-content-items: items
  user-content-mobs: mobs
  user-content-sounds: sounds
  user-content-user-interface: user-interface
  user-content-vanilla-parity: vanilla-parity
  user-content-technical-updates: technical-updates
  user-content-ai-goals: ai-goals
  user-content-api: api
  01J5AT7F7112FKRS80B4BZ24QZ: blocks-2
  user-content-editor: editor
  01J5AT7F72HK9EYMEJYBFD733N: items-1
  user-content-trade-tables: trade-tables
  user-content-experimental-technical-updates: experimental-technical-updates
  01J5AT7F747HTZ1P0K2PG1P7HM: api-1
  user-content-graphical: graphical
---

**发布时间：** 2024年8月15日

**Minecraft Preview 和 Beta 信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft Preview 可在 Xbox、PlayStation、Windows 和 iOS 设备上使用。更多信息请参见 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta 版可在 Android（Google Play）上获取。加入或退出 Beta 版的详细说明请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

![一个丛林神庙，外面有一只吃竹子的熊猫。墙上有一个物品展示框中的收纳袋。附近还有一个使用海晶灯的小型红石装置](https://feedback.minecraft.net/hc/article_attachments/29288233240717)

本周的预览版本**非常令人兴奋**。为什么？因为鹦鹉终于可以模仿末影螨了！等等，抱歉，这不是重大新闻。我的意思是——因为收纳袋现在可以在 Minecraft: 基岩版的预发布版本中测试了！收纳袋是一种物品，可以让你将其他物品堆叠存储，从而最大化你的物品栏空间。你甚至可以将收纳袋放入收纳袋中！一旦你将收纳袋塞满了其他收纳袋，你现在可以使用新的提示框选择要提取的物品或物品堆。我们一如既往地希望收到你对收纳袋的反馈（如果你愿意，也包括鹦鹉模仿末影螨的反馈），请在 [aka.ms/mcbundlesfeedback](https://aka.ms/mcbundlesfeedback) 告诉我们你的想法，并在 [bugs.mojang.com](http://bugs.mojang.com/) 报告任何漏洞。

# 实验性功能

## 收纳袋

收纳袋是一种物品，允许你将不同的区块或物品堆叠存放在同一个物品栏槽位中。不同的物品通常不能堆叠在一起，因此你可能会因为每个槽位只装几件物品而浪费空间。收纳袋可以将这些物品打包在一起，避免空间浪费。

- 收纳袋是一个实验性功能——要使用它们，你必须在创建新世界时开启收纳袋实验
- 收纳袋是一种可以将不同物品打包在同一堆中的物品
- 一个收纳袋只能容纳一堆（通常64件）物品，但可以包含多种不同类型的物品
- 你可以直接在物品栏中将物品插入收纳袋
- 收纳袋有一个提示框，显示内部的物品
  - 如果收纳袋内的物品类型少于8种，提示框会显示所有物品
  - 否则，提示框只会显示前两行物品，其他物品会被隐藏在下方
- 你可以选择任何可见的物品从收纳袋中提取
  - 使用鼠标滚轮、游戏控制器的右摇杆，或触摸设备上的点击

> **开发者注：** *在最初的收纳袋实验中，你只能选择顶层物品。我们收到了很多玩家希望在提取物品时有更多灵活性的反馈。为了解决这个问题，我们在收纳袋中添加了一个子菜单，这是 Minecraft 中前所未有的！*

- 在选择要移除的物品时，收纳袋图标会显示该物品从收纳袋中突出
- 当手持收纳袋时，你可以将其内容倒在地上
- 收纳袋的合成配方为一个线在一个皮革上方

> **开发者注：** *收纳袋的原型合成成本更高，并使用兔子皮，这只在某些生物群系中可获得，因此玩家必须探索以获取第一个收纳袋。在此版本中，我们降低了成本，使其几乎在任何生物群系中都可以在家中合成。我们希望在新世界中容易获得收纳袋，以便你在早期冒险中使用。*

- 已知问题：
  - 收纳袋的配方可能不会作为建议的合成项显示，但仍然可以合成
  - 在触摸设备上移动物品时，错误的物品图标可能会短暂出现

# 功能和漏洞修复

## 区块

- "tnt" 区块现在拆分为独立实例："tnt" 和 "underwater_tnt"
- 解析 blocks.json 时，如果 format_version 大于或等于它覆盖的区块名称，则会产生内容错误
- 从 format_version 1.21.30 起，以下区块名称在 "blocks.json" 中被视为过时 ([MCPE-100267](https://bugs.mojang.com/browse/MCPE-100267))：
  - `minecraft:carpet`
  - `minecraft:colored_torch_bp`
  - `minecraft:colored_torch_rg`
  - `minecraft:concrete`
  - `minecraft:concrete_powder`
  - `minecraft:coral`
  - `minecraft:coral_block`
  - `minecraft:coral_fan`
  - `minecraft:coral_fan_dead`
  - `minecraft:coral_fan_hang`
  - `minecraft:coral_fan_hang2`
  - `minecraft:coral_fan_hang3`
  - `minecraft:double_plant`
  - `minecraft:double_stone_block_slab`
  - `minecraft:double_stone_block_slab2`
  - `minecraft:double_stone_block_slab3`
  - `minecraft:double_stone_block_slab4`
  - `minecraft:double_wooden_slab`
  - `minecraft:fence`
  - `minecraft:hard_stained_glass`
  - `minecraft:hard_stained_glass_pane`
  - `minecraft:leaves`
  - `minecraft:leaves2`
  - `minecraft:light_block`
  - `minecraft:log`
  - `minecraft:log2`
  - `minecraft:monster_egg`
  - `minecraft:planks`
  - `minecraft:red_flower`
  - `minecraft:sapling`
  - `minecraft:shulker_box`
  - `minecraft:stained_glass`
  - `minecraft:stained_glass_pane`
  - `minecraft:stone_block_slab`
  - `minecraft:stone_block_slab2`
  - `minecraft:stone_block_slab3`
  - `minecraft:stone_block_slab4`
  - `minecraft:stonebrick`
  - `minecraft:tallgrass`
  - `minecraft:terracotta`
  - `minecraft:wood`
  - `minecraft:wooden_slab`
  - `minecraft:wool`
- "chemistry_table" 已拆分为4个独立实例："compound_creator"、"material_reducer"、"element_constructor" 和 "lab_table"
  - 需要开启教育版切换

## 游戏玩法

- 修复了 End Gateway 传送门可能错误传送部分玩家的问题 ([MCPE-66061](https://bugs.mojang.com/browse/MCPE-66061))
- 当已有相机插值运行时，'/camera set' 命令现在会按正确的顺序执行 ([MCPE-183986](https://bugs.mojang.com/browse/MCPE-183986))

## 通用

- 在实体上显示的命名牌中添加了输入字形支持

## 物品

- 修复了在导入 1.5.0 以下旧世界时，区块物品转换为不正确变种的问题 ([MCPE-181944](https://bugs.mojang.com/browse/MCPE-181944))
- 教育版：修复了材料还原器配方无法与某些压平区块（如安山岩或陶瓦）一起使用的问题

## 生物

- Breeze（旋风人）不再需要最小攻击距离 ([MCPE-183011](https://bugs.mojang.com/browse/MCPE-183011))
- 鹦鹉现在可以模仿末影螨
- 鹦鹉现在可以模仿溺尸 ([MCPE-46302](https://bugs.mojang.com/browse/MCPE-46302))

## 音效

- 玄武岩三角洲现在再次拥有情绪化的环境音效

## 用户界面

- 在 OreUI 玩屏幕中将 “所有世界” 标签重命名为 “世界”（仅预览版）
- 在新 Play 屏幕中显示的极限模式心形图标在悬停时现在会动画显示（仅预览版）
- 基岩版本用户界面中的信标标题文本不再与其他容器不同 ([MCPE-176186](https://bugs.mojang.com/browse/MCPE-176186))
- 修复了在经典用户界面中隐藏配方书后，基岩版本用户界面中的合成类别标签不可见的错误 ([MCPE-183825](https://bugs.mojang.com/browse/MCPE-183825))
- 切石机屏幕中的箭头现在始终可见，就像其他类似屏幕一样 ([MCPE-160236](https://bugs.mojang.com/browse/MCPE-160236))
- 修复了某些屏幕上物品耐久度和存储条大小及位置不正确的问题
- 添加了在游戏中使用控制器和键盘进行截图的热键。在鼠标/键盘上：F2。在控制器上：LB+RB，L1+R1，L键+R键

## 原版趋同

- 修复了林地府邸中的蘑菇农场错误生成泥土而不是砂土的问题
- 以下区块在红石动力方面已与 Java 版趋同：
  - `minecraft:mangrove_roots` -> 现在有动力 ([MCPE-153838](https://bugs.mojang.com/browse/MCPE-153838))
  - `minecraft:beacon` -> 不再有动力
  - `minecraft:tnt` -> 不再有动力
  - `minecraft:sea_lantern` -> 不再有动力 ([MCPE-79271](https://bugs.mojang.com/browse/MCPE-79271))
- 使用附魔精准采集的锹开采顶雪时，顶雪按区块层数掉落相应数量的雪块 ([MCPE-59729](https://bugs.mojang.com/browse/MCPE-59729))
  - 如果有8层，将掉落一个雪块

# 技术更新

## AI 意向

- 移除了从未使用过的 `minecraft:behavior.peek` AI 意向组件

## API

- 更改了迭代器，使其正确存储自身状态，简化并更好地处理常见用法
- 修复了可迭代对象的 `next` 方法
- 以下 API 已从实验性中移除：`PlayerCursorInventoryComponent` API、Actor 属性目标选择器 API 和 Block Record Player Component API

## 区块

- 区块几何中的 "item_display_transforms" 字段不再需要 "Upcoming Creator Features" 切换

## 编辑器

编辑器及其对应的 API 正处于早期开发阶段，并在 Windows PC 基岩版预览构建中支持键盘/鼠标。请在社交媒体上使用 **#BedrockEditor** 标记我们。在 [如何使用](https://learn.microsoft.com/zh-cn/minecraft/creator/documents/editoroverview?view=minecraft-bedrock-stable) 学习编辑器，加入 [GitHub 讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛与团队互动，并通过 [starter kit](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [samples](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

本周我们发布了编辑器 V0.7！此版本充满了众多新功能：

- 粘贴预览
- 延迟光照设置
- 自定义输入映射
- 实体事务
- 附加调试器
- 客户端小部件系统
- 导出面板
- 刷子工具 + 遮罩支持
- 标尺工具
- 结构管理器
- 导航面板
- 简单工具包装器
- 更新的属性面板 API
- 动作栏 API

在 [GitHub 讨论](https://github.com/Mojang/minecraft-editor/discussions) 页面查看包含演示的完整更新日志。

本周更新：

- 添加了导航面板，增加了一个迷你地图以在世界中传送并为关键点添加标签
- 为项目中存储的结构管理添加了结构面板动作栏项
  - 添加了与之接口的编辑器结构管理器 API
- 在导出面板中添加了极限模式选项
- 向 `IModalToolContainer` API 添加了 `getSelectedToolId` 和 `setSelectedToolId` 函数
- 修复了编辑器操作可能耗尽所有可用常加载区域导致所有未来操作失败的错误
- 修复了有时 `IModalTool.onModalToolActivation` API 事件调用顺序错误的问题
- 修复了有时会导致刷子遮罩加载失败的错误

## 物品

- 物品数据版本 1.16.100+ 现在可以被包堆叠中更高版本的物品数据 1.16.100+ 覆盖
- 允许创作者使用 1.16.100+ 数据覆盖 1.16.100+ 数据驱动的原版物品
- 添加了 "minecraft:storage_item" 物品组件，允许物品存储与之关联的动态容器数据
  - 此组件需要启用收纳袋切换
  - 动态容器是与物品链接的存储容器，而不是与区块或实体链接
  - 要使用此组件，物品必须将 "minecraft:max_stack_size" 设置为 1
  - "max_slots" 字段（1 至 64）定义动态容器的槽位数量
  - "max_weight_limit" 字段定义动态容器中所有槽位中物品重量的最大允许总和
    - 堆叠到64的物品每个重量为1，堆叠到16的物品每个重量为4，无法堆叠的物品重量为64
  - "allow_nested_storage_items" 字段允许将其他具有 "minecraft:storage_item" 组件的物品放入其中
  - "weight_in_storage_item"（0 至 64）定义物品在另一个存储物品内时增加的额外重量
    - 值为0表示不允许此物品放入另一个存储物品内
  - "banned_items" 字段定义不允许放入物品动态容器的物品
  - "allowed_items" 字段定义仅允许放入物品动态容器的物品
    - 如果为空，所有物品都允许放入物品动态容器内
- 添加了 "minecraft:bundle_interaction" 物品组件，以启用特定于收纳袋的交互方案和提示框
  - 此组件需要启用收纳袋切换
  - 要使用此组件，物品必须定义了 "minecraft:storage_item" 组件
  - "minecraft:bundle_interaction" 组件与 "minecraft:storage_item" 组件创建的容器交互
  - "num_viewable_slots" 字段（1 至 64）定义从收纳袋顶部可访问的物品堆叠的最大数量，其余槽位被隐藏
  - 必须在 textures/textures_list.json 中添加名为 \[item_name\]\_open_front 和 \[item_name\]\_open_back 的纹理

## 交易表

- 交易表文件现在已版本化
  - 交易等级的 "total_exp_required" 从版本 1.21.30 起为必需成员
  - 交易等级的 "groups" 从版本 1.21.30 起为必需成员
  - 交易物品的数量 "min" 从版本 1.21.30 起不能低于 "max"

# 实验性技术更新

## API

- 将 `PlayerCursorInventoryComponent` 类从 `beta` 移动到 `1.14.0`

## 区块

- 修复了自定义区块的 'minecraft:redstone_conductivity' 支持问题

## 图形

- 修复了延迟技术预览中夜视药水无效的问题
- 当延迟技术预览中的 FOV 设置更改时，钓鱼线在第一人称视角中现在正确渲染