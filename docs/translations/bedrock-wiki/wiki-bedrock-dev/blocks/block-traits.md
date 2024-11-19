---
title: 方块特性
description: 方块特性可以轻松地将原版方块状态（例如方向）应用于你的自定义方块，无需事件和触发器。
category: 一般
nav_order: 5
mentions:
    - QuazChick
    - SmokeyStack
---

/// tip | 格式与最低引擎版本 `1.21.40`
在学习方块特性之前，你应该对[方块状态](../blocks/block-states.md)有信心。

在处理方块状态时，请确保你的包清单中的 `min_engine_version` 为 `1.20.20` 或更高。
///

## 应用特性

方块特性可以轻松地将原版方块状态（例如方向）应用于你的自定义方块，无需事件和触发器。

```json title="BP/blocks/custom_slab.json"
{
  "format_version": "1.21.40",
  "minecraft:block": {
    "description": {
      "identifier": "wiki:custom_slab",
      "menu_category": {
        "category": "construction",
        "group": "itemGroup.name.slab"
      },
      "traits": {
        "minecraft:placement_position": {
          "enabled_states": ["minecraft:vertical_half"]
        }
      }
    },
    "components": { ... },
    "permutations": [ ... ]
  }
}
```

_此示例将在放置时将 `minecraft:vertical_half` 方块状态设置为 `'top'` 或 `'bottom'` - 具体取决于玩家的视角。_

**要使此状态产生功能性差异，仍然需要使用条件查询的排列**

```c
q.block_state('minecraft:vertical_half')
```

## 特性列表

### 放置方向

包含有关玩家放置方块时旋转的信息。

_已从实验 `即将推出的创作者功能` 发布，适用于格式版本 1.20.20 及更高版本。_

#### 提供的状态

| 状态                          | 值                                                                                  | 描述                                          |
| ----------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------- |
| `minecraft:cardinal_direction` | `"south"` _(默认)_<br>`"north"`<br>`"west"`<br>`"east"`                          | 玩家放置时的基本朝向。                       |
| `minecraft:facing_direction`   | `"down"` _(默认)_<br>`"up"`<br>`"south"`<br>`"north"`<br>`"west"`<br>`"east"`  | 玩家放置时的整体方向。                       |

#### 附加参数

-   `y_rotation_offset` - 此旋转偏移仅适用于水平状态值（北、南、东、西）。只能指定轴对齐的角度（例如 90、180、-90）。

```json title="minecraft:block > description > traits"
"minecraft:placement_direction": {
  "enabled_states": ["minecraft:cardinal_direction"],
  "y_rotation_offset": 180
}
```

### 放置位置

包含有关玩家放置方块位置的信息。

_已从实验 `即将推出的创作者功能` 发布，适用于格式版本 1.20.20 及更高版本。_

#### 提供的状态

| 状态                     | 值                                                                                  | 描述                                         |
| ------------------------ | ----------------------------------------------------------------------------------- | -------------------------------------------- |
| `minecraft:block_face`    | `"down"` _(默认)_<br>`"up"`<br>`"south"`<br>`"north"`<br>`"west"`<br>`"east"`   | 方块被放置的面。                             |
| `minecraft:vertical_half` | `"top"`<br>`"bottom"` _(默认)_                                                    | 方块被放置的垂直半部分。                     |

```json title="minecraft:block > description > traits"
"minecraft:placement_position": {
  "enabled_states": [
    "minecraft:block_face",
    "minecraft:vertical_half"
  ]
}
```