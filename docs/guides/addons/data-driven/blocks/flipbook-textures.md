# 翻书纹理

翻书纹理是基岩版实现方块动态纹理的标准方式，通过将多个纹理帧按顺序播放来产生动画效果，就像翻书一样。

## 定义翻书纹理

翻书纹理在资源包的 `textures/flipbook_textures.json` 中定义：

```json title="RP/textures/flipbook_textures.json"
[
    {
        "flipbook_texture": "textures/wiki/blocks/my_animated_block",
        "atlas_tile": "wiki:my_animated_block",
        "ticks_per_frame": 4
    }
]
```

- `flipbook_texture`：纹理文件路径（不带扩展名）。纹理文件的高度应等于宽度乘以帧数（例如16宽×64高表示4帧16×16纹理）。
- `atlas_tile`：该纹理在 `terrain_texture.json` 中的短名，**不需要**在 `terrain_texture.json` 中再次注册。
- `ticks_per_frame`：每帧持续的游戏刻数（20刻=1秒）。

## 制作动画纹理文件

将所有帧垂直排列在一张纹理图片中，从上到下依次是第1帧、第2帧……例如4帧16×16像素的动画，图片尺寸为16×64像素：

```
┌───────┐
│ 帧 1  │  y=0～15
├───────┤
│ 帧 2  │  y=16～31
├───────┤
│ 帧 3  │  y=32～47
├───────┤
│ 帧 4  │  y=48～63
└───────┘
```

## 高级参数

除了基础参数外，翻书纹理还支持以下可选参数：

```json
{
    "flipbook_texture": "textures/wiki/blocks/fire_animation",
    "atlas_tile": "wiki:fire_block",
    "ticks_per_frame": 2,
    "frames": [0, 1, 2, 3, 2, 1],
    "replicate": 2,
    "blend_frames": true,
    "atlas_index": 0,
    "atlas_tile_variant": 3
}
```

/// define
`frames`

- 整数数组，指定播放的帧顺序（从0开始的索引）。省略则按顺序播放所有帧。可以重复或倒序播放。

`replicate`

- 整数，将所有帧在图集中复制的份数。默认为1。用于处理不同分辨率的纹理缩放。

`blend_frames`

- 布尔值，是否在帧之间应用平滑过渡插值。默认为 `true`。设为 `false` 则帧与帧之间直接切换。

`atlas_index`

- 整数，指定纹理在图集中的索引位置。一般不需要手动设置。

`atlas_tile_variant`

- 整数，当纹理有多个变体时，指定使用哪个变体的索引。与[纹理变体](texture-variation.md)配合使用。

///

## 在材质实例中使用

翻书纹理定义好后，在材质实例中直接使用 `atlas_tile` 指定的短名即可，与普通静态纹理写法完全相同：

```json title="BP/blocks/my_block.json > components"
"minecraft:material_instances": {
    "*": {
        "texture": "wiki:my_animated_block",
        "render_method": "opaque"
    }
}
```

不需要在 `terrain_texture.json` 中另外注册翻书纹理——`flipbook_textures.json` 的定义会自动将纹理注册到图集。

/// tip | 水流动画参考
原版水面和熔岩等流动动画都使用翻书纹理机制，可以在原版资源包的 `textures/flipbook_textures.json` 中查看完整配置作为参考。
///
