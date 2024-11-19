---
title: 区块组件
description: 区块组件用于改变你的区块在世界中的外观和功能。
category: 通用
nav_order: 2
mentions:
    - SirLich
    - solvedDev
    - yanasakana
    - SmokeyStack
    - MedicalJewel105
    - aexer0e
    - Chikorita-Lover
    - Luthorius
    - TheDoctor15
    - XxPoggyisLitxX
    - TheItsNameless
    - ThomasOrs
    - Kaioga5
    - QuazChick
---

:::tip 格式 & 最低引擎版本 `1.21.40`
在创建自定义区块时使用最新的格式版本可以访问新功能和改进。维基旨在分享有关自定义区块的最新信息，当前目标格式版本为 `1.21.40`。
:::
:::danger 覆盖组件
每种组件只能同时激活一个实例。重复的组件将被最新的[排列](../blocks/block-permutations.md)条目覆盖。
:::

## 应用组件

区块组件用于改变你的区块在世界中的外观和功能。它们应用于`minecraft:block`的`components`子项或[排列](../blocks/block-permutations.md)。

```json title="BP/blocks/lamp.json"
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:lamp",
            "menu_category": {
                "category": "items"
            }
        },
        "components": {
            "minecraft:light_dampening": 0,
            "minecraft:light_emission": 15,
            "minecraft:map_color": [210, 200, 190],
            "minecraft:geometry": "geometry.lamp",
            "minecraft:material_instances": {
                "*": {
                    "texture": "lamp"
                },
                "shade": {
                    "texture": "lamp_shade"
                }
            }
        }
    }
}
```

## 组件列表

### 碰撞盒

定义区块与实体碰撞的区域。如果设置为 true，将使用默认值。如果设置为 false，将禁用该区块与实体的碰撞。如果省略此组件，将使用默认值。

_在格式版本 1.19.50 及更高版本中，取消了实验性功能 `Holiday Creator Features`。_

类型：布尔值/对象

-   `origin`: 向量 [a, b, c]
    -   碰撞盒边界的最小位置。`origin` 以 `[x, y, z]` 指定，范围必须在 `(-8, 0, -8)` 到 `(8, 16, 8)`（含）之间。
-   `size`: 向量 [a, b, c]
    -   碰撞盒每个面的大小。大小以 `[x, y, z]` 指定。`origin` + `size` 必须在 `(-8, 0, -8)` 到 `(8, 16, 8)`（含）之间。

#### 使用布尔值的示例

```json title="minecraft:block > components"
"minecraft:collision_box": true
```

#### 使用对象的示例

```json title="minecraft:block > components"
"minecraft:collision_box": {
    "origin": [-8, 0, -8],
    "size": [16, 16, 16]
}
```

### 合成台

将你的区块变为自定义合成台，启用合成台界面和合成配方的能力。

_在格式版本 1.19.50 及更高版本中，取消了实验性功能 `Holiday Creator Features`。_

类型：对象

-   `crafting_tags`: 数组
    -   必填字段
    -   定义配方应在此合成台上进行合成的标签。限制为 64 个标签。每个标签限制为 64 个字符。
-   `table_name`: 字符串
    -   指定映射到此合成台界面中显示文本的语言文件键。如果给定的字符串无法解析为本地化字符串，将显示原始字符串。如果省略此字段，显示的名称将默认使用“display_name”组件中指定的名称。如果该区块没有“display_name”组件，显示的名称将默认使用区块的名称。

```json title="minecraft:block > components"
"minecraft:crafting_table": {
    "table_name": "Wiki Workbench",
    "crafting_tags": [
        "crafting_table",
        "wiki_workbench"
    ]
}
```

### 可被爆炸破坏

描述此区块的可被爆炸破坏属性。如果设置为 true，区块将具有默认的爆炸抗性。如果设置为 false，此区块将无法被爆炸破坏。如果省略此组件，区块将具有默认的爆炸抗性。

类型：布尔值/对象

