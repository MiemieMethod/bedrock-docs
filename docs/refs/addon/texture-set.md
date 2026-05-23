# 纹理集

本页列出国际版资源包中`*.texture_set.json`文件的结构和约束。纹理集用于为同一纹理资源声明PBR相关层数据，供Vibrant Visuals与光线追踪相关渲染路径读取。本页不包含中国版私有接口。

## 文件位置

| 项目 | 说明 |
| --- | --- |
| 目录 | 资源包`textures/`目录及其子目录。 |
| 命名 | 与目标纹理同名并以`.texture_set.json`结尾。 |
| 引用规则 | 纹理层引用的图像必须位于同一个资源包中。 |

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本字符串 | 未设置 | 纹理集文件使用的格式版本。Microsoft Learn在当前批次中给出的纹理集架构版本为`1.21.30`。 |
| `minecraft:texture_set` | 对象 | 未设置 | 纹理集层定义对象。 |

## `minecraft:texture_set`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `color` | 字符串、四通道数组或十六进制颜色字符串 | 未设置 | 颜色层。可引用纹理，也可直接给统一值。该层为必选。 |
| `normal` | 字符串 | 未设置 | 法线层。引用法线纹理。 |
| `heightmap` | 字符串或单通道数值 | 未设置 | 高度图层。可引用高度图纹理，或使用单通道统一值。 |
| `metalness_emissive_roughness` | 字符串、三通道数组或十六进制颜色字符串 | 未设置 | MER层。可引用纹理，也可直接给统一值。 |
| `metalness_emissive_roughness_subsurface` | 字符串、四通道数组或十六进制颜色字符串 | 未设置 | MERS层。可引用纹理，也可直接给统一值。 |

## 层通道语义

| 层 | 通道语义 |
| --- | --- |
| `color` | RGB表示基色，Alpha表示不透明度。若来源为三通道图像，Alpha视为`1.0`。 |
| `normal` | RGB表示法线方向，若为四通道图像则Alpha通道被忽略。 |
| `heightmap` | 单通道高度值。 |
| `metalness_emissive_roughness` | Red为金属度，Green为自发光，Blue为粗糙度。若为四通道图像则Alpha通道被忽略。 |
| `metalness_emissive_roughness_subsurface` | Red为金属度，Green为自发光，Blue为粗糙度，Alpha为次表面散射。 |

## 统一值格式

纹理集层不引用图像时，可直接在JSON中写统一值。

| 格式 | 说明 |
| --- | --- |
| 数值或数值数组 | 使用`0`到`255`范围整数。多通道层使用对应长度数组。 |
| 十六进制字符串 | 三通道或四通道层可使用RGB或ARGB形式；单通道层可使用两位十六进制。 |

## 约束

- 必须定义`color`层。
- 同一个纹理集中不能同时定义`normal`和`heightmap`。
- 高度图层不能用于物品等基于纹理的对象，相关场景应使用法线层。
- 同一个纹理集中不能同时定义`metalness_emissive_roughness`和`metalness_emissive_roughness_subsurface`。
- `metalness_emissive_roughness_subsurface`仅由Vibrant Visuals使用。光线追踪相关渲染路径会忽略其中的次表面散射值。
- 在MERS中，金属度与次表面散射互斥。每个像素取两者较大值对应的性质；若两者相等，优先次表面散射。
- Microsoft Learn指出，纹理变体场景下MERS统一值不受支持，应提供图像形式的MERS层。

## 无效判定

纹理集无效时，内容日志会记录`CONTENT_ERROR`，并忽略该纹理集。常见无效原因如下：

- JSON无法解析，或不符合纹理集架构。
- 缺少`color`层。
- 同时定义`normal`与`heightmap`。
- 在纹理对象场景中使用`heightmap`。
- 同时定义MER与MERS层。
- 引用纹理不存在于同一资源包，或引用纹理本身无法解析。
- 层通道数量不符合要求：
    - 图像引用时：`color`、MER、`normal`要求三通道或四通道；MERS要求四通道；`heightmap`要求单通道。
    - 统一值时：`color`要求四通道；MER要求三通道；MERS要求四通道。

## 资源栈行为

- 纹理集仅能引用同一资源包中的图像。
- 高优先级资源包中的同名纹理图像，不会替换低优先级资源包纹理集对本包图像的引用。
- 不同资源包中的同名纹理集定义不会合并，而是由高优先级资源包整体覆盖低优先级定义。

## 同名扩展名优先级

当同一路径下存在同名不同扩展名图像时，解析优先级为`.tga`>` .png`>` .jpg`>` .jpeg`。

## 示例

```json title="使用MERS层的纹理集示例"
{
  "format_version": "1.21.30",
  "minecraft:texture_set": {
    "color": "cactus_side",
    "metalness_emissive_roughness_subsurface": "cactus_side_mers",
    "normal": "cactus_side_normal"
  }
}
```
