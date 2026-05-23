# 配方

本页汇总行为包`recipes/`目录中配方文件的结构字段。配方用于定义工作台、切石机、锻造台、熔炉、营火及酿造台的物品转化规则。

## 通用结构

所有配方文件均包含`format_version`和一个根对象键。根对象键决定配方类型，其值包含配方主体字段。

| 顶层字段 | 类型 | 说明 |
| --- | --- | --- |
| `format_version` | 字符串 | 文件格式版本。建议填写与目标游戏版本匹配的值。`1.20.0`及之后格式不再支持旧式附加值字段。 |
| `minecraft:recipe_shaped` | 对象 | 有序合成配方。 |
| `minecraft:recipe_shapeless` | 对象 | 无序合成配方。 |
| `minecraft:recipe_furnace` | 对象 | 烧炼/烹饪配方。 |
| `minecraft:recipe_brewing_mix` | 对象 | 酿造混合配方。 |
| `minecraft:recipe_brewing_container` | 对象 | 酿造容器配方。 |
| `minecraft:recipe_smithing_transform` | 对象 | 锻造转化配方（需`format_version` ≥ `1.20.0`）。 |
| `minecraft:recipe_smithing_trim` | 对象 | 锻造盔甲纹饰配方（需`format_version` ≥ `1.20.0`）。 |

## 通用字段

所有配方类型共享以下字段，位于根对象内。

### `description`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 配方赋命名空间标识符，在所有行为包范围内唯一。建议加命名空间前缀。 |

### `tags`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `tags` | 字符串数组 | 未设置 | 合成标签数组。指定配方适用的合成站。至少提供一个标签。 |

常见合成标签：

| 标签 | 适用配方类型 | 说明 |
| --- | --- | --- |
| `crafting_table` | 合成 | 工作台与玩家2×2合成网格。 |
| `stonecutter` | 合成 | 切石机。 |
| `smithing_table` | 合成 | 锻造台（旧式）。 |
| `furnace` | 烧炼 | 熔炉。 |
| `blast_furnace` | 烧炼 | 高炉。 |
| `smoker` | 烧炼 | 烟熏炉。 |
| `campfire` | 烧炼 | 营火。 |
| `soul_campfire` | 烧炼 | 灵魂营火。 |
| `brewing_stand` | 酿造 | 酿造台。 |

设置为`[""]`可禁用配方，常用于覆盖原版配方。

### `unlock`

`unlock`数组指定配方解锁条件（需`min_engine_version` ≥ `1.20.11`）。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | 字符串 | 未设置 | 玩家背包中需包含的物品标识符。支持数据值后缀。 |
| `data` | 整数 | `0` | 物品数据值。 |
| `context` | 字符串 | 未设置 | 触发解锁的上下文。已知值：`AlwaysUnlocked`、`PlayerInWater`、`PlayerHasManyItems`、`None`。 |

`unlock`数组内各对象之间为逻辑或关系，满足任一条件即可解锁。

## 物品描述符

物品描述符用于在配方中引用物品，可为字符串或对象。

### 字符串格式

直接写物品标识符，可附数据值后缀：

```
"minecraft:planks"
"minecraft:planks:2"
```

### 对象格式

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | 字符串 | 未设置 | 物品标识符。支持数据值后缀。 |
| `data` | 整数或Molang表达式 | `0` | 物品数据值。在加载时计算一次。 |
| `count` | 整数 | `1` | 物品数量。仅在合成输出与无序配方原料中有效。 |
| `tag` | 字符串 | 未设置 | 物品标签标识符。用于匹配具有该标签的一组物品（部分场景支持）。 |

不可堆叠物品的`count`不能大于`1`。

### 药水特殊标识符

酿造配方支持以下药水类型特殊标识符（仅字符串格式）：

格式：`minecraft:potion_type:<效果名>`，效果名支持`long_`和`strong_`前缀。

常见效果名：`water`、`awkward`、`mundane`、`thick`、`healing`、`regeneration`、`swiftness`、`strength`、`harming`、`poison`、`slowness`、`weakness`、`water_breathing`、`fire_resistance`、`nightvision`、`invisibility`、`leaping`、`slow_falling`、`turtle_master`、`wither`

## 有序配方字段

