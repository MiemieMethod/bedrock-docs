# 实体计数器

**实体计数器（Entity Counter）**用于统计目标数量，再按区间执行命令。常见用途是玩家数量门槛、怪物密度门槛、刷怪开关等。

## 初始化

```mcfunction title="BP/functions/wiki/scoreboard/players/tally_count.setup.mcfunction"
scoreboard objectives add wiki:count dummy
```

## 计数主逻辑

```mcfunction title="BP/functions/wiki/scoreboard/players/tally_count.mcfunction"
# 重置上一轮统计
scoreboard players set * wiki:count 0

# 统计示例
execute as @e[type=player] run scoreboard players add .Players.Alive wiki:count 1
execute as @e[type=creeper] run scoreboard players add .Creeper wiki:count 1

# 业务示例
execute if score .Players.Alive wiki:count matches 4.. run title @a actionbar 当前在线玩家不少于4人
execute if score .Creeper wiki:count matches ..3 run title @a actionbar 苦力怕数量不超过3个
```

/// note | 性能建议
当记分项里分数持有者很多时，优先对固定分数持有者逐个`set 0`，而不是总用`*`全量重置。
///

## 函数目录示例

/// html | div.treeview
- `BP`
    - `functions`
        - `wiki`
            - `scoreboard`
                - `players`
                    - `tally_count.mcfunction`
        - `tick.json`
///

在`tick.json`中把`wiki/scoreboard/players/tally_count`加入`values`即可每刻循环。

## 继续阅读

- [记分板](../../docs/general/scoreboard.md)
- [分数比较](./comparing-scores.md)
