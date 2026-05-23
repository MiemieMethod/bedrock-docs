# 地物规则

本页列出行为包`feature_rules/`目录中地物规则文件的主要字段。地物规则用于把一个地物挂接到满足条件的生物群系，并指定该地物在世界生成流程中的放置阶段和初始散植参数。

/// note | 字段类型说明
Microsoft Learn的`FeatureRulesReference`自动生成字段表将`description.identifier`和`description.places_feature`列为布尔值；同一官方资料中的地物规则架构、示例和表单定义均将二者说明为字符串或地物引用。本页按后者记录。
///

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 地物规则文件的格式版本。官方参考要求使用`1.13.0`或更高版本。 |
| `minecraft:feature_rules` | 对象 | 未设置 | 地物规则定义。 |

## `minecraft:feature_rules`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 地物规则的标识信息和被放置地物。 |
| `conditions` | 对象 | 未设置 | 控制地物挂接到哪些生物群系以及在哪个放置阶段执行的条件。 |
| `distribution` | 对象 | 未设置 | 初始散植参数。官方地物规则架构将该字段列为可选。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 地物规则的赋命名空间标识符。官方架构要求冒号后的规则名与文件名一致。 |
| `places_feature` | 字符串 | 未设置 | 由该规则放置的地物标识符。一个地物规则只控制一个地物。 |

### `conditions`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `placement_pass` | 字符串 | 未设置 | 地物相对于其他地物执行的放置阶段。较早阶段保证早于较晚阶段执行；同一阶段内不保证顺序。 |
| `minecraft:biome_filter` | 过滤器组 | 未设置 | 用于判断该规则应挂接到哪些生物群系的过滤器列表。常用测试为`has_biome_tag`。 |

`placement_pass`当前可使用下列值：

- `first_pass`
- `before_underground_pass`
- `underground_pass`
- `after_underground_pass`
- `before_surface_pass`
- `surface_pass`
- `after_surface_pass`
- `before_sky_pass`
- `sky_pass`
- `after_sky_pass`
- `final_pass`

洞穴雕刻类地物的官方参考另要求将地物规则放置在`pregeneration_pass`。该阶段面向地形预生成雕刻，不属于普通地表或地下装饰地物的常规放置阶段。

### `distribution`

`distribution`控制地物的初始散植。该对象使用与散植地物相同的散植参数结构。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `iterations` | 整数或Molang表达式 | `1` | 尝试放置的次数。数值越大，生成集中度通常越高。 |
| `x` | 整数、Molang表达式或坐标范围对象 | `0` | 每次尝试时的X坐标分布。 |
| `y` | 整数、Molang表达式或坐标范围对象 | `0` | 每次尝试时的Y坐标分布。 |
| `z` | 整数、Molang表达式或坐标范围对象 | `0` | 每次尝试时的Z坐标分布。 |
| `coordinate_eval_order` | 字符串 | `xzy` | 坐标表达式的求值顺序。坐标依赖其他坐标时应显式设置。 |
| `scatter_chance` | 十进制数、Molang表达式或对象 | `1` | 散植整体发生的概率。该概率不按单次迭代计算；若未通过，则本次散植不会执行任何迭代。 |

`coordinate_eval_order`支持`xyz`、`xzy`、`yxz`、`yzx`、`zxy`和`zyx`。当坐标范围使用对象表示时，可包含`distribution`、`extent`、`grid_offset`和`step_size`；其中`distribution`支持`uniform`、`gaussian`、`inverse_gaussian`、`triangle`、`fixed_grid`和`jittered_grid`。

## 示例

```json title="feature_rules/birch_forest_surface_trees_feature.json"
{
  "format_version": "1.13.0",
  "minecraft:feature_rules": {
    "description": {
      "identifier": "minecraft:birch_forest_surface_trees_feature",
      "places_feature": "minecraft:legacy:birch_forest_tree_feature"
    },
    "conditions": {
      "placement_pass": "surface_pass",
      "minecraft:biome_filter": [
        {
          "test": "has_biome_tag",
          "operator": "==",
          "value": "forest"
        },
        {
          "all_of": [
            {
              "test": "has_biome_tag",
              "operator": "==",
              "value": "birch"
            },
            {
              "test": "has_biome_tag",
              "operator": "!=",
              "value": "mutated"
            }
          ]
        }
      ]
    },
    "distribution": {
      "iterations": 1,
      "x": 0,
      "y": 0,
      "z": 0
    }
  }
}
```
