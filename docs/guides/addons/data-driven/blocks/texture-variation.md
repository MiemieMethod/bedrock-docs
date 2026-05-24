# 纹理变体

纹理变体允许同一种方块在世界中随机呈现不同的外观，就像原版的石头、草方块一样各有细微差别。

## 基础变体配置

在 `terrain_texture.json` 中，为一个纹理短名提供多个纹理路径的数组：

```json title="RP/textures/terrain_texture.json"
{
    "texture_data": {
        "wiki:my_block": {
            "textures": [
                {
                    "path": "textures/wiki/blocks/my_block_0",
                    "weight": 4
                },
                {
                    "path": "textures/wiki/blocks/my_block_1",
                    "weight": 2
                },
                {
                    "path": "textures/wiki/blocks/my_block_2",
                    "weight": 1
                }
            ]
        }
    }
}
```

- `path`：纹理文件路径（不带扩展名）。
- `weight`：相对权重，权重越高出现概率越大。省略时默认为1。

然后在材质实例中正常引用短名：

```json title="BP/blocks/my_block.json > components"
"minecraft:material_instances": {
    "*": {
        "texture": "wiki:my_block",
        "render_method": "opaque"
    }
}
```

变体的选取基于方块在世界中的坐标，相同位置始终显示相同的变体，不会每次加载都随机改变。

## 在material_instances中使用变体（1.21.110+）

从格式版本 `1.21.110` 起，可以在材质实例组件中直接通过 `variations` 字段设置变体，而无需修改 `terrain_texture.json`：

```json title="BP/blocks/my_block.json > components"
"minecraft:material_instances": {
    "*": {
        "texture": "wiki:my_block",
        "render_method": "opaque",
        "variations": [
            { "weight": 4, "texture": "wiki:my_block_0" },
            { "weight": 2, "texture": "wiki:my_block_1" },
            { "weight": 1, "texture": "wiki:my_block_2" }
        ]
    }
}
```

这种写法不需要在 `terrain_texture.json` 中注册变体纹理组，更加集中。

## 搭配翻书纹理

翻书纹理同样支持 `atlas_tile_variant` 参数，用于在变体图集中选择特定变体的动画帧：

```json title="RP/textures/flipbook_textures.json"
{
    "flipbook_texture": "textures/wiki/blocks/my_animated_block",
    "atlas_tile": "wiki:my_animated_block",
    "atlas_tile_variant": 2,
    "ticks_per_frame": 3
}
```

这样可以为同一纹理短名的不同变体定义独立的动画配置。