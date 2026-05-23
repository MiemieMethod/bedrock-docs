# 战利品表

本页汇总行为包`loot_tables/`目录中战利品表的结构字段、常见条件与函数。战利品表用于描述实体掉落、方块掉落、容器战利品、钓鱼和其他随机产出流程。

## 根对象

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `pools` | 数组 | 未设置 | 战利品池数组。每个池独立执行，最终结果合并。 |

## 战利品池

池对象位于`pools`数组中。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `rolls` | 整数或对象 | `1` | 该池抽取次数。对象形式表示随机范围。 |
| `bonus_rolls` | 整数、小数或对象 | `0` | 额外抽取次数。通常与幸运相关。 |
| `entries` | 数组 | 未设置 | 候选条目数组。 |
| `conditions` | 数组 | 未设置 | 池级条件。仅条件通过时执行该池。 |
| `tiers` | 对象 | 未设置 | 分层抽取配置。存在该字段时按分层模式抽取。 |

### 数值范围对象

`rolls`、`bonus_rolls`、`count`、`damage`、`data`、`levels`等字段可使用范围对象。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `min` | 整数或小数 | 因字段而异 | 最小值。 |
| `max` | 整数或小数 | 因字段而异 | 最大值。 |

### 分层抽取对象

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `initial_range` | 整数 | 未设置 | 初始随机索引范围。 |
| `bonus_rolls` | 整数 | 未设置 | 追加检定次数。 |
| `bonus_chance` | 小数 | 未设置 | 每次追加检定成功概率。 |

分层抽取通常用于“按层级选一项”的掉落。分层池内条目存在顺序语义；索引超出条目数量时可产生空结果。兼容性资料显示，分层池通常不依赖条目级条件，应优先使用池级条件控制分层池启用。

## 条目

条目对象位于`pools > entries`数组中。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `type` | 字符串 | 未设置 | 条目类型。常见值为`item`、`loot_table`、`empty`。 |
| `name` | 字符串 | 未设置 | `item`时为物品标识符；`loot_table`时为被调用战利品表路径。 |
| `weight` | 整数 | `1` | 条目相对权重。 |
| `quality` | 整数 | `0` | 受幸运影响的权重修正值。 |
| `conditions` | 数组 | 未设置 | 条目级条件。 |
| `functions` | 数组 | 未设置 | 条目被选中后应用的函数数组。 |
| `pools` | 数组 | 未设置 | 内联池。多用于嵌套结构。 |

## 条件

条件对象可用于池、条目或函数。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `condition` | 字符串 | 未设置 | 条件类型。 |
| `chance` | 小数 | 未设置 | 随机条件基础概率。常见于`random_chance`。 |
| `looting_multiplier` | 小数 | 未设置 | `random_chance_with_looting`每级抢夺附加概率。 |
| `entity` | 字符串 | 未设置 | `entity_properties`检查对象，可为`this`、`attacker`、`attacking_player`。 |
| `properties` | 对象 | 未设置 | `entity_properties`实体属性约束。 |
| `match_tool` | 对象 | 未设置 | 工具匹配条件。 |
| `value` | 整数 | 未设置 | `has_mark_variant`或`has_variant`比较值。 |
| `peaceful` | 小数 | 未设置 | 和平难度概率。 |
| `easy` | 小数 | 未设置 | 简单难度概率。 |
| `normal` | 小数 | 未设置 | 普通难度概率。 |
| `hard` | 小数 | 未设置 | 困难难度概率。 |
| `default_chance` | 小数 | 未设置 | 难度未匹配时概率。 |

常见条件类型包括`killed_by_player`、`killed_by_player_or_pets`、`random_chance`、`random_chance_with_looting`、`has_mark_variant`、`has_variant`、`entity_properties`、`match_tool`、`random_difficulty_chance`。

### `properties`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `on_fire` | 布尔值 | 未设置 | 实体是否着火。 |
| `on_ground` | 布尔值 | 未设置 | 实体是否在地面。 |

