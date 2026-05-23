# 中国版数据驱动维度与地形<!-- md:flag china -->

这一课只讲中国版的数据驱动维度与地形配置。它使用`netease_dimension`、`netease_biomes`、`netease_features`、`netease_feature_rules`、`netease_large_feature_pools`和`netease_large_feature_rules`等中国版专有目录；不要把这些文件放进国际版附加包的`dimensions`、`biomes`、`features`或`feature_rules`目录中。

/// warning | 不要混用两套格式
国际版数据驱动维度使用`minecraft:dimension`等格式；中国版数据驱动维度使用`netease:dimension_info`和`netease:`组件。两者的根对象、目录名、字段和运行时接口都不同，不能互相覆盖结论。
///

## 先声明维度

中国版内置主世界、下界和末地三个原生维度，维度ID分别为`0`、`1`和`2`。旧版中国版还保留了`3`至`20`的自定义维度ID；新版自定义维度推荐通过配置声明`22`至`2147483647`范围内的维度ID，以降低不同模组之间的维度ID冲突概率。

在行为包中创建`netease_dimension`目录，并用维度ID命名JSON文件。例如，`23333`号维度使用`dm23333.json`：

/// html | div.treeview
- behavior
    - netease_dimension
        - `dm23333.json`
///

```json title="behavior/netease_dimension/dm23333.json"
{
  "format_version": "1.14.0",
  "netease:dimension_info": {
    "components": {
      "netease:dimension_type": "minecraft:overworld",
      "netease:generator_noise": {},
      "netease:spawn_biomes": [
        "dm23333_plains"
      ],
      "netease:ban_vanilla_structure": {}
    }
  }
}
```

修改原生维度时，不使用维度ID命名文件，而是使用`overworld.json`、`nether.json`或`the end.json`。部分组件对原生维度无效，例如维度类型和生成器类组件；屏蔽原版结构的组件仍可用于原生维度。

常用组件如下：

| 组件 | 作用 |
| --- | --- |
| `netease:dimension_type` | 指定维度类型，可使用`minecraft:overworld`、`minecraft:nether`或`minecraft:the_end`。 |
| `netease:generator_noise` | 使用噪声生成器。 |
| `netease:generator_flat` | 使用超平坦生成器，仅适用于主世界和下界类型。 |
| `netease:generator_legacy` | 使用旧世界生成器，仅适用于主世界类型。 |
| `netease:spawn_biomes` | 指定玩家出生可用的生物群系列表。 |
| `netease:biome_source` | 指定中国版自定义生物群系源。 |
| `netease:ban_vanilla_feature` | 屏蔽原版小型地物。 |
| `netease:ban_vanilla_structure` | 屏蔽或选择性保留原版结构。 |

`netease:ban_vanilla_structure`可以使用白名单或黑名单。只允许生成古城和要塞时，可写作：

```json
"netease:ban_vanilla_structure": {
  "allowlist": [
    "ancient_city",
    "stronghold"
  ]
}
```

只屏蔽破坏的传送门和海底神殿时，可写作：

```json
"netease:ban_vanilla_structure": {
  "blocklist": [
    "ruined_portal",
    "monument"
  ]
}
```

`allowlist`和`blocklist`只能选择其一。二者都不写时，空对象表示屏蔽所有原版结构。若需要屏蔽中国版大型结构地物，可以使用`netease_large_feature`作为结构类型名称。

/// warning | 已探索维度会保留旧地形
如果玩家已经进入过某个维度，维度区块会写入存档。之后再修改维度类型或生成器，可能出现旧地形与新地形混合。中国版模组SDK提供`UpgradeMapDimensionVersion`接口用于提升维度版本并废弃旧区块数据，但这属于运行时脚本接口，不是数据驱动JSON字段。
///

## 编写维度生物群系

中国版自定义维度中的生物群系通常放在行为包`netease_biomes`目录下，并按维度名分组。维度ID为`23333`时，维度名为`dm23333`，该维度的自定义生物群系可放在`netease_biomes/dm23333`中：

/// html | div.treeview
- behavior
    - netease_biomes
        - dm23333
            - `dm23333_plains.json`
            - `dm23333_desert.json`
///

自定义生物群系通常继承一个原版生物群系，并把标识符写成“维度名前缀+原版生物群系名”的形式：

```json title="behavior/netease_biomes/dm23333/dm23333_plains.json"
{
  "format_version": "1.14.0",
  "minecraft:biome": {
    "description": {
      "identifier": "dm23333_plains",
      "inherits": "plains"
    },
    "components": {
      "dm23333": {},
      "minecraft:overworld_generation_rules": {
        "hills_transformation": "dm23333_forest_hills",
        "mutate_transformation": "dm23333_sunflower_plains",
        "generate_for_climates": [
          [
            "medium",
            1
          ]
        ]
      }
    }
  }
}
```

没有重写的属性会沿用被继承的原版生物群系。官方模板会给每个自定义生物群系添加与维度名相同的标签，例如`dm23333`；这个标签可用于生成规则、地物规则和生物生成规则中过滤维度。