-   `explosion_resistance`: 双精度
    -   描述区块对爆炸的抗性。数值越大，区块在靠近爆炸时越不易破碎（或具有更高的抗爆性）。不同爆炸强度级别的比例不同。负值或 0 表示区块容易被爆炸破坏；较大的数值增加抗性级别。

#### 使用布尔值的示例

```json title="minecraft:block > components"
"minecraft:destructible_by_explosion": false
```

#### 使用对象的示例

```json title="minecraft:block > components"
"minecraft:destructible_by_explosion": {
    "explosion_resistance": 20
}
```

### 可被矿采破坏

描述此区块的可被矿采破坏属性。如果设置为 true，区块将需要默认的破坏时间。如果设置为 false，此区块将无法被矿采破坏。如果省略此组件，区块将需要默认的破坏时间。

类型：布尔值/对象

-   `seconds_to_destroy`: 双精度
    -   设置使用基础工具破坏区块所需的秒数。数值越大，矿采时间越长。
    -   注意：实际破坏时间为定义秒数的 2 倍。

#### 使用布尔值的示例

```json title="minecraft:block > components"
"minecraft:destructible_by_mining": false
```

#### 使用对象的示例

```json title="minecraft:block > components"
"minecraft:destructible_by_mining": {
    "seconds_to_destroy": 20
}
```

### 显示名称

指定映射到当你在物品栏和快捷栏中悬停区块时显示的文本的语言文件键。如果给定的字符串无法解析为本地化字符串，将显示原始字符串。如果省略此组件，区块的名称将作为显示名称使用。

_在格式版本 1.19.60 及更高版本中，取消了实验性功能 `Holiday Creator Features`。_

类型：字符串

#### 使用字符串的示例

```json title="minecraft:block > components"
"minecraft:display_name": "Custom Block"
```

#### 使用本地化字符串的示例

```json title="minecraft:block > components"
"minecraft:display_name": "tile.wiki:custom_block.name"
```

```c title="RP/texts/en_US.lang"
tile.wiki:custom_block.name=Custom Block
```

### 实体坠落触发

当实体坠落到此区块上时触发事件。

类型：对象

-   `min_fall_distance`: 双精度
    -   实体必须坠落的最小距离（以区块为单位）以触发事件。

_在格式版本 1.21.10 及更高版本中，取消了实验性功能 `Beta APIs`。_

```json title="minecraft:block > components"
"minecraft:entity_fall_on": {
    "min_fall_distance": 5
}
```

### 可燃性

描述此区块的可燃性属性。如果设置为 true，将使用默认值。如果设置为 false，或省略此组件，区块将无法自然从邻近区块起火，但仍然可以被直接点燃。

类型：布尔值/对象

-   `catch_chance_modifier`: 整数
    -   影响此区块在靠近火源时起火几率的修正值。值大于或等于 0，数值越高，起火几率越大。对于 `catch_chance_modifier` 大于 0 的情况，火将持续燃烧直到区块被摧毁（或如果 `destroy_chance_modifier` 为 0，则将永远燃烧）。如果 `catch_chance_modifier` 为 0，并且区块被直接点燃，火最终将熄灭而不摧毁区块（或者如果 `destroy_chance_modifier` 大于 0，则有机会被摧毁）。默认值 5 与木板相同。

#### 使用布尔值的示例

```json title="minecraft:block > components"
"minecraft:flammable": true
```

#### 使用对象的示例

```json title="minecraft:block > components"
"minecraft:flammable": {
    "catch_chance_modifier": 5,
    "destroy_chance_modifier": 20
}
```

### 摩擦

描述此区块的摩擦，范围为 (0.0-0.9)。摩擦影响实体在区块上移动的速度。数值越大，摩擦越大。

类型：双精度

```json title="minecraft:block > components"
"minecraft:friction": 0.4
```

### 几何体

用于渲染此区块的几何体描述符。此描述符必须与任何已加载资源包中的现有几何体描述符匹配，或是当前支持的原版描述符之一：`minecraft:geometry.full_block` 或 `minecraft:geometry.cross`。

**自定义区块模型限制：**

