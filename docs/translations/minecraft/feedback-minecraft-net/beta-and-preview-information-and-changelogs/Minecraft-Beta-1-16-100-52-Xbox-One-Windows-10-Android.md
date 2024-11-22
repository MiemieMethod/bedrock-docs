---
标题: Minecraft Beta - 1.16.100.52 (Xbox One/Windows 10/Android)
日期: 2020-08-19T15:32:29Z
更新: 2020-08-19T16:05:33Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360048306131-Minecraft-Beta-1-16-100-52-Xbox-One-Windows-10-Android
---

**2020年8月19日**

**在参与Minecraft Beta之前，请阅读以下内容：**

- 加入测试版将用Minecraft的一个进行中的版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**原版趋同**

- 酿造台现在可以用黑石制作（[MCPE-90465](https://bugs.mojang.com/browse/MCPE-90465)）
- 玩家现在可以使用/give命令生成耕地，并使用取块功能选择它（[MCPE-25691](https://bugs.mojang.com/browse/MCPE-25691)）
- 被火焰伤害杀死的鳕鱼和鲑鱼现在掉落熟鱼（[MCPE-30693](https://bugs.mojang.com/browse/MCPE-30693)）

**性能与稳定性**

- 修复了在启用特定纹理包时进入游戏导致崩溃的问题
- 向末影龙添加标签不再在重新加载世界时导致游戏崩溃（[MCPE-89076](https://bugs.mojang.com/browse/MCPE-89076)）

**方块**

- 栅栏门现在与黑石墙对齐（[MCPE-78002](https://bugs.mojang.com/browse/MCPE-78002)）
- 在绯红菌索和诡异菌索上放置方块现在会正确移除菌索（[MCPE-81521](https://bugs.mojang.com/browse/MCPE-81521)）
- 标靶方块不再为其上方的额外方块供电（[MCPE-85455](https://bugs.mojang.com/browse/MCPE-85455)）
- 可可豆现在可以放置在所有丛林木变种上并存活（[MCPE-46638](https://bugs.mojang.com/browse/MCPE-46638)）

**经验球**

- 经验球现在忽略世界光照，使其始终保持最大亮度（[MCPE-67448](https://bugs.mojang.com/browse/MCPE-67448)）

**物品**

- 掉落的物品不再悬浮得太低
- 龙蛋在被爆炸摧毁时现在总是掉落（[MCPE-52632](https://bugs.mojang.com/browse/MCPE-52632)）

**生物**

- 在熔岩中的生物无法找到逃生路径。此修复使它们可以在已经在熔岩中的情况下进入熔岩方块
- 路径寻找现在将考虑“minecraft:scale”组件
- 更新了酿造台、按钮、箱子、末影箱、台阶和灵魂沙方块类型，以允许路径寻找和导航（[MCPE-47075](https://bugs.mojang.com/browse/MCPE-47075)）

**技术更新**

- 更新了活动对象属性。两个无效字段在某些原版内容中出现时将显示内容错误。“minecraft:can_fly”上的“value”字段和“minecraft:foot_size”属性应从任何实体文件中删除
- 使船使用浮力组件。添加了两个新组件，inside_block_notifier组件，当活动对象进入或退出指定方块时触发指定事件，以及out_of_control组件，设置相应的活动对象标志，以实现这一点
- 为解析Minecraft共享物品添加了错误检查。如果物品名称无效或数组为空，将显示内容日志
- 尝试加载未定义的自定义材料不再导致崩溃。现在会抛出适当的内容错误
- 暴露新的数据参数以控制“为目标掉落物品”的行为。这包括：“seconds_before_pickup”、“cooldown”、“minimum_teleport_distance”、“max_head_look_at_height”、“teleport_offset”和“entity_types”。请查看新的活动对象组件文档！
- 暴露新的数据参数以控制“收获农田方块目标”的行为，包括“max_seconds_before_search”、“search_cooldown_max_seconds”和“seconds_until_new_task”。请查看新的活动对象组件文档！

**Aseprite**

- 用户界面现在支持使用aseprite JSON文件进行动画，这允许比简单翻页书更高级的动画

**命令**

- 添加了新的/structure命令，允许保存和加载结构，而无需使用结构方块
- 添加了/playanimation命令，允许您运行一次性动画。它假设所有变量都已正确设置以运行动画
- 添加了/ride命令，允许您使实体骑乘其他实体，阻止实体骑乘，使骑乘驱逐其骑乘者，或召唤骑乘或骑乘者

**格式版本检查**

- 更新了几何体、粒子和动画文件中的format_version字段，使其行为与实体行为文件相同。也就是说，您不再需要指定特定版本以被接受，而只需指定您所针对的发布版本

**SetBannerDetailsFunction**

- 现在支持自定义非掠夺者旗帜
- 可以指定最多6种图案和颜色

**接受的旗帜类型**

- "default"
- "illager_captain"

**接受的颜色值**

- "black"
- "red"
- "green"
- "brown"
- "blue"
- "purple"
- "cyan"
- "silver"
- "gray"
- "pink"
- "lime"
- "yellow"
- "light_blue"
- "magenta"
- "orange"
- "white"

**接受的图案值**

- "base"
- "border"
- "bricks"
- "circle"
- "creeper"
- "cross"
- "curly_border"
- "diagonal_left"
- "diagonal_right"
- "diagonal_up_left"
- "diagonal_up_right"
- "flower"
- "gradient"
- "gradient_up"
- "half_horizontal"
- "half_horizontal_bottom"
- "half_vertical"
- "half_vertical_right"
- "mojang"
- "piglin"
- "rhombus"
- "skull"
- "small_stripes"
- "square_bottom_left"
- "square_bottom_right"
- "square_top_left"
- "square_top_right"
- "straight_cross"
- "stripe_bottom"
- "stripe_center"
- "stripe_downleft"
- "stripe_downright"
- "stripe_left"
- "stripe_middle"
- "stripe_right"
- "stripe_top"
- "triangle_bottom"
- "triangle_top"
- "triangles_bottom"
- "triangles_top"

**可能的输入**

"function": "set_banner_details","type": "default","base_color": "blue","patterns": \[ { "pattern": "flower", "color": "white" }, { "pattern": "triangle_bottom", "color": "brown" }\]