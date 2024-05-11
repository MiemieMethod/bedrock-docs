# 未命名

> 文档版本：1.21.0.24

该组件能实现当两个方块相邻时，相邻面渲染其中一个方块的一面，与原版2个叶子方块相邻效果一致，不会把相邻面都裁剪掉。
为了避免相邻面变黑需要在配置中新增minecraft:block_light_absorption组件并将值设置为0。
需要配合netease:render_layer使用，使用 optionalAlpha 能实现原版的叶子方块效果，使用 alpha 超过一定距离后方块将不渲染。

## 架构

```mcschema
netease:no_crop_face_block:
{
}

```

/// html | div.result

///

