---
title: 材料
tags:
    - 专家
category: 一般
mentions:
    - SirLich
    - Joelant05
    - MedicalJewel105
    - Luthorius
description: 了解Minecraft基岩版中的材料。
---

:::warning
材料并不适合心志脆弱的人。请准备好应对潜在的崩溃、内容日志错误和较长的加载时间。
:::

## 概述

材料用于指定渲染游戏不同部分的着色器，以及着色器在处理每个元素时应考虑的状态和设置。目前，游戏中的大多数内容都是硬编码为使用特定材料，无法分配新的材料。更改这些元素的渲染方式的唯一方法是直接编辑它们的材料（可能会对其他部分产生意想不到的影响）或创建新的着色器（这是一个不再由Mojang官方支持的旧实验性功能）。唯一允许分配或移除默认或自定义材料的元素是实体和粒子。

如果你不准备深入了解材料的细节，可以在[这里](../documentation/materials.md)找到材料预设。

## 语法和结构

大多数材料继承先前定义材料的设置，然后在此基础上进一步构建。其格式如下：

```json title="RP/materials/name.material"
{
	"materials": {
		"version": "1.0.0",
		"<新材料ID>:<用作基础的材料ID>": {
    		<定义、状态和其他设置>
		}
	}
}
```

:::warning
尽管看起来相似，但不要混淆包中的材料格式文件。材料中不使用命名空间。
:::

一些材料文件包含广泛的材料分支树。例如，几乎所有默认实体使用的材料最终都是材料`entity_static`在entity.material文件中的派生物。如果我们查看当前村民使用的材料：

```json title=""
"villager_v2_masked:entity_multitexture_masked": {
    "depthFunc": "LessEqual"
},
```

我们可以看到材料的名称是`villager_v2_masked`，并且基于名为`entity_multitexture_masked`的材料。在文件中向上滚动，我们可以找到“entity_multitexture_masked”继承自“entity_alphatest”的设置，并在此基础上进一步构建：

```json title=""
"entity_multitexture_masked:entity_alphatest":{
    "+defines":[
        "MASKED_MULTITEXTURE"
    ],
    "+samplerStates":[
        {
            "samplerIndex":0,
            "textureWrap":"Clamp"
        },
        {
            "samplerIndex":1,
            "textureWrap":"Clamp"
        }
    ]
}
```

“entity_alphatest”可以继续追溯到“entity_nocull”

```json title=""
"entity_alphatest:entity_nocull":{
    "+defines":[
        "ALPHA_TEST"
    ],
    "+samplerStates":[
        {
            "samplerIndex":1,
            "textureWrap":"Repeat"
        }
    ],
    "msaaSupport":"Both"
}
```

可以继续追溯到普通的“entity”

```json title=""
"entity_nocull:entity":{
    "+states":[
        "DisableCulling"
    ]
}
```

最终可以追溯到“entity_static”

```json title=""
"entity:entity_static":{
    "+defines":[
        "USE_OVERLAY"
    ],
    "msaaSupport":"Both"
},
```

“entity_static”后面没有冒号和其他材料，表明它是这个继承树的底部。

```json title=""
"entity_static":{
    "vertexShader":"shaders/entity.vertex",
    "vrGeometryShader":"shaders/entity.geometry",
    "fragmentShader":"shaders/entity.fragment",
    "vertexFields":[
        {
            "field":"Position"
        },
        {
            "field":"Normal"
        },
        {
            "field":"UV0"
        }
    ],
    "variants":[
        {
            "skinning":{
                "+defines":[
                    "USE_SKINNING"
                ],
                "vertexFields":[
                    {
                        "field":"Position"
                    },
                    {
                        "field":"BoneId0"
                    },
                    {
                        "field":"Normal"
                    },
                    {
                        "field":"UV0"
                    }
                ]
            }
        },
        {
            "skinning_color":{
                "+defines":[
                    "USE_SKINNING",
                    "USE_OVERLAY"
                ],
                "+states":[
                    "Blending"
                ],
                "vertexFields":[
                    {
                        "field":"Position"
                    },
                    {
                        "field":"BoneId0"
                    },
                    {
                        "field":"Color"
                    },
                    {
                        "field":"Normal"
                    },
                    {
                        "field":"UV0"
                    }
                ]
            }
        }
    ],
    "msaaSupport":"Both",
    "+samplerStates":[
        {
            "samplerIndex":0,
            "textureFilter":"Point"
        }
    ]
}
```

## 1.16.100+ 注意事项

警告：任何使用自定义材料的人！

自定义材料继承不再有效，会导致内容日志错误，解决方法是完全自定义定义材料，仅使用前缀和材料名称。

在1.16.100之前，这不是一个问题。

```json
{
    "materials": {
        "version": "1.0.0",
        "prefix:window_glass:entity": { //现在会抛出内容日志错误。
            "+states": [
                "Blending"
            ],
            "defines": [
                "ENABLE_FOG",
                "ENABLE_LIGHT",
                "USE_ONLY_EMISSIVE"
            ]
        },
        "prefix:window_glass:": { //修正内容日志错误。注意：可能还需要定义旧的继承值。
            "+states": [
                "Blending"
            ],
            "defines": [
                "ENABLE_FOG",
                "ENABLE_LIGHT",
                "USE_ONLY_EMISSIVE"
            ]
        }
    }
}
```