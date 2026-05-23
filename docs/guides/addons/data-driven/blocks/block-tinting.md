# 方块着色

方块着色允许为方块纹理叠加颜色，可以是固定颜色，也可以是随生物群系变化的动态颜色，还可以控制在地图上显示的颜色。

## 静态颜色

### tint_color（纹理着色）

在材质实例中使用 `tint_color` 可以将纹理乘以一个固定颜色：

```json title="BP/blocks/my_block.json > components"
"minecraft:material_instances": {
    "*": {
        "texture": "wiki:my_block",
        "tint_method": "none",
        "tint_color": "#72a931"
    }
}
```

`tint_color` 接受十六进制颜色字符串，颜色会乘以纹理像素颜色，黑色（`#000000`）使纹理全黑，白色（`#ffffff`）不改变纹理。

### overlay_color（覆盖色）

`minecraft:material_instances` 中的 `overlay_color` 与 `tint_color` 类似，但它覆盖在纹理上层而非与纹理混合：

```json title="BP/blocks/my_block.json > components"
"minecraft:material_instances": {
    "*": {
        "texture": "wiki:my_block",
        "overlay_color": "#ff000080"
    }
}
```

## 生物群系动态着色

`tint_method` 指定根据方块所在生物群系来动态调整颜色的方法：

```json title="材质实例"
"minecraft:material_instances": {
    "*": {
        "texture": "wiki:my_grass",
        "tint_method": "grass"
    }
}
```

可用的 `tint_method` 值：

| 值 | 效果 |
|----|------|
| `"none"` | 不应用动态着色（默认） |
| `"grass"` | 使用草地颜色（随生物群系变化） |
| `"foliage"` | 使用树叶颜色（随生物群系变化） |
| `"birch"` | 使用白桦叶颜色（固定偏黄绿色） |
| `"spruce"` | 使用云杉叶颜色（固定偏蓝绿色） |
| `"default"` | 使用默认着色（偏灰绿色） |
| `"water"` | 使用水颜色（随生物群系变化） |
| `"redstone_signal_0"` ～ `"redstone_signal_15"` | 使用对应红石信号强度的颜色 |

`tint_method` 会和 `tint_color` 相乘。如果你要用纯粹的生物群系颜色，将纹理设计为白色，则着色后会直接呈现生物群系颜色。

## 破坏粒子着色

`minecraft:destruction_particles` 组件也支持 `tint_method`，让破坏时产生的粒子颜色随生物群系变化：

```json title="components"
"minecraft:destruction_particles": {
    "texture": "wiki:my_grass",
    "tint_method": "grass"
}
```

## 地图颜色

`minecraft:map_color` 组件控制方块在地图上显示的颜色：

```json title="components"
"minecraft:map_color": "#5f9d24"
```

也可以使用RGB数组格式：

```json title="components"
"minecraft:map_color": [95, 157, 36]
```

如果省略 `minecraft:map_color`，方块在地图上会显示为透明（地图上看不到）。
