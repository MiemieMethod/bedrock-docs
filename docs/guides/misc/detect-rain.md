# 降雨检测

这套方案利用"雨会熄灭火焰"这个原版机制，配合记分板状态机，实现对天气变化（开始下雨/停止下雨）的精准检测。

## 原理

在一个**上方无遮挡、暴露于天空**的位置放一块火焰方块。火焰在晴天持续存在，但一旦下雨就会被雨水熄灭。通过每刻检测该位置是否还有火焰，就可以判断当前天气状态。

配合记分板做状态机，可以区分三种状态：

| 状态值 | 含义 |
|:---:|---|
| `0` | 晴天 |
| `1` | 刚开始下雨（仅触发一刻） |
| `2` | 持续下雨中 |

## 初始化

先建立记分项，并选定一个检测坐标。检测坐标需满足：**Y方向上方无方块遮挡，且该位置方块更新会被服务端处理（位于已加载区块内）**。建议使用靠近世界中心的固定坐标，例如`0 100 0`（请确保该高度在你的世界里是空气且无遮挡）。

```mcfunction title="BP/functions/wiki/detect/weather/setup.mcfunction"
scoreboard objectives add wiki:q.is_raining dummy
```

在世界初始化时，手动在检测坐标放置火焰方块（或在设置函数中执行）：

```mcfunction title="初始化命令"
setblock 0 100 0 fire
```

将示例中的`0 100 0`替换成你自己选定的坐标（下面的命令同步修改）。

## 状态机主循环

```mcfunction title="BP/functions/wiki/detect/weather/is_raining.mcfunction"
# 晴天维护：火焰仍存在 → 状态设为0
execute if block 0 100 0 fire run scoreboard players set .Weather wiki:q.is_raining 0

# 雨天触发：火焰消失，且上一刻不是持续雨态 → 状态1（刚开始下雨）
execute unless block 0 100 0 fire unless score .Weather wiki:q.is_raining matches 2 run scoreboard players set .Weather wiki:q.is_raining 1

# 每刻重新放置火焰，保证晴天时检测点始终有效
setblock 0 100 0 fire

# 业务逻辑：根据状态执行命令
execute if score .Weather wiki:q.is_raining matches 1 run say 刚开始下雨！
execute if score .Weather wiki:q.is_raining matches 1.. run title @a actionbar 正在下雨

# 状态1→状态2：防止下一刻重复触发"刚开始下雨"
execute if score .Weather wiki:q.is_raining matches 1 run scoreboard players set .Weather wiki:q.is_raining 2
```

## 注意事项

/// warning | 遮挡问题
若检测坐标上方有任何不透明方块，雨水无法接触到火焰，检测将永远失败。若世界中存在"雷暴不着火"的游戏规则，也需要考虑其影响。
///

/// tip | 坐标选择建议
选择一个始终在常加载区块内的坐标，例如靠近出生点或玩家聚集区。如果玩家会离开该区域，考虑使用tick.json配合常加载区域（`tickingarea`命令）来保持该区块活跃。
///

## 函数目录示例

/// html | div.treeview
- `BP/functions/wiki/detect/weather`
    - `is_raining.mcfunction`
    - `setup.mcfunction`
- `BP/functions/tick.json`
///

## 继续阅读

- [命令系统实践模板](./command-systems.md)
- [记分板计时器](./scoreboard-timers.md)
