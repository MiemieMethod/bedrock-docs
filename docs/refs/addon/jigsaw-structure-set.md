# 结构集

本页列出国际版行为包拼图结构集定义。结构集用于声明一组可选拼图结构，并指定其在世界中的放置算法和网格分布参数。

## 文件位置

结构集定义通常放置于行为包`worldgen/structure_sets/`目录。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 结构集定义格式版本。 |
| `minecraft:structure_set` | 对象 | 未设置 | 结构集定义主体。 |

## `minecraft:structure_set`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 结构集标识信息。 |
| `placement` | 对象 | 未设置 | 放置算法配置。 |
| `structures` | 对象数组 | 未设置 | 可参与抽样的拼图结构列表。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 结构集赋命名空间标识符。 |

### `structures`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `structure` | 字符串 | 未设置 | 拼图结构标识符。 |
| `weight` | 整数 | 未设置 | 在结构集内的相对权重。 |

### `placement`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `type` | 字符串 | 未设置 | 放置算法类型。 |
| `salt` | 整数 | 未设置 | 随机播种附加值。 |
| `separation` | 整数 | `8` | 结构之间最小分离距离（区块）。 |
| `spacing` | 整数 | `34` | 结构平均间距（区块），必须大于`separation`。 |
| `spread_type` | 字符串 | `linear` | 随机散布算法。 |

`type`支持下列值：

- `minecraft:random_spread`
- `minecraft:concentric_rings`

`spread_type`支持下列值：

- `linear`
- `triangular`

## 放置策略说明

- `minecraft:random_spread`按网格单元随机选点放置结构，`spacing`决定网格尺寸，`separation`决定单元内保留边距。
- `salt`应在不同结构集之间保持唯一，以减少同参数结构集重叠。
- 结构集中的`weight`越高，被选中参与放置的概率越大。
