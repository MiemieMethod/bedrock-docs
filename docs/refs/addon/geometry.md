# 几何体定义

本页列出国际版资源包几何体定义文件的主要结构。几何体定义文件通常位于`models/entity/`目录，也可用于方块物品显示等场景。内容基于VisualReference中的`minecraft:geometry`系列版本，不包含中国版私有接口。

## 版本形态

| 版本 | 根结构 | 主要差异 |
| --- | --- | --- |
| `1.8.0` | `geometry.<名称>` | 旧版根结构；支持骨骼级`inflate`和`reset`，现已弃用。 |
| `1.12.0`、`1.14.0` | `minecraft:geometry`数组 | 切换为统一数组结构，支持立方体逐面UV。 |
| `1.16.0`、`1.19.30` | `minecraft:geometry`数组 | 新增骨骼`binding`字段。 |
| `1.21.0` | `minecraft:geometry`数组 | 新增`item_display_transforms`与面级`uv_rotation`。 |

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 几何体文件格式版本。 |
| `minecraft:geometry` | 数组 | 未设置 | 几何体对象列表。 |

## 几何体对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 几何体元数据。 |
| `bones` | 数组 | 未设置 | 骨骼定义列表。 |
| `cape` | 字符串 | 未设置 | 披风相关字段。 |
| `item_display_transforms` | 对象 | 未设置 | 物品显示变换，仅`1.21.0+`。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 标识符 | 未设置 | 几何体标识符，供客户端实体、附着物或方块组件引用。 |
| `texture_width` | 整数 | 未设置 | 纹理宽度。 |
| `texture_height` | 整数 | 未设置 | 纹理高度。 |
| `visible_bounds_offset` | 三元素数组 | 未设置 | 可见边界偏移。 |

## 骨骼对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `name` | 字符串 | 未设置 | 骨骼名称。 |
| `parent` | 字符串 | 未设置 | 父骨骼名称。 |
| `pivot` | 三元素数组 | 未设置 | 轴心点。 |
| `rotation` | 三元素数组 | 未设置 | 旋转。 |
| `mirror` | 布尔值 | 未设置 | 是否镜像UV。 |
| `binding` | Molang表达式 | 未设置 | 骨骼绑定表达式，仅`1.16.0+`。 |
| `cubes` | 数组 | 未设置 | 立方体列表。 |
| `locators` | 对象 | 未设置 | 定位器映射。 |
| `texture_meshes` | 数组 | 未设置 | 纹理网格定义。 |
| `poly_mesh` | 对象 | 未设置 | 网格定义，官方标注为弃用。 |

### `locators`

`locators`可写为定位器名到向量数组的映射，或定位器对象。定位器对象常见字段如下：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `offset` | 三元素数组 | 未设置 | 定位器偏移。 |
| `rotation` | 三元素数组 | 未设置 | 定位器旋转。 |
| `ignore_inherited_scale` | 布尔值 | 未设置 | 是否忽略父级缩放。 |

## 立方体对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `origin` | 三元素数组 | 未设置 | 立方体原点。 |
| `size` | 三元素数组 | 未设置 | 立方体尺寸。 |
| `pivot` | 三元素数组 | 未设置 | 立方体轴心点。 |
| `rotation` | 三元素数组 | 未设置 | 立方体旋转。 |
| `mirror` | 布尔值 | 未设置 | 覆盖骨骼镜像设置。 |
| `uv` | 二元素数组或对象 | 未设置 | UV定义。对象形态可按六个面分别定义。 |

### 逐面UV对象

面对象键通常为`north`、`south`、`east`、`west`、`up`、`down`，每个面可包含：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `uv` | 二元素数组 | 未设置 | UV起点。 |
| `uv_size` | 二元素数组 | 未设置 | UV尺寸。 |
| `material_instance` | 字符串 | 未设置 | 面材质实例名。 |
| `uv_rotation` | 整数 | `0` | UV旋转角度，仅`1.21.0+`，取值为`0`、`90`、`180`、`270`。 |

## `item_display_transforms`

`item_display_transforms`用于控制几何体在不同物品渲染场景的变换。支持场景键如下：

- `gui`
- `firstperson_righthand`
- `firstperson_lefthand`
- `thirdperson_righthand`
- `thirdperson_lefthand`
- `ground`
- `fixed`
- `head`
- `embedded`

每个场景对象可包含以下字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `translation` | 三元素数组 | 未设置 | 平移。 |
| `rotation` | 三元素数组 | 未设置 | 旋转。 |
| `scale` | 三元素数组 | 未设置 | 缩放。 |
| `rotation_pivot` | 三元素数组 | 未设置 | 旋转轴心点。 |
| `scale_pivot` | 三元素数组 | 未设置 | 缩放轴心点。 |
| `fit_to_frame` | 布尔值 | `true` | 仅`gui`场景可用。 |

## 弃用与兼容性说明

- 骨骼级`inflate`与`reset`仅见于旧版结构，不建议在新内容中使用。
- `poly_mesh`在官方自动导出参考中标注为弃用，新内容建议避免使用。
- 多版本字段可被旧版兼容解析与否，需以目标版本内容日志为准。

## 相关参考

- [方块定义](block.md)
- [方块组件](block-component.md)
- [客户端实体定义](client-entity.md)