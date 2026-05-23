# 使用Aseprite序列帧动画<!-- md:flag vanilla -->

本页介绍如何把Aseprite导出的精灵表动画接入JSON UI的`image`控件，并说明`aseprite_flip_book`的最小接入方式。

## 准备工具

- [Aseprite](https://www.aseprite.org/)
- [LibreSprite](https://libresprite.github.io/)（Aseprite开源分支）

## 导出要求

1. 在Aseprite中完成序列帧并导出精灵表。
2. 导出JSON描述时选择数组模式。
3. 保证图像文件与JSON描述文件同名，仅扩展名不同。

## JSON UI接入

```json title="RP/ui/example_file.json"
{
  "image_element": {
    "type": "image",
    "texture": "textures/ui/my_sprite_file",
    "uv_size": [32, 32],
    "uv": "@example_namespace.image_uv_animation"
  },
  "image_uv_animation": {
    "anim_type": "aseprite_flip_book",
    "initial_uv": [0, 0]
  }
}
```

## 关键点

- `texture`填精灵表路径，不写扩展名。
- `uv_size`应与单帧尺寸一致。
- `aseprite_flip_book`仅控制UV播放，控件本体仍是`image`。
