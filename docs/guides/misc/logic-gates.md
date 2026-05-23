# execute逻辑门

命令里常说的**逻辑门（Logic Gate）**，本质上就是把布尔判断写进`execute if`或`execute unless`。你可以把它理解成“命令版电路”。

## 八种常用逻辑门

下面示例统一使用标签作为输入条件。

```mcfunction title="BP/functions/wiki/logic-gates/basic.mcfunction"
# 缓冲门Buffer
execute if entity @s[tag=red] run <command>

# 非门NOT
execute if entity @s[tag=!red] run <command>

# 与门AND
execute if entity @s[tag=red,tag=green] run <command>

# 与非门NAND
execute unless entity @s[tag=red,tag=green] run <command>

# 或门OR
execute unless entity @s[tag=!red,tag=!green] run <command>

# 或非门NOR
execute if entity @s[tag=!red,tag=!green] run <command>

# 异或门XOR
execute unless entity @s[tag=!red,tag=!green] unless entity @s[tag=red,tag=green] run <command>

# 同或门XNOR
execute unless entity @s[tag=red,tag=!green] unless entity @s[tag=!red,tag=green] run <command>
```

## 怎么迁移到其他选择器参数

你不需要把逻辑门绑定在`tag`上，`type`、`scores`、`name`、`family`、`hasitem`都能套同样结构。

```mcfunction title="BP/functions/wiki/logic-gates/examples.mcfunction"
# 玩家满足任一分数条件
execute unless entity @p[scores={test.a=!5,test.b=!5}] run say 命中OR条件

# 玩家有任一武器
execute unless entity @p[hasitem=[{item=diamond_sword,quantity=0},{item=iron_sword,quantity=0}]] run say 可执行

# 实体是鸡或牛
execute unless entity @e[type=!chicken,type=!cow] run say 命中
```

/// note | 实战建议
先把每个输入条件拆成单独命令验证，再组合成门电路。这样排错最快。
///

## 继续阅读

- [新版execute命令](./execute-command.md)
- [分数比较](./comparing-scores.md)
