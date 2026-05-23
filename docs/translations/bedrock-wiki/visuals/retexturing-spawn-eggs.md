---
title: 重绘刷怪蛋纹理
description: 为自定义实体刷怪蛋更换纹理。
category: 教程
---

/// details-info | 署名信息
- 该页面内容翻译自[Retexturing Spawn Eggs](https://wiki.bedrock.dev/visuals/retexturing-spawn-eggs.html)
- 原文版权归原作者所有
///

自定义实体会自动获得刷怪蛋。若希望它在创造模式物品栏中更像实体本身，可以为这个刷怪蛋重新指定纹理。

## 纹理文件

先准备一张正方形PNG纹理。可以截取实体图，也可以直接绘制像素图。

## 放到资源包

把图片放进资源包的`textures`目录，并建议为项目单独建子目录，避免与其他包冲突。

## 注册短名称

在`item_texture.json`里为刷怪蛋纹理注册短名称：

```json
{
    "texture_data": {
        "wiki:custom_entity_spawn_egg": {
            "textures": "textures/wiki/items/spawn_egg/custom_entity"
        }
    }
}
```

## 在实体文件中引用

在客户端实体定义里，把刷怪蛋纹理设为刚才注册的短名称：

```json
"spawn_egg": {
    "texture": "wiki:custom_entity_spawn_egg",
    "texture_index": 0
}
```

完成后，这个实体的刷怪蛋就会使用新纹理。
