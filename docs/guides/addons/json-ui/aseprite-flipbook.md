# 使用Aseprite序列帧动画<!-- md:flag vanilla -->

本页介绍如何把Aseprite导出的精灵表动画接入JSON UI的`image`控件，并说明`aseprite_flip_book`的最小接入方式。

## 准备工具

- [Aseprite](https://www.aseprite.org/)
- [LibreSprite](https://libresprite.github.io/)（Aseprite开源分支）

## 在Aseprite中制作动画

1. 打开Aseprite，新建或打开已有的精灵文件。
2. 按序制作每一帧动画。可以通过"File > Import Sprite Sheet"将已有的精灵表按行列切割为序列帧，也可以逐帧手绘。
3. 完成后，按++ctrl+e++打开导出对话框（"File > Export Sprite Sheet"）。
4. 在导出对话框中：
   - **Layout** 标签：将排列方式（Sheet type）设为**Horizontal Strip**（横向排列，一行多帧）。
   - **Output** 标签：勾选 **Output File**，设置图片输出路径；同时勾选 **JSON Data**，选择数组模式（**Array**）。
5. 点击 **Export** 导出精灵表图片（`.png`）和对应的JSON描述文件（`.json`）。

/// tip | 命名规范
导出时建议让图片文件与JSON文件同名，仅扩展名不同。例如`my_sprite.png`与`my_sprite.json`。JSON UI的`aseprite_flip_book`依赖这一命名约定来自动匹配数据文件。
///

## JSON UI接入

将图片放入资源包的`textures/`目录，然后在UI文件中引用：

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
- JSON描述文件与图片同名放置，引擎会自动读取帧时序数据。