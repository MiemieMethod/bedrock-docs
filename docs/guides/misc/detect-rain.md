# 降雨检测

这套方案利用“雨会熄灭火”这个原版机制，做一个天气状态机。

/// warning | 前置条件
必须开启火焰蔓延相关规则，且检测点上方不能被方块遮挡天空。
///

## 初始化

```mcfunction title="BP/functions/wiki/detect/weather/is_raining.setup.mcfunction"
scoreboard objectives add wiki:q.is_raining dummy
```

## 状态机实现

```mcfunction title="BP/functions/wiki/detect/weather/is_raining.mcfunction"
# 火消失且此前不是稳定雨态→状态1(刚开始下雨)
execute unless block 0 0 0 fire unless score .Weather wiki:q.is_raining matches 2 run scoreboard players set .Weather wiki:q.is_raining 1
# 火仍存在→状态0(晴天)
execute if block 0 0 0 fire run scoreboard players set .Weather wiki:q.is_raining 0

# 维持检测火
setblock 0 0 0 fire

# 业务命令
execute if score .Weather wiki:q.is_raining matches 1.. run title @a actionbar 正在下雨
execute if score .Weather wiki:q.is_raining matches 1 run say 刚开始下雨
execute if score .Weather wiki:q.is_raining matches 0 run title @a actionbar 当前无雨

# 状态1→状态2，避免“刚下雨”重复触发
execute if score .Weather wiki:q.is_raining matches 1 run scoreboard players set .Weather wiki:q.is_raining 2
```

将示例中的`0 0 0`替换成你选好的检测坐标即可。

## 函数目录示例

/// html | div.treeview
- `BP/functions/wiki/detect/weather`
    - `is_raining.mcfunction`
- `BP/functions/tick.json`
///

## 继续阅读

- [记分板计时器](./scoreboard-timers.md)
- [命令系统实践模板](./command-systems.md)
