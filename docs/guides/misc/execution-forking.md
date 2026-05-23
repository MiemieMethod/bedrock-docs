# 乘法执行分叉

本页介绍**乘法执行分叉（Multiplicative Execution Forking，MEF）**在命令系统里的用法。它的核心思想很简单：`execute as`或`execute at`一次命中多个目标时，后续命令会被复制执行多次。

## 什么是执行分叉

先看一个很直观的例子：

```mcfunction title="BP/functions/wiki/execution-forking/basic.mcfunction"
execute at @a run particle minecraft:basic_flame_particle ~ ~ ~
```

如果在线有5名玩家，这条命令并不是“执行1次”，而是会在5个玩家位置各执行1次。

## 为什么叫“乘法”

当你把多个`as`或`at`叠在一起时，每一层都会继续分叉，最终执行次数呈乘法增长。

$$
	ext{执行实例数}=n^x
$$

其中，$n$是每层命中的目标数量，$x$是分叉层数。

```mcfunction title="BP/functions/wiki/execution-forking/mef.mcfunction"
execute as @e[c=2] as @e[c=2] as @e[c=2] run say hi
```

上面这条命令会在1刻里输出8次`hi`。

## 典型用途

- 光线投射与“子弹”碰撞检测。
- 大批量实体逻辑刷新。
- 高频记分板计时器。

/// tip | 性能提示
使用分叉时，务必给选择器加限制，例如`[c=]`、`[type=]`、`[tag=标签名]`。直接对`@e`无限分叉很容易造成命令溢出和严重卡顿。
///

## 可视化工具

/// html | div.grid.cards
- [Execute Visualizer](https://komaramune.github.io/execute-visualizer/)：用于观察分叉上下文树。
///

## 继续阅读

- [新版execute命令](./execute-command.md)
- [记分板计时器](./scoreboard-timers.md)
