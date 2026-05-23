---
title: 发光纹理
description: 通过纹理和材质制作发光效果。
category: 教程
---

/// details-info | 署名信息
- 该页面内容翻译自[Glowing Entity Texture](https://wiki.bedrock.dev/visuals/glowing-texture.html)
- 原文版权归原作者所有
///

这个技巧的目标是做出类似末影人眼睛那样的发光纹理。

## 纹理

先在图像编辑器里把想发光的区域“半擦除”，也就是降低透明度，但不要完全擦掉。

## 材质

然后在客户端实体里把材质切到`entity_emissive_alpha`一类支持发光通道的材质。

```json
"materials": {
    "default": "entity_emissive_alpha"
}
```

## 测试

进游戏后，在夜晚或洞穴里观察效果。若纹理和材质都正确，发光会非常明显。
