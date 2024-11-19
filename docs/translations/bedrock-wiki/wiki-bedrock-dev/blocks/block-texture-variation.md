---
title: 纹理变化
description: 块纹理变化是指一种块类型可以根据其在世界中的位置随机应用多种纹理。
category: 教程
tags:
    - 中级
mentions:
    - SirLich
    - solvedDev
    - Hatchibombotar
    - SmokeyStack
    - MedicalJewel105
    - QuazChick
---

/// warning | 材料实例
[材料实例](../blocks/block-components.md#material-instances)组件不支持纹理变化。要应用变化纹理，你必须确保块上没有应用[几何体](../blocks/block-components.md#geometry)组件，并且纹理必须在`RP/blocks.json`中引用。
///

块纹理变化是指一种块类型可以根据其在世界中的位置随机应用多种纹理。这对于像泥土或草地这样的块非常有用，因为某些块可能有细微的变化，例如小石头，而其他块则没有。

**问题：**

-   引用纹理集文件的变化不使用定义的高度图、MER或法线图文件（[MCPE-126617](https://bugs.mojang.com/browse/MCPE-126617)）。

## 应用纹理变化

要启用纹理变化，请在资源包的`textures`文件夹中创建一个`terrain_texture.json`文件。

该文件包含块纹理的列表。变化的块纹理具有一个`variation`参数，这是一个不同纹理的数组，这些纹理将随机显示在块上。通过使用`weight`参数，可以使某些纹理变化比其他变化更常见（[见此处](#weighted-texture-variation)）。

以下是如何为原版泥土块创建3种纹理变化的示例：

-   创建或修改三种泥土纹理，命名为`dirt0.png`、`dirt1.png`和`dirt2.png`。
-   将`dirt0.png`、`dirt1.png`和`dirt2.png`复制到路径变量中指定的位置。如果你想保持整洁，可以包含额外的文件夹。
-   将以下内容添加到泥土的纹理条目中：

```json title="RP/textures/terrain_texture.json"
{
    "texture_name": "atlas.terrain",
    "resource_pack_name": "wiki", // 你的资源包ID
    "num_mip_levels": 4, // 从远处或角度查看时的纹理质量
    "padding": 8, // 防止纹理在视觉上溢出到彼此中
    "texture_data": {
        "dirt": {
            "textures": {
                "variations": [
                    { "path": "textures/blocks/dirt0" },
                    { "path": "textures/blocks/dirt1" },
                    { "path": "textures/blocks/dirt2" }
                ]
            }
        }
    }
}
```

## 加权纹理变化

在使用上述示例后，你可能想要调整权重，编辑`terrain_textures.json`以包含权重字段，如下所示。

要计算纹理变化的可能性，请将所有权重相加（在此情况下为70 + 20 + 10 = 100），然后将权重除以这个总和。例如，选择`dirt0`变化的概率为70 &div; 100，因此如果在该位置放置泥土，70%的位置将显示`dirt0`。

```json title="RP/textures/terrain_texture.json"
{
    "texture_name": "atlas.terrain",
    "resource_pack_name": "wiki", // 你的资源包ID
    "num_mip_levels": 4, // 从远处或角度查看时的纹理质量
    "padding": 8, // 防止纹理在视觉上溢出到彼此中
    "texture_data": {
        "dirt": {
            "textures": {
                "variations": [
                    { "path": "textures/blocks/dirt0", "weight": 70 },
                    { "path": "textures/blocks/dirt1", "weight": 20 },
                    { "path": "textures/blocks/dirt2", "weight": 10 }
                ]
            }
        }
    }
}
```