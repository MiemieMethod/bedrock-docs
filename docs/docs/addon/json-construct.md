# JSON共用构件

**JSON共用构件（JSON Shared Construct）**是附加包系统中可复用的、跨多处系统通用的标准化JSON结构体。这些构件不以独立文件的形式存在，而是内嵌于各类定义文件的特定字段中，用于简洁地描述方块、物品或数值范围等通用概念。

## 方块描述符

**方块描述符（Block Descriptor）**用于匹配满足指定条件的方块。方块描述符常见于方块[放置过滤器](../../refs/addon/block-component.md)等需要鉴定方块类型的场合。

方块描述符有三种形式，可在同一接受位置交替使用。

### 方块类型描述符

按赋命名空间标识符匹配单一方块类型：

```json
{
    "name": "wiki:custom_block"
}
```

### 方块置换描述符

按赋命名空间标识符与方块状态组合匹配特定方块置换：

```json
{
    "name": "wiki:custom_block",
    "states": {
        "wiki:custom_state": 5
    }
}
```

### 方块标签描述符

通过Molang标签查询函数匹配带有指定标签的方块。该形式仅支持`q.all_tags()`和`q.any_tag()`两个查询函数：

```json
{
    "tags": "q.any_tag('minecraft:is_axe_item_destructible', 'wiki:custom_tag')"
}
```

## 物品描述符

**物品描述符（Item Descriptor）**用于匹配满足指定条件的物品。物品描述符常见于物品可修复组件等需要鉴定物品类型的场合。

物品描述符有两种形式，可在同一接受位置交替使用。

### 物品类型描述符

按赋命名空间标识符匹配单一物品类型：

```json
{
    "name": "wiki:custom_item"
}
```

### 物品标签描述符

通过Molang标签查询函数匹配带有指定标签的物品。该形式仅支持`q.all_tags()`和`q.any_tag()`两个查询函数：

```json
{
    "tags": "q.any_tag('minecraft:is_axe', 'wiki:custom_tag')"
}
```

## 范围对象

**范围对象（Range Object）**以最小值与最大值定义一个数值区间，供所在字段随机取值：

```json
{
    "min": 2,
    "max": 4
}
```

范围对象在每次被引用时独立随机取值，取值结果在闭合区间`[min, max]`内均匀分布。最大值不可小于最小值，但两者相等时等效于固定常量。范围对象广泛用于战利品表的数量字段、生成规则的高度字段等需要随机化数值的场合。

## 分数对象

**分数对象（Fraction Object）**以分子与分母的形式表达分数，其计算结果（分子 ÷ 分母）将代入所在字段参与逻辑：

```json
{
    "numerator": 3,
    "denominator": 5
}
```

分子与分母均须至少为`1`，且分母不可等于分子（即分数值不可为`1`）。分数对象常见于生成规则、概率相关组件等以概率值驱动逻辑的场合。

## 相关页面

- [方块](../general/block.md)
- [物品](../general/item.md)
- [战利品表](loot-table.md)
- [生成规则](spawn-rule.md)
