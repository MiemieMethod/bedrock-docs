# 自定义方块系列教程

自定义方块从行为包定义开始，再由资源包提供名称、纹理、模型和声音。简单方块可以只使用完整立方体和纹理；复杂方块可以使用自定义几何体、材质实例、碰撞箱、选择箱、破坏时间、亮度和战利品表。

## 基本文件关系

/// html | div.treeview
- `demo_BP`
    - `blocks`
        - `die.json`
- `demo_RP`
    - `textures`
        - `blocks`
            - `die_1.png`
        - `terrain_texture.json`
    - `texts`
        - `en_US.lang`
///

官方教程指出，行为包方块组件可以控制部分视觉属性；当你使用`minecraft:geometry`和`minecraft:material_instances`等组件时，资源包`blocks.json`中的视觉设置会被覆盖，`blocks.json`更多用于声音等旧式资源定义。

## 学习路线

1. 先完成“第一个方块”，理解`minecraft:block`、纹理图集和本地化。
2. 再学习自定义工作台，理解方块组件如何打开专用界面或关联配方标签。
3. 如果需要非完整立方体，再回到“制作模型”，为方块准备`models/blocks`中的几何体。

## 方块调试重点

- 方块定义放在行为包`blocks`目录。
- 纹理短名写在资源包`textures/terrain_texture.json`。
- 方块显示名写作`tile.<identifier>.name`。
- 自定义方块需要行为包和资源包同时启用。
- 复杂渲染问题优先检查`minecraft:geometry`和`minecraft:material_instances`。
