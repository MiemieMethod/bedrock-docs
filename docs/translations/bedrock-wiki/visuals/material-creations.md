---
title: 材质示例
description: 社区整理的几个可复用材质片段。
category: 参考
---


/// details-info | 来源信息
- 原文仓库：[github.com/Bedrock-OSS/bedrock-wiki](https://github.com/Bedrock-OSS/bedrock-wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///

/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/visuals/material-creations](https://wiki.bedrock.dev/visuals/material-creations)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

这一页收录几个常见的材质思路，重点在“能做什么”而不是“为什么这样设计”。

## 发光+半透明

适合做局部发光、半透明边缘等效果。

```json
{
    "customblend:entity_alphablend": {
        "+defines": ["USE_EMISSIVE"],
        "+states": ["Blending", "DisableCulling", "DisableDepthWrite", "DisableAlphaWrite"]
    }
}
```

## RenderDragon下的Alpha纹理

可用于让纹理保留透明通道：

```json
{
    "ambient_alpha:entity": {
        "+states": ["Blending", "DisableCulling"],
        "blendSrc": "SourceAlpha",
        "blendDst": "OneMinusSrcAlpha"
    }
}
```

## 覆盖色相关

有些材质会影响`overlay_color`在渲染控制器中的表现。若要限制覆盖色影响范围，需要根据具体实体逐个测试。

## 注意

这类材质内容高度依赖版本与渲染路径，适合参考，不适合盲抄。