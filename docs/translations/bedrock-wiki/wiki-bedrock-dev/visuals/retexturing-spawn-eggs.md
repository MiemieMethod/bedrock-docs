---
title: 重新纹理生成蛋
tags:
    - 初学者
category: 教程
mentions:
    - SirLich
    - Joelant05
    - MedicalJewel105
    - aexer0e
description: 更改生成蛋的默认纹理。
---

自定义实体将自动生成一个生成蛋。这个生成蛋可以在创意菜单中找到，名称类似于 `item.spawn_egg.entity.wiki:my_entity.name`。如果你想重命名你的生成蛋并设置纹理，可以在语言文件中进行。

在本教程中，我们将重新纹理生成蛋，使其看起来更像你生成的物品，而不是一个蛋。

## 创建纹理

你可以使用 Blockbench 软件轻松截取实体的屏幕截图。加载模型，然后从下拉菜单中选择导出截图。

如果你不想要这样的图像，也可以创建自己的像素艺术，或者使用任何你喜欢的图像。

## 添加纹理

在 `textures/items/` 下添加纹理文件。我个人建议创建一个 `eggs` 文件夹来存放所有生成蛋的纹理。例如，`textures/items/eggs/my_entity.png`。文件本身应该是正方形的。

## 给纹理命名

现在我们需要给我们的纹理一个短名称。这可以在 item_texture 文件中完成：

```json title="RP/textures/item_texture.json"
{
	"resource_pack_name": "我的地图名称", //我不确定这个字段是否有用。
	"texture_name": "atlas.items",
	"texture_data": {
		"my_entity": { //"my_entity" 是纹理的短名称，我们可以在后面引用
			"textures": "textures/items/egg/my_entity"
		}
        //在这里添加更多生成蛋纹理
    }
}
```

## 使用新纹理：

现在我们可以在资源包实体文件中使用我们的新纹理：

```json title="RP/entity/my_entity.json#description"
"spawn_egg": {
    "texture": "my_entity", //"my_entity" 应与我们在第一步创建的纹理短名称匹配。
    "texture_index": 0
}
```

现在去测试一下吧！