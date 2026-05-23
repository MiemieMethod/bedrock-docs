# 移动状态检测

这页把常见的玩家状态检测整理到一起：睡觉、潜行、爬行，以及进阶的滑翔/游泳区分。

/// warning | 适用边界
纯命令检测依赖碰撞箱与环境条件，稳定性不如动画控制器。高精度需求建议优先使用动画控制器方案。
///

## 睡觉检测

睡觉时玩家高度会降到约0.2方块。

```mcfunction title="BP/functions/wiki/detect/player/is_sleeping.mcfunction"
execute as @a at @s if entity @s[y=~0.3,dy=0] run scoreboard players set @s wiki:q.is_sleeping 0
execute as @a at @s unless entity @s[y=~0.3,dy=0] run scoreboard players add @s wiki:q.is_sleeping 1

execute as @a[scores={wiki:q.is_sleeping=1}] run say 刚开始睡觉
execute as @a[scores={wiki:q.is_sleeping=1..}] run say 仍在睡觉
```

## 潜行检测

1.20.10后短潜行趋同让纯命令潜行检测更可靠。

```mcfunction title="BP/functions/wiki/detect/player/is_sneaking.mcfunction"
execute as @a at @s if entity @s[y=~1.5,dy=0] run scoreboard players set @s wiki:q.is_sneaking 0
execute as @a at @s unless entity @s[y=~1.5,dy=0] if entity @s[y=~0.7,dy=0] run scoreboard players add @s wiki:q.is_sneaking 1
```

## 爬行检测

```mcfunction title="BP/functions/wiki/detect/player/is_crawling.mcfunction"
execute as @a at @s if entity @s[y=~0.7,dy=0] run scoreboard players set @s wiki:q.is_crawling 0
execute as @a at @s unless entity @s[y=~0.7,dy=0] if entity @s[y=~0.3,dy=0] run scoreboard players add @s wiki:q.is_crawling 1
```

/// warning | 已知问题
单独做爬行检测时，游泳和鞘翅滑翔可能被误判为爬行。
///

## 区分滑翔、爬行、游泳

```mcfunction title="BP/functions/wiki/detect/player/is_crawling.advanced.mcfunction"
# 重置状态
execute as @a at @s if entity @s[y=~0.7,dy=0] run scoreboard players set @s wiki:q.is_gliding 0
execute as @a at @s if entity @s[y=~0.7,dy=0] run scoreboard players set @s wiki:q.is_crawling 0
execute as @a at @s if entity @s[y=~0.7,dy=0] run scoreboard players set @s wiki:q.is_swimming 0

# 滑翔
execute as @a[hasitem={item=elytra,location=slot.armor.chest}] at @s unless entity @s[y=~0.7,dy=0] if entity @s[y=~0.3,dy=0] run scoreboard players add @s wiki:q.is_gliding 1

# 爬行
execute as @a[scores={wiki:q.is_gliding=0}] at @s unless entity @s[y=~0.7,dy=0] if entity @s[y=~0.3,dy=0] unless block ~~~ water run scoreboard players add @s wiki:q.is_crawling 1

# 游泳
execute as @a[scores={wiki:q.is_gliding=0,wiki:q.is_crawling=0}] at @s unless entity @s[y=~0.7,dy=0] if entity @s[y=~0.3,dy=0] run scoreboard players add @s wiki:q.is_swimming 1
```

## 目录参考

/// html | div.treeview
- `BP/functions/wiki/detect/player`
    - `is_sleeping.mcfunction`
    - `is_sneaking.mcfunction`
    - `is_crawling.mcfunction`
///

/// danger | 已移除
旧版“行走/奔跑检测”依赖拴绳结行为。由于近期版本机制变化，该方案已失效。
///

## 继续阅读

- [注视检测](./detect-looking.md)
- [罗盘显示](./compass-display.md)
