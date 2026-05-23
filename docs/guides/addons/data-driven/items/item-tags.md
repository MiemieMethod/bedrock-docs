# 物品标签

物品标签（item tag）是附加在物品上的字符串标记，用于在过滤器、配方、Molang查询等场景中批量匹配一类物品。基岩版内置了若干原版标签，同时允许附加包定义自定义标签。

## 添加标签

通过`minecraft:tags`组件为物品添加一个或多个标签：

```json title="BP/items/my_item.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:my_item"
        },
        "components": {
            "minecraft:tags": {
                "tags": [
                    "wiki:my_custom_tag",
                    "minecraft:is_food"
                ]
            }
        }
    }
}
```

自定义标签建议使用命名空间前缀（如`wiki:`）避免与原版标签冲突。

## 使用标签过滤

### 实体过滤器

在实体的行为文件中，通过`has_equipment_tag`过滤器检测指定槽位是否有带有特定标签的物品：

```json title="实体过滤器"
{
    "test": "has_equipment_tag",
    "domain": "hand",
    "operator": "==",
    "value": "wiki:my_custom_tag"
}
```

### 实体Molang查询

在实体客户端定义或动画控制器中，通过以下查询函数检测装备标签：

/// define
`q.equipped_item_all_tags(slot, ...tags)`

- 返回指定槽位的物品是否**同时拥有**所有列出的标签。

`q.equipped_item_any_tag(slot, ...tags)`

- 返回指定槽位的物品是否**至少拥有**一个列出的标签。
///

```json title="客户端实体描述 > scripts > pre_animation"
"v.is_holding_pickaxe = q.equipped_item_all_tags('slot.weapon.mainhand', 'minecraft:is_tool', 'minecraft:is_pickaxe');"
```

### 物品描述符

在配方或战利品表等需要物品描述符的地方，通过`tags`字段使用Molang来匹配具有标签的物品：

```json title="物品描述符"
{
    "tags": "q.all_tags('minecraft:is_tool', 'minecraft:is_pickaxe') && q.any_tag('minecraft:diamond_tier', 'minecraft:netherite_tier')"
}
```

/// define
`q.all_tags(...tags)`

- 当前物品是否**同时拥有**所有列出的标签。

`q.any_tag(...tags)`

- 当前物品是否**至少拥有**一个列出的标签。
///

### 配方原料

在配方文件的`ingredients`中，通过标签匹配一类原料，而不必写死某种具体物品：

```json title="minecraft:recipe_shapeless"
"ingredients": [
    {
        "item": { "tag": "minecraft:planks" }
    }
]
```

## 常用原版标签

以下是一些常见的原版物品标签及其功能：

| 标签 | 说明 |
|------|------|
| `minecraft:is_food` | 标记为食物，影响某些AI意向 |
| `minecraft:is_meat` | 标记为肉类食物 |
| `minecraft:is_fish` | 标记为鱼类食物 |
| `minecraft:is_cooked` | 标记为熟食 |
| `minecraft:is_tool` | 标记为工具 |
| `minecraft:is_pickaxe` | 具有镐的功能（配合`on_tool_used`） |
| `minecraft:is_axe` | 具有斧的功能（可去除木头表皮） |
| `minecraft:is_hoe` | 具有锄的功能（可耕地） |
| `minecraft:is_sword` | 具有剑的特性 |
| `minecraft:is_armor` | 标记为盔甲 |
| `minecraft:diamond_tier` | 钻石品质 |
| `minecraft:netherite_tier` | 下界合金品质 |
| `minecraft:iron_tier` | 铁品质 |
| `minecraft:gold_tier` | 金品质 |
| `minecraft:planks` | 各种木板 |
| `minecraft:decorated_pot_sherds` | 可用于陶罐合成的陶片 |

完整的原版标签列表及其适用物品，参见[原版物品标签](../../../../refs/tables/items/vanilla_tags.md)。