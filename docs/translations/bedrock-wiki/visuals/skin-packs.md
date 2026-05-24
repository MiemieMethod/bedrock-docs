---
title: 皮肤包
description: 皮肤包的基本结构与常见注意事项。
category: 教程
---


/// details-info | 来源信息
- 原文仓库：[github.com/Bedrock-OSS/bedrock-wiki](https://github.com/Bedrock-OSS/bedrock-wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///

/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/visuals/skin-packs](https://wiki.bedrock.dev/visuals/skin-packs)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

皮肤包用于分发玩家皮肤。它本质上仍然是一个附加包，只是模块类型不同，重点放在`skins.json`、本地化文件和皮肤纹理上。

## 需要什么

典型皮肤包至少包含：

- `manifest.json`
- `skins.json`
- `texts/en_US.lang`
- 皮肤纹理PNG

## `skins.json`

这个文件定义每个皮肤的纹理、几何体、本地化名称与类型。最常见的字段是：

- `localization_name`：皮肤条目的本地化键。
- `texture`：皮肤纹理文件名。
- `geometry`：皮肤所用几何体。
- `type`：通常设为`free`。

## 几何体

皮肤包一般只使用标准体型或纤细体型。自定义几何体在早期版本中曾可行，但官方已收紧这一能力，因此不要把它当作稳定方案。

## 角色创建器

角色创建器与传统皮肤包是两个独立系统。前者更接近部件式外观组合，后者则是整张皮肤纹理的分发方式。

## 注意事项

`development_skin_packs`在一些版本中表现不稳定，实际测试时通常仍然建议使用`skin_packs`目录并重启游戏验证结果。