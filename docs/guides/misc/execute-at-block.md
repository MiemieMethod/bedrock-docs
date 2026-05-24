# 在方块位置执行命令

这套技巧用“满堆肥桶掉落骨粉”的机制，把任意方块位置临时转成可被选择器捕获的掉落物位置。

![系统演示1](../../../assets/images/guides/misc/execute-at-block/demo_1.gif)
<!-- 图片获取方式：从资料源文件execute-at-block.md中的demo_1.gif提取。 -->

/// warning | 使用注意
该系统会临时生成大量掉落物。扫描范围太大时会产生明显卡顿。
///

## 标准版

```mcfunction title="BP/functions/wiki/execute_at_blocks/diamond_block.mcfunction"
# 把目标方块替换成满堆肥桶
execute at @a run fill ~8~8~8 ~-8~-1~-8 composter ["composter_fill_level"=8] replace diamond_block

# 保护原有掉落物
tag @e[type=item] add wiki:ignored.item

# 还原方块并触发骨粉掉落
execute at @a run fill ~8~8~8 ~-8~-1~-8 diamond_block replace composter ["composter_fill_level"=8]

# 在“系统产生的掉落物”位置执行命令
execute at @e[type=item,tag=!wiki:ignored.item] align xyz positioned ~0.5~0.5~0.5 run particle minecraft:shulker_bullet ~~1~

# 清理系统掉落物
kill @e[type=item,tag=!wiki:ignored.item]
```

## 改进版(兼容世界里原有满堆肥桶)

```mcfunction title="BP/functions/wiki/execute_at_blocks/diamond_block.safe.mcfunction"
tag @e[type=item] add wiki:ignored.item
execute at @a run fill ~8~8~8 ~-8~-1~-8 air replace composter ["composter_fill_level"=8]
tag @e[type=item,tag=!wiki:ignored.item] add wiki:ignored.composter
execute at @a run fill ~8~8~8 ~-8~-1~-8 composter ["composter_fill_level"=8] replace diamond_block
execute at @a run fill ~8~8~8 ~-8~-1~-8 diamond_block replace composter ["composter_fill_level"=8]
execute at @e[type=item,tag=wiki:ignored.composter] run setblock ~~~ composter ["composter_fill_level"=8]
execute at @e[type=item,tag=!wiki:ignored.item,tag=!wiki:ignored.composter] align xyz positioned ~0.5~0.5~0.5 run particle minecraft:shulker_bullet ~~1~
kill @e[type=item,tag=!wiki:ignored.item]
```

![系统演示2](../../../assets/images/guides/misc/execute-at-block/demo_2.gif)
<!-- 图片获取方式：从资料源文件execute-at-block.md中的demo_2.gif提取。 -->

## 继续阅读

- [分叉执行](./execution-forking.md)
- [二进制逻辑](./binary-logic.md)