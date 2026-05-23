# 迷雾

**迷雾（Fog）**是Minecraft基岩版中控制远处场景可见度和颜色的渲染系统。迷雾通过逐渐混合远处物体的颜色与指定的迷雾颜色来模拟大气效果，是生物群系视觉表现的重要组成部分。

## 概述

迷雾定义了游戏世界中远处场景的淡化方式，包括迷雾的颜色、起始距离、终止距离和介质效果。不同的生物群系、天气条件和特殊场景（如水下、岩浆中、粉雪中）会应用不同的迷雾设置，以营造不同的氛围效果。

**迷雾定义（Fog Definition）**文件以JSON格式编写，存放在资源包的`fogs/`目录中。每个迷雾定义通过赋命名空间标识符引用。迷雾属于客户端资源，通常与客户端生物群系定义、功能域、命令或脚本共同决定玩家实际看到的环境效果。

## 迷雾设置

迷雾定义文件的根键为`minecraft:fog_settings`，其`description.identifier`字段给出该迷雾定义的赋命名空间标识符。`format_version`用于声明该文件依据的格式版本；当前官方资料中迷雾文件的最低格式版本为`1.16.100`。

`minecraft:fog_settings`主要包含距离迷雾与体积迷雾两类设置。字段结构参考见[迷雾定义参考](../../refs/addon/fog-settings.md)。

### 距离迷雾

**距离迷雾（Distance Fog）**控制基于距离的可见度衰减。它通常用于限制玩家能看清的最远距离，并为远景指定统一的迷雾颜色。距离迷雾位于`distance`对象中，并按摄像机所处环境或天气状态分为多个类别：

- `air`：摄像机位于空气中时的迷雾。
- `weather`：摄像机位于空气中且存在雨、雪等天气时的迷雾。
- `water`：摄像机位于水中时的迷雾。
- `lava`：摄像机位于岩浆中时的迷雾。
- `lava_resistance`：摄像机位于岩浆中且玩家具有抗火状态效果时的迷雾。
- `powder_snow`：摄像机位于粉雪方块中时的迷雾。

每个类别可以独立指定`fog_start`、`fog_end`、`fog_color`和`render_distance_type`。`render_distance_type`为`fixed`时，起止值按方块距离解释；为`render`时，起止值按当前渲染距离的比例解释。水下迷雾还可以使用`transition_fog`定义玩家进入水中时从初始迷雾向目标水下迷雾过渡的过程。

### 体积迷雾

**体积迷雾（Volumetric Fog）**控制光线穿过空气、水、岩浆、天气和云等介质时的密度、散射和吸收效果。它位于`volumetric`对象中，主要由`density`和`media_coefficients`两组设置组成。

`density`描述介质对光线的遮蔽程度，可按`air`、`weather`、`water`、`lava`和`lava_resistance`分别设置。`media_coefficients`描述光线在介质中的散射与吸收，可按`air`、`water`和`cloud`分别设置。体积迷雾最初主要用于光线追踪资源包；在**鲜艳视觉（Vibrant Visuals）**相关资源中，体积迷雾和光束效果也复用迷雾定义与功能域等既有资源包机制<!-- md:flag vanilla -->。

## 迷雾栈

**迷雾栈（Fog Stack）**是游戏在渲染时按优先级叠加多个迷雾设置的机制。玩家的迷雾栈中可能同时存在多个迷雾定义（如生物群系迷雾、天气迷雾、脚本推送的迷雾等），游戏按照优先级从高到低合并这些设置，最终确定实际的渲染迷雾参数。

当游戏需要确定某个迷雾参数时，会从迷雾栈顶部向下查找第一个定义了该参数的迷雾设置；如果某一层未提供该字段，则继续检查下一层。若所有数据驱动层均未提供对应字段，游戏会使用引擎内置默认值。

官方资料描述的初始优先级从高到低为：

1. **命令层**：通过`/fog`命令为玩家设置的迷雾。
2. **生物群系层**：玩家附近生物群系指定的迷雾，其结果由周围生物群系的设置共同影响。
3. **数据默认层**：资源包根目录`biomes_client.json`中`default`条目指定的迷雾（兼容层）。
4. **引擎默认层**：游戏硬编码的最终回退值。

