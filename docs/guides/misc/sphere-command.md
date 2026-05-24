# 单命令球体生成

本页介绍一个基于执行分叉和旋转向量的球体采样方案。

/// note | 前置知识
建议先阅读[分叉执行](./execution-forking.md)。
///

![球体命令演示](../../../assets/images/guides/misc/sphere-command/sphere-command-demo.png)
<!-- 图片获取方式：从资料源文件sphere-command.md中的sphere-command-demo.png提取。 -->

## 准备旋转锚点

```mcfunction title="BP/functions/wiki/sphere/setup.mcfunction"
# 召唤两艘船作为旋转锚点
summon boat ~~1~ 0 -90
summon boat ~~1~ 180 90 none
tag @e[type=boat,c=2] add wiki:r
```

## 主命令

```mcfunction title="BP/functions/wiki/sphere/run.mcfunction"
execute positioned 0 0 0 rotated as @e[tag=wiki:r] positioned ^1^^ rotated as @e[tag=wiki:r] rotated ~ 0 positioned ^^^1 rotated as @e[tag=wiki:r] positioned ^1.414^^ facing 0 0 0 positioned 0 0 0 positioned ^^^1 rotated as @e[tag=wiki:r] positioned ^1^^ facing 0 0 0 positioned 0 0 0 positioned ^^^1 rotated as @e[tag=wiki:r] positioned ^1^^ facing 0 0 0 positioned 0 0 0 positioned ^^^1 rotated as @e[tag=wiki:r] positioned ^^^1 rotated as @e[tag=wiki:r] positioned ^^^1.414 facing 0 0 0 positioned 0 0 0 positioned ^^^1 rotated as @e[tag=wiki:r] positioned ^^^1 facing 0 0 0 positioned 0 0 0 positioned ^^^1 rotated as @e[tag=wiki:r] positioned ^^^1 facing 0 0 0 positioned as @p run particle minecraft:balloon_gas_particle ^^^3
```

## 拆解理解

1. 横向分叉：`positioned ^1^^`反复叠加形成近似圆环。
2. 纵向扩展：`positioned ^^^1`与`positioned ^^^1.414`把圆环拉成立体壳层。
3. 回看中心：`facing 0 0 0 positioned 0 0 0`确保半径方向统一。

![分段示意1](../../../assets/images/guides/misc/sphere-command/segment-1.png)
<!-- 图片获取方式：从资料源文件sphere-command.md中的segment-1.png提取。 -->

![分段示意2](../../../assets/images/guides/misc/sphere-command/segment-2.png)
<!-- 图片获取方式：从资料源文件sphere-command.md中的segment-2.png提取。 -->

![分段示意3](../../../assets/images/guides/misc/sphere-command/segment-3.png)
<!-- 图片获取方式：从资料源文件sphere-command.md中的segment-3.png提取。 -->

![分段示意3.1](../../../assets/images/guides/misc/sphere-command/segment-3.1.png)
<!-- 图片获取方式：从资料源文件sphere-command.md中的segment-3.1.png提取。 -->

![分段示意4](../../../assets/images/guides/misc/sphere-command/segment-4.png)
<!-- 图片获取方式：从资料源文件sphere-command.md中的segment-4.png提取。 -->

## 自定义

- 改半径：修改最终`run`里`^^^3`的3。
- 改密度：增加横向或纵向分叉次数。
- 改安全性：锚点船请放在常加载、安全区域。