### `match_tool`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | 字符串 | 未设置 | 工具物品标识符。 |
| `enchantments` | 数组 | 未设置 | 工具魔咒条件。 |

`enchantments`数组项可包含`enchantment`和`levels`字段，`levels`可使用范围对象。

## 函数

函数对象通常位于`entries > functions`中。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `function` | 字符串 | 未设置 | 函数类型。 |
| `conditions` | 数组 | 未设置 | 函数级条件。 |
| `count` | 整数或对象 | 未设置 | `set_count`、`looting_enchant`数量参数。 |
| `damage` | 小数或对象 | 未设置 | `set_damage`耐久比例。 |
| `data` | 整数或对象 | 未设置 | `set_data`数据值。 |
| `levels` | 整数或对象 | 未设置 | `enchant_with_levels`等级参数。 |
| `treasure` | 布尔值 | 未设置 | 是否允许宝藏魔咒。 |
| `chance` | 小数 | 未设置 | `enchant_random_gear`等概率参数。 |
| `id` | 字符串 | 未设置 | `set_actor_id`实体标识符。 |
| `name` | 字符串 | 未设置 | `set_name`物品名。 |
| `lore` | 字符串或数组 | 未设置 | `set_lore`描述文本。 |
| `loot_table` | 字符串 | 未设置 | `fill_container`引用的容器战利品表路径。 |
| `destination` | 字符串 | 未设置 | `exploration_map`目标结构。 |
| `base_cost` | 整数 | 未设置 | `enchant_book_for_trading`基础花费。 |
| `base_random_cost` | 整数 | 未设置 | `enchant_book_for_trading`基础随机花费。 |
| `per_level_cost` | 整数 | 未设置 | `enchant_book_for_trading`每级固定花费。 |
| `per_level_random_cost` | 整数 | 未设置 | `enchant_book_for_trading`每级随机花费。 |

### 函数适用场景

| 函数 | 容器战利品 | 方块掉落 | 钓鱼 | 实体掉落 | 实体装备 | 交易表 |
| --- | --- | --- | --- | --- | --- | --- |
| `set_count` | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| `set_name` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `set_lore` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `set_data` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `random_block_state` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `random_aux_value` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `set_damage` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `furnace_smelt` | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| `set_book_contents` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `exploration_map` | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| `set_banner_details` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `random_dye` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `set_actor_id` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `fill_container` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `enchant_book_for_trading` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `enchant_with_levels` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `enchant_randomly` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `enchant_random_gear` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `specific_enchants` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `looting_enchant` | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| `explosion_decay` | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| `set_data_from_color_index` | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| `trader_material_type` | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

⚠️ `exploration_map`在交易表中仅`destination`为`monument`或`mansion`时结果正确，其他目标会显示"未知地图"。

### 函数参数详情

#### `set_count`

交易表中不生效，交易数量应使用`quantity`字段。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `count` | 整数或范围对象 | `0` | 输出数量。可超过堆叠上限，超出时在容器中占用多个槽位。 |

#### `set_name`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | 字符串 | 未设置 | 物品名称。默认显示为斜体，支持格式代码（如`§r`重置格式）。不支持原始文本，支持`\n`换行。 |

#### `set_lore`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `lore` | 字符串或字符串数组 | 未设置 | 描述文本。每行支持格式代码，格式上下文独立。默认紫色斜体，`\n`可在单行内换行。 |

#### `set_data`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 整数或范围对象 | `0` | 数据值。仅影响方块数据值或物品附加值，不能设置工具耐久。 |

#### `random_block_state`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `block_state` | 字符串 | 未设置 | 方块状态名称。 |
| `values` | 整数或范围对象 | `0` | 状态取值范围，均匀随机选取。 |

#### `random_aux_value`

仅影响辅助值（如羊毛颜色），不影响工具耐久。会覆盖物品标识符中的数据值后缀（如`minecraft:wool:10`中的`10`）。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | 整数或范围对象 | 未设置 | 辅助值范围，均匀随机选取。 |

