---
title: 高分辨率物品
category: 教程
mentions:
    - BlazeDrake
description: 学习如何以正确的方式制作高分辨率纹理的物品。
---

::: tip
本教程使用了附加包。如果您不知道什么是附加包，请先阅读此页面：[附加包](/items/attachables)
:::

## 介绍

在创建物品时，标准的16x16分辨率通常已经足够。然而，有时您可能希望拥有更详细的物品。不过，您可能会注意到高分辨率物品的一个问题：它们看起来更大，而不是更详细！

<WikiImage
	src="/assets/images/items/high-resolution-items/large_item_broken_thirdperson.png"
	alt="替代文本"
	width=1080
/>

解决这个问题的方法是使用附加包在持有时缩小物品的比例。进行这些计算可能需要相当多的调整，因此本页面提供了您需要的代码，以创建一个附加包，将您的物品缩小到正常大小！虽然不是完美的，但它看起来会非常类似于普通物品，只是在旋转和攻击时的动画上有一些细微的差别。它的主要功能是使用动画将物品的大小缩小到应有的尺寸。

## 文件

为了实现这个修复，我们需要一个几何体文件、一个渲染控制器文件、一个附加包文件和一个动画文件。

以下是几何体文件。它的作用是使用纹理网格读取您附加包中使用的纹理，并基于此创建几何体，而无需费力地建模与物品匹配的立方体！此文件不需要任何编辑。

<CodeHeader>RP/models/entity/large_item.geo.json</CodeHeader>

```json
{
    "format_version": "1.16.0",
    "minecraft:geometry": [
        {
            "description": {
                "identifier": "geometry.large_item",
                "texture_width": 16,
                "texture_height": 16,
                "visible_bounds_width": 2,
                "visible_bounds_height": 1.5,
                "visible_bounds_offset": [0, 0.25, 0]
            },
            "bones": [
                {
                    "name": "rightitem",
                    "pivot": [0, 0, 0],
                    "texture_meshes": [
                        {
                            "texture": "default",
                            "position": [0, 0, 0],
                            "local_pivot": [8, 0, 8]
                        }
                    ]
                }
            ]
        }
    ]
}
```

这是渲染控制器文件的样子。这个文件也很简单，因此不需要任何编辑。

<CodeHeader>RP/render_controllers/large_item.render_controllers.json</CodeHeader>

```json
{
    "format_version": "1.8.0",
    "render_controllers": {
        "controller.render.large_item": {
            "geometry": "Geometry.default",
            "materials": [{ "*": "variable.is_enchanted ? Material.enchanted : Material.default" }],
            "textures": ["Texture.default", "Texture.enchanted"]
        }
    }
}
```

这是附加包文件的样子。请注意，您需要将`<identifier>`更改为与您的物品标识符匹配，并将`<path>`替换为您的物品纹理的文件路径（与`item_texture.json`中使用的相同）。

<CodeHeader>RP/attachables/large_item.json</CodeHeader>

```json
{
    "format_version": "1.10.0",
    "minecraft:attachable": {
        "description": {
            //将 <identifier> 替换为您物品的完整标识符
            "identifier": "<identifier>",
            "materials": {
                "default": "entity_alphatest",
                "enchanted": "entity_alphatest_glint"
            },
            "textures": {
                //将 <path> 替换为您物品纹理的文件路径。它应该与 item_texture.json 中给出的文件路径匹配
                "default": "<path>",
                "enchanted": "textures/misc/enchanted_item_glint"
            },
            "geometry": {
                "default": "geometry.large_item"
            },
            "animations": {
                "hold": "animation.large_item.hold"
            },
            "scripts": {
                "animate": ["hold"]
            },
            "render_controllers": ["controller.render.large_item"]
        }
    }
}
```

现在我们已经准备好这些文件，可以创建执行所有魔法的动画！这个动画将旋转您的物品，使其与持有时的原版物品旋转方式相匹配。它还会将您的物品缩小到正确的大小。

<CodeHeader>RP/animations/large_item.animation.json</CodeHeader>

```json
{
    "format_version": "1.10.0",
    "animations": {
        "animation.large_item.hold": {
            "loop": true,
            "bones": {
                "rightitem": {
                    //这些动画将其定位到正确的位置
                    "position": [
                        "c.is_first_person ? -6 : 1",
                        "c.is_first_person ? 0 : -1",
                        "c.is_first_person ? -1 : -6"
                    ],
                    "rotation": [
                        "c.is_first_person ? 45 : 15",
                        "c.is_first_person ? -15 : 0",
                        "c.is_first_person ? 30 : -165"
                    ],
                    "scale": [
                        "c.is_first_person ? 1 : 0.5",
                        "c.is_first_person ? 1 : 0.5",
                        "c.is_first_person ? 1 : 0.5"
                    ]
                }
            }
        }
    }
}
```

## 结果

将所有这些文件放在一起后，您的物品应该看起来好多了！例如，以下是我在第一张图片中使用的物品，当我将本教程中的所有文件添加到资源包中，并将所有适当的值替换为我物品中使用的值时的样子：

<WikiImage
	src="/assets/images/items/high-resolution-items/large_item_fixed_thirdperson.png"
	alt="替代文本"
	width=1080
/>