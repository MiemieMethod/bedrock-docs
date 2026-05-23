# 发放NBT物品

这页整理命令侧可直接写入的物品组件。当前常用的是：

1. `minecraft:can_place_on`
2. `minecraft:can_destroy`
3. `minecraft:keep_on_death`
4. `minecraft:item_lock`

## can_place_on与can_destroy

这两项主要影响冒险模式。

```mcfunction title="BP/functions/wiki/nbt/can_place_destroy.mcfunction"
# 只能放在木板上
/give @p cobblestone 1 0 {"minecraft:can_place_on":{"blocks":["planks"]}}

# 只能破坏木板和木头
/give @p diamond_axe 1 0 {"minecraft:can_destroy":{"blocks":["planks","wood"]}}
```

/// warning | 已知行为
带`can_place_on`的方块被放下并再次拾回后，通常不会保留该组件。
///

## item_lock

`lock_in_inventory`禁止丢弃与移动，`lock_in_slot`还会强制槽位锁定。

```mcfunction title="BP/functions/wiki/nbt/item_lock.mcfunction"
# 背包锁
/give @p diamond_axe 1 0 {"minecraft:item_lock":{"mode":"lock_in_inventory"}}

# 槽位锁
/give @p wooden_pickaxe 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
/replaceitem entity @p slot.hotbar 0 iron_shovel 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
```

## keep_on_death

```mcfunction title="BP/functions/wiki/nbt/keep_on_death.mcfunction"
/replaceitem entity @e[type=zombie] slot.weapon.mainhand 0 cooked_beef 1 0 {"minecraft:keep_on_death":{}}
```

对玩家来说，它相当于“仅指定物品保留”，比全局保留背包更细粒度。

## 组件组合示例

```mcfunction title="BP/functions/wiki/nbt/combined.mcfunction"
/give @a oak_planks 64 0 {"minecraft:can_place_on":{"blocks":["dirt","grass","cobblestone"]},"minecraft:item_lock":{"mode":"lock_in_inventory"}}
/give @a bow 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"},"minecraft:keep_on_death":{}}
/give @s stone_shovel 1 0 {"minecraft:can_destroy":{"blocks":["dirt","sand"]},"minecraft:item_lock":{"mode":"lock_in_inventory"}}
```

## 用structure发放预制NBT物品

```mcfunction title="BP/functions/wiki/nbt/structure_item.mcfunction"
# 保存
execute at @e[type=item,c=1] run structure save wiki:nbt_item ~~~ ~~~ true disk false
# 发放(生成到玩家脚下)
execute at @p run structure load wiki:nbt_item ~~~
```

## 用loot发放带内容潜影盒

```mcfunction title="BP/functions/wiki/nbt/loot_shulker.mcfunction"
loot give @p mine <xyz:source>
loot replace entity @p slot.hotbar 0 mine <xyz:source>
loot replace block <xyz:target> slot.container 0 mine <xyz:source>
```

## 当前限制

- 交易表/战利品表中不能直接写入这些NBT组件。
- 某些“带数据值方块”会触发`could not be updated`错误。

## 继续阅读

- [记分板运算](./scoreboard-operations.md)
- [自定义合成器](./custom-crafting.md)
