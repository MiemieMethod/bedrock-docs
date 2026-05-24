# 轨道摄像机

**轨道摄像机（Orbital Camera）**技术利用`/camera`命令，把玩家视角锁定在目标周围环绕。环绕半径和高度可以实时调整，还支持围绕实体或固定坐标旋转。

{{video|youtube|yOlWjTpInFE}}

/// warning | 实验性功能
`/camera`命令目前需要开启**实验性游戏玩法**中的"摄像机命令"（Camera Command）选项才能使用。<!-- md:flag experimental -->
///

## 基础命令

将以下命令放入循环命令方块或每刻执行的函数中：

```mcfunction title="BP/functions/wiki/camera/orbital.mcfunction"
execute as @p at @s anchored eyes rotated ~ 0 positioned ^^1^-2 run camera @s set minecraft:free ease 0.1 linear pos ~~~ facing @s
```

## 命令逐段解析

| 片段 | 作用 |
|---|---|
| `as @p` | 以最近的玩家作为执行者 |
| `at @s` | 执行位置移至该玩家位置 |
| `anchored eyes` | 执行位置上移至眼部高度 |
| `rotated ~ 0` | 沿用玩家水平朝向，但将俯仰角固定为0°（水平）；改为`rotated 0 ~`可固定水平朝向 |
| `positioned ^^1^-2` | 从眼部位置沿局部坐标前移：上移1格，后退2格；`1`控制高度，`-2`控制半径（负值在玩家背后） |
| `run camera @s set minecraft:free ease 0.1 linear pos ~~~` | 将摄像机设为自由视角，以0.1的线性缓动追随该位置；数值越小镜头越慢 |
| `facing @s` | 摄像机始终朝向玩家自身 |

## 调整参数

- **高度**：修改`^^1^-2`中的`1`。正值越大，摄像机越高。
- **半径**：修改`^^1^-2`中的`-2`。绝对值越大，轨道半径越大；改为正值则切换到玩家正前方。
- **镜头速度**：修改`ease 0.1`的数值。`0.1`较慢，`1.0`为瞬间跟随。
- **固定方向**：将`rotated ~ 0`改为`rotated 0 ~`可以固定水平方向，此时镜头只会上下移动。

## 围绕实体或固定坐标

```mcfunction title="BP/functions/wiki/camera/orbital.entity.mcfunction"
# 围绕带有 wiki:orbital_camera.focus 标签的实体
execute as @p at @e[tag=wiki:orbital_camera.focus] anchored eyes rotated as @s rotated ~ 0 positioned ^^1^-5 run camera @s set minecraft:free ease 0.1 linear pos ~~~ facing @e[tag=wiki:orbital_camera.focus]

# 围绕固定坐标 (6, 7, 8)
execute as @p positioned 6 7 8 rotated as @s rotated ~ 0 positioned ^^1^-5 run camera @s set minecraft:free ease 0.1 linear pos ~~~ facing 6 7 8
```

## 恢复默认摄像机

在轨道摄像机结束后，执行以下命令将玩家视角恢复正常：

```mcfunction title="恢复默认摄像机"
camera @a clear
```

## 示意图

![轨道摄像机二维示意图](../../../assets/images/guides/misc/orbital-camera/2d-visualization.gif)
<!-- 图片获取方式：从资料源文件orbital-camera.md引用的2d-visualization.gif提取并放入指定目录。 -->

## 继续阅读

- [新版execute命令](./execute-command.md)
- [注视检测](./detect-looking.md)