---
title: 动画中的特效
description: 在动画里直接触发粒子和音效。
category: 教程
---

/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/visuals/animation-effects](https://wiki.bedrock.dev/visuals/animation-effects)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

有些时候，把粒子和音效直接写进动画里，比放在动画控制器里更简单。

## 粒子

在实体定义里先给粒子注册短名称，再在动画的`particle_effects`里按时间点触发。

## 音效

音效的写法与粒子类似，也是在动画时间轴上按时间点播放。

## Blockbench

也可以在Blockbench里直接添加特效和定位器，然后导出到动画文件。

## 离屏更新

如果希望实体不在镜头里时仍然播放这些效果，可以把`scripts.should_update_bones_and_effects_offscreen`设为`true`。