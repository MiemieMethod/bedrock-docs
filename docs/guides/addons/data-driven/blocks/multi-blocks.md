# 多方块结构 <!-- md:flag experimental -->

/// warning | 实验性功能
多方块萃取目前仍处于实验性阶段，需要在世界设置中启用"即将推出的创作者功能"实验性开关，且方块定义的 `format_version` 不低于 `1.26.20`。
///

多方块结构允许一个方块定义横跨多个方块位置，例如原版的门（2格高）、向日葵（2格高）或大型装置。

## 基本概念

多方块结构由一个**主方块**（part_index 0）和若干**附属方块**（part_index 1、2……）组成。主方块定义整个结构的逻辑，附属方块只是占位方块，在主方块被破坏时会自动移除。

## 配置多方块萃取

使用 `minecraft:multi_block` 萃取，并声明结构中每个方块部分的相对坐标和索引：

```json title="BP/blocks/tall_block.json"
{
    "format_version": "1.26.20",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:tall_block",
            "traits": {
                "minecraft:multi_block": {
                    "blocks": [
                        { "position": [0, 0, 0], "part_index": 0 },
                        { "position": [0, 1, 0], "part_index": 1 }
                    ]
                }
            },
            "states": {
                "wiki:part": [0, 1]
            }
        },
        "components": {
            "minecraft:movable": {
                "movement_type": "immovable"
            },
            "minecraft:geometry": "geometry.tall_block_bottom",
            "minecraft:material_instances": {
                "*": { "texture": "wiki:tall_block" }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('wiki:part') == 1",
                "components": {
                    "minecraft:geometry": "geometry.tall_block_top"
                }
            }
        ]
    }
}
```

/// warning | 必须包含 minecraft:movable
多方块萃取的方块**必须**包含 `minecraft:movable` 组件，且 `movement_type` 必须设置为 `"immovable"` 或 `"popped"`。省略此组件会导致方块注册失败。
///

## 状态约束

多方块结构中，除 `part_index` 状态（通常是 `wiki:part`）外，所有方块部分必须拥有**相等**的状态值。这意味着如果主方块朝北，所有附属方块也必须朝北。

## 选取和破坏行为

- 点击选取任何部分都会高亮整个结构的主方块轮廓。
- 破坏任何一个部分都会移除整个结构（但战利品只由主方块定义决定）。

## 脚本API支持 <!-- md:flag vanilla -->

脚本中可以通过 `getParts()` 方法获取多方块的所有部分：

```js
const block = dimension.getBlock(location);
const multiBlock = block.getComponent("minecraft:multi_block");
if (multiBlock) {
    const parts = multiBlock.getParts();
    for (const part of parts) {
        console.log(`Part at ${JSON.stringify(part.location)}`);
    }
}
```

## 含水支持（1.26.30+）

从 `format_version: "1.26.30"` 起（同样需要实验性开关），多方块支持含水（waterlogging）行为——在水中放置时多方块结构各部分可以显示水。

```json title="description > traits"
"minecraft:multi_block": {
    "blocks": [
        { "position": [0, 0, 0], "part_index": 0 },
        { "position": [0, 1, 0], "part_index": 1 }
    ],
    "waterlogging": true
}
```