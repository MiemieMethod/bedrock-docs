---
标题: Minecraft Beta & Preview - 1.21.40.21
日期: 2024-09-11T10:26:49Z
更新: 2024-09-11T15:39:57Z
分类: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/30155721026317-Minecraft-Beta-Preview-1-21-40-21
哈希:
  用户内容-实验性特性: experimental-features
  用户内容-收纳袋: bundles
  用户内容-特性和漏洞修复: features-and-bug-fixes
  用户内容-辅助功能特性: accessibility-features
  用户内容-方块: blocks
  用户内容-游戏玩法: gameplay
  用户内容-常规: general
  用户内容-图形: graphical
  用户内容-生物: mob
  用户内容-声音: sound
  01J7G9SJ2P85AAM8XM54AETF6R: blocks-1
  用户内容-生物: mobs
  用户内容-用户界面: user-interface
  用户内容-创造模式物品栏更改: creative-inventory-changes
  用户内容-技术更新: technical-updates
  用户内容-方块: block
  用户内容-组件: components
  用户内容-编辑器: editor
  用户内容-实体事件响应: entity-event-responses
  用户内容-特性: feature
  01J7G9SJ2P4NJRJSX1HRMEVS33: graphical-2
  用户内容-物品: items
  用户内容-资源和行为包: resource-and-behavior-packs
  用户内容-交易: trading
  用户内容-技术实验性更新: technical-experimental-updates
  用户内容-Molang: molang
  用户内容-脚本: scripting
---

**发布:** 2024年9月11日

**关于Minecraft预览和Beta的信息:**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明

