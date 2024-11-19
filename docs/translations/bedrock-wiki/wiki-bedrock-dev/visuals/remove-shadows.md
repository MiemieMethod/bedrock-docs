---
title: 移除实体阴影
tags:
    - 中级
category: 教程
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - MedicalJewel105
    - SmokeyStack
    - ThomasOrs
description: 摆脱那些恼人的阴影。
---

有很多方法可以移除实体的阴影，而几乎所有方法都有不良影响。没有万无一失的方法可以完美地从特定实体中移除阴影，而不引起副作用。

本文档将展示一些移除阴影的不同方法，以及这样做可能产生的效果。

## 小碰撞盒

一种可能性是将碰撞组件的大小设置得非常小。这将使得很难与该实体进行交互/攻击，但它会使阴影消失！

```json title=""
"minecraft:collision_box": {
    "width": 0.1,
    "height": 0.1
}
```

你还可以添加[自定义命中测试组件](https://bedrock.dev/docs/stable/Entities#minecraft:custom_hit_test)。`custom_hit_test`组件将允许你攻击该实体，尽管你将无法与其交互。`custom_hit_test`不会产生阴影。

```json title=""
"minecraft:custom_hit_test": {
    "hitboxes": [
        {
            "pivot": [0, 0.5, 0],//这是命中盒的位置，你可以更改X、Y和Z值。
            "width": 0.8,
            "height": 0.7
        }//你可以根据需要添加更多命中盒，只需将命中盒复制粘贴到“hitboxes”数组中。
    ]
}
```

## 传送到地下

如果你有一个需要与之交互的虚拟实体（不可见），你可以使用 `/teleport @x ~ ~-0.01 ~` 进行传送。这将稍微将实体插入地下，并阻止阴影显示。

## 使用运行时标识符

某些实体没有阴影，或者至少阴影非常小。通过使用这些实体的运行时标识符，我们可以移除阴影。缺点是需要承担该实体的硬编码行为，这有时可能会非常麻烦。有关更多信息，请参见[运行时标识符文档](../entities/runtime-identifier.md)。

## 使用材质

/// danger
此方法不再支持。随着渲染龙的出现，这种材质不再有效。请不要尝试以严肃的方式使用此代码，绝对不要在市场地图上尝试。
///

/// warning
    - 此文件夹不包含在原版RP包示例中，必须从APK文件导出或手动添加。
    - 此方法尚未针对方块进行测试，仅针对实体进行了验证。如果你发现它也适用于方块，请告诉我们，以便我们添加相关内容。
///

<Spoiler title="通过材质移除阴影。">

#### 有效阴影代码：所有实体的阴影：

```json title="RP/materials/shadows.material"
"shadow_overlay":{
    "+states":[
        "DisableDepthTest",
        "DisableCulling",
        "Blending",
        "EnableStencilTest"
    ],
    "vertexShader":"shaders/color.vertex",
    "vrGeometryShader":"shaders/color.geometry",
    "fragmentShader":"shaders/shadow_stencil_overlay.fragment",
    "blendSrc":"DestColor",
    "blendDst":"Zero",
    "frontFace":{
        "stencilFunc":"Equal",
        "stencilPass":"Replace"
    }
}
```

#### 禁用阴影代码：所有实体无阴影：

```json title=""
"shadow_overlay":{
    "+states":[
        "DisableDepthTest",
        "DisableCulling",
        "Blending",
        "EnableStencilTest"
    ],
    "vertexShader":"",
    "vrGeometryShader":"",
    "fragmentShader":"",
    "blendSrc":"DestColor",
    "blendDst":"Zero",
    "frontFace":{
        "stencilFunc":"Equal",
        "stencilPass":"Replace"
    }
}
```

</Spoiler>

#### 几何体 + 材质变通方法

如果你在实体上应用一个模型以覆盖阴影并使用 `"banner_pole"` 材质，你可以隐藏实体的阴影。