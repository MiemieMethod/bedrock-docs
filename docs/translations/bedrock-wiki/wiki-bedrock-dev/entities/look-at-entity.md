---
title: 查看实体
category: 教程
tags:
  - 中级
mentions:
  - shanewolf38
  - MedicalJewel105
  - TheItsNameless
  - SmokeyStack
description: 本教程提供了一种资源包方法，用于检测玩家何时在查看一个实体。
---

本教程提供了一种资源包方法，用于检测玩家何时在查看一个实体。以下代码必须放置在玩家将要查看的实体内部，并提供一个变量 `v.look_at_entity`，当实体被查看时返回 true。

## 变量

<CodeHeader>RP/entity/mob.entity.json</CodeHeader>

```json
"pre_animation": [
  "v.look_at_entity = Math.abs(Math.abs(q.rotation_to_camera(1) - q.camera_rotation(1)) - 180) < (20 / q.distance_from_camera) && Math.abs(q.rotation_to_camera(0) + q.camera_rotation(0)) < (10 / q.distance_from_camera);"
],
```

:::tip
由于查询 `q.rotation_to_camera` 是基于实体的原点（其脚部），因此垂直检测范围将围绕实体的底部进行。以下代码创建了一个修改后的变量，用于垂直角度，考虑了位置偏移，使垂直检测范围围绕实体的中心进行。
:::

<CodeHeader>RP/entity/mob.entity.json</CodeHeader>

```json
"pre_animation": [
  "v.rotation_to_camera_0 = -Math.atan2(-q.distance_from_camera * Math.sin(q.rotation_to_camera(0)) - 1, q.distance_from_camera * Math.cos(q.rotation_to_camera(0)));",
  "v.look_at_entity = Math.abs(Math.abs(q.rotation_to_camera(1) - q.camera_rotation(1)) - 180) < (20 / q.distance_from_camera) && Math.abs(v.rotation_to_camera_0 + q.camera_rotation(0)) < (60 / q.distance_from_camera);"
],
```

## 修改

提供的代码对于标准的Minecraft生物（宽1块，高2块）非常准确，但对于不同大小的实体，参数应进行调整。`- 1` 控制生物中心的位移偏移（-为向上，+为向下），`20` 控制水平角度灵敏度，`60` 控制垂直角度灵敏度。

## 解释

该变量通过检查实体看向玩家所需的旋转角度是否与玩家看向实体所需的旋转角度相反来检测玩家是否在查看实体。水平和垂直角度灵敏度由实体与相机的距离进行调整，以保持准确性。