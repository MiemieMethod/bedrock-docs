# 乘法执行分叉

**乘法执行分叉（Multiplicative Execution Forking，MEF）**是利用`execute`命令在同一个刻内多次执行某条命令的技术。当`execute as @e[...]`或`execute as @a`选中N个目标时，后续子命令会被执行N次——每次都以不同的执行者身份运行。把多个`execute`层级嵌套起来，执行次数就会按乘法增长，这正是"乘法"二字的来源。

## 为什么需要它？

先从一个具体问题出发：假设你要做一个子弹系统，为了保证子弹不会穿墙，你需要每移动1格就做一次碰撞检测。每刻移动1格的子弹太慢，但如果你想让子弹每刻飞行32格、每格都检测碰撞，就需要在同一刻内执行32次"移动+检测"逻辑。手动放32个命令方块显然不现实——这正是MEF大显身手的时候。

## 单层分叉：实例化

先理解一个基础事实：在基岩版里，一条命令不一定只运行一次。当选择器命中多个目标时，每个目标都会得到一个独立的**执行实例（Instance）**。

```mcfunction title="BP/functions/wiki/execution-forking/basic.mcfunction"
execute at @a run particle minecraft:basic_flame_particle ~ ~ ~
```

如果服务器上有5名玩家，这条命令会在5个位置各生成一颗粒子——不是1颗，而是5颗。这就是"分叉"：执行路径从1条分叉成了5条。

## 多层嵌套：乘法增长

当你把多个`execute as`或`execute at`层叠在一起时，每一层都会对之前的实例数量继续乘以它自己命中的目标数。总执行次数遵循如下公式：

$$\text{执行实例数} = n^x$$

其中$n$是每个子命令每次选中的目标数量，$x$是嵌套层数。

```mcfunction title="BP/functions/wiki/execution-forking/mef.mcfunction"
execute as @e[c=2] as @e[c=2] as @e[c=2] run say hi
```

这条命令分三层：

1. **第一层**：选中2个实体 → **2个实例**
2. **第二层**：每个实例再选中2个实体 → **2×2=4个实例**
3. **第三层**：每个实例再选中2个实体 → **4×2=8个实例**

一个刻里，`hi`会被说8次。

## 典型应用场景

| 场景 | 说明 |
|---|---|
| 光线投射/碰撞检测 | 每刻让子弹前进多步，每步检测碰撞，避免穿透 |
| 批量实体逻辑 | 对全场已加载实体一刻内完成复杂更新 |
| 高速计时器 | 每刻多次递增计时器，实现亚刻精度 |
| 球形生成 | 三层嵌套分别遍历X/Y/Z轴，一刻完成整个球体 |

## 实际示例：范围效果分发

利用MEF给所有来源实体附近的玩家施加特效。如果有3个`wiki:source`标签实体，每个范围内有2名玩家，这条命令在一刻内触发6次：

```mcfunction title="BP/functions/wiki/execution-forking/area_effect.mcfunction"
execute at @e[tag=wiki:source] as @a[r=5] run effect @s speed 5 1 true
```

## 实际示例：等效循环展开

下面是利用MEF做光线投射的基本思路。每刻让盔甲架沿视线方向移动4次，每次移动后检测是否碰到玩家：

```mcfunction title="BP/functions/wiki/execution-forking/raycast.mcfunction"
# 4层 × c=1，确保每层的结果维持单一实体上下文
execute as @e[type=armor_stand,tag=wiki:bullet] as @e[c=1] as @e[c=1] as @e[c=1] as @e[c=1] at @s positioned ^ ^ ^1 run function wiki/bullet/move_and_check
```

## 注意事项

/// warning | 防止命令溢出
使用MEF时务必配合`c=`（数量限制）、`type=`（类型过滤）或`tag=`（标签过滤）来控制每层分叉的数量。对`@e`不加任何限制地多层嵌套，可能在一瞬间生成数百乃至数千个实例，导致严重卡顿甚至触发命令溢出错误。
///

/// tip | 可视化工具
[@komaramune](https://komaramune.github.io/execute-visualizer/)开发了一个交互式Execute可视化工具，可以帮助你直观理解MEF和命令上下文树的结构，推荐用于调试。
///

## 继续阅读

- [新版execute命令](./execute-command.md)
- [球形命令](./sphere-command.md)
- [记分板计时器](./scoreboard-timers.md)