命令层本身也按栈处理。`/fog push`会把一个迷雾定义和用户提供ID推入目标玩家的命令层顶部；`/fog pop`移除顶部匹配该用户提供ID的迷雾；`/fog remove`移除所有匹配该用户提供ID的迷雾。命令层迷雾会随玩家保存，并在世界重新加载后恢复。

## 原版迷雾标识符

以下列出基岩版中内置的原版迷雾定义标识符及其适用的生物群系。这些标识符可在`/fog`命令、客户端生物群系定义和附加包迷雾定义中直接引用。

| 迷雾标识符 | 适用生物群系 |
|-----------|------------|
| `minecraft:fog_bamboo_jungle` | 竹林（`bamboo_jungle`） |
| `minecraft:fog_bamboo_jungle_hills` | 竹林丘陵（`bamboo_jungle_hills`） |
| `minecraft:fog_basalt_deltas` | 玄武岩三角洲（`basalt_deltas`） |
| `minecraft:fog_beach` | 沙滩（`beach`） |
| `minecraft:fog_birch_forest` | 桦木林（`birch_forest`） |
| `minecraft:fog_birch_forest_hills` | 桦木林丘陵（`birch_forest_hills`） |
| `minecraft:fog_cherry_grove` | 樱花树林（`cherry_grove`） |
| `minecraft:fog_cold_beach` | 寒冷沙滩（`cold_beach`） |
| `minecraft:fog_cold_ocean` | 寒冷海洋（`cold_ocean`） |
| `minecraft:fog_cold_taiga` | 寒冷针叶林（`cold_taiga`） |
| `minecraft:fog_cold_taiga_hills` | 寒冷针叶林丘陵（`cold_taiga_hills`） |
| `minecraft:fog_cold_taiga_mutated` | 突变寒冷针叶林（`cold_taiga_mutated`） |
| `minecraft:fog_crimson_forest` | 绯红森林（`crimson_forest`） |
| `minecraft:fog_deep_cold_ocean` | 深层寒冷海洋（`deep_cold_ocean`） |
| `minecraft:fog_deep_frozen_ocean` | 深层冰冻海洋（`deep_frozen_ocean`） |
| `minecraft:fog_deep_lukewarm_ocean` | 深层温水海洋（`deep_lukewarm_ocean`） |
| `minecraft:fog_deep_ocean` | 深层海洋（`deep_ocean`） |
| `minecraft:fog_deep_warm_ocean` | 深层温暖海洋（`deep_warm_ocean`） |
| `minecraft:fog_default` | 默认（`default`） |
| `minecraft:fog_desert` | 沙漠（`desert`） |
| `minecraft:fog_desert_hills` | 沙漠丘陵（`desert_hills`） |
| `minecraft:fog_extreme_hills` | 峭壁（`extreme_hills`） |
| `minecraft:fog_extreme_hills_edge` | 峭壁边缘（`extreme_hills_edge`） |
| `minecraft:fog_extreme_hills_mutated` | 突变峭壁（`extreme_hills_mutated`） |
| `minecraft:fog_extreme_hills_plus_trees` | 带树林的峭壁（`extreme_hills_plus_trees`） |
| `minecraft:fog_extreme_hills_plus_trees_mutated` | 突变带树林的峭壁（`extreme_hills_plus_trees_mutated`） |
| `minecraft:fog_flower_forest` | 繁花森林（`flower_forest`） |
| `minecraft:fog_forest` | 森林（`forest`） |
| `minecraft:fog_forest_hills` | 森林丘陵（`forest_hills`） |
| `minecraft:fog_frozen_ocean` | 冰冻海洋（`frozen_ocean`） |
| `minecraft:fog_frozen_river` | 冰冻河流（`frozen_river`） |
| `minecraft:fog_hell` | 下界荒地（`hell`） |
| `minecraft:fog_ice_mountains` | 冰封山脉（`ice_mountains`） |
| `minecraft:fog_ice_plains` | 冰原（`ice_plains`） |
| `minecraft:fog_ice_plains_spikes` | 冰刺平原（`ice_plains_spikes`） |
| `minecraft:fog_jungle` | 丛林（`jungle`） |
| `minecraft:fog_jungle_edge` | 丛林边缘（`jungle_edge`） |
| `minecraft:fog_jungle_hills` | 丛林丘陵（`jungle_hills`） |
| `minecraft:fog_jungle_mutated` | 突变丛林（`jungle_mutated`） |
| `minecraft:fog_lukewarm_ocean` | 温水海洋（`lukewarm_ocean`） |
| `minecraft:fog_mangrove_swamp` | 红树林沼泽（`mangrove_swamp`） |
| `minecraft:fog_mega_spruce_taiga` | 巨型云杉针叶林（`mega_spruce_taiga`） |
| `minecraft:fog_mega_spruce_taiga_mutated` | 突变巨型云杉针叶林（`mega_spruce_taiga_mutated`） |
| `minecraft:fog_mega_taiga` | 巨型针叶林（`mega_taiga`） |
| `minecraft:fog_mega_taiga_hills` | 巨型针叶林丘陵（`mega_taiga_hills`） |
| `minecraft:fog_mega_taiga_mutated` | 突变巨型针叶林（`mega_taiga_mutated`） |
| `minecraft:fog_mesa` | 平顶山（`mesa`） |
| `minecraft:fog_mesa_bryce` | 布莱斯平顶山（`mesa_bryce`） |
| `minecraft:fog_mesa_mutated` | 突变平顶山（`mesa_mutated`） |
| `minecraft:fog_mesa_plateau` | 平顶山高原（`mesa_plateau`） |
| `minecraft:fog_mesa_plateau_stone` | 石质平顶山高原（`mesa_plateau_stone`） |
| `minecraft:fog_mushroom_island` | 蘑菇岛（`mushroom_island`） |
| `minecraft:fog_mushroom_island_shore` | 蘑菇岛海岸（`mushroom_island_shore`） |
| `minecraft:fog_ocean` | 海洋（`ocean`） |
| `minecraft:fog_plains` | 平原（`plains`） |
| `minecraft:fog_river` | 河流（`river`） |
| `minecraft:fog_roofed_forest` | 黑森林（`roofed_forest`） |
| `minecraft:fog_savanna` | 热带草原（`savanna`） |
| `minecraft:fog_savanna_mutated` | 突变热带草原（`savanna_mutated`） |
| `minecraft:fog_savanna_plateau` | 热带高原（`savanna_plateau`） |
| `minecraft:fog_soulsand_valley` | 灵魂沙峡谷（`soulsand_valley`） |
| `minecraft:fog_stone_beach` | 石滩（`stone_beach`） |
| `minecraft:fog_sunflower_plains` | 向日葵平原（`sunflower_plains`） |
| `minecraft:fog_swampland` | 沼泽（`swampland`） |
| `minecraft:fog_swampland_mutated` | 突变沼泽（`swampland_mutated`） |
| `minecraft:fog_taiga` | 针叶林（`taiga`） |
| `minecraft:fog_taiga_hills` | 针叶林丘陵（`taiga_hills`） |
| `minecraft:fog_taiga_mutated` | 突变针叶林（`taiga_mutated`） |
| `minecraft:fog_the_end` | 末地（`the_end`） |
| `minecraft:fog_warm_ocean` | 温暖海洋（`warm_ocean`） |
| `minecraft:fog_warped_forest` | 诡异森林（`warped_forest`） |

每个生物群系可以在资源包客户端生物群系定义中，通过`minecraft:fog_appearance.fog_identifier`字段关联一个迷雾定义。当前推荐使用`biomes/`目录下按生物群系拆分的`minecraft:client_biome`文件；`biomes_client.json`仍可用于兼容既有内容。当玩家进入不同的生物群系时，游戏会根据附近生物群系的客户端设置计算生物群系层迷雾，从而呈现出不同生物群系的独特氛围。

`biomes_client.json`中的`default`条目也可以指定`fog_identifier`。该默认迷雾不完全替代生物群系迷雾，而是位于生物群系层之下，作为数据驱动默认值参与迷雾栈回退。客户端生物群系字段结构见[客户端生物群系定义](../../refs/addon/client-biome.md)。
