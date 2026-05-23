# 记分板运算

本页讲**记分板运算（Scoreboard Operation）**，也就是`scoreboard players operation`这套操作符。它既能做算术，也能做逻辑选择。

## 基础语法

```mcfunction title="通用语法"
scoreboard players operation <targetScore> <objective> <operation> <sourceScore> <objective>
```

`targetScore`是被修改的一方，`sourceScore`通常只读（`><`除外）。

## 算术操作

```mcfunction title="BP/functions/wiki/scoreboard/operations/math.mcfunction"
scoreboard players operation .A wiki:var += .B wiki:var
scoreboard players operation .A wiki:var -= .B wiki:var
scoreboard players operation .A wiki:var *= .B wiki:var
scoreboard players operation .A wiki:var /= .B wiki:var
scoreboard players operation .A wiki:var %= .B wiki:var
```

- `/=`是取整除法。
- `%=`是取余运算。

## 逻辑操作

```mcfunction title="BP/functions/wiki/scoreboard/operations/logic.mcfunction"
scoreboard players operation .A wiki:var = .B wiki:var
scoreboard players operation .A wiki:var < .B wiki:var
scoreboard players operation .A wiki:var > .B wiki:var
scoreboard players operation .A wiki:var >< .B wiki:var
```

- `<`取两者最小值。
- `>`取两者最大值。
- `><`交换两者值。

## 两个实用模板

```mcfunction title="BP/functions/wiki/scoreboard/operations/templates.mcfunction"
# 判断是否相等
scoreboard objectives add wiki:temp dummy
execute if score .Steve wiki:temp = .Alex wiki:temp run say 分数相同

# 仅在未注册时初始化为0
scoreboard players add .Player wiki:temp 0
```

## 继续阅读

- [记分板](../../docs/general/scoreboard.md)
- [记分板计时器](./scoreboard-timers.md)
