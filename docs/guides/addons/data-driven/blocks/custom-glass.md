# 自定义玻璃方块

这一页演示如何创建一个类似原版玻璃的透明方块——使用 `blend` 渲染方法，并在相邻同类方块时隐藏接触面。

## 所需文件

/// html | div.treeview
- `demo_BP`
    - `blocks`
        - `custom_glass.json`
- `demo_RP`
    - `block_culling`
        - `custom_glass.json`
    - `models`
        - `blocks`
            - `custom_glass.geo.json`
    - `textures`
        - `blocks`
            - `custom_glass.png`
        - `terrain_texture.json`
///

## 方块模型

使用Blockbench创建一个填满整个方块空间（16×16×16像素）的完整立方体模型，命名骨骼为 `glass`。关键：骨骼名 `glass` 需要与后面的剔除规则一致。

## 剔除规则

相邻同类玻璃时隐藏接触面：

```json title="RP/block_culling/custom_glass.json"
{
    "format_version": "1.21.80",
    "minecraft:block_culling_rules": {
        "description": {
            "identifier": "wiki:culling.custom_glass"
        },
        "rules": [
            { "geometry_part": { "bone": "glass", "face": "north" }, "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }] },
            { "geometry_part": { "bone": "glass", "face": "south" }, "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }] },
            { "geometry_part": { "bone": "glass", "face": "east" }, "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }] },
            { "geometry_part": { "bone": "glass", "face": "west" }, "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }] },
            { "geometry_part": { "bone": "glass", "face": "up" }, "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }] },
            { "geometry_part": { "bone": "glass", "face": "down" }, "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }] }
        ]
    }
}
```

## 方块定义

```json title="BP/blocks/custom_glass.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_glass",
            "menu_category": {
                "category": "construction"
            }
        },
        "components": {
            "minecraft:destructible_by_mining": { "seconds_to_destroy": 0.45 },
            "minecraft:destructible_by_explosion": { "explosion_resistance": 1.5 },
            "minecraft:map_color": "#b3efef",
            "minecraft:light_dampening": 0,
            "minecraft:geometry": {
                "identifier": "geometry.custom_glass",
                "culling": "wiki:culling.custom_glass"
            },
            "minecraft:material_instances": {
                "*": {
                    "texture": "wiki:custom_glass",
                    "render_method": "blend",
                    "face_dimming": false,
                    "ambient_occlusion": false
                }
            }
        }
    }
}
```

要点：
- `render_method: "blend"` 启用半透明渲染。
- `face_dimming: false` 和 `ambient_occlusion: false` 禁用玻璃上不需要的阴影效果。
- `light_dampening: 0` 让光线完全穿透。

## 纹理注册

```json title="RP/textures/terrain_texture.json（相关部分）"
{
    "texture_data": {
        "wiki:custom_glass": {
            "textures": "textures/blocks/custom_glass"
        }
    }
}
```

## 本地化

```lang title="RP/texts/en_US.lang"
tile.wiki:custom_glass.name=Custom Glass
```

中文本地化：

```lang title="RP/texts/zh_CN.lang"
tile.wiki:custom_glass.name=自定义玻璃
```