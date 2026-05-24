# 物品函数

本页汇总战利品表与交易表中可用的物品函数。物品函数用于修改条目的数量、名称、说明、耐久、附魔、容器内容和其他派生属性。函数写在条目的`functions`数组中，通常不接受Molang。

## 适用范围

| 函数 | 战利品表 | 交易表 | 说明 |
| --- | --- | --- | --- |
| `set_count` | ✅ | ❌ | 设置物品数量。交易表使用`quantity`字段。 |
| `set_name` | ✅ | ✅ | 设置物品显示名称。 |
| `set_lore` | ✅ | ✅ | 设置物品说明文字。 |
| `set_data` | ✅ | ✅ | 设置数据值或附加值。 |
| `random_block_state` | ✅ | ✅ | 为方块物品随机设置方块状态。 |
| `random_aux_value` | ✅ | ✅ | 随机设置辅助值。 |
| `set_damage` | ✅ | ✅ | 设置耐久比例。 |
| `set_book_contents` | ✅ | ✅ | 设置书页内容。 |
| `set_banner_details` | ✅ | ✅ | 设置旗帜类型与图案。 |
| `random_dye` | ✅ | ✅ | 随机染色可染色物品。 |
| `set_actor_id` | ✅ | ✅ | 设置刷怪蛋对应实体。 |
| `fill_container` | ✅ | ✅ | 为容器物品指定内容表。 |
| `set_potion` | ✅ | ✅ | 设置药水类型。 |
| `enchant_book_for_trading` | ✅ | ✅ | 生成适合交易的附魔书。 |
| `enchant_with_levels` | ✅ | ✅ | 按等级范围附魔。 |
| `enchant_randomly` | ✅ | ✅ | 随机附魔。 |
| `enchant_random_gear` | ✅ | ✅ | 随机附魔装备。 |
| `specific_enchants` | ✅ | ✅ | 指定附魔组合。 |
| `set_stew_effect` | ✅ | ✅ | 设置可疑炖菜效果。 |
| `set_ominous_bottle_amplifier` | ✅ | ⚠️ | 设置不祥之瓶强化值。 |
| `set_armor_trim` | ✅ | ❌ | 设置盔甲纹饰。 |
| `looting_enchant` | ✅ | ❌ | 按抢夺等级追加掉落。 |
| `furnace_smelt` | ✅ | ❌ | 火焰掉落烧炼。 |
| `exploration_map` | ✅ | ⚠️ | 生成探险地图或藏宝图。 |
| `explosion_decay` | ✅ | ❌ | 爆炸衰减。 |
| `set_data_from_color_index` | ❌ | ✅ | 使用颜色索引设置数据值。 |
| `trader_material_type` | ❌ | ✅ | 交易者材料类型。 |

## 通用函数

### `set_count`

设置条目的物品数量。数量可以是整数，也可以是范围对象。

### `set_name`

设置物品名称。名称默认以斜体显示，支持格式代码。

### `set_lore`

设置物品说明文字。可以使用字符串或字符串数组。

### `set_data`

设置数据值或附加值。对方块和物品的含义不同。

### `random_block_state`

为方块物品随机设置方块状态。

### `random_aux_value`

随机设置辅助值，常用于旧式数据值兼容内容。

### `set_damage`

设置耐久比例。`0`表示完全损坏，`1`表示全新。

## 附魔函数

### `enchant_randomly`

随机附加一个魔咒及其等级。

### `enchant_with_levels`

按指定等级范围模拟附魔台附魔。

### `enchant_random_gear`

随机为装备附魔，但不包含宝藏魔咒。

### `specific_enchants`

直接指定一个或多个魔咒及其等级。

### `enchant_book_for_trading`

为交易场景生成附魔书，并据此计算需求物品数量。

### `looting_enchant`

仅在实体死亡上下文生效，按抢夺等级增加额外掉落。

## 其他函数

### `furnace_smelt`

仅在实体死亡且实体处于着火状态时生效，将掉落物烧炼。

### `set_book_contents`

设置书名、作者与页面内容。

### `set_banner_details`

设置旗帜类型与图案细节。

### `random_dye`

随机染色可染色物品。

### `set_actor_id`

为刷怪蛋指定实体标识符。

### `fill_container`

为容器物品指定战利品表路径，生成后会从该表填充内容。

### `set_potion`

设置药水类型，作用于兼容药水物品。

### `exploration_map`

将地图转换为指定目的地的探险地图。部分目的地在交易中支持有限。

### `explosion_decay`

在爆炸场景中按概率丢失掉落。

### `set_data_from_color_index`

在交易表中将物品数据值设为交易者的颜色索引。

### `trader_material_type`

在交易表中根据交易者材料类型调整物品数据值。

### `set_stew_effect`

设置可疑炖菜的效果。

### `set_ominous_bottle_amplifier`

设置不祥之瓶的强化值。

### `set_armor_trim`

为支持纹饰的物品设置盔甲纹饰。当前仅在战利品表中使用。

## 兼容性说明

- 交易表与战利品表共享部分物品函数，但并非完全等价。
- 同一条目可以叠加多个函数。
- 函数与条件都可以作用于池、条目或函数自身的层级。
