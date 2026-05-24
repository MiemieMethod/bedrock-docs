# 动态文本显示

本页介绍如何用记分板+`titleraw`做大规模动态文本映射，避免写大量`if score`分支。

{{video|youtube|s8QGwsHuEk4}}

## 核心思路

把分数拆成两个索引：

- `wiki:array`：第几组(书架)
- `wiki:element`：组内第几项(书)

这样1到81共81条文本，可以用一套模板完成。

## 初始化

```mcfunction title="BP/functions/wiki/rawtext/setup.mcfunction"
scoreboard objectives add wiki:q.var_changed dummy
scoreboard objectives add wiki:const dummy
scoreboard objectives add wiki:array dummy
scoreboard objectives add wiki:element dummy
scoreboard objectives add wiki:var dummy
scoreboard objectives add wiki:delta_var dummy

scoreboard players set .1 wiki:const 1
scoreboard players set .8 wiki:const 8
scoreboard players set .9 wiki:const 9
```

## 显示逻辑

```mcfunction title="BP/functions/wiki/rawtext/display_logic.mcfunction"
# 仅在分数变化时计算
scoreboard players set @a[scores={wiki:q.var_changed=1}] wiki:q.var_changed 0
execute as @a unless entity @s[scores={wiki:var=82..}] unless score @s wiki:delta_var = @s wiki:var run scoreboard players set @s wiki:q.var_changed 1

# element=(var-1)%9+1
execute as @a[scores={wiki:q.var_changed=1}] run scoreboard players operation @s wiki:element = @s wiki:var
execute as @a[scores={wiki:q.var_changed=1}] run scoreboard players operation @s wiki:element -= .1 wiki:const
execute as @a[scores={wiki:q.var_changed=1}] run scoreboard players operation @s wiki:element %= .9 wiki:const
execute as @a[scores={wiki:q.var_changed=1}] run scoreboard players operation @s wiki:element += .1 wiki:const

# array=(var+8)/9
execute as @a[scores={wiki:q.var_changed=1}] run scoreboard players operation @s wiki:array = @s wiki:var
execute as @a[scores={wiki:q.var_changed=1}] run scoreboard players operation @s wiki:array += .8 wiki:const
execute as @a[scores={wiki:q.var_changed=1}] run scoreboard players operation @s wiki:array /= .9 wiki:const

# 保存当前值
execute as @a unless score @s wiki:delta_var = @s wiki:var run scoreboard players operation @s wiki:delta_var = @s wiki:var
```

## titleraw模板骨架

```mcfunction title="titleraw模板骨架"
titleraw @a actionbar {"rawtext":[{"translate":"%%%%s","with":{"rawtext":[{"score":{"name":"*","objective":"wiki:array"}},{"rawtext":[{"translate":"%%%%s","with":{"rawtext":[{"score":{"name":"*","objective":"wiki:element"}},{"text":"文本1"},{"text":"文本2"},{"text":"文本3"},{"text":"文本4"},{"text":"文本5"},{"text":"文本6"},{"text":"文本7"},{"text":"文本8"},{"text":"文本9"}]}}]}]}}]}
```

/// warning | 范围与维护
命令方块直写方案推荐控制在1到81。超过81时，建议改函数分片方案，按区间分发到`display/1`、`display/2`、`display/3`等函数。
///

## 扩展到更大范围

- 函数法可先把`wiki:var`归一化到1到81循环区间，再按“第几组81”调用不同显示函数。
- **多重嵌套翻译（Multiple Nested Translates，MNT）**可继续扩展到729甚至6561，但单条`titleraw`会非常长，编辑与性能压力都更大。

## 继续阅读

- [记分板运算](./scoreboard-operations.md)
- [记分板计时器](./scoreboard-timers.md)