#### `set_damage`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `damage` | 小数或范围对象 | 未设置 | 耐久比例，范围`0`~`1`。`0`表示完全损坏，`1`表示全新。 |

#### `furnace_smelt`

仅在实体死亡上下文生效，且实体必须在死亡时处于着火状态。无额外参数。

#### `set_book_contents`

仅适用于`writable_book`和`written_book`。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `title` | 字符串 | 未设置 | 书名。 |
| `author` | 字符串 | 未设置 | 作者名。 |
| `pages` | 字符串数组 | 未设置 | 页面内容，每个元素为一页。最多50页，每页最多798字符，总计12800字符。支持`\n`换行，支持格式代码，每页格式独立。不支持制表符。 |

#### `set_banner_details`

仅适用于`banner`。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `type` | 整数 | 未设置 | 旗帜类型。`0`为白色旗帜，`1`为灾厄旗帜（不祥之旗）。 |

#### `random_dye`

随机染色皮革装备或马铠，不适用于羊毛等方块。无额外参数。

#### `set_actor_id`

适用于刷怪蛋。在交易表中，若不指定则默认使用交易者自身的实体类型。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | 字符串 | 未设置 | 生物标识符。 |

#### `fill_container`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `loot_table` | 字符串 | 未设置 | 从行为包根目录开始的战利品表路径。不能指向当前战利品表本身。 |

#### `enchant_book_for_trading`

用于交易场景的附魔书算法。在给予物品上使用时，会同时覆盖第一个需求物品的数量。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `base_cost` | 整数 | 未设置 | 基础花费（需求物品数量基础值）。 |
| `base_random_cost` | 整数 | 未设置 | 基础随机花费。 |
| `per_level_cost` | 整数 | 未设置 | 每附魔等级固定花费增量。 |
| `per_level_random_cost` | 整数 | 未设置 | 每附魔等级随机花费增量。 |

#### `enchant_with_levels`

模拟附魔台逻辑附魔，不限于30级。在给予物品上使用时，会同时覆盖第一个需求物品的数量。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `levels` | 整数或范围对象 | `0` | 附魔等级。负值视为`0`。极高等级（如99999）会产生包含几乎所有附魔的结果。 |
| `treasure` | 布尔值 | `false` | 是否允许宝藏附魔（含诅咒附魔）。 |

#### `enchant_randomly`

随机选择一种附魔及其等级。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `treasure` | 布尔值 | `false` | 是否允许宝藏附魔。 |

#### `enchant_random_gear`

类似`enchant_randomly`，但不包含宝藏附魔。适用于胡萝卜钓竿等非常规装备。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `chance` | 小数 | `0` | 决定是否进行附魔的概率，范围`0`~`1`。 |

#### `specific_enchants`

指定应用特定附魔组合。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchants` | 字符串数组或对象数组 | 未设置 | 附魔列表。字符串元素表示附魔标识符（等级默认`1`）；对象元素可含`id`（字符串）和`level`（整数或`[min, max]`数组，默认`1`）字段。 |

#### `looting_enchant`

仅在实体死亡上下文生效。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `count` | 整数或范围对象 | 未设置 | 每抢夺等级额外增加的数量范围。 |

#### `explosion_decay`

仅在方块爆炸上下文生效。无额外参数。不在爆炸中时掉落物默认保留；处于爆炸中时，根据爆炸威力有概率不产出掉落。

#### `set_data_from_color_index`

仅在交易表中生效。将物品数据值设为交易者实体`minecraft:color`组件的值。无额外参数。

#### `trader_material_type`

仅在特定交易上下文出现。在原版中用于根据交易者变种设置物品数据值，自定义场景中无法可靠使用。无额外参数。

### 探险地图目标

`exploration_map`的`destination`常见可选值如下：

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

## 兼容性说明

- 交易表与战利品表共享部分函数集合，但并非全部函数在交易中有效。
- 同一条目可叠加多个函数；同类型函数冲突时，后定义项通常覆盖先定义项。
- 条件与函数可同时作用在池、条目和函数层级，建议按“先池后条目后函数”理解执行顺序。
