# 方块标签

方块标签是附加到方块上的字符串标记，可用于在命令、战利品表、配方和Molang查询中按类别批量引用方块。

## 添加标签

在方块JSON的 `components` 中，使用 `tag:` 前缀添加标签：

```json title="BP/blocks/my_ore.json > components"
"tag:minecraft:is_pickaxe_item_tier_4": {},
"tag:wiki:custom_ore": {},
"tag:wiki:mineable_with_diamond": {}
```

每个标签组件是一个空对象，标签标识符即为键名的 `tag:` 后面的部分。

## 查询方块标签

### 在Molang中查询

在Molang表达式（如置换条件、动画等）中，可以查询方块是否具有某个标签：

```molang
q.any_tag('wiki:custom_ore', 'wiki:mineable_with_diamond')
```

```molang
q.all_tags('minecraft:is_pickaxe_item_tier_4', 'wiki:custom_ore')
```

- `q.any_tag(...)` — 方块拥有其中**任意一个**标签时为真
- `q.all_tags(...)` — 方块拥有**所有**列出的标签时为真

### 在物品挖掘组件中查询

物品的 `minecraft:digger` 组件可以根据方块标签定义挖掘速度和适合性：

```json title="BP/items/diamond_pickaxe.json（示意）"
"minecraft:digger": {
    "use_efficiency": true,
    "destroy_speeds": [
        {
            "block": {
                "tags": "q.any_tag('minecraft:stone', 'wiki:custom_ore')"
            },
            "speed": 8.0
        }
    ]
}
```

### 在实体Molang中查询

实体的Molang可以通过 `q.relative_block_has_any_tag` 查询相邻方块的标签：

```molang
q.relative_block_has_any_tag(0, -1, 0, 'minecraft:dirt', 'minecraft:sand')
```

参数含义：`(x偏移, y偏移, z偏移, 标签列表...)`。

## 原版常用标签

原版游戏预定义了大量方块标签，可以直接在自定义方块中使用以获得相应行为：

| 标签 | 作用 |
|------|------|
| `minecraft:crop` | 标记为农作物，可被特定物品收割 |
| `minecraft:wood` | 标记为木材，影响斧的挖掘加速 |
| `minecraft:stone` | 标记为石头，影响镐的挖掘加速 |
| `minecraft:dirt` | 标记为泥土类方块 |

完整的原版方块标签列表见[参考表](../../../refs/tables/blocks/vanilla_tags.md)。

## 用tags组件（1.26.20+）<!-- md:flag experimental -->

从格式版本 `1.26.20` 起（需启用"即将推出的创作者功能"实验性开关），可以使用 `minecraft:tags` 组件集中声明多个标签：

```json title="BP/blocks/my_block.json > components"
"minecraft:tags": {
    "tags": [
        "wiki:custom_ore",
        "wiki:mineable_with_diamond",
        "minecraft:is_pickaxe_item_tier_4"
    ]
}
```

这与分别写 `"tag:wiki:custom_ore": {}` 等价，只是写法更集中。