![一艘Minecraft沉船，上面有流浪商人和羊驼。](https://feedback.minecraft.net/hc/article_attachments/30155721025165)

是时候进行新的Minecraft预览和Beta了！我们非常希望您对收纳袋提供反馈，请在 <https://aka.ms/mcbundlesfeedback> 告诉我们您的想法，并在 [bugs.mojang.com](http://bugs.mojang.com/) 报告任何漏洞。

# 实验性特性

## 收纳袋

- 重命名的收纳袋名称现在在提示框中以斜体显示 ([MCPE-185502](https://bugs.mojang.com/browse/MCPE-185502))

# 特性和漏洞修复

## 辅助功能特性

- 在触摸设备上重新实现了左手模式，以便从快捷栏访问物品栏 ([MCPE-179608](https://bugs.mojang.com/browse/MCPE-179608))

## 方块

- 修复了沉船仅生成下层台阶的问题。（此修复不会更改已生成的沉船） ([MCPE-186235](https://bugs.mojang.com/browse/MCPE-186235))
- 更新了行为包木材配方文件中对旧方块名称的引用
- 更新了其余行为包配方文件中对旧方块名称的引用

## 游戏玩法

- 修复了一个漏洞，导致在玩家死亡时未应用渗浆、盘丝和蓄风效果 ([MCPE-180640](https://bugs.mojang.com/browse/MCPE-180640))
- 生物现在可以执行重锤攻击

## 常规

- 从设置中移除了一些仅应存在于Minecraft教育版的键盘按键绑定：控制提示、代码构建器和沉浸式阅读器

## 图形

- 修复了导致某些方块失去环境光遮蔽的问题，以及某些生物群系中的树叶显得过于明亮的问题 ([MCPE-186343](https://bugs.mojang.com/browse/MCPE-186343))

## 生物

- 当佩戴时，雕刻南瓜和头颅现在会随着沼骸的头部旋转 ([MCPE-178959](https://bugs.mojang.com/browse/MCPE-178959))

## 声音

### 方块

- 生物刷怪笼的脚步声和击打声现在以预期音量播放
- 试炼刷怪笼的击打声现在以预期音量播放

### 生物

- 凋灵骷髅的脚步声现在以预期音量播放 ([MCPE-185913](https://bugs.mojang.com/browse/MCPE-185913))

## 用户界面

- LAN世界现在在OreUI游戏界面的“世界”标签中可见（仅限预览）
- 修复了在实验性床铺界面中，对于某些玩家睡眠百分比游戏规则显示不正确消息的漏洞 ([MCPE-183431](https://bugs.mojang.com/browse/MCPE-183431))

## 创造模式物品栏更改

> **开发者注释**：*创造模式物品栏中的物品和方块已重新组织，旨在使整体排序更加直观。*

- 试炼室物品
  - 试炼钥匙被移动到不祥试炼钥匙旁边，非常不祥 ([MCPE-180280](https://bugs.mojang.com/browse/MCPE-180280))
  - 不祥之瓶被移动到现有药水旁边，并被分为自己的“不祥之瓶”组 ([MCPE-180278](https://bugs.mojang.com/browse/MCPE-180278))
- 自然标签中的石头组
  - 石头被移动到石头组中，终于 ([MCPE-116364](https://bugs.mojang.com/browse/MCPE-116364))
  - 石头现在是石头组的前方块
  - 玄武岩和平滑玄武岩被移动到石头组中
  - 凝灰岩和磨制凝灰岩被移动到石头组中 ([MCPE-176383](https://bugs.mojang.com/browse/MCPE-176383))
- 建筑标签中的装饰石
  - 平滑石被移动到装饰石中
  - 凝灰岩砖、雕纹凝灰岩和雕纹凝灰岩砖被从自然类别移动到建筑类别的装饰石中
  - 海晶石砖从装饰石组中移动，现在它们在海晶石和暗海晶石旁边
- 铜系列等 ([MCPE-176384](https://bugs.mojang.com/browse/MCPE-176384))
  - 粗铁、粗铜、粗金的顺序调整为粗铜、粗铁、粗金
  - 铜、铁和金块被移动以匹配粗版本的顺序
  - 铜门被移动到所有其他门旁边
  - 铜活板门被移动到所有其他活板门的组中，这不是一个陷阱
  - 铜块和铜格栅现在按方块类型然后按氧化等级排序，而不是按氧化等级然后按方块类型
- 凝灰岩系列
  - 凝灰岩楼梯、凝灰岩台阶、凝灰岩墙及其磨制版本被移动从自然标签到建筑标签的各自组中
- 其他方块
  - 红砖现在被放置在台阶组之前
    - 此更改仅影响由黏土制成的红砖，而不是所有砖块
  - 雕纹下界砖和裂纹下界砖被移动到下界砖块和红下界砖旁边
  - 石英砖被放置在其他石英块旁边
  - 缠根泥土现在在其他泥土块旁边
  - 许多泥土块和草的变种被重新排列以匹配Java版
  - 沙砾现在在石头组之后，并在沙子和红沙旁边
  - 黏土从建筑类别移动到自然类别，放置在泥巴块旁边

# 技术更新

## 方块

- 当"carried_textures"或"blockshape"在blocks.json中写错时，添加内容警告

## 组件

- 将"minecraft:lookat"组件重命名为"minecraft:looked_at"，以更好地反映其功能
  - 其"look_event"字段也重命名为"looked_at_event"
  - 其"look_cooldown"字段也重命名为"looked_at_cooldown"
- 扩展了"minecraft:looked_at"组件的功能，增加了六个新的\[Beta\]字段：
  - "find_players_only"限制查找看着拥有者实体的生物仅限于玩家，确保选择满足指定"filters"的最近玩家
  - "look_at_locations"定义了目标看向的拥有者实体的部分
    - 对于这些部分，执行视线检查以确保没有方块阻挡视线
    - 支持的值为"head"、"body"和"feet"
  - "not_looked_at_event"指定当没有合适的实体看着拥有者实体时触发的事件
  - "field_of_view"定义了看着拥有者实体的生物的视野宽度，以度为单位：
    - 如果"scale_fov_by_distance"设置为true，则该值对应于实体之间一块距离的视野
  - "scale_fov_by_distance"决定当拥有者实体和看着它的实体之间的距离增加时，视野是否变窄
    - 这确保了在拥有者实体位置的视锥宽度保持相对恒定，无论距离如何
  - "line_of_sight_obstruction_type"定义在检查视线阻挡时考虑的方块形状
    - 支持的值为"outline"、"collision"和"collision_for_camera"
  - 此外，"set_target"现在支持三种不同的值：
    - "never"，看着的实体永远不会被设置为目标，但事件会被发出
    - "once_and_stop_scanning"，第一次检测到的看着实体被设置为目标，但如果拥有者实体有目标，则暂停扫描和事件发出
    - \[Beta\] "once_and_keep_scanning"，第一次检测到的看着实体被设置为目标，但扫描和事件发出继续
  - 所有这些字段计划在稍后从\[Beta\]中移除并完全发布

## 编辑器

- 添加了初始编辑器设置面板，选项包括“显示不可见方块”和“显示区块边界”

## 实体事件响应

- 添加了"reset_target"实体事件响应，允许实体重置其目标

## 特性

- 在"pregeneration_pass"中使用不支持的特性放置现在将抛出内容错误，而不是崩溃

## 图形

- 添加新的the_end.client_biome.json作为第一种新类型文件，以包含资源包中的每个生物群系的渲染和音频设置

## 物品

- `"minecraft:item"`对象从1.21.40开始使用严格加载器解析
  - 数字和布尔值在JSON输入中不再可以互换
  - 在期望整数的地方不再接受浮点数

## 资源和行为包

- 修复了在加入启用CDN的服务器时未下载或应用包的问题
- 修复了在服务器启用CDN时，用户选择在加入服务器时下载/应用资源包被忽略的问题

## 交易

- 修复了负“max_use”值的交易无法交易的问题

# 技术实验性更新

## 图形

- 改进了在手中持有和放置在框架中的地图的光照效果，在延迟技术预览中
- 修复了在延迟技术预览中启用上采样时水面抖动的问题
- 在延迟技术预览的视频设置中添加了一个滑块，用于控制上采样分辨率因子

## Molang

- 添加即将推出的创作者特性：
  - `query.client_memory_tier`。返回一个数字，表示客户端RAM内存等级，0 = '未确定'，1 = '超级低'，2 = '低'，3 = '中'，4 = '高'，或5 = '超级高'。仅在客户端（资源包）上可用
  - `query.server_memory_tier`。返回一个数字，表示服务器RAM内存等级，0 = '未确定'，1 = '超级低'，2 = '低'，3 = '中'，4 = '高'，或5 = '超级高'。仅在服务器端（行为包）上可用

## 脚本

- 添加枚举 `MemoryTier`

``` hljs
    export enum MemoryTier {
        Undetermined = 0,
        SuperLow = 1,
        Low = 2,
        Mid = 3,
        High = 4,
        SuperHigh = 5
    }
```

- 添加基类 `SystemInfo`
  - 字段 `MemoryTier`
- 添加类 `ClientSystemInfo`
  - 字段 `MemoryTier`
- 类 `Player`
  - 添加属性 `clientSystemInfo`
- 类 `System`
  - 添加属性 `serverSystemInfo`
