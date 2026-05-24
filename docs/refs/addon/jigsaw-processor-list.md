# 处理器列表

本页列出国际版行为包拼图结构处理器列表定义。处理器列表用于在结构模板放置过程中按顺序检查并替换方块，或保护方块不被替换。

/// warning | 自动导出差异
JigsawReference不同子页面对`minecraft:protected_blocks`和`minecraft:capped`等处理器的字段类型存在差异。以下内容保留可确认字段，并对冲突字段给出并行记录。
///

## 文件位置

处理器列表定义通常放置于行为包`worldgen/processor_lists/`目录。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 处理器列表定义格式版本。 |
| `minecraft:processor_list` | 对象 | 未设置 | 处理器列表定义主体。 |

## `minecraft:processor_list`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 处理器列表标识信息。 |
| `processors` | 对象数组 | 未设置 | 按顺序执行的处理器配置。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 处理器列表赋命名空间标识符。模板池可引用该值。 |

## `processors`条目

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `processor_type` | 字符串 | 未设置 | 处理器类型。 |
| `rules` | 对象数组 | 未设置 | `minecraft:rule`处理器使用的规则列表。 |
| `blocks` | 字符串数组 | 未设置 | `minecraft:block_ignore`等处理器使用的方块列表。 |
| `delegate` | 对象 | 未设置 | `minecraft:capped`委托执行的处理器。 |
| `limit` | 整数或对象 | 未设置 | `minecraft:capped`的执行次数上限。 |
| `value` | 字符串 | 未设置 | `minecraft:protected_blocks`可使用的方块标签值。 |

`processor_type`支持下列值：

- `minecraft:rule`
- `minecraft:block_ignore`
- `minecraft:block_rot`
- `minecraft:protected_blocks`
- `minecraft:capped`
- `minecraft:gravity`
- `minecraft:jigsaw_replacement`
- `minecraft:blackstone_replace`
- `minecraft:nop`

/// note | 可确认范围
仅提供了`minecraft:rule`、`minecraft:block_ignore`、`minecraft:protected_blocks`和`minecraft:capped`的字段细节。其余类型在本批次缺少字段说明。
///

## `minecraft:rule`规则对象

`rules`数组中的每一项为一条方块处理规则。规则按顺序执行；当前规则成功并写入`output_state`后，后续规则将以更新后的方块状态继续匹配。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `input_predicate` | 对象 | 未设置 | 作用于结构模板输入方块的谓词。 |
| `location_predicate` | 对象 | 未设置 | 作用于世界目标方块位置的谓词。 |
| `position_predicate` | 对象 | 未设置 | 作用于结构原点与目标方块距离关系的谓词。 |
| `output_state` | 对象 | 未设置 | 规则成功时写入的输出方块状态。 |
| `block_entity_modifier` | 对象 | 未设置 | 规则成功时应用的方块实体修改器。 |

### 谓词对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `predicate_type` | 字符串 | 未设置 | 谓词类型。 |
| `block` | 字符串 | 未设置 | 方块匹配类谓词要匹配的方块标识符。 |
| `tag` | 字符串 | 未设置 | 标签匹配谓词要匹配的方块标签。 |
| `probability` | 十进制数 | 未设置 | 随机匹配谓词命中概率。 |
| `axis` | 字符串 | 未设置 | 轴向线性谓词的测量轴。 |
| `min_dist` | 整数 | 未设置 | 轴向线性谓词最小距离。 |
| `max_dist` | 整数 | 未设置 | 轴向线性谓词最大距离。 |
| `min_chance` | 十进制数 | 未设置 | 轴向线性谓词最小概率。 |
| `max_chance` | 十进制数 | 未设置 | 轴向线性谓词最大概率。 |

可确认的`predicate_type`包括：

- `minecraft:always_true`
- `minecraft:block_match`
- `minecraft:random_block_match`
- `minecraft:tag_match`
- `minecraft:axis_aligned_linear_pos`

### `output_state`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `name` | 字符串 | 未设置 | 输出方块标识符。 |
| `states` | 对象 | 未设置 | 输出方块状态键值映射。 |

### `block_entity_modifier`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `type` | 字符串 | 未设置 | 方块实体修改器类型。 |
| `loot_table` | 字符串 | 未设置 | `minecraft:append_loot`使用的战利品表路径。 |

`type`支持下列值：

- `minecraft:append_loot`
- `minecraft:passthrough`
- `minecraft:clear`