若维度类型为末地，并且不希望生成末影龙及相关战斗逻辑，可在对应生物群系组件中添加`netease:no_spawn_end_dragon`。这个组件只能阻止后续相关逻辑；如果存档中已经生成过末影龙，它不能删除既有实体。

资源包根目录的`biomes_client.json`可为中国版自定义生物群系配置客户端显示颜色：

```json title="resource/biomes_client.json"
{
  "biomes": {
    "dm23333_plains": {
      "water_surface_color": "#905957",
      "water_fog_color": "#905957",
      "fog_color": "#4B0082"
    }
  }
}
```

## 使用自定义高度

中国版可在自定义生物群系组件中使用`netease:overworld_surface`控制高度后处理。官方资料说明该高度控制发生在“生物群系→高度→地物”的地形生成流程中，因此它不能影响已经进入地物阶段的生成结果。当前资料记载的自定义维度高度区间为`0`至`256`。

`netease:overworld_surface`的`adjustments`是流水线式节点列表。常用节点如下：

| 节点 | 作用 |
| --- | --- |
| `fill` | 选取`min_height`至`max_height`之间的高度区间，并按权重填充方块。 |
| `move` | 选取高度区间，并用`move_offset`整体上移或下移。 |
| `replace` | 选取高度区间，并按比例把一组方块替换为另一组方块。 |

示例：

```json
"netease:overworld_surface": {
  "adjustments": [
    {
      "type": "fill",
      "min_height": 90,
      "max_height": "110 + math.sin(variable.worldx * 180 / math.pi / 10) * 10",
      "pool": [
        {
          "fill_block": "minecraft:grass",
          "weight": 10
        },
        {
          "fill_block": {
            "name": "minecraft:wool",
            "states": {
              "color": "yellow"
            }
          },
          "weight": 1
        }
      ]
    }
  ]
}
```

`min_height`、`max_height`和`move_offset`可使用`variable.worldx`、`variable.worldz`、`variable.height`以及`query.noise`。方块池不适合填写床、附魔台、自定义方块实体外观等特殊方块。

## 使用自定义生物群系源

`netease:biome_source`写在维度文件的`components`中，用于替代原版硬编码生物群系生成流程。一旦启用自定义生物群系源，生物群系文件中的`minecraft:overworld_generation_rules`不再控制布局。官方资料还说明，使用自定义生物群系源后不会生成原版要塞。

一个简单的棋盘式布局如下：

```json title="behavior/netease_dimension/dm23333.json"
{
  "format_version": "1.14.0",
  "netease:dimension_info": {
    "components": {
      "netease:dimension_type": "minecraft:overworld",
      "netease:biome_source": [
        {
          "type": "random_with_weight",
          "pool": [
            {
              "biome_type": "dm23333_plains",
              "weight": 1
            },
            {
              "biome_type": "dm23333_desert",
              "weight": 1
            }
          ]
        },
        {
          "type": "fixed_zoom_2x"
        },
        {
          "type": "fuzzy_zoom_2x"
        }
      ]
    }
  }
}
```

常用生物群系源节点如下：

| 节点 | 作用 |
| --- | --- |
| `random_with_weight` | 在初始区域内按权重随机分配生物群系。 |
| `fixed_zoom_2x` | 将布局等比放大2倍。 |
| `fuzzy_zoom_2x` | 将布局模糊放大2倍。 |
| `vanilla_zoom_2x` | 使用接近原版的放大逻辑。 |
| `replace` | 按比例把某个生物群系替换成另一个生物群系。 |
| `transition` | 在两个相邻生物群系之间生成过渡生物群系。 |
| `associated` | 在核心生物群系周围生成伴生生物群系。 |
| `gen_key_biomes` | 在固定大小区域内生成关键生物群系。 |
| `condition` | 使用MoLang条件表达式决定当前位置的生物群系。 |

`condition`节点可以使用`variable.worldx`、`variable.worldz`、`variable.originx`、`variable.originz`和`query.get_neighborhood_is_biome`。该节点会参与生物群系初始布局，表达式过多或过复杂时可能带来性能问题。

## 控制生物和地物生成

生物生成可继续使用生成规则。通常把自定义维度标签写进`minecraft:biome_filter`，使生物只在该维度的生物群系中生成：

```json
"minecraft:biome_filter": [
  {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "dm23333"
  }
]
```

中国版结构地物放在`netease_features`目录，地物规则放在`netease_feature_rules`目录。中国版的网易结构地物使用`netease:structure_feature`根对象，并引用`structures`目录中导出的结构：

/// html | div.treeview
- behavior
    - structures
        - demo
            - `pumpkins.mcstructure`
    - netease_features
        - `pumpkins_feature.json`
    - netease_feature_rules
        - `pumpkins_rule.json`
///

