# 战利品表

本页列出行为包`loot_tables/`目录中战利品表文件的主要字段。战利品表用于定义实体死亡、容器开启、钓鱼和其他玩法事件可生成的物品；部分战利品表函数也可在交易表中复用。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `pools` | 数组 | 未设置 | 战利品池数组。每个池独立执行随机抽取。 |

## 战利品池

战利品池对象位于`pools`数组中。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `rolls` | 整数或对象 | `1` | 该池执行抽取的次数。使用对象时表示随机范围。 |
| `bonus_rolls` | 整数 | `0` | 基于幸运特性增加的额外抽取次数。 |
| `conditions` | 数组 | 未设置 | 战利品条件数组。条件满足时，该池才会执行。 |
| `entries` | 数组 | 未设置 | 候选条目数组。 |
| `tiers` | 对象 | 未设置 | 分层抽取配置。 |

### 随机范围

`rolls`、`count`、`damage`、`data`等字段可在需要随机数值时使用范围对象。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min` | 整数或小数 | 因字段而异 | 最小值。 |
| `max` | 整数或小数 | 因字段而异 | 最大值。 |

### 分层抽取

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `initial_range` | 整数 | 未设置 | 初始抽取范围。 |
| `bonus_rolls` | 整数 | 未设置 | 额外抽取次数。 |
| `bonus_chance` | 小数 | 未设置 | 额外抽取概率。 |

## 条目

条目对象位于`pools > entries`数组中。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `type` | 字符串 | 未设置 | 条目类型。常见值为`item`、`loot_table`和`empty`。 |
| `name` | 字符串 | 未设置 | 当`type`为`item`时表示物品标识符；当`type`为`loot_table`时表示被引用的战利品表路径。 |
| `weight` | 整数 | `1` | 条目在同一池中的相对权重。数值越大，抽中概率越高。 |
| `conditions` | 数组 | 未设置 | 条目条件数组。条件满足时，该条目才可被选中。 |
| `functions` | 数组 | 未设置 | 战利品函数数组。函数会在条目被选中后修改输出物品。 |
| `pools` | 数组 | 未设置 | 内联嵌套战利品池。通常用于`loot_table`类型条目。 |

## 条件

条件对象可用于池、条目或函数。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `condition` | 字符串 | 未设置 | 条件类型。 |
| `chance` | 小数 | 未设置 | `random_chance`和`random_chance_with_looting`的基础概率，通常位于`0.0`至`1.0`之间。 |
| `looting_multiplier` | 小数 | 未设置 | `random_chance_with_looting`中每级抢夺魔咒增加的概率。 |
| `entity` | 字符串 | 未设置 | `entity_properties`检查的实体，可为`this`、`attacker`或`attacking_player`。 |
| `properties` | 对象 | 未设置 | `entity_properties`检查的实体属性。 |
| `match_tool` | 对象 | 未设置 | `match_tool`检查的工具条件。 |
| `value` | 整数 | 未设置 | `has_mark_variant`或`has_variant`检查的变种值。 |
| `peaceful` | 小数 | 未设置 | `random_difficulty_chance`在和平难度下的概率。 |
| `easy` | 小数 | 未设置 | `random_difficulty_chance`在简单难度下的概率。 |
| `normal` | 小数 | 未设置 | `random_difficulty_chance`在普通难度下的概率。 |
| `hard` | 小数 | 未设置 | `random_difficulty_chance`在困难难度下的概率。 |
| `default_chance` | 小数 | 未设置 | `random_difficulty_chance`未匹配难度时使用的概率。 |

常见条件类型包括`killed_by_player`、`killed_by_player_or_pets`、`random_chance`、`random_chance_with_looting`、`has_mark_variant`、`has_variant`、`entity_properties`、`match_tool`和`random_difficulty_chance`。

### `properties`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `on_fire` | 布尔值 | 未设置 | 实体是否着火。 |
| `on_ground` | 布尔值 | 未设置 | 实体是否位于地面。 |

### `match_tool`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `item` | 字符串 | 未设置 | 工具物品标识符。 |
| `enchantments` | 数组 | 未设置 | 工具上的魔咒条件数组。 |

`enchantments`项可包含`enchantment`和`levels`。`levels`可包含`min`。

## 函数

函数对象可用于条目或其他支持战利品函数的表结构。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `function` | 字符串 | 未设置 | 函数类型。 |
| `conditions` | 数组 | 未设置 | 函数条件数组。条件满足时，该函数才会应用。 |
| `count` | 整数或对象 | 未设置 | `set_count`和`looting_enchant`使用的数量或数量范围。 |
| `damage` | 小数或对象 | 未设置 | `set_damage`使用的耐久剩余比例或范围。`1.0`表示未损坏，`0.0`表示无剩余耐久。 |
| `data` | 整数或对象 | 未设置 | `set_data`使用的数据值或数据值范围。 |
| `levels` | 整数或对象 | 未设置 | `enchant_with_levels`使用的魔咒等级或等级范围。 |
| `treasure` | 布尔值 | 未设置 | `enchant_randomly`和`enchant_with_levels`是否允许宝藏魔咒。 |
| `id` | 字符串 | 未设置 | `set_actor_id`使用的实体标识符。 |
| `destination` | 字符串 | 未设置 | `exploration_map`使用的目标结构类型。 |

### 物品修改函数

| 函数 | 描述 |
| --- | --- |
| `set_count` | 设置输出物品数量。 |
| `looting_enchant` | 根据击杀工具上的抢夺魔咒调整掉落数量。该函数只适用于由实体死亡调用的战利品表。 |
| `set_damage` | 设置具有耐久的物品剩余耐久比例。 |
| `set_data` | 设置物品或方块物品的数据值。 |
| `set_data_from_color_index` | 从关联实体的颜色索引继承数据值；无颜色索引或位于容器战利品表中时产生`0`。 |
| `random_aux_value` | 从给定范围随机选择附加值。 |
| `random_block_state` | 随机设置结果物品携带的方块状态值。 |
| `random_dye` | 为皮革类交易物品随机染色。 |
| `set_actor_id` | 设置刷怪蛋的实体标识符。省略`id`时会尝试继承关联实体的标识符。 |
| `set_banner_details` | 设置旗帜细节。官方资料说明当前仅支持`type`为`1`的村民旗帜。 |
| `set_book_contents` | 设置成书内容。官方资料说明`rawtext`仅适用于`pages`，不适用于`author`或`title`。 |
| `set_lore` | 设置物品描述文本。官方资料说明当前不支持`rawtext`。 |
| `set_name` | 设置物品名称。官方资料说明当前不支持`rawtext`。 |

### 魔咒函数

| 函数 | 描述 |
| --- | --- |
| `enchant_book_for_trading` | 使用村民交易售书算法为书附魔。该函数只适用于交易表。 |
| `enchant_random_gear` | 按原版生物生成装备的算法随机附魔装备，并可通过`chance`调整概率。 |
| `enchant_randomly` | 为物品生成一个兼容的随机魔咒。 |
| `enchant_with_levels` | 按类似附魔台的等级算法为物品附魔。 |
| `set_potion` | 使用药水ID设置兼容物品的药水类型。 |
| `specific_enchants` | 指定一个或多个魔咒，也可用对象形式指定魔咒等级。最高等级受游戏硬编码限制。 |

`enchant_book_for_trading`的花费由`base_cost`、`base_random_cost`、`per_level_random_cost`和`per_level_cost`共同决定。官方给出的公式为`base_cost + (base_random_cost + enchantmentLevel * per_level_random_cost) + enchantmentLevel * per_level_cost`。

### 其他函数

| 函数 | 描述 |
| --- | --- |
| `exploration_map` | 将普通地图转换为指向指定结构的探险地图。 |
| `fill_container` | 为箱子等容器物品指定放置后的容器战利品表。容器内容在打开或破坏时生成。 |
| `furnace_smelt` | 实体被火焰相关方式击杀时，将掉落物转换为烧炼后的形式。该函数不适用于交易或容器。 |
| `trader_material_type` | 影响渔夫等交易对特定材料类型物品的处理。 |

同一条目可以同时定义多个函数。多个相同函数发生冲突时，官方资料说明后定义的函数会覆盖先定义的结果。

### 探险地图目标

`exploration_map`的`destination`当前支持下列值：

- `buriedtreasure`
- `endcity`
- `fortress`
- `mansion`
- `mineshaft`
- `monument`
- `pillageroutpost`
- `ruins`
- `shipwreck`
- `stronghold`
- `temple`
- `village`

## 示例

```json title="loot_tables/entities/example.json"
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "conditions": [
        {
          "condition": "killed_by_player"
        }
      ],
      "entries": [
        {
          "type": "item",
          "name": "minecraft:diamond",
          "weight": 1,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "empty",
          "weight": 3
        }
      ]
    }
  ]
}
```