-   区块大小限制为 30&times;30&times;30 <abbr title="16分之一区块单位">像素</abbr>。
-   区块在每个轴上的至少 1 个像素必须包含在基础 16&times;16&times;16 区块内。
-   30&times;30&times;30 区块位置的绝对边界为原点每个方向 30 <abbr title="16分之一区块单位">像素</abbr>。只要遵守规则 #2，区块可以在这些边界内的任何位置放置。

注意：不导电红石，即使使用原版 `full_block` 描述符。使你的区块可呼吸，生物无法在其上生成。有趣的是，蝙蝠能够倒挂在其上，尽管它们在生成性和导电性方面是“非固体”区块。

_在格式版本 1.19.40 及更高版本中，取消了实验性功能 `Holiday Creator Features`。_

类型：字符串/对象

-   `identifier`: 字符串
    -   几何体的标识符。
-   `bone_visibility`: 对象
    -   可选的布尔值“数组”，定义几何文件中各个骨骼的可见性。为了设置 `bone_visibility`，几何文件名必须作为标识符输入。在指定标识符后，可以基于指定几何文件中骨骼的名称以真/假方式定义 `bone_visibility`。
    -   请注意，所有骨骼默认设置为 true，因此仅在设置为 false 时才应定义骨骼。包括设置为 true 的骨骼将与默认值相同。

#### 使用字符串的示例

```json title="minecraft:block > components"
"minecraft:geometry": "geometry.example_block"
```

#### 使用对象的示例

```json title="minecraft:block > components"
"minecraft:geometry": {
    "identifier": "geometry.example_block"
}
```

---

#### 骨骼可见性

在模型中隐藏骨骼的直接子立方体。

