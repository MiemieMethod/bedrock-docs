# 装备物品效果

基岩版没有内置的"装备物品时触发效果"事件，但可以通过两种方式实现：命令轮询和服务端动画。

## 方法一：命令轮询

### 原理

使用`tick.json`让函数每刻运行，配合`/effect`命令的短持续时间（2刻），以刷新的方式维持状态效果；利用`hasitem`选择器参数精确匹配持有/穿戴特定物品的玩家。

### 示例：持有特定物品时给予效果

```mcfunction title="BP/functions/item_effects.mcfunction"
# 主手持有 wiki:magic_wand 时，给予夜视效果（持续2刻）
effect @a[hasitem={item: wiki:magic_wand, slot: slot.weapon.mainhand}] night_vision 2 0 true

# 副手持有时同样匹配
effect @a[hasitem={item: wiki:magic_wand, slot: slot.weapon.offhand}] night_vision 2 0 true

# 穿戴自定义头盔时给予水下呼吸
effect @a[hasitem={item: wiki:diving_helmet, slot: slot.armor.head}] water_breathing 2 0 true
```

```json title="BP/functions/tick.json"
{
    "values": ["item_effects"]
}
```

### 检测数量

`hasitem`还支持`quantity`参数，例如"背包中至少有3件特定物品"：

```mcfunction
effect @a[hasitem={item: wiki:power_gem, quantity: 3..}] strength 2 0 true
```

### 多条件组合

```mcfunction
# 同时穿戴全套才触发（数组写法）
effect @a[
    hasitem=[
        {item: wiki:flame_helmet,     slot: slot.armor.head},
        {item: wiki:flame_chestplate, slot: slot.armor.chest},
        {item: wiki:flame_leggings,   slot: slot.armor.legs},
        {item: wiki:flame_boots,      slot: slot.armor.feet}
    ]
] fire_resistance 2 0 true
```

## 方法二：服务端动画

### 原理

在玩家行为文件（`player.json`）的动画控制器中加入Molang条件，当条件成立时运行`/function`或`/effect`命令——动画控制器中的`on_entry`/`on_exit`以及`timeline`命令只在服务端执行，效果等同于函数。

### 修改玩家行为文件

在`BP/entities/player.json`的`description`节中添加动画控制器引用：

```json title="player.json（description 节，节选）"
"animations": {
    "item_effect_ctrl": "controller.animation.player.item_effects"
},
"scripts": {
    "animate": [
        "item_effect_ctrl"
    ]
}
```

### 创建动画控制器

```json title="BP/animation_controllers/player.item_effects.json"
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.player.item_effects": {
            "initial_state": "no_effect",
            "states": {
                "no_effect": {
                    "transitions": [
                        {
                            "has_wand": "q.equipped_item_all_tags('slot.weapon.mainhand', 'wiki:magic_wand')"
                        }
                    ]
                },
                "has_wand": {
                    "on_entry": ["/effect @s night_vision 300 0 true"],
                    "transitions": [
                        {
                            "no_effect": "!q.equipped_item_all_tags('slot.weapon.mainhand', 'wiki:magic_wand')"
                        }
                    ],
                    "on_exit": ["/effect @s night_vision 0 0 true"]
                }
            }
        }
    }
}
```

`on_entry`中的命令在进入该状态时执行一次（给予较长时间的效果），`on_exit`在离开时执行（清除效果）。这样比每刻刷新开销更小，但效果持续时间需要估算。

### 物品标签匹配

若使用动画控制器方法，建议给物品添加自定义标签，通过`q.equipped_item_all_tags`匹配，避免硬编码物品ID：

```json title="BP/items/magic_wand.json（components）"
"minecraft:tags": {
    "tags": ["wiki:magic_wand"]
}
```

关于标签的更多使用方式，参见[物品标签](item-tags.md)。

## 两种方法对比

| | 命令轮询 | 服务端动画 |
|---|---|---|
| 实现难度 | 低 | 中 |
| 性能 | 每刻执行，玩家多时有影响 | 仅状态变化时执行 |
| 修改玩家文件 | 不需要 | 需要 |
| 效果持续精确度 | 高（持续刷新） | 需预估持续时长 |
| 适用场景 | 简单、快速原型 | 生产环境、复杂条件 |