# 多人位置错排

这套函数会把多名目标随机互换位置，并保证没人留在原位。数学上它属于“错排（Derangement）”。

## 方法概览

1. 给每个目标分配唯一`wiki:id`。
2. 用盔甲架记录原始位置。
3. 逐轮分配新位置，已分配目标打标记。
4. 若最后出现碰撞，执行一次冲突解法。

## ID分配

```mcfunction title="BP/functions/wiki/scoreboard/players/id.mcfunction"
scoreboard players add @a wiki:id 0
execute if entity @a[scores={wiki:id=0}] run scoreboard players add .Total wiki:id 1
scoreboard players operation @r[scores={wiki:id=0}] wiki:id = .Total wiki:id
```

## 发起错排

```mcfunction title="BP/functions/wiki/derange_position/initiate.mcfunction"
execute at @a run summon armor_stand "wiki:position_marker" ~~~
execute as @a at @s run scoreboard players operation @e[type=armor_stand,name="wiki:position_marker",r=0.01,c=1] wiki:id = @s wiki:id

function wiki/derange_position/process

execute if score .Players.NotAllocated wiki:count matches 1 unless score @a[tag=!wiki:pos.allocated,c=1] wiki:id = @e[type=armor_stand,name="wiki:position_marker",c=1] wiki:id run function wiki/derange_position/process

execute as @a[tag=!wiki:pos.allocated] at @s run tp @r[tag=wiki:pos.allocated,r=0.01] @e[type=armor_stand,name="wiki:position_marker",c=1]
kill @e[type=armor_stand,name="wiki:position_marker"]
tag @a[tag=wiki:pos.allocated] remove wiki:pos.allocated
```

## 处理轮询

```mcfunction title="BP/functions/wiki/derange_position/process.mcfunction"
execute as @a[tag=!wiki:pos.allocated] at @s run function wiki/derange_position/teleport
execute as @a[tag=!wiki:pos.allocated] at @s if score @s wiki:id = @e[type=armor_stand,name="wiki:position_marker",r=0.01,c=1] wiki:id run function wiki/derange_position/teleport

execute as @e[type=armor_stand,name="wiki:position_marker"] at @s run tag @a[tag=!wiki:pos.allocated,r=0.01,c=1] add wiki:pos.allocated
execute as @a[tag=wiki:pos.allocated] at @s run kill @e[type=armor_stand,name="wiki:position_marker",r=0.01,c=1]

scoreboard players set .Players.NotAllocated wiki:count 0
execute as @a[tag=!wiki:pos.allocated] run scoreboard players add .Players.NotAllocated wiki:count 1
execute if score .Players.NotAllocated wiki:count matches 2.. run function wiki/derange_position/process
```

## 跨维度传送子函数

```mcfunction title="BP/functions/wiki/derange_position/teleport.mcfunction"
tag @e[type=armor_stand,name="wiki:position_marker",r=0.01] add wiki:pos.ignored
tp @s @r[type=armor_stand,name="wiki:position_marker",tag=!wiki:pos.ignored]
tag @e remove wiki:pos.ignored
```

## 初始化与调用

```mcfunction title="BP/functions/wiki/scoreboard/objectives/add_all.mcfunction"
scoreboard objectives add wiki:id dummy
scoreboard objectives add wiki:count dummy
```

```mcfunction title="运行入口"
function wiki/derange_position/initiate
```

## 目录示例

/// html | div.treeview
- `BP/functions/wiki/derange_position`
    - `initiate.mcfunction`
    - `process.mcfunction`
    - `teleport.mcfunction`
- `BP/functions/wiki/scoreboard/players/id.mcfunction`
- `BP/functions/tick.json`
///

## 继续阅读

- [实体计数器](./entity-counter.md)
- [分数比较](./comparing-scores.md)