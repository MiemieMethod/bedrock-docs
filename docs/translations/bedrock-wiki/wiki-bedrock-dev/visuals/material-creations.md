---
title: 材料创作
tags:
    - 专家
category: 综合
description: 社区提供的有用材料创作。
---

:::warning
材料创作并不适合胆小的人。请准备好应对潜在的崩溃、内容日志错误和较长的加载时间。
:::

在此页面中，你可以找到社区的材料创作。

## 自定义发光材料与半透明效果

注意：通过禁用剔除可以解决那些奇怪的剔除问题，这样你就可以看到材料应用于的纹理后面的实体和物体。

注意：纹理需要具有半透明效果才能添加发光效果。

“customblend”是你在实体中调用的材料名称。

<Spoiler title="显示">

```json title=""
{
    "customblend:entity_alphablend": {
        "+defines": [
            "USE_EMISSIVE"
        ],
        "+states": [
            "Blending",
            "DisableCulling",
            "DisableDepthWrite",
            "DisableAlphaWrite"
        ]
    }
}
```

</Spoiler>

致谢：StealthyX。

## 带有Render Dragon的Alpha通道纹理

允许使用Alpha通道纹理的材料，适用于Render Dragon：

<Spoiler title="显示">

```json title=""
{
    "ambient_alpha:entity": {
        "+states": [
            "Blending",
            "DisableCulling"
        ],
        "vertexShader": "shaders/color_uv.vertex",
        "vrGeometryShader": "shaders/color_uv.geometry",
        "fragmentShader": "shaders/color_texture.fragment",
        "blendSrc": "SourceAlpha",
        "blendDst": "OneMinusSrcAlpha",
        "vertexFields": [
            {
                "field": "Position"
            },
            {
                "field": "Color"
            },
            {
                "field": "Normal"
            },
            {
                "field": "UV0"
            }
        ],
        "variants": [
            {
                "skinning": {
                    "+defines": [
                        "USE_SKINNING"
                    ],
                    "vertexFields": [
                        {
                            "field": "Position"
                        },
                        {
                            "field": "BoneId0"
                        },
                        {
                            "field": "Color"
                        },
                        {
                            "field": "Normal"
                        },
                        {
                            "field": "UV0"
                        }
                    ]
                }
            }
        ]
    }
}
```

</Spoiler>

经过进一步测试发现，这仅在第三人称视角下有效，但仍然有用，因为无论视角如何，原版混合材料仍然存在问题。

致谢：Ambient。

## render controllers中的overlay_color

不允许在渲染控制器中使用overlay_color的材料：

<Spoiler title="显示">

```json title=""
{
    "materials": {
        "version": "1.0.0",
        "ambient_no_overlay": {
            "defines": [
                "ALPHA_TEST"
            ],
            "vertexShader": "shaders/entity.vertex",
            "vrGeometryShader": "shaders/entity.geometry",
            "fragmentShader": "shaders/entity.fragment",
            "vertexFields": [
                {
                    "field": "Position"
                },
                {
                    "field": "Normal"
                },
                {
                    "field": "UV0"
                }
            ],
            "variants": [
                {
                    "skinning": {
                        "+defines": [
                            "USE_SKINNING"
                        ],
                        "vertexFields": [
                            {
                                "field": "Position"
                            },
                            {
                                "field": "BoneId0"
                            },
                            {
                                "field": "Normal"
                            },
                            {
                                "field": "UV0"
                            }
                        ]
                    }
                },
                {
                    "skinning_color": {
                        "+defines": [
                            "USE_SKINNING"
                        ],
                        "+states": [
                            "Blending"
                        ],
                        "vertexFields": [
                            {
                                "field": "Position"
                            },
                            {
                                "field": "BoneId0"
                            },
                            {
                                "field": "Color"
                            },
                            {
                                "field": "Normal"
                            },
                            {
                                "field": "UV0"
                            }
                        ]
                    }
                }
            ],
            "msaaSupport": "Both",
            "+samplerStates": [
                {
                    "samplerIndex": 0,
                    "textureFilter": "Point"
                },
                {
                    "samplerIndex": 1,
                    "textureWrap": "Repeat"
                }
            ]
        }
    }
}
```

</Spoiler>

可能对特定骨骼而非整个几何体的应用有用。

致谢：Ambient。

## entity_alphablend_nocolorentity_static 材料

使用`entity_alphablend_nocolorentity_static`材料会可靠地导致Minecraft崩溃。

致谢：Gecko。