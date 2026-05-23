# 体素形状文档

本页列出行为包体素形状文档的结构。体素形状文档主要用于`minecraft:geometry.culling_shape`，用于方块相邻面剔除判定。

## 适用范围

- 体素形状文档用于描述剔除边界，不直接替代`minecraft:collision_box`或`minecraft:selection_box`。
- `minecraft:geometry.culling_shape`需要与`minecraft:geometry.culling`配合使用。
- Microsoft Learn当前说明：`minecraft:geometry.culling_shape`需在“VoxelShape”实验开关开启时使用；当使用`minecraft:`命名空间时，目前只列出`minecraft:empty`和`minecraft:unit_cube`两个可用标识符。
- 使用`minecraft:geometry.full_block`时，游戏会固定采用单位立方体剔除形状，并忽略自定义体素形状。

## 根结构

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本字符串 | 未设置 | 体素形状文档格式版本。Microsoft Learn当前示例为`1.21.110`。 |
| `minecraft:voxel_shape` | 对象 | 未设置 | 体素形状定义容器，包含`description`与`shape`。 |

## `minecraft:voxel_shape`

**JSON路径：**`minecraft:voxel_shape`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 体素形状描述对象。 |
| `shape` | 对象 | 未设置 | 体素形状几何对象。 |

## `description`

**JSON路径：**`minecraft:voxel_shape > description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 标识符 | 未设置 | 体素形状标识符。用于被`minecraft:geometry.culling_shape`引用。 |

## `shape`

**JSON路径：**`minecraft:voxel_shape > shape`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `boxes` | 数组 | 未设置 | 边界框列表。每项为一个`box`对象。 |

## `box`

**JSON路径：**`minecraft:voxel_shape > shape > boxes`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min` | 数组或对象 | 未设置 | 边界框最小坐标。 |
| `max` | 数组或对象 | 未设置 | 边界框最大坐标。 |

### `min`与`max`对象形态

**JSON路径：**`minecraft:voxel_shape > shape > boxes > min/max`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `x` | 十进制数 | `0` | X轴坐标。 |
| `y` | 十进制数 | `0` | Y轴坐标。 |
| `z` | 十进制数 | `0` | Z轴坐标。 |

## 示例

```json title="体素形状文档示例"
{
  "format_version": "1.21.110",
  "minecraft:voxel_shape": {
    "description": {
      "identifier": "example:thin_pillar_shape"
    },
    "shape": {
      "boxes": [
        {
          "min": {
            "x": 7.0,
            "y": 0.0,
            "z": 7.0
          },
          "max": {
            "x": 9.0,
            "y": 16.0,
            "z": 9.0
          }
        }
      ]
    }
  }
}
```

/// note | 相关页面
- [方块定义](block.md)
- [方块组件](block-component.md)
///
