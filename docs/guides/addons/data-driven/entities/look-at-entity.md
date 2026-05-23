# 注视实体检测

本文提供一种资源包方法，用于检测玩家是否正在注视某个实体。代码写在被注视的实体的客户端实体定义文件中，最终会提供一个变量`v.look_at_entity`，当玩家正在注视该实体时返回`true`。

## 基础实现

将以下Molang表达式添加到实体资源包定义文件的`pre_animation`数组中：

```json title="RP/entity/my_entity.json（片段）"
"pre_animation": [
    "v.look_at_entity = Math.abs(Math.abs(q.rotation_to_camera(1) - q.camera_rotation(1)) - 180) < (20 / q.distance_from_camera) && Math.abs(q.rotation_to_camera(0) + q.camera_rotation(0)) < (10 / q.distance_from_camera);"
]
```

这段代码通过比较摄像机方向与实体方向的角度差来判断玩家是否在注视实体。

## 居中修正版本

上面的基础版本以实体的**脚部**（原点）为垂直方向的检测中心，这意味着对于一个高2格的生物而言，你需要盯着它的脚才算"看着它"。以下改进版本加入了垂直偏移修正，将检测中心提升到实体的**中心**：

```json title="RP/entity/my_entity.json（片段）"
"pre_animation": [
    "v.rotation_to_camera_0 = -Math.atan2(-q.distance_from_camera * Math.sin(q.rotation_to_camera(0)) - 1, q.distance_from_camera * Math.cos(q.rotation_to_camera(0)));",
    "v.look_at_entity = Math.abs(Math.abs(q.rotation_to_camera(1) - q.camera_rotation(1)) - 180) < (20 / q.distance_from_camera) && Math.abs(v.rotation_to_camera_0 + q.camera_rotation(0)) < (60 / q.distance_from_camera);"
]
```

## 参数调整

上面的参数适用于标准Minecraft生物（宽1格、高2格）。如需适配不同大小的实体，可以调整以下参数：

| 参数 | 位置 | 说明 |
|---|---|---|
| `- 1` | `rotation_to_camera_0`的`atan2`中 | 垂直中心的偏移量（负值向上，正值向下），单位为格 |
| `20` | 水平角度判断 | 水平方向的检测灵敏度，值越大越容易触发 |
| `60` | 垂直角度判断 | 垂直方向的检测灵敏度，值越大越容易触发 |

## 使用示例

`v.look_at_entity`可以用在动画控制器的转移条件中，也可以用于渲染控制器或任何支持Molang的字段。例如，当玩家注视实体时，高亮显示实体：

```json title="RP/render_controllers/my_entity.json（片段）"
"overlay_color": {
    "r": "v.look_at_entity ? 1.0 : 0.0",
    "g": "v.look_at_entity ? 1.0 : 0.0",
    "b": "v.look_at_entity ? 0.0 : 0.0",
    "a": "v.look_at_entity ? 0.5 : 0.0"
}
```

## 原理说明

这段代码通过以下逻辑检测注视：

- `q.rotation_to_camera`返回实体看向摄像机所需的旋转角度
- `q.camera_rotation`返回摄像机的旋转角度
- 如果这两个方向互相"反向"（差值接近180度），说明摄像机正在看着实体
- 将角度差除以`q.distance_from_camera`是为了在不同距离下保持检测范围的视角一致
