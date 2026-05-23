# 模板池

本页列出国际版行为包拼图结构模板池定义。模板池用于向拼图结构提供可选结构模板及其权重，并为模板绑定处理器列表。

## 文件位置

模板池定义通常放置于行为包`worldgen/template_pools/`目录。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 模板池定义格式版本。 |
| `minecraft:template_pool` | 对象 | 未设置 | 模板池定义主体。 |

## `minecraft:template_pool`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 模板池标识信息。 |
| `elements` | 对象数组 | 未设置 | 候选池元素列表。 |
| `fallback` | 字符串 | 未设置 | 可选兜底模板池标识符。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 模板池赋命名空间标识符。 |

### `elements`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `element` | 对象 | 未设置 | 池元素定义。 |
| `weight` | 整数 | `1` | 当前元素被抽中的相对权重。 |

## 池元素对象

`elements[].element`用于指定结构模板、处理器和投影方式。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `element_type` | 字符串 | 未设置 | 池元素类型。 |
| `location` | 字符串 | 未设置 | 结构模板路径，相对于行为包`structures/`目录。 |
| `processors` | 字符串或对象 | 未设置 | 处理器列表标识符，或内联处理器配置。 |
| `projection` | 字符串 | `rigid` | 结构相对地形的投影方式。 |

`element_type`支持下列值：

- `minecraft:single_pool_element`
- `minecraft:list_pool_element`
- `minecraft:feature_pool_element`
- `minecraft:empty_pool_element`
- `minecraft:legacy_single_pool_element`

`projection`支持下列值：

- `rigid`
- `terrain_matching`

## 字段关系说明

- `elements[].weight`控制元素抽样概率，权重越大越容易被选中。
- `elements[].element.processors`可引用[处理器列表](jigsaw-processor-list.md)中的`description.identifier`。
- `fallback`通常用于当当前模板池无法放置任何元素时继续尝试其他模板池。
