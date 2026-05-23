# 记分板计时器

你可以把**记分板计时器（Scoreboard Timer）**理解成“可编程时钟”。它很适合函数环境，因为函数没有命令方块的Tick Delay可点。

## 初始化

```mcfunction title="BP/functions/wiki/scoreboard/timers/setup.mcfunction"
scoreboard objectives add wiki:ticks dummy
scoreboard objectives add wiki:events dummy

# 2h=20×60×60×2=144000刻
scoreboard players set .2h wiki:ticks 144000
# 10m=20×60×10=12000刻
scoreboard players set .10m wiki:ticks 12000
# 30s=20×30=600刻
scoreboard players set .30s wiki:ticks 600
```

## 世界同步计时器

```mcfunction title="BP/functions/wiki/scoreboard/world_timer.mcfunction"
# 世界时钟+1刻
scoreboard players add .Timer wiki:ticks 1
# 复制当前刻到所有事件
scoreboard players operation * wiki:events = .Timer wiki:ticks

# 每2小时
scoreboard players operation .ChatMessage wiki:events %= .2h wiki:ticks
execute if score .ChatMessage wiki:events matches 0 run say Technoblade never dies!

# 每10分钟
scoreboard players operation .LagClear wiki:events %= .10m wiki:ticks
execute if score .LagClear wiki:events matches 0 run function clear_lag

# 每30秒
scoreboard players operation .SpeedEffect wiki:events %= .30s wiki:ticks
execute if score .SpeedEffect wiki:events matches 0 run effect @a speed 10 2 true
```

## 限次事件

```mcfunction title="BP/functions/wiki/scoreboard/world_timer_limited.mcfunction"
scoreboard objectives add wiki:occurrences dummy
scoreboard players set .ChatMessage wiki:occurrences 5

execute if score .ChatMessage wiki:events matches 0 if score .ChatMessage wiki:occurrences matches 1.. run say 限次触发
execute if score .ChatMessage wiki:events matches 0 if score .ChatMessage wiki:occurrences matches 1.. run scoreboard players remove .ChatMessage wiki:occurrences 1
```

## 实体异步计时器

```mcfunction title="BP/functions/wiki/scoreboard/players/entity_timer.mcfunction"
# 每个实体独立走表
scoreboard players add @e[name="wiki:station",scores={wiki:ticks=0..}] wiki:ticks 1

# 计时期间持续执行
execute as @e[name="wiki:station",scores={wiki:ticks=0..}] at @s run particle minecraft:shulker_bullet ~~~

# 固定时刻触发
execute as @e[name="wiki:station",scores={wiki:ticks=3600}] at @s run playsound note.pling @a[r=10]

# 停止、循环、结束
execute as @e[name="wiki:station"] at @s if entity @e[family=pacified,r=10,c=1] run scoreboard players set @s wiki:ticks -1
execute as @e[name="wiki:station",scores={wiki:ticks=6000}] at @s if entity @e[family=monster,r=10,c=1] run scoreboard players set @s wiki:ticks 0
kill @e[name="wiki:station",scores={wiki:ticks=6000}]
```

## 继续阅读

- [记分板运算](./scoreboard-operations.md)
- [命令系统实践模板](./command-systems.md)
