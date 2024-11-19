---
title: Molang 查询
description: 解释了一些 MoLang 查询。
outline_depth: 2
mentions:
    - SirLich
    - solvedDev
    - stirante
    - SmokeyStack
    - Dreamedc2015
    - Ultr4Anubis
    - MedicalJewel105
    - TreaBeane
    - r4isen1920
    - ChillRx
    - Luthorius
    - TheItsNameless
    - ThomasOrs
---

Molang 的基岩版文档以其糟糕著称。本页面将尝试通过为个别查询提供额外细节来改善这一点，**在可能的情况下**。本页面旨在供搜索使用，而非全文阅读。请使用侧边栏或使用 `ctrl-f` 进行导航。

:::tip
本页面并非详尽无遗！它只包含我们为其编写了额外信息的查询。完整的查询列表可在[此处](https://bedrock.dev/docs/stable/Molang#List%20of%20Entity%20Queries)找到！
:::

## query.armor_texture_slot

格式如下：`query.armor_texture_slot(x) = y`。

其中 `x` 和 `y` 均为整数参数，取自下表：

### X

| 参数 | 插槽       |
| ---- | ---------- |
| 0    | 头盔       |
| 1    | 胸甲       |
| 2    | 护腿       |
| 3    | 靴子       |

### Y

| 参数 | 类型                  |
| ---- | --------------------- |
| -1   | 无                    |
| 0    | 皮革护甲部件           |
| 1    | 链甲部件               |
| 2    | 铁甲部件               |
| 3    | 钻石护甲部件           |
| 4    | 金甲部件               |
| 5    | 翼鲨装备               |
| 6    | 海龟头盔               |
| 7    | 下界合金护甲部件       |

### Y 对于马匹

| 参数 | 类型                |
| ---- | ------------------- |
| 1    | 皮革护甲部件         |
| 2    | 铁甲部件            |
| 3    | 金甲部件            |
| 4    | 钻石护甲部件         |

### 示例

`query.armor_texture_slot(3) == 1`：查询铁靴。

## query.armor_material_slot

格式如下：`query.armor_material_slot(x) = y`。

其中 `x` 和 `y` 均为整数参数，取自下表：

### X

| 参数 | 插槽       |
| ---- | ---------- |
| 0    | 头盔       |
| 1    | 胸甲       |
| 2    | 护腿       |
| 3    | 靴子       |

### Y

未知，可能是：

| 参数 | 插槽                       |
| ---- | -------------------------- |
| 0    | 默认护甲材质               |
| 1    | 附魔护甲材质               |
| 2    | 皮革护甲材质               |
| 3    | 皮革附魔材质               |

## query.armor_color_slot

_注意：自 `1.16.100.51` 版本起，此查询会导致 Minecraft 崩溃。可能在后续版本中已修复。_

格式如下：`color = query.armor_color_slot(slot, channel)`。

其中 `slot` 和 `channel` 均为整数参数，取自下表：

### 插槽

| 参数 | 插槽       |
| ---- | ---------- |
| 0    | 头盔       |
| 1    | 胸甲       |
| 2    | 护腿       |
| 3    | 靴子       |

### 通道

| 参数 | 插槽          |
| ---- | ------------- |
| 0    | 红色通道      |
| 1    | 绿色通道      |
| 2    | 蓝色通道      |
| 3    | Alpha 通道    |

### 颜色

查询返回指定通道的颜色值。

## query.get_equipped_item_name

:::warning
**已弃用查询：** 建议尽可能使用新的查询（`query.is_item_name_any`），因为它是此查询的更新版本。然而，为了向后兼容，此查询未来仍将继续有效。
:::

格式如下：`query.get_equipped_item_name('main_hand') = 'item_name'`

接受一个可选的手槽参数（0 或 `'main_hand'` 为主手，1 或 `'off_hand'` 为副手），以及第二个参数（0=默认）如果你希望获取已装备的物品或任何非零数以获取当前渲染的物品，并返回请求槽位中的物品名称（如果未提供参数，默认为主手），否则返回 ''。

其中 `item_name` 是你要测试的物品名称。无需命名空间，请注意引号。

示例：`"query.get_equipped_item_name == 'diamond'"`

**你可以测试物品栏中的物品吗？可以！使用新的查询 `query.is_item_name_any`。**

## query.get_name

:::warning
**已弃用查询：** 建议尽可能使用新的查询（`query.is_name_any`），因为它是此查询的更新版本。然而，为了向后兼容，此查询未来仍将继续有效。
:::

格式如下：`query.get_name == 'Name'`

如果实际游戏中显示的名称与名称匹配，则返回真（使用 OnixClient 查看第三人称视图中的名称）。需要在特殊条件下使用。

<details>
<summary>显示</summary>

```json title="animation_controllers/ac.json"
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.ac": {
            "initial_state": "default",
            "states": {
                "default": {
                    "transitions": [
                        {
                            "active": "query.is_alive"
                        }
                    ]
                },
                "active": {
                    "transitions": [
                        {
                            "default": "(1.0)"
                        }
                    ],
                    "animations": [
                        {
                            "anim": "query.get_name == '...'" // 只能在这里使用！
                        }
                    ]
                }
            }
        }
    }
}
```

</details>

## query.is_name_any

格式如下：`query.get_name('Name1', 'Name2')`。

接受一个或多个参数。如果实际游戏中显示的名称与给定名称之一匹配，则返回真。需要在特殊条件下使用。

<details>
<summary>显示</summary>

```json title="animation_controllers/ac.json"
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.ac": {
            "initial_state": "default",
            "states": {
                "default": {
                    "transitions": [
                        {
                            "active": "query.is_alive"
                        }
                    ]
                },
                "active": {
                    "transitions": [
                        {
                            "default": "(1.0)"
                        }
                    ],
                    "animations": [
                        {
                            "anim": "query.is_name_any(...)" // 只能在这里使用！
                        }
                    ]
                }
            }
        }
    }
}
```

</details>

## query.is_item_name_any

格式如下：`query.is_item_name_any('slot.weapon.mainhand', 0, 'namespace:item_name')`

首先接受装备槽名称，其次是槽位索引值，然后是带命名空间的物品名称列表。

可能的装备槽如下：

| 槽名称                    | 槽数量      | 描述                                                                             |
| ------------------------ | ----------- | -------------------------------------------------------------------------------- |
| `slot.weapon.mainhand`   | 0           | 通常持有的物品都在这里                                                          |
| `slot.weapon.offhand`    | 0           | 副手槽，用于 `Shield`、`Totem of Undying` 或 `Map` 等                       |
| `slot.armor.head`        | 0           | 头部护甲部件                                                                     |
| `slot.armor.chest`       | 0           | 胸甲护甲部件                                                                     |
| `slot.armor.legs`        | 0           | 护腿护甲部件                                                                     |
| `slot.armor.feet`        | 0           | 靴子护甲部件                                                                     |
| `slot.armor`             | 0           | 马匹护甲                                                                         |
| `slot.saddle`            | 0           | 马鞍槽                                                                           |
| `slot.hotbar`            | 0 to 8      | 玩家快捷栏槽位                                                                   |
| `slot.inventory`         | 0+ (varies) | 具有物品栏的实体，例如玩家、带有箱子的矿车、驴等                                   |
| `slot.enderchest`        | 0 to 26     | 仅适用于玩家的末影箱物品栏                                                        |

### 测试玩家物品栏中的物品

格式如下：`t.val = 0; t.i = 0; loop(27, {t.val = q.is_item_name_any('slot.inventory', t.i, 'namespace:item_name'); t.val ? {return t.val;}; t.i = t.i+1;});`

将 `namespace:item_name` 替换为你想要检查的任何物品。这将简单地循环检查物品栏的所有27个槽位，如果找到任何具有指定物品的槽位，则返回 `1.0`。请注意，快捷栏与主物品栏槽位不同，因此需要单独检查。

## query.is_enchanted

格式如下：`is_enchanted = query.is_enchanted`。

根据实体是否附魔返回 `1.0` 或 `0.0`。

_目前，仅可用于材质中。_

## query.is_eating

此查询跟踪某些实体什么时候在“进食”。不适用于玩家。要触发，请使用以下组件之一：
- `minecraft:behavior.eat_carried_item`
- `minecraft:behavior.snacking`

## query.is_ghost

格式如下：`is_ghost = query.is_ghost`。

根据实体是否为鬼魂返回 `1.0` 或 `0.0`。

_目前，仅对守卫鬼魂返回 `1.0`，并由其渲染器使用。_

## query.is_grazing

格式如下：`is_grazing = query.is_grazing`。

根据实体是否正在吃块返回 `1.0` 或 `0.0`。

_目前，仅对绵羊及使用绵羊运行时标识符的实体返回 `1.0`。_

## query.is_jumping

格式如下：`is_jumping = query.is_jumping`。

根据实体是否正在跳跃返回 `1.0` 或 `0.0`。

对于玩家，其激活条件为：

- 按下跳跃按钮（包括在水中和攀爬脚手架）
- 或者触发自动跳跃
- 或者在自动跳跃时游泳
- 或者给可骑乘实体充能跳跃

## query.modified_move_speed

格式如下：`modified_move_speed = query.modified_move_speed`。

返回实体当前的行走速度，受到诸如是否为婴儿或是否在燃烧等状态标志的修改。

数值示例：

- 玩家行走时：约为 0.86
- 玩家冲刺时：1.0
- 玩家冲刺并跳跃时：0.35
- 玩家在火上行走时：1.0
- 玩家在火上冲刺时：1.0
- 玩家在火上冲刺并跳跃时：0.525

## query.log

内容日志不是调试日志，它们是不同的文件。`query.log` 只输出到调试日志。

## query.on_fire_time

格式如下：`on_fire_time = query.on_fire_time`。

返回实体开始或停止燃烧的时间（以刻为单位），否则返回 `0.0`。

数值示例：

- 实体被召唤时：值为 0
- 实体被点燃时：值为 0，并每刻增加 1
- 实体已在火上燃烧 2 秒：值为 40，且仍每刻增加 1
- 实体停止燃烧时：值重置为 0，尽管不再燃烧，仍每刻增加 1
- 实体第二次被点燃时：值重置为 0，并继续每刻增加 1
- 实体第二次停止燃烧时：值重置为 0，尽管不再燃烧，仍每刻增加 1

基本上，这是一个在实体首次被点燃后开始并在每次变化为/停止燃烧时重置的刻计时器。

## query.scoreboard

格式如下：`query.scoreboard('objective_name') > 0`

如果查询的值在指定范围内，则返回 `1.0` 或 `0.0`。或基于分数计数、Molang 运算符和数字。

请注意，有时由于未知原因可能无法正常工作。其中一个原因是无法查询带有大写字母的记分板目标名称。在这种情况下，例如，目标 `testfoo` 可以正常工作，但 **不能** 使用 `testFoo`。

## query.structural_integrity

格式如下：`structural_integrity = query.structural_integrity`。

用于船和矿车的破坏。攻击实体时会减少，并会随时间恢复。可能无法被船和矿车之外的实体使用。

## variable.attack_time

### 解释

此变量设置为如果它是一个查询。换句话说，它可以在任何实体上使用，无论是在客户端还是服务器，无需正确设置/定义变量。

### 对于实体

该变量跟踪实体攻击时挥舞的时间。当不攻击时，返回 `0.0`，攻击时范围从 `0.0` 到总攻击时间，可能约为 `0.3` 或类似。对于玩家，此值范围为 `0.0` 到 `1.0`。该变量以小数形式返回实体攻击进度的百分比。例如，如果实体的攻击挥舞进行到一半，则变量返回 `0.5`。它线性递增。

### 对于玩家

对于玩家，该变量将跟踪手臂骨骼的挥动，包括：

- 放置方块
- 放置实体
- 互动（当启用挥动时）
- 近战攻击

## query.is_roaring

当发生 `knockback_roar` 攻击时返回真。

## query.head_x_rotation

格式如下：`query.head_x_rotation(x)`

其中 `x` 指定实体的头部。实际上仅对凋灵相关。

返回头部俯仰角。向上看返回 `-89.9`，向下看返回 `89.9`。

## query.head_y_rotation

格式如下：`query.head_y_rotation(x)`

其中 `x` 指定实体的头部。实际上仅对凋灵相关。

返回头部的偏航角，从 `-179.9` 到 `179.9`。值会绕回，例如如果你在 `-179.9`，稍微转动一下，则立即变为 `179.9`。

## query.target_x_rotation 和 query.target_y_rotation

与各自的 `query.head_*_rotation` 相同，但没有选择头部的可选参数。

## query.time_of_day

返回实体所在维度的时间（午夜=0.0，日出=0.25，中午=0.5，日落=0.75）。
白天时间通过以下公式计算：

`f(x) = (x*0.25/2400)mod 1`

query.time_of_day - 白天时间表

<details>
<summary>显示</summary>

| `query.time_of_day` | 白天时间 |
| ------------------- | -------- |
| 0.00                | 18000    |
| 0.01                | 18240    |
| 0.02                | 18480    |
| 0.03                | 18720    |
| 0.04                | 18960    |
| 0.05                | 19200    |
| 0.06                | 19440    |
| 0.07                | 19680    |
| 0.08                | 19920    |
| 0.09                | 20162    |
| 0.10                | 20400    |
| 0.11                | 20640    |
| 0.12                | 20880    |
| 0.13                | 21120    |
| 0.14                | 21360    |
| 0.15                | 21602    |
| 0.16                | 21840    |
| 0.17                | 22080    |
| 0.18                | 22322    |
| 0.19                | 22560    |
| 0.20                | 22800    |
| 0.21                | 23040    |
| 0.22                | 23280    |
| 0.23                | 23520    |
| 0.24                | 23760    |
| 0.25                | 0        |
| 0.26                | 240      |
| 0.27                | 480      |
| 0.28                | 720      |
| 0.29                | 960      |
| 0.30                | 1202     |
| 0.31                | 1440     |
| 0.32                | 1680     |
| 0.33                | 1922     |
| 0.34                | 2160     |
| 0.35                | 2400     |
| 0.36                | 2642     |
| 0.37                | 2880     |
| 0.38                | 3120     |
| 0.39                | 3360     |
| 0.40                | 3600     |
| 0.41                | 3840     |
| 0.42                | 4080     |
| 0.43                | 4320     |
| 0.44                | 4560     |
| 0.45                | 4800     |
| 0.46                | 5040     |
| 0.47                | 5280     |
| 0.48                | 5520     |
| 0.49                | 5760     |
| 0.50                | 6000     |
| 0.51                | 6240     |
| 0.52                | 6480     |
| 0.53                | 6720     |
| 0.54                | 6960     |
| 0.55                | 7200     |
| 0.56                | 7440     |
| 0.57                | 7680     |
| 0.58                | 7920     |
| 0.59                | 8160     |
| 0.60                | 8402     |
| 0.61                | 8640     |
| 0.62                | 8880     |
| 0.63                | 9120     |
| 0.64                | 9360     |
| 0.65                | 9600     |
| 0.66                | 9842     |
| 0.67                | 10080    |
| 0.68                | 10320    |
| 0.69                | 10560    |
| 0.70                | 10800    |
| 0.71                | 11040    |
| 0.72                | 11282    |
| 0.73                | 11520    |
| 0.74                | 11760    |
| 0.75                | 12000    |
| 0.76                | 12240    |
| 0.77                | 12480    |
| 0.78                | 12720    |
| 0.79                | 12962    |
| 0.80                | 13200    |
| 0.81                | 13440    |
| 0.82                | 13680    |
| 0.83                | 13920    |
| 0.84                | 14160    |
| 0.85                | 14402    |
| 0.86                | 14640    |
| 0.87                | 14880    |
| 0.88                | 15120    |
| 0.89                | 15360    |
| 0.90                | 15600    |
| 0.91                | 15842    |
| 0.92                | 16080    |
| 0.93                | 16320    |
| 0.94                | 16560    |
| 0.95                | 16800    |
| 0.96                | 17040    |
| 0.97                | 17282    |
| 0.98                | 17520    |
| 0.99                | 17760    |
| 1.00                | 18000    |

Credit: [Analysis of query.time_of_day](https://gist.github.com/DoubleF3lix/a03afde0a979dfa41e8525ee92f12ca5)

</details>

## query.eye_target_x_rotation 和 query.eye_target_y_rotation

对玩家无效。不太确定它的用途。

## variable.short_arm_offset_right

返回玩家右臂骨骼相对于默认皮肤几何的偏移因子。装备在玩家身上的细臂（3像素宽）皮肤返回 `0.5`，普通（4像素宽）皮肤返回 `0.0`。注意：玩家必须至少切换到第一人称视角一次，才能初始化此变量并在实体的其他地方使用。

## variable.short_arm_offset_left

与 `variable.short_arm_offset_right` 行为相同，只是引用了玩家左臂骨骼。

## query.movement_direction

返回实体移动的归一化向量的其中一个3个分量，意味着向量的模/长度在0到1之间。

**注意**：根据当前文档撰写时的情况，任何轴返回的值将根据实体的速度而变化（如果实体在地面上，值将小于实体在空中时的值，即使它们朝相同方向移动）。

要获取实体移动的实际归一化速度向量，你需要对值进行归一化。以下是 Molang 设置：

```
variable.mag = math.sqrt( math.pow( query.movement_direction(0), 2 ) + math.pow( query.movement_direction(1), 2) + math.pow( query.movement_direction(2), 2));
variable.xNorm = query.movement_direction(0) / variable.mag;
variable.yNorm = query.movement_direction(1) / variable.mag;
variable.zNorm = query.movement_direction(2) / variable.mag;
```

有关归一化向量的更多信息，你可以尝试使用这个 <a href=https://www.desmos.com/calculator/hhoamwgve2>Desmos 图表</a>

| 参数 | 轴 |
| ---- | -- |
| 0    | X  |
| 1    | Y  |
| 2    | Z  |

## query.block_neighbor_has_any_tag 和 query.relative_block_has_any_tag

需要启用 `Experimental Molang Features` 才能使用。文档中说明 `接受一个相对位置和一个或多个标签名称，并根据该位置的块是否具有提供的任何标签返回 0 或 1`。这对于使用连接块或检测实体有用。

`query.block_neighbor_has_any_tag` - 接受块位置  
`query.relative_block_has_any_tag` - 接受实体位置

其语法为 `q.block_neighbor_has_any_tag(x,y,z,'tag_name')` 和 `q.relative_block_has_any_tag(x,y,z,'tag_name')`。

示例：

- `q.relative_block_has_any_tag(0,-1,0,'grass')` 将尝试检测实体下方一个块是否具有 grass 标签。
- `q.block_neighbor_has_any_tag(0,-1,0,'grass')` 将尝试检测该块下方一个块是否具有 grass 标签。

要使用多个标签，可以使用 `q.correct_query(0,-1,0,'grass', 'plant')`，其中 `correct_query` 需替换为正确的查询。

请注意，这也可以检测自定义标签和[原版标签](../blocks/block-tags.md)。