```json title="behavior/netease_features/pumpkins_feature.json"
{
  "format_version": "1.14.0",
  "netease:structure_feature": {
    "description": {
      "identifier": "demo:pumpkins_feature"
    },
    "places_structure": "demo:pumpkins",
    "rotation": 0
  }
}
```

```json title="behavior/netease_feature_rules/pumpkins_rule.json"
{
  "format_version": "1.14.0",
  "minecraft:feature_rules": {
    "description": {
      "identifier": "demo:pumpkins_rule",
      "places_feature": "demo:pumpkins_feature"
    },
    "conditions": {
      "placement_pass": "surface_pass",
      "minecraft:biome_filter": [
        {
          "test": "has_biome_tag",
          "operator": "==",
          "value": "dm23333"
        }
      ]
    },
    "distribution": {
      "iterations": 1,
      "coordinate_eval_order": "xzy",
      "scatter_chance": 100.0,
      "x": 0,
      "y": "query.get_height_at(variable.worldx, variable.worldz)",
      "z": 0
    }
  }
}
```

自网易1.21版本起，官方资料要求地物和地物规则的标识符添加命名空间，并使用`1.14.0`格式版本。地物文件名、地物规则文件名还应与标识符冒号后的部分保持一致。

/// note | 结构地物的限制
中国版资料说明，单个结构地物的结构尺寸不应超过一个区块的平面范围，即`16×16`。结构地物不生成结构中保存的实体。若结构包含空气但不希望覆盖地形，应在导出前使用结构空位。
///

## 生成大型结构地物

大型结构地物用于解决多个小结构拼接成大型结构的问题。它依赖拼图方块、结构池和大型结构地物规则。结构池放在`netease_large_feature_pools`目录，大型结构地物规则放在`netease_large_feature_rules`目录：

/// html | div.treeview
- behavior
    - netease_large_feature_pools
        - `center_pool.json`
    - netease_large_feature_rules
        - `village_like_rule.json`
    - structures
        - demo
            - `center.mcstructure`
            - `road.mcstructure`
///

结构池用于按权重保存可拼接的结构：

```json title="behavior/netease_large_feature_pools/center_pool.json"
{
  "format_version": "1.18.0",
  "netease:large_feature_pool": {
    "description": {
      "identifier": "demo:center_pool"
    },
    "pool": [
      {
        "structure_name": "demo:center",
        "path": "demo:center",
        "weight": 1,
        "match_terrain": false
      }
    ],
    "end_pool": "minecraft:empty"
  }
}
```

大型结构地物规则决定中心结构池、允许生成的生物群系标签、间距、递归深度和高度：

```json title="behavior/netease_large_feature_rules/village_like_rule.json"
{
  "format_version": "1.14.0",
  "netease:large_feature_rules": {
    "description": {
      "identifier": "demo:village_like_rule",
      "place_pool": "demo:center_pool"
    },
    "allowed_biomes": [
      "dm23333"
    ],
    "town_spacing": 8,
    "min_town_separation": 1,
    "max_depth": 8,
    "height": "variable.height",
    "ignore_fit_in_context": false,
    "center_pool_rotation": [
      0,
      90,
      180,
      270
    ]
  }
}
```

`height`可使用固定数值、`variable.worldx`、`variable.worldz`、`variable.height`和`query.noise`。官方资料说明，网易2.9版本后大型结构支持下界和末地；在下界中，`variable.height`为固定值`128`。

## 连接维度入口

自定义传送门不是单纯的数据驱动维度文件。官方传送门示例使用带传送组件的自定义方块，并配合服务端脚本检测门框、放置传送门方块、监听维度切换完成事件，以及保存传送门位置数据。

实现时通常需要：

1. 创建目标维度。
2. 创建用于传送门的自定义方块。
3. 在服务端脚本中监听物品使用事件，检测门框结构。
4. 使用地图接口放置传送门方块。
5. 监听维度切换完成事件，实现类似原版传送门定位器的返回门逻辑。

官方资料还指出，自定义传送门方块通过脚本放置时应使用非零附加值控制延伸方向：`aux`为`1`表示沿X轴延伸，`aux`为`2`表示沿Z轴延伸。手动放置的传送门方块附加值通常为`0`，不建议作为正式传送门使用。

## 常见排错

| 报错或现象 | 常见原因 |
| --- | --- |
| `lookupByName can not find biome` | 生物群系名写错，或自定义群系源引用的生物群系文件不存在。 |
| `different Dimension between` | `hills_transformation`或`mutate_transformation`指向了其他维度的生物群系。 |
| `total weight of xxx is zero` | 某类温度下的生成权重总和为`0`。 |
| `Feature rule identifier xxx does not match filename yyy` | 地物规则文件名和标识符冒号后的名称不一致。 |
| `No definition found for feature xxx` | 地物规则引用的地物文件不存在或标识符不匹配。 |
| `The feature name XXX did not match the expected name of YYY` | 地物文件名和地物标识符不一致。 |
| `Failed to load feature XXX` | `places_structure`对应的结构路径或结构文件位置错误。 |

