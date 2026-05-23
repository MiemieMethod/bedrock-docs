# 轨道摄像机

**轨道摄像机（Orbital Camera）**用于把摄像机锁定在目标周围环绕。半径和高度都能实时调。

{{video|youtube|yOlWjTpInFE}}

## 基础命令

```mcfunction title="BP/functions/wiki/camera/orbital.mcfunction"
execute as @p at @s anchored eyes rotated ~ 0 positioned ^^1^-2 run camera @s set minecraft:free ease 0.1 linear pos ~~~ facing @s
```

## 参数怎么改

- `positioned ^^1^-2`中的`1`控制高度。
- 同一段里的`-2`控制环绕半径。
- `rotated ~ 0`可以锁定俯仰角，避免镜头钻地。
- `ease 0.1`控制镜头追随速度。

## 围绕实体或固定坐标

```mcfunction title="BP/functions/wiki/camera/orbital.entity.mcfunction"
execute as @p at @e[tag=wiki:orbital_camera.focus] anchored eyes rotated as @s rotated ~ 0 positioned ^^1^-5 run camera @s set minecraft:free ease 0.1 linear pos ~~~ facing @e[tag=wiki:orbital_camera.focus]

execute as @p positioned 6 7 8 rotated as @s rotated ~ 0 positioned ^^1^-5 run camera @s set minecraft:free ease 0.1 linear pos ~~~ facing 6 7 8
```

![轨道摄像机二维示意图](../../../assets/images/guides/misc/orbital-camera/2d-visualization.gif)
<!-- 图片获取方式：从知识库源文件orbital-camera.md引用的2d-visualization.gif提取并放入指定目录。 -->

## 继续阅读

- [新版execute命令](./execute-command.md)
- [注视检测](./detect-looking.md)
