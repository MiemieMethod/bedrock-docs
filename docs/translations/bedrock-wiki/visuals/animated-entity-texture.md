---
title: 实体纹理动画
description: 让实体纹理像方块翻书动画一样播放。
category: 教程
---

/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/visuals/animated-entity-texture](https://wiki.bedrock.dev/visuals/animated-entity-texture)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

这个技巧的思路很简单：把多帧纹理竖着排，再让材质与渲染控制器按时间去切换UV。

## 纹理

先准备一张竖向排列的多帧纹理，每一帧占据同一尺寸。

## 材质

让材质启用`USE_UV_ANIM`，这样渲染器才会按UV动画方式取帧。

```json
{
    "materials": {
        "version": "1.0.0",
        "custom_animated:entity": {
            "+defines": ["USE_UV_ANIM"]
        }
    }
}
```

## 渲染控制器

在`uv_anim`里用`life_time`和帧数计算偏移与缩放即可。

## 结论

适合做眨眼、呼吸、状态条、闪烁灯光这类“连续但不需要骨骼动画”的效果。