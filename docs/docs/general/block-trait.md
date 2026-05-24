# 方块萃取

**方块萃取（Block Trait）**是自定义方块用于复用部分原版方块状态和相关设置逻辑的机制。方块萃取使自定义方块可以通过声明获得类似原版方块的放置方向、附着位置或连接关系，而无需完整手写对应的状态更新逻辑。

## 概述

方块萃取不是普通组件。普通组件通常直接定义方块的某项属性或行为，而方块萃取更接近一组由引擎维护的状态和状态设置规则。方块放置、邻近方块变化或特定交互发生时，萃取可以自动更新其启用的方块状态。

方块萃取的核心价值在于复用原版方块已有的常见模式。例如，许多方块需要根据玩家放置时的朝向旋转；许多附着型方块需要记录被放置在地面、墙面还是天花板；栅栏或玻璃板类方块需要根据相邻方块决定连接方向。

## 常见萃取

基岩版公开的方块萃取会随版本扩展。常见萃取包括：

| 萃取 | 作用 |
|------|------|
| `minecraft:placement_direction` | 根据玩家放置方块时的朝向设置方向相关状态 |
| `minecraft:placement_position` | 根据方块相对于相邻方块的放置位置设置附着面、上下半部等状态 |
| `minecraft:connection` | 根据相邻方块关系设置水平连接方向状态<!-- md:flag experimental --> |
| `minecraft:multi_block` | 使一个定义表示跨越多个方块位置的多方块结构<!-- md:flag experimental --> |

具体可用萃取、可启用状态和实验性要求应以对应游戏版本的官方参考为准。

## 与方块状态

方块萃取通常通过启用一个或多个原版方块状态发挥作用。例如，`minecraft:placement_direction`可以启用水平朝向、六面朝向或楼梯角部相关状态，`minecraft:placement_position`可以启用附着面或上下半部相关状态。启用后，这些状态会成为该自定义方块置换的一部分。

方块萃取生成或维护的是状态值，而不是最终外观本身。方块要根据这些状态改变几何体、材质、碰撞箱或其他组件，仍然需要通过[方块置换](block-permutation.md)配置相应组件。

### 放置方向

`minecraft:placement_direction`记录玩家放置方块时面对的方向。该萃取可以启用`minecraft:cardinal_direction`、`minecraft:facing_direction`或`minecraft:corner_and_cardinal_direction`。其中，`minecraft:cardinal_direction`提供`north`、`south`、`east`和`west`四个水平取值；`minecraft:facing_direction`在水平四向之外增加`up`和`down`；`minecraft:corner_and_cardinal_direction`还会使`minecraft:corner`提供`inner_left`、`inner_right`、`outer_left`、`outer_right`和`none`等角部取值。

该萃取还可以使用`y_rotation_offset`改变记录的水平朝向偏移。偏移值以逆时针方向计，可使用`0.0`、`90.0`、`180.0`或`270.0`。

### 放置位置

`minecraft:placement_position`记录方块相对于其他方块被放置的位置。该萃取可以启用`minecraft:block_face`或`minecraft:vertical_half`。`minecraft:block_face`表示该方块附着的相邻方块面，取值为`north`、`south`、`east`、`west`、`up`或`down`。`minecraft:vertical_half`表示方块被放置在相邻方块的上半或下半，取值为`top`或`bottom`。

### 连接关系

`minecraft:connection`记录方块是否与相邻方块连接。该萃取目前要求`format_version`不低于`1.21.130`，并需要启用“Upcoming Creator Features”实验性开关。该萃取目前只能启用`minecraft:cardinal_connections`，并由此提供`minecraft:connection_north`、`minecraft:connection_south`、`minecraft:connection_east`和`minecraft:connection_west`四个可查询布尔状态。

## 与组件和事件

组件用于声明方块的属性，事件用于响应触发条件，方块萃取用于提供一组常见状态的维护逻辑。三者可以组合使用，但职责不同。

例如，一个自定义灯具可以使用`minecraft:placement_position`记录自身附着在哪个面，再通过方块置换为不同附着面应用不同几何体；同时，它还可以使用组件定义光照，并使用事件处理玩家交互。

## 版本影响

方块萃取与格式版本和实验性开关关系密切。部分萃取最初需要实验性玩法，之后才进入稳定接口；较新的萃取可能仍处于实验性阶段。文档编写和附加包开发时应同时关注方块定义的格式版本、世界实验性开关和目标游戏版本。