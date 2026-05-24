# 物品标签

物品标签是附加在物品上的字符串标记，用于在过滤器、配方、Molang查询等场景中批量匹配一类物品。基岩版内置了一批原版标签，同时允许附加包定义自定义标签。

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

自定义标签建议使用命名空间前缀（如`wiki:`）避免与原版标签冲突。根据Microsoft Learn当前物品标签参考，只有原版内置标签可以使用`minecraft:`命名空间。

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

以下是一些常见的原版物品标签及其功能。表中名称已按Microsoft Learn当前“Vanilla Item Tags”页校正：

| 标签 | 说明 |
|------|------|
| `minecraft:is_food` | 标记为食物。 |
| `minecraft:is_meat` | 标记为肉类食物。 |
| `minecraft:is_fish` | 标记为鱼类物品。 |
| `minecraft:is_cooked` | 标记为熟食。 |
| `minecraft:is_tool` | 标记为工具总类。 |
| `minecraft:is_pickaxe` | 标记为镐类工具。 |
| `minecraft:is_axe` | 标记为斧类工具。 |
| `minecraft:is_hoe` | 标记为锄类工具。 |
| `minecraft:is_sword` | 标记为剑类武器。 |
| `minecraft:is_armor` | 标记为盔甲。 |
| `minecraft:copper_tier` | 铜品质。 |
| `minecraft:diamond_tier` | 钻石品质。 |
| `minecraft:golden_tier` | 金品质。 |
| `minecraft:iron_tier` | 铁品质。 |
| `minecraft:netherite_tier` | 下界合金品质。 |
| `minecraft:planks` | 各种木板。 |
| `minecraft:decorated_pot_sherds` | 可用于饰纹陶罐配方的陶片。 |
| `minecraft:spawn_egg` | 刷怪蛋总类。 |

完整的原版标签列表及其适用物品，参见[原版物品标签](../../../../refs/tables/items/vanilla_tags.md)。

## 最新确认

- `q.equipped_item_any_tag`与`q.equipped_item_all_tags`仍在Microsoft Learn的最新版Molang查询文档中保留。
- `minecraft:tags`仍是Microsoft Learn当前物品组件参考中的正式组件。
- 原版标签表已经包含`minecraft:copper_tier`、`minecraft:golden_tier`等较新的标签名称；编写教程时不应继续使用`minecraft:gold_tier`这类过时写法。