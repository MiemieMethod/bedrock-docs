# 方块视觉效果

自定义方块的外观由纹理、几何体、材质实例三个要素共同决定。本文逐一介绍这三者，以及影响外观的着色选项。

## 纹理

基岩版将所有方块纹理打包合并成一张**地形图集**（`atlas.terrain`），而非在运行时按需加载独立文件。每个资源包中的纹理会在启动时合并进这张图集。

要注册一张纹理，编辑资源包中的 `textures/terrain_texture.json`：

```json title="RP/textures/terrain_texture.json"
{
    "texture_data": {
        "wiki:my_block": {
            "textures": "textures/wiki/blocks/my_block"
        },
        "wiki:my_block_top": {
            "textures": "textures/wiki/blocks/my_block_top"
        }
    }
}
```

`"wiki:my_block"` 就是**纹理短名**，在 `minecraft:material_instances` 中就用这个短名引用纹理。路径省略扩展名，图片放在 `textures/wiki/blocks/my_block.png`。

关于纹理文件的几点限制：

- 标准尺寸是16×16像素；更小的纹理会被拉伸到至少16×16。
- 纹理的高度不能大于宽度，否则会被当作翻书动画的帧序列处理。
- 纹理尺寸无需是2的幂次方。

/// tip | 动态纹理
若要制作动态纹理，请查阅[翻书纹理](flipbook-textures.md)教程；若要一个纹理有多种随机变体，请查阅[纹理变体](texture-variation.md)教程。
///

## 材质实例

`minecraft:material_instances` 组件将纹理和渲染设置绑定到几何体的面上。

```json title="BP/blocks/my_log.json > components"
"minecraft:material_instances": {
    "*": {
        "texture": "wiki:my_log_side",
        "render_method": "opaque"
    },
    "end": {
        "texture": "wiki:my_log_end",
        "render_method": "opaque"
    },
    "up": "end",
    "down": "end"
}
```

面目标的匹配优先级（从高到低）：

1. 几何体文件中为UV单独指定的 `material_instance` 名称。
2. 与面方向名称相同的实例（`down`、`up`、`north`、`south`、`east`、`west`）。
3. 通配符实例 `*`。

`"up": "end"` 这种字符串写法是对已有命名实例的**引用**，与 `end` 实例共享相同配置。

### 渲染方法

渲染方法决定了方块使用的底层着色器。**同一个方块的所有材质实例必须使用相同的渲染方法。**

| 渲染方法 | 透明像素 | 半透明像素 | 背面可见 | 远处可见 |
|---------|:-------:|:---------:|:-------:|:-------:|
| `opaque` | ✗ | ✗ | ✗ | ✓ |
| `double_sided` | ✗ | ✗ | ✓ | ✓ |
| `blend` | ✓ | ✓ | ✗ | ✗ |
| `alpha_test` | ✓ | ✗ | ✗ | ✓ |
| `alpha_test_single_sided` | ✓ | ✗ | ✓ | ✓ |

- 大多数固体方块用 `opaque`。
- 玻璃、水晶等半透明效果用 `blend`。
- 树叶、花草、链条等有镂空透明的用 `alpha_test`。

### 着色选项

```json
"minecraft:material_instances": {
    "*": {
        "texture": "wiki:my_block",
        "ambient_occlusion": 1.0,
        "face_dimming": true
    }
}
```

- `ambient_occlusion`：控制方块旁接触阴影的强度，范围0.0～10.0。发光方块默认为0.0，其他方块默认为1.0。
- `face_dimming`：是否对方块面进行方向性暗化（朝下的面更暗）。发光方块默认关闭，其他方块默认开启。

## 几何体

### 原版内置几何体

游戏内置了若干以 `minecraft:` 为命名空间的几何体，可直接用于自定义方块：

```json title="BP/blocks/my_block.json > components"
"minecraft:geometry": "minecraft:geometry.full_block"
```

常用原版几何体：

| 标识符 | 描述 |
|--------|------|
| `minecraft:geometry.full_block` | 标准完整立方体 |
| `minecraft:geometry.cross` | 十字形（适合植物、花卉） |
| `minecraft:geometry.carpet` | 地毯形（1像素厚） |

/// warning | 限制
原版几何体是硬编码的，**不支持** `bone_visibility` 和 `culling` 参数，也无法在JSON文件中找到或修改其内容。
///

### 自定义几何体

自定义几何体用Blockbench制作，导出为Bedrock方块格式（`.geo.json`），放入资源包的 `models/blocks/` 目录。详见[Blockbench建模](../../tools/blockbench/how-to-use.md)教程。

```json title="BP/blocks/my_block.json > components"
"minecraft:geometry": {
    "identifier": "geometry.my_block"
}
```

标识符对应 `.geo.json` 文件中 `description.identifier` 的值。

### 骨骼条件显示

使用对象格式的几何体组件时，可以通过 `bone_visibility` 根据方块状态条件显示或隐藏模型中的特定骨骼：

```json title="BP/blocks/my_jar.json > components"
"minecraft:geometry": {
    "identifier": "geometry.my_jar",
    "bone_visibility": {
        "lid": "q.block_state('wiki:has_lid')",
        "empty_label": "!q.block_state('wiki:has_lid')"
    }
}
```

`bone_visibility` 中的值是Molang表达式，结果为真时骨骼显示，为假时隐藏。

### 剔除规则

剔除规则允许根据相邻方块隐藏几何体的特定部分，可以提升性能表现。详见[方块剔除](block-culling.md)教程。

## 着色综述

默认情况下：

- **不发光**的方块同时开启接触阴影和面方向暗化。
- **发光**的方块（`minecraft:light_emission` > 0）不应用任何着色。
- 发光方块作为手持物品时，外观也会呈现自发光效果。

此外，部分其他组件也会影响方块外观：

- `minecraft:random_offset`：为方块模型添加随机偏移，常用于植物。
- `minecraft:transformation`：对方块模型进行旋转、缩放和平移变换。
