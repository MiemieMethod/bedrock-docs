---
title: 创建方块模型
description: 学习如何为您的方块设置自定义模型。
category: 教程
tags:
    - 初学者
    - 简易
mentions:
    - QuazChick
    - SmokeyStack
---

尽管自定义方块无法使用原版的[方块形状](/blocks/block-shapes)，我们可以创建遵循类似于实体模型格式的自定义模型。本教程将引导您使用[Blockbench](https://blockbench.net)创建一个“纸袋”的自定义方块模型。您应该能够从本教程中学习到Minecraft几何体的主要特性，以便创建自定义方块。

**注意：** 自定义方块模型必须在[模型大小限制](/blocks/block-components.html#geometry)之内。

## 模型设置

打开Blockbench并创建一个新的`Bedrock Block`项目。

![新项目面板，选择了Bedrock Block](/assets/images/blocks/block-models/new_project.png)

现在您可以为模型指定一个标识符！文件名可以在此处决定，或稍后更改。

UV模式和纹理大小应保持不变。

:::danger 命名空间
模型标识符**不带命名空间且不能包含冒号**。冒号以前用于模型继承，在现代几何格式中无效。
:::

![](/assets/images/blocks/block-models/project_settings.png)

## 添加立方体

尽管模型中的元素不一定是完美的立方体形状，但它们被称为**立方体**。所有立方体必须包含在**骨骼**中，骨骼充当组。

首先，从大纲中创建一个根骨骼，点击`添加组`。按`F2`可以重命名骨骼。

![](/assets/images/blocks/block-models/root_bone.png)

“纸袋”模型需要两个立方体：一个用于手柄，一个用于主袋。可以通过选择根骨骼并点击`添加立方体`来添加这些立方体。

<WikiImage src="/assets/images/blocks/block-models/new_cube.png" alt width="600" class="my-4" />

可以通过顶部工具栏移动、调整大小和旋转立方体。以下是我的“paper_bag”模型将使用的两个立方体。

<WikiImage src="/assets/images/blocks/block-models/paper_bag_cubes.png" alt="" width="300" />

## 移除面

我们的一些立方体的面可能不需要可见。在我的例子中，纸袋的顶部面应该被移除，以便可以看到内部。

要移除一个面，请在预览中点击它并删除其UV。

<WikiImage src="/assets/images/blocks/block-models/paper_bag_top_removed.png" alt="" width="600" />

此外，手柄的北面和南面应该是可见的。您可以通过按住Ctrl并点击UV面板中的面名称来选择多个面。

<WikiImage
    src="/assets/images/blocks/block-models/paper_bag_handle_faces_removed.png"
    alt=""
    width="600"
/>

## 预览纹理

:::tip
可以通过点击`创建纹理`并选择`空白`在Blockbench中创建纹理。
:::

“纸袋”模型有多个预制纹理，列举如下：

-   `textures/blocks/paper_bag.png`

    <WikiImage
        src="/assets/images/blocks/block-models/paper_bag.png"
        style="background-color: rgb(0,0,0,0.15);"
        pixelated
        width="128"
    />

-   `textures/blocks/paper_bag_bottom_fold.png`

    <WikiImage
        src="/assets/images/blocks/block-models/paper_bag_bottom_fold.png"
        style="background-color: rgb(0,0,0,0.15);"
        pixelated
        width="128"
    />

-   `textures/blocks/paper_bag_side_gusset.png`

    <WikiImage
        src="/assets/images/blocks/block-models/paper_bag_side_gusset.png"
        style="background-color: rgb(0,0,0,0.15);"
        pixelated
        width="128"
    />

这些可以导入到Blockbench中，然后拖到每个适当的方块面上，尽管它们可能看起来不太正确……

<WikiImage
    src="/assets/images/blocks/block-models/preview_textures_applied.png"
    alt=""
    width="300"
/>

## 重新排列UV

为了将纹理放置到正确的位置，您可能需要重新定位/调整面UV映射的大小。这可以通过选择受影响的面并使用UV面板来完成。

<WikiImage src="/assets/images/blocks/block-models/paper_bag_handle_uv.png" alt="" width="300" />

<WikiImage src="/assets/images/blocks/block-models/paper_bag_final.png" alt="" width="300" />

## 更改材质实例

应用自定义材质实例名称可以轻松定义某些面的渲染方式。

可以通过右键点击立方体并打开`编辑材质实例`进行编辑。

![](/assets/images/blocks/block-models/select_edit_material_instances.png)

对于“纸袋”模型，东面和西面应该有自己的纹理。我们可以通过为它们指定材质实例来表示这一点。

![](/assets/images/blocks/block-models/edit_material_instances.png)

## 应用几何体和纹理

一旦从`文件 > 导出 > 导出Bedrock几何体`导出到您的`RP/models/blocks`文件夹中，您可以在方块JSON中引用模型。

然后，可以通过其`RP/textures/terrian_texture.json`短名称通过材质实例应用纹理。在这个例子中，纸袋不应该阻挡光线，因此其光线减弱设置为0。

:::warning BLOCKS.JSON
将[`minecraft:geometry`](/blocks/block-components#geometry)添加到您的方块将导致游戏忽略`RP/blocks.json`中的纹理定义。

如果您在该文件中定义了方块的纹理，请确保将它们迁移到[`minecraft:material_instances`](/blocks/block-components#material-instances)中，以便它们能够出现。
:::

<CodeHeader>BP/blocks/paper_bag.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:paper_bag",
            "menu_category": {
                "category": "items"
            }
        },
        "components": {
            // 通过引用其标识符应用模型
            "minecraft:geometry": "geometry.paper_bag",
            // 应用纹理和其他渲染配置
            "minecraft:material_instances": {
                "*": {
                    "texture": "paper_bag",
                    "render_method": "alpha_test" // 禁用背面剔除并允许透明
                },
                "down": {
                    "texture": "paper_bag_bottom_fold",
                    "render_method": "alpha_test" // 所有实例中必须相同
                },
                // 模型中使用的自定义实例名称
                "side_gusset": {
                    "texture": "paper_bag_side_gusset",
                    "render_method": "alpha_test" // 所有实例中必须相同
                }
            },
            // 防止阴影
            "minecraft:light_dampening": 0
        }
    }
}
```

## 接下来做什么？

<CardGrid>
<Card
    title="创建剔除规则"
    link="/blocks/block-culling"
    image="/assets/images/homepage/crafting_table_0.png"
>

为您的模型创建剔除规则可以通过告诉游戏不渲染隐藏部分来提高性能。

</Card>
<Card
    title="条件骨骼"
    link="/blocks/block-components#bone-visibility"
    image="/assets/images/homepage/scripting.png"
>

使用[几何体](/blocks/block-components#geometry)组件的“bone_visibility”参数，根据方块的当前排列渲染不同的模型骨骼。

</Card>
</CardGrid>
