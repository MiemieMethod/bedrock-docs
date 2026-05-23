# 翻书动画

**翻书动画（Flipbook Animation）**是Minecraft基岩版资源包中用于实现方块和物品纹理逐帧动画的机制。翻书动画通过在一张包含所有帧的纵向拼接纹理图片中逐帧切换来产生动画效果。在中国版中，翻书动画亦称作**序列帧动画（Frame Animation）**。<!-- md:flag china -->

## 概述

基岩版中许多原版方块和物品的纹理具有动画效果，如水面、岩浆、海带、紫水晶方块和传送门等。这些动画通过翻书动画机制实现：一张纹理文件中纵向排列所有动画帧，引擎按照指定的播放速度依次显示每一帧。

翻书动画的定义文件为资源包根目录下的{{file|textures/flipbook_textures.json}}。中国版另有专门用于物品翻书动画的{{file|textures/flipbook_textures_items.json}}文件，与前者共享相同的文件格式。<!-- md:flag china -->

## 纹理文件格式

翻书动画使用的纹理文件为一张宽度等于单帧宽度、高度为单帧高度乘以帧数的PNG图片。例如，一个16×16像素、包含32帧的翻书动画，其纹理文件尺寸为16×512像素。

帧从上到下依次排列，引擎按照定义的顺序和速度逐帧播放。

## 定义文件

`flipbook_textures.json`为一个JSON数组，每个元素定义一个翻书动画条目：

```json title="翻书动画定义示例"
[
  {
    "flipbook_texture": "textures/blocks/custom_animated",
    "atlas_tile": "custom_animated",
    "atlas_index": 0,
    "atlas_tile_variant": 0,
    "ticks_per_frame": 10,
    "frames": [0, 1, 2, 3, 2, 1],
    "replicate": 3,
    "blend_frames": true
  }
]
```

## 字段说明

/// define
`flipbook_texture`

- 翻书动画使用的纹理文件路径，不包含文件扩展名。

`atlas_tile`

- 此动画在地形图集或物品图集中对应的短名称。该名称需要与{{file|terrain_texture.json}}或{{file|item_texture.json}}中定义的名称匹配。

`atlas_index`

- 可选。指定同一纹理短名称中要应用动画的纹理索引。用于`textures`字段定义了多个纹理路径的图集条目。

`atlas_tile_variant`

- 可选。指定同一纹理短名称中要应用动画的变种索引。用于图集条目通过`variations`定义多个变种的情况。

`ticks_per_frame`

- 每一帧的持续时间，以游戏刻为单位。值越大，动画播放越慢。

`frames`

- 可选。定义帧的播放顺序。数组中的每个数字为帧索引（从0开始）。若不指定，则按纹理文件中从上到下的顺序依次播放。

`replicate`

- 可选。纹理在图集中的复制次数，用于处理纹理分辨率和图集排列。

`blend_frames`

- 可选。是否在帧之间进行插值平滑过渡。默认为`true`。

///
