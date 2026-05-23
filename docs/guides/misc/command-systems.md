# 命令系统实践模板

这篇教程把命令系统里最常见的几类“可复用模板”整理到一起：初始化、玩家事件、周期计时、文本反馈与排错。你可以把它当成一个起步骨架，再替换成自己的玩法逻辑。

/// note | 适用范围
以下流程以国际版命令参考为基准整理。跨版本或跨实现环境复用前，请先核对[命令清单](../../refs/commands/command-list.md)和[命令版本](../../refs/commands/version.md)。
///

## 一、先选入口：命令方块还是函数

- 快速试验、可视化排线：优先命令方块。
- 可复用、可版本管理：优先`.mcfunction`。
- 需要长期运行：把入口函数登记到{{file|tick.json}}。

一个最小结构如下：

/// html | div.treeview
- `demo_BP`
    - `manifest.json`
    - `functions`
        - `tick.json`
        - `system`
            - `main.mcfunction`
///

```json title="functions/tick.json"
{
  "values": [
    "system/main"
  ]
}
```

## 二、玩家事件模板

这些模板都基于“每刻轮询+状态标记”。

### 1)首次进入

```mcfunction title="functions/system/on_first_join.mcfunction"
give @a[tag=!joined] bread 16
tag @a[tag=!joined] add joined
```

### 2)加入事件

```mcfunction title="functions/system/on_player_join.mcfunction"
scoreboard players add @a joined 0
execute as @a[scores={joined=0}] run tellraw @s {"rawtext":[{"text":"欢迎加入世界。"}]}
scoreboard players reset * joined
scoreboard players set @a joined 1
```

### 3)离开事件

```mcfunction title="functions/system/on_player_leave.mcfunction"
scoreboard players reset new total
execute as @a run scoreboard players add new total 1
scoreboard players operation new total -= old total
execute if score new total matches ..-1 run say 有玩家离开了世界。
scoreboard players reset old total
execute as @a run scoreboard players add old total 1
```

### 4)死亡与重生

```mcfunction title="functions/system/on_player_death.mcfunction"
scoreboard players set @a[scores={alive=!2}] alive 0
scoreboard players set @e[type=player] alive 1
execute as @a[scores={alive=0}] run say 我死了。
scoreboard players set @a[scores={alive=0}] alive 2
```

```mcfunction title="functions/system/on_player_respawn.mcfunction"
execute as @e[scores={respawn=1}] run say 我已重生。
scoreboard players set @a respawn 1
scoreboard players set @e[type=player] respawn 0
```

## 二·五、世界首次加载事件

除了玩家事件，还有一类常见需求：在整包应用后**世界第一次加载时**执行一次性初始化逻辑（例如生成出生点结构、初始化全局记分板、给世界创建者发放礼包等）。这个模板依赖`tick.json`每刻执行主函数，并用记分板标记"已初始化"状态。

```mcfunction title="BP/functions/wiki/main.mcfunction"
# 世界首次加载时调用初始化函数
execute unless score .World wiki:q.is_initialised matches 1 run function wiki/event/worlds/on_initialise
```

```mcfunction title="BP/functions/wiki/event/worlds/on_initialise.mcfunction"
## 在此处放置你的初始化命令（示例）
say 世界初始化完成，附加包已首次加载。

## 初始化收尾
### 添加状态记分项
scoreboard objectives add wiki:q.is_initialised dummy
### 标记为已初始化，防止下次加载重复触发
scoreboard players set .World wiki:q.is_initialised 1
```

一旦`on_initialise`函数执行完毕，记分板中`.World`的`wiki:q.is_initialised`分数被设为`1`，此后每次世界加载时`execute unless score`条件都会失败，初始化逻辑就永远不会再运行。

/// html | div.treeview
- `BP/functions/wiki`
    - `main.mcfunction`
    - `event`
        - `worlds`
            - `on_initialise.mcfunction`
- `BP/functions/tick.json`
///

## 三、周期计时模板

先建记分项：

```mcfunction
scoreboard objectives add ticks dummy
scoreboard objectives add events dummy
```

再写周期逻辑：

```mcfunction title="functions/system/timer.mcfunction"
scoreboard players add timer ticks 1
scoreboard players operation * events = timer ticks

scoreboard players set ten_seconds ticks 200
scoreboard players operation message events %= ten_seconds ticks
execute if score message events matches 0 run tellraw @a {"rawtext":[{"text":"10秒已到。"}]}
```

当你需要多个周期事件时，只要继续增加“目标虚拟玩家+取模判定”即可。

## 四、文本与音效反馈

### tellraw最小结构

```mcfunction
tellraw @a {"rawtext":[{"text":"阶段完成。"},{"selector":"@s"}]}
```

### 带分数反馈

```mcfunction
tellraw @a {"rawtext":[{"text":"当前分数："},{"score":{"name":"@s","objective":"value"}}]}
```

### 播放音效

```mcfunction
playsound random.orb @a ~ ~ ~ 1 1 0
```

如果逻辑先`tp`再播音，建议用`execute as @a at @s run playsound ...`，避免上下文位置不一致。

## 五、排错顺序

1. 先在聊天栏单条验证命令，再写入函数。
2. 观察选择器是否命中，必要时临时插入`/say`或`/tellraw`。
3. 逐步检查记分板值变化，确认范围表达式是否正确（`N..`、`..N`、`N..M`）。
4. 函数修改后执行`/reload`；仍异常时重进世界再测。
5. 大系统优先拆分成多个函数，避免单次调用命令过多。

## 继续学习

- [命令](../../docs/general/command.md)
- [目标选择器](../../docs/general/target-selector.md)
- [记分板](../../docs/general/scoreboard.md)
- [选择器参数参考](../../refs/commands/selector-parameter.md)
