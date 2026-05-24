# 方块标签

方块标签是附加到方块上的字符串标记，可用于在方块描述符、物品组件和Molang查询中按类别批量匹配方块，也可直接启用部分原版交互逻辑。

## 添加标签

### `1.26.20`及以上格式版本

自`1.26.20`起，方块标签应写入`minecraft:tags`组件。根据Microsoft Learn的`1.26.20`更新说明，旧式直接写在`components`下的`tag:`键在这一格式版本起不再是推荐写法。

```json title="BP/blocks/my_ore.json > components"
"minecraft:tags": [
    "minecraft:is_pickaxe_item_destructible",
    "wiki:custom_ore",
    "wiki:mineable_with_diamond"
]
```

标签值必须使用`命名空间:标签名`格式。

### 旧式写法

较低格式版本的历史工程仍可能使用`tag:`前缀：

```json title="BP/blocks/my_ore.json > components"
"tag:minecraft:is_pickaxe_item_destructible": {},
"tag:wiki:custom_ore": {},
"tag:wiki:mineable_with_diamond": {}
```

维护旧包时，这种写法仍常用于识别历史资料；但新写法应优先采用`minecraft:tags`组件。

## 查询方块标签

### 在方块描述符中查询

方块描述符的`tags`字段可用`q.all_tags`与`q.any_tag`表达式匹配标签：

```json title="方块描述符"
{
    "tags": "q.any_tag('wiki:glowing') && q.all_tags('wiki:custom_ore', 'minecraft:stone')"
}
```

/// define
`q.any_tag(...tags)`

- 当前方块是否拥有列出的任意一个标签。

`q.all_tags(...tags)`

- 当前方块是否同时拥有列出的全部标签。
///

### 在实体Molang中查询

在实体客户端定义、动画控制器等位置，可以查询绝对坐标或相对坐标处的方块标签：

```molang
q.relative_block_has_any_tag(0, -1, 0, 'minecraft:crop', 'minecraft:wood')
```

```molang
q.block_has_all_tags(v.target_x, v.target_y, v.target_z, 'minecraft:stone')
```

Microsoft Learn当前仍记录以下查询函数：

/// define
`q.block_has_any_tag(x, y, z, ...tags)`

- 检查指定坐标处方块是否拥有任意一个标签。

`q.block_has_all_tags(x, y, z, ...tags)`

- 检查指定坐标处方块是否拥有全部标签。

`q.relative_block_has_any_tag(x, y, z, ...tags)`

- 检查相对实体偏移位置的方块是否拥有任意一个标签。

`q.relative_block_has_all_tags(x, y, z, ...tags)`

- 检查相对实体偏移位置的方块是否拥有全部标签。
///

### 在物品挖掘组件中查询

物品的`minecraft:digger`组件可以根据方块标签定义挖掘速度和适合性：

```json title="BP/items/diamond_pickaxe.json（示意）"
"minecraft:digger": {
    "use_efficiency": true,
    "destroy_speeds": [
        {
            "block": {
                "tags": "q.any_tag('minecraft:is_pickaxe_item_destructible', 'wiki:custom_ore')"
            },
            "speed": 8.0
        }
    ]
}
```

## 原版常用标签

原版游戏预定义了大量方块标签。根据最新版Bedrock Wiki标签表与Microsoft Learn当前查询文档，以下几类最常用于附加包：

| 标签 | 作用 |
|------|------|
| `minecraft:crop` | 允许带有`minecraft:grows_crops`组件的实体对其授粉或促进生长。 |
| `minecraft:is_axe_item_destructible` | 使带有斧类标签的物品按原版逻辑更快破坏此方块。 |
| `minecraft:is_pickaxe_item_destructible` | 使带有镐类标签的物品按原版逻辑更快破坏此方块。 |
| `wood` | 用于木质方块的通用分类，常与破坏、合成和过滤逻辑一起出现。 |
| `stone` | 用于石质方块的通用分类，可在描述符和过滤表达式中复用。 |

完整的原版方块标签列表见[参考表](../../../refs/tables/blocks/vanilla_tags.md)。

## 兼容提示

- Bedrock Wiki当前仍使用旧式`tag:`示例，是因为该写法便于解释历史工程。
- Microsoft Learn的`1.26.20`更新说明已明确：面向较新方块格式版本时，应改用`minecraft:tags`数组写法。
- 旧资料中部分“按工具品质”标签已经被标为弃用。若遇到这类标签，应优先查阅当前原版标签表，而不要只照抄旧教程中的名字。