根对象键：`minecraft:recipe_shaped`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 含`identifier`的描述对象。 |
| `tags` | 字符串数组 | 未设置 | 合成标签。 |
| `pattern` | 字符串数组 | 未设置 | 合成图案。每个字符串代表一行，每个字符代表一个槽位。空格表示空槽位。最大3×3。 |
| `key` | 对象 | 未设置 | 图案字符到物品描述符的映射。键区分大小写，空格键不可用，超一字符时仅首字符有效。 |
| `result` | 物品描述符或数组 | 未设置 | 合成输出。数组时首项为可见输出，其余放入背包。 |
| `priority` | 整数 | `0` | 同输入冲突时的优先级。值越小优先级越高，支持负值。 |
| `assume_symmetry` | 布尔值 | `true` | 是否将水平镜像图案视为同一配方。设为`false`时可分别定义镜像形状。 |
| `group` | 字符串 | 未设置 | 配方分组标识。当前效果未知。 |
| `unlock` | 数组 | 未设置 | 解锁条件数组。 |

图案字符串自动补全至同行最长长度（用空格填充），图案可在比网格更小时自由移动。

## 无序配方字段

根对象键：`minecraft:recipe_shapeless`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 含`identifier`的描述对象。 |
| `tags` | 字符串数组 | 未设置 | 合成标签。 |
| `ingredients` | 数组 | 未设置 | 原料物品描述符数组。 |
| `result` | 物品描述符或数组 | 未设置 | 合成输出。 |
| `priority` | 整数 | `0` | 同输入冲突时的优先级。 |
| `group` | 字符串 | 未设置 | 配方分组标识。 |
| `unlock` | 数组 | 未设置 | 解锁条件数组。 |

无序配方的`ingredients`若设置了`count`，需要多个合成网格槽位分别放置（单槽堆叠无效）。

## 烧炼配方字段

根对象键：`minecraft:recipe_furnace`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 含`identifier`的描述对象。 |
| `tags` | 字符串数组 | 未设置 | 热源标签。 |
| `input` | 物品描述符 | 未设置 | 输入物品。`count`被忽略。 |
| `output` | 物品描述符 | 未设置 | 输出物品。 |

加热时间和经验返还由热源方块决定，配方无法修改。

## 酿造混合配方字段

根对象键：`minecraft:recipe_brewing_mix`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 含`identifier`的描述对象。 |
| `tags` | 字符串数组 | 未设置 | 应为`["brewing_stand"]`。 |
| `input` | 物品描述符 | 未设置 | 输入物品。指定数据值时对非药水物品通常失效。 |
| `reagent` | 物品描述符 | 未设置 | 催化剂物品。指定数据值时无论是否匹配均触发酿造，但仅匹配时转换成功。 |
| `output` | 物品描述符 | 未设置 | 输出物品。数量被忽略，每次转换一个。 |

/// warning | 注意
若`input`为可堆叠物品，将消耗整个堆叠，目前无法规避。酿造完成后催化剂被消耗，输出直接替换输入。
///

## 酿造容器配方字段

根对象键：`minecraft:recipe_brewing_container`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 含`identifier`的描述对象。 |
| `tags` | 字符串数组 | 未设置 | 应为`["brewing_stand"]`。 |
| `input` | 物品描述符 | 未设置 | 输入物品。仅支持`minecraft:potion`、`minecraft:splash_potion`、`minecraft:lingering_potion`或药水特殊标识符。 |
| `reagent` | 物品描述符 | 未设置 | 催化剂物品。 |
| `output` | 物品描述符 | 未设置 | 输出物品。数据值从输入传递到输出，`input`与`output`中指定的数据值被忽略。 |

## 锻造转化配方字段

根对象键：`minecraft:recipe_smithing_transform`（需`format_version` ≥ `1.20.0`）

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 含`identifier`的描述对象。 |
| `tags` | 字符串数组 | 未设置 | 应为`["smithing_table"]`。 |
| `template` | 物品描述符 | 未设置 | 模板物品。 |
| `base` | 物品描述符 | 未设置 | 基底物品。结果继承基底物品的属性（如附魔）。 |
| `addition` | 物品描述符 | 未设置 | 附加材料。 |
| `result` | 物品描述符 | 未设置 | 输出物品。 |

## 锻造盔甲纹饰配方字段

根对象键：`minecraft:recipe_smithing_trim`（需`format_version` ≥ `1.20.0`）

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 含`identifier`的描述对象。 |
| `tags` | 字符串数组 | 未设置 | 应为`["smithing_table"]`。 |
| `template` | 物品描述符 | 未设置 | 纹饰模板物品。 |
| `base` | 物品描述符 | 未设置 | 可修饰盔甲。支持物品标签匹配。 |
| `addition` | 物品描述符 | 未设置 | 纹饰材料。支持物品标签匹配。 |

## 覆盖与优先级

- 行为包以路径和内容匹配覆盖（配方标识符和类型均需一致）；不同类型间不能覆盖，强行操作通常新建配方而不是覆盖。
- 多配方匹配同一输入时，优先顺序为：包列表更靠前的包 > `priority`值更小的 > 有序配方优于无序配方 > 字典序更小的标识符。
