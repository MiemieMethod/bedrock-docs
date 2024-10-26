---
title: Aseprite 动画
category: 教程
mentions:
    - TheDataLioness
    - shanewolf38
    - TheItsNameless
    - LeGend077
    - stirante
description: 在 JSON-UI 中使用 Aseprite 动画。
---

## Aseprite 简介

[Aseprite](https://www.aseprite.org/) 是一款付费的像素艺术应用程序，专为轻松创建皮肤和资源包而设计。它提供了丰富的工具、详尽的文档和教程，适合各个技能水平的艺术家使用。

[LibreSprite](https://libresprite.github.io/) 是 Aseprite 的一个免费开源替代品。它是 Aseprite 最后一个开源许可版本的分支，本教程同样适用于 LibreSprite。

## 在 Aseprite 中创建动画

假设你有一系列名为“frameimage”的帧图像，序号从 1 到 5。导入第一张图像后，Aseprite 会自动识别其他同名但序号不同的图像，并将它们按正确顺序排列，创建动画。

<FolderView
:paths="[
    'frameimage1.png',
    'frameimage2.png',
    'frameimage3.png',
    'frameimage4.png',
    'frameimage5.png'
]"
></FolderView>

使用 `方向键` 在所有帧之间导航，使用 `回车` 键播放或暂停动画。按 `Tab` 键打开时间轴并选择单独的帧。在时间轴中右键单击某一帧以访问各种设置。

要导出动画，请使用快捷键 `Ctrl + E` 或导航至 `文件 -> 导出到精灵表`。在输出设置中，选择输出文件和 JSON 数据。你会看到一个下拉菜单，包含 Hash 和 Array 选项。确保选择 Array 选项，否则导出将无法正常工作。

现在你应该有两个文件：精灵表图像和一个 JSON 文件。确保这两个文件具有相同的名称但不同的扩展名。

## 在 JSON-UI 中使用 Aseprite 动画

`aseprite_flip_book` 动画类型只能用于类型为 `image` 的元素的 `uv` 属性。

<CodeHeader>RP/ui/example_file.json</CodeHeader>
```json
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

将 `texture` 字段设置为导出文件的路径，不带扩展名。`uv_size` 字段应设置为单个帧的宽度和高度。