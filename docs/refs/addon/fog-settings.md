# 迷雾定义

本页列出资源包`fogs/`目录中迷雾定义文件的主要字段。迷雾定义的根对象包含`format_version`和`minecraft:fog_settings`。`minecraft:fog_settings`用于定义距离迷雾、体积迷雾和标识信息。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 迷雾定义文件使用的格式版本。官方教程中记载的最低版本为`1.16.100`。 |
| `minecraft:fog_settings` | 对象 | 未设置 | 迷雾设置对象。 |

## `minecraft:fog_settings`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 迷雾定义的描述信息。 |
| `distance` | 对象 | 未设置 | 不同摄像机位置或天气状态的距离迷雾设置。 |
| `volumetric` | 对象 | 未设置 | 体积迷雾设置。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 迷雾定义的赋命名空间标识符，必须包含命名空间。 |

## `distance`

`distance`对象按摄像机环境或天气状态组织距离迷雾。未设置的字段会由迷雾栈中的较低优先级迷雾或引擎默认值补足。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `air` | 对象 | 未设置 | 摄像机位于空气中时的迷雾。 |
| `weather` | 对象 | 未设置 | 摄像机位于空气中且存在雨、雪等天气时的迷雾。 |
| `water` | 对象 | 未设置 | 摄像机位于水中时的迷雾。 |
| `lava` | 对象 | 未设置 | 摄像机位于岩浆中时的迷雾。 |
| `lava_resistance` | 对象 | 未设置 | 摄像机位于岩浆中且玩家具有抗火状态效果时的迷雾。 |
| `powder_snow` | 对象 | 未设置 | 摄像机位于粉雪方块中时的迷雾。 |

### 距离迷雾项

`air`、`weather`、`water`、`lava`、`lava_resistance`和`powder_snow`使用相同的基本结构。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `fog_start` | 数值 | 未设置 | 迷雾开始出现的距离。 |
| `fog_end` | 数值 | 未设置 | 迷雾完全不透明的距离。 |
| `fog_color` | 字符串 | 未设置 | 迷雾颜色，通常使用十六进制颜色字符串。 |
| `render_distance_type` | 字符串 | 未设置 | 决定距离值的解释方式。可为`fixed`或`render`。`fixed`按方块距离计算，`render`按当前渲染距离比例计算。 |
| `transition_fog` | 对象 | 未设置 | 额外的过渡迷雾数据。官方教程说明该对象只适用于`water`设置。 |

### `transition_fog`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `init_fog` | 对象 | 未设置 | 玩家进入水中时用于开始过渡的初始迷雾。 |
| `min_percent` | 数值 | 未设置 | 迷雾过渡的最小进度。 |
| `mid_seconds` | 数值 | 未设置 | 到达`mid_percent`所需的秒数。 |
| `mid_percent` | 数值 | 未设置 | 经过`mid_seconds`后的过渡进度。 |
| `max_seconds` | 数值 | 未设置 | 完成整个过渡所需的总秒数。 |

`init_fog`使用与距离迷雾项相同的`fog_start`、`fog_end`、`fog_color`和`render_distance_type`字段。

## `volumetric`

`volumetric`对象定义体积迷雾。官方参考将其分为`density`和`media_coefficients`两组。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `density` | 对象 | 未设置 | 不同摄像机位置或天气状态的体积迷雾密度。 |
| `media_coefficients` | 对象 | 未设置 | 光线穿过不同介质时的体积迷雾系数。 |

### `density`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `air` | 对象 | 未设置 | 光线穿过空气方块时的迷雾密度。 |
| `weather` | 对象 | 未设置 | 空气中存在雨、雪等天气时的迷雾密度。 |
| `water` | 对象 | 未设置 | 光线穿过水方块时的迷雾密度。 |
| `lava` | 对象 | 未设置 | 光线穿过岩浆方块时的迷雾密度。 |
| `lava_resistance` | 对象 | 未设置 | 玩家具有抗火状态效果且光线穿过岩浆方块时的迷雾密度。 |

### 密度项

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `max_density` | 数值 | 未设置 | 迷雾扰乱光线的最大强度。`0.0`表示无迷雾，`1.0`接近不透明。 |
| `uniform` | 布尔值 | 未设置 | 是否在所有高度均匀应用密度。 |
| `zero_density_height` | 数值 | 未设置 | 迷雾开始出现的高度。仅在`uniform`不为`true`时使用。 |
| `max_density_height` | 数值 | 未设置 | 达到`max_density`的高度。仅在`uniform`不为`true`时使用。 |

### `media_coefficients`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `air` | 对象 | 未设置 | 光线穿过空气时的体积迷雾系数。 |
| `water` | 对象 | 未设置 | 光线穿过水时的体积迷雾系数。 |
| `cloud` | 对象 | 未设置 | 光线穿过云时的体积迷雾系数。 |

### 系数项

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `scattering` | 数组或字符串 | 未设置 | 雾对光的散射程度。可使用三个`0.0`到`1.0`范围内的通道乘数，或使用十六进制颜色值。 |
| `absorption` | 数组或字符串 | 未设置 | 雾对光的吸收程度。可使用三个`0.0`到`1.0`范围内的通道乘数，或使用十六进制颜色值。 |

## 示例

```json
{
  "format_version": "1.16.100",
  "minecraft:fog_settings": {
    "description": {
      "identifier": "demo:blue_fog"
    },
    "distance": {
      "air": {
        "fog_start": 0.25,
        "fog_end": 0.75,
        "fog_color": "#88AAFF",
        "render_distance_type": "render"
      },
      "water": {
        "fog_start": 0,
        "fog_end": 40,
        "fog_color": "#3355AA",
        "render_distance_type": "fixed"
      }
    }
  }
}
```