**Molang 表达式必须遵守[排列条件](../blocks/block-permutations.md#permutation-conditions)的限制。**

_在格式版本 1.20.10 及更高版本中，`bone_visibility` 支持 Molang 表达式。_

```json title="minecraft:block > components"
"minecraft:geometry": {
    "identifier": "geometry.example_block",
    "bone_visibility": {
        "wiki_bone": false,
        "conditional_bone": "q.block_state('wiki:example_state') == 3",
        "another_bone": true
    }
}
```

### 光线衰减

光通过区块时的衰减量，范围为 (0-15)。数值越高，光线衰减越多。

类型：整数

```json title="minecraft:block > components"
"minecraft:light_dampening": 7
```

### 光线发射

此区块发射的光量，范围为 (0-15)。数值越高，发射的光量越多。

类型：整数

```json title="minecraft:block > components"
"minecraft:light_emission": 10
```

### 掉落物

掉落表的路径，相对于行为包。

**如果省略，将掉落区块作为物品。**

类型：字符串

```json title="minecraft:block > components"
"minecraft:loot": "loot_tables/blocks/custom_block.json"
```

### 映射颜色

设置在地图上渲染时的区块颜色。颜色以 `#RRGGBB` 的十六进制值表示。也可以表示为 [R, G, B] 数组，范围为 0 到 255。如果省略此组件，区块将不会在地图上显示。

类型：字符串/向量 [a, b, c]

#### 使用字符串的示例

```json title="minecraft:block > components"
"minecraft:map_color": "#FFFFFF"
```

#### 使用向量 [a, b, c] 的示例

```json title="minecraft:block > components"
"minecraft:map_color": [255, 255, 255]
```

### 材质实例

配置区块的渲染，包括纹理和照明。

-   所有实例必须具有相同的渲染方法。
-   如果与另一个区块相交，区块面将无条件地变暗。

材质实例可以与`RP/blocks.json`条目组合，以创建表现出不透明属性的区块。这主要用于启用[自定义玻璃区块](../blocks/custom-glass-blocks.md)的面剔除。

_在格式版本 1.19.40 及更高版本中，取消了实验性功能 `Holiday Creator Features`。_

#### 渲染方法

渲染方法基本上控制区块在世界中的外观，就像实体材质一样。以下是每种类型的关键属性：

| 渲染方法               | _透明度_   | _半透明性_ | _背面剔除_      | _远程剔除_       | 原版示例                          |
| ----------------------- | :--------: | :--------: | :--------------: | :---------------: | --------------------------------- |
| alpha_test              |     ✔️     |     ❌     |        ❌         |        ✔️         | 藤蔓、铁轨、树苗。                 |
| alpha_test_single_sided |     ✔️     |     ❌     |        ✔️         |        ✔️         | 门、活板门。                       |
| blend                   |     ✔️     |     ✔️     |        ✔️         |        ❌         | 玻璃、信标、蜂蜜块。               |
| double_sided            |     ❌     |     ❌     |        ❌         |        ❌         | 无 - 用于不透明的二维平原。         |
| opaque _(默认)_         |     ❌     |     ❌     |        ✔️         |        ❌         | 泥土、石头、混凝土。               |

-   **_透明度_** - 完全透视区域。
-   **_半透明性_** - 半透明区域。
-   **_背面剔除_** - 从后方查看时，面将变得不可见。
-   **_远程剔除_** - 区块在达到完全渲染距离之前变得不可见。

```json title="minecraft:block > components"
"minecraft:material_instances": {
  // '*' 实例必需 - 区块的默认实例（也用于破坏粒子效果）
  // 通配符遵循渲染控制器语法
  // 实例名称 'up'、'down'、'north'、'east'、'south' 和 'west' 是内置的
  "*": {
    "texture": "texture_name", // 在 `RP/textures/terrain_textures.json` 中定义的简短名称
    "render_method": "blend", // 上表中的渲染方法之一
    "face_dimming": true, // 默认为 true；应根据方向对具有此材质的面进行暗化吗？
    "ambient_occlusion": true // 默认为 true；应根据周围区块创建阴影吗？
  }
}
```

#### 自定义实例名称

:::tip
可以通过右键点击区块并打开其“材质实例”在 Blockbench 中定义模型的面上的自定义材质实例名称。
:::

可以在材质实例中定义自定义实例名称，并且可以通过内置实例名称或在区块模型中引用。

```json title="minecraft:block > components"
"minecraft:material_instances": {
  "*": {
    "texture": "texture_name",
    "render_method": "blend" // 必须与其他实例匹配
  },
  // 自定义实例名称
  "end": {
    "texture": "texture_name_end",
    "render_method": "blend" // 必须与其他实例匹配
  },
  "up": "end",
  "down": "end",
  // 在模型中定义的实例名称：
  "flower": {
    "texture": "texture_name_flower",
    "render_method": "blend" // 必须与其他实例匹配
  }
}
```

### 放置过滤器

设置规则，定义区块可以被放置或存续的条件。

_在格式版本 1.19.60 及更高版本中，取消了实验性功能 `Holiday Creator Features`。_

类型：对象

-   `conditions`: 数组 - 区块可以被放置/存续的条件列表。限制为 64 个条件。每个条件是一个 JSON 对象，必须至少包含以下参数之一（可以同时包含两者）：`allowed_faces` 或 `block_filter`，如下所示。
    -   `allowed_faces`: 数组 - 描述此区块可以放置在哪些面上的字符串列表：`up`、`down`、`north`、`south`、`east`、`west`、`side`、`all`。限制为 6 个面。
    -   `block_filter`: 数组 - 此区块可以在 `allowed_faces` 方向上放置的区块列表。限制为 64 个区块。此列表中的每个区块可以指定为字符串（区块名称）或 BlockDescriptor 对象。

#### 区块描述符

区块描述符是一个对象，允许你基于区块的标签，或基于其名称和状态来引用一个或多个区块。BlockDescriptor 的字段如下所述。

-   `name`: 字符串
    -   区块的名称。
-   `states`: 对象
    -   区块可以拥有的原版区块状态及其值的列表，以键/值对的形式表示。
-   `tags`: 字符串
    -   使用 Molang 查询的条件，结果为 true/false，可用于查询具有特定标签的区块。

```json title="minecraft:block > components"
    "minecraft:placement_filter": {
        "conditions": [
            {
                "allowed_faces": [
                    "up"
                ],
                "block_filter": [
                    "minecraft:dirt",
                    {
                        "name": "minecraft:sand",
                        "states": {
                            "sand_type": "red"
                        }
                    },
                    {
                        "tags": "!q.any_tag('stone', 'wiki_tag')"
                    }
                ]
            }
        ]
    }
```

参见 [此页面](../blocks/block-tags.md) 获取原版标签和相关区块的列表。

### 红石导电性

定义区块导电红石电力的能力。

_在格式版本 1.21.40 及更高版本中，取消了实验性功能 `Upcoming Creator Features`。_

类型：对象

-   `redstone_conductor`: 布尔值
    -   决定此区块是否导电直接红石电力。
-   `allows_wire_to_step_down`: 布尔值
    -   决定红石线是否可以沿此区块的侧面向下传导。

```json title="minecraft:block > components"
"minecraft:redstone_conductivity": {
    "redstone_conductor": true,
    "allows_wire_to_step_down": false
}
```

### 选择框

定义玩家光标选择此区块的区域。如果设置为 true，将使用默认值。如果设置为 false，玩家的光标将无法选择此区块。如果省略此组件，将使用默认值。

_在格式版本 1.19.60 及更高版本中，取消了实验性功能 `Holiday Creator Features`。_

类型：布尔值/对象

-   `origin`: 向量 [a, b, c]
    -   选择框边界的最小位置。`origin` 以 `[x, y, z]` 指定，范围必须在 `(-8, 0, -8)` 到 `(8, 16, 8)`（含）之间。
-   `size`: 向量 [a, b, c]
    -   选择框每个面的大小。大小以 `[x, y, z]` 指定。`origin` + `size` 必须在 `(-8, 0, -8)` 到 `(8, 16, 8)`（含）之间。

#### 使用布尔值的示例

```json title="minecraft:block > components"
"minecraft:selection_box": true
```

#### 使用对象的示例

```json title="minecraft:block > components"
"minecraft:selection_box": {
    "origin": [-8, 0, -8],
    "size": [16, 16, 16]
}
```

### 计时

使区块在指定的 `interval_range` 范围内的随机延迟后进行一次计时。

类型：对象

-   `interval_range`: 范围 [a, b]
    -   两个持续时间（以刻为单位），将作为随机性的最小和最大延迟。
-   `looping`: 布尔值
    -   决定此区块是否应持续计时，而不仅仅是计时一次。

_在格式版本 1.21.10 及更高版本中，取消了实验性功能 `Beta APIs`。_

```json title="minecraft:block > components"
"minecraft:tick": {
    "interval_range": [10, 20],
    "looping": true
}
```

### 转换

支持旋转、缩放和平移。此组件可以添加到整个区块和/或单个区块排列中。转换后的几何体仍然具有与未转换几何体相同的限制，例如最大尺寸为 30/16 单位。

**转换后的模型不得超过[区块几何体限制](#几何体)。**

:::tip
了解[可旋转区块](../blocks/rotatable-blocks.md)，根据区块的放置方式应用旋转，就像熔炉和生物头部一样！
:::

类型：对象

-   `rotation`: 向量 [a, b, c]
    -   几何体旋转的度数。[x, y, z]。必须为 90 的倍数。可以为负值。如果不是 90 的倍数，游戏将四舍五入到最近的 90 度倍数。
-   `rotation_pivot`: 向量 [a, b, c]
    -   旋转区块的枢轴点（以区块单位）。
-   `scale`: 向量 [a, b, c]
    -   几何体缩放的像素数。[x, y, z]
-   `scale_pivot`: 向量 [a, b, c]
    -   缩放区块的枢轴点（以区块单位）。
-   `translation`: 向量 [a, b, c]
    -   几何体平移的像素数。[x, y, z]

```json title="minecraft:block > components"
"minecraft:transformation": {
    "translation": [-5, 8, 0 ],
    "rotation": [90, 180, 0],
    "scale": [0.5, 1, 0.5],
    "rotation_pivot": [0, 0, 0],
    "scale_pivot": [0, 0, 0]
}
```

---