# 分数比较

本页讲三类高频玩法：最高分、最低分、分数匹配。

## 最高分模板

```mcfunction title="BP/functions/wiki/scoreboard/players/get_highest_score.mcfunction"
scoreboard players operation .Highest <objective> > * <objective>
execute as <target> if score @s <objective> = .Highest <objective> run <command>
```

示例：给击杀最高玩家打标签。

```mcfunction title="BP/functions/wiki/scoreboard/players/get_highest_score/kills.mcfunction"
scoreboard players operation .Highest wiki:kills > * wiki:kills
tag @a remove wiki:top_kills
execute as @a if score @s wiki:kills = .Highest wiki:kills run tag @s add wiki:top_kills
```

## 最低分模板

```mcfunction title="BP/functions/wiki/scoreboard/players/get_lowest_score.mcfunction"
scoreboard players operation .Lowest <objective> < * <objective>
execute as <target> if score @s <objective> = .Lowest <objective> run <command>
```

## 分数匹配模板

```mcfunction title="BP/functions/wiki/scoreboard/players/get_matching_score.mcfunction"
execute as @a at @s at @a[rm=0.01] if score @s <objective> = @p <objective> run say @s和@p分数相同
```

在这类命令里，`@s`通常是“被检查方”，`@p`或`@e[c=1]`是“对比方”。

## 典型场景

```mcfunction title="BP/functions/wiki/scoreboard/players/get_matching_score/pet.mcfunction"
# 宠物按id跟随主人
execute as @e[tag=pet] at @s at @a[rm=7] if score @s wiki:id = @p wiki:id run tp @s @p

# 领地所有者创意，其他玩家冒险
execute as @e[tag=plot] at @s at @a[r=16] if score @s wiki:id = @p wiki:id run gamemode c @p[m=!c]
execute as @e[tag=plot] at @s at @a[r=16] unless score @s wiki:id = @p wiki:id run gamemode a @p[m=!a]
```

/// tip | 关于`*`
`*`会包含离线玩家分数。仅比较在线目标时，请改用`@a`或`@e`。
///

## 继续阅读

- [记分板运算](./scoreboard-operations.md)
- [记分板计时器](./scoreboard-timers.md)
