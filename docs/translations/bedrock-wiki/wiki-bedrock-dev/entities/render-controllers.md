---
title: 渲染控制器
category: 一般
tags:
    - 初学者
mentions:
    - SirLich
    - MedicalJewel105
    - Overload252
    - ChibiMango
description: 了解渲染控制器。
---

渲染控制器是资源包中一个常常被误解的部分。但你不需要害怕！你可以将渲染控制器视为逻辑包，它从RP实体文件中获取短名称定义，并确定它们在游戏中如何组合、分层和渲染。

## 定义短名称

渲染控制器基于RP实体文件的短名称定义工作。短名称是本地标识符，我们在RP实体文件中定义，然后可以在渲染控制器（以及其他地方）中使用。诸如`geometry`、`materials`和`textures`等变量可以在实体中定义。

让我们看一个简化版的蜘蛛RP实体文件：

```json title="RP/entity/spider.json"
{
	"format_version": "1.8.0",
	"minecraft:client_entity": {
		"description": {
			"identifier": "minecraft:cave_spider",
			"materials": {
				"default": "spider",
				"invisible": "spider_invisible"
			},
			"textures": {
				"default": "textures/entity/spider/cave_spider"
			},
			"geometry": {
				"default": "geometry.spider.v1.8"
			},
			"render_controllers": ["controller.render.spider"]
		}
	}
}
```

在这种情况下，创建了四个短名称定义：

- `default`，在材料数组中
- `invisible`，在材料数组中
- `default`，在纹理数组中
- `default`，在几何体数组中

你可以在每个数组中定义多个短名称，例如上面的`materials`示例。

你应该将短名称定义视为`导入`你想要的资产。在这个阶段，你定义了想要在实体中使用的纹理、几何体和材料。在渲染控制器阶段，你不会导入任何东西。你只需使用已经导入的资产来创建渲染的实体。

## 简单渲染控制器

一个简单的渲染控制器如下所示：

```json title="RP/render_controllers/cow.render.json"
{
	"format_version": "1.8.0",
	"render_controllers": {
		"controller.render.cow": {
			"geometry": "Geometry.default",
			"materials": [
				{
					"*": "Material.default"
				}
			],
			"textures": ["Texture.default"]
		}
	}
}
```

这个控制器从实体文件中获取短名称定义并进行`渲染`。例如，行`"textures": [ "Texture.default"]`表示：“获取默认纹理，并将其应用于实体”。渲染控制器并不知道默认纹理是什么；它只是简单地应用它。

## 重用渲染控制器

由于渲染控制器基于短名称工作，因此可以为所有实体重用相同的渲染控制器。对于具有一个材料、一个纹理和一个几何体的简单实体，不需要自定义渲染控制器。

例如，上面的渲染控制器用于`minecraft:cow`实体。如果你想在自己的包中使用这个渲染控制器，只需在实体文件中定义为：`"render_controllers": [ "controller.render.cow" ]`。

/// warning | 请记住！
渲染控制器基于短名称工作。如果你想使用牛的渲染控制器，你需要提供它所使用的短名称。在这种情况下，你需要提供：

- `default`几何体
- `default`纹理
- `default`材料
///

## 创建自定义渲染控制器

我们通常希望对实体的渲染有更多控制，例如渲染分层纹理、多种几何体或将不同材料应用于不同骨骼。要创建自定义渲染控制器，只需将原版渲染控制器复制并粘贴到`render_controllers`文件夹中，然后根据需要进行编辑！

## 纹理分层

有时，为自定义实体创建分层纹理是有帮助的。在这个上下文中，分层仅意味着多个纹理叠加在一起，其中顶部纹理具有透明像素并允许底部纹理透出。

作为一个简单的例子，想象一个**画作**实体。画作的框架始终是相同的，但画面本身可以改变。虽然你可以复制框架10次并绘制10幅画，但你现在创建了一个问题：如果你想更改框架呢？现在你需要编辑10个纹理。

这可以通过纹理分层来解决。只需先放置框架纹理，然后在上面添加不同的画作。你现在可以在一个简单的位置编辑框架。

或者，你甚至可以为每幅画作创建多个框架！这允许你在画作实体中增加更多的变化，因为玩家可以独立更改两个纹理。

### 渲染控制器

纹理分层是通过使用渲染控制器实现的。如果你对渲染控制器不熟悉，应该查看原版的用法。像`horse`这样的实体，包含多个纹理，是值得关注的。

### 纹理分层

#### 渲染控制器

```json title="RP/render_controllers/controller.render.texture_layering.json"
{
	"format_version": "1.10.0",
	"render_controllers": {
		"controller.render.texture_layering": {
			"geometry": "Geometry.default",
			"materials": [
				{
					"*": "Material.default"
				}
			],
			"textures": [
				//你可以添加任意多的层。层是从上到下添加的。
				"Texture.bottom_layer",
				"Texture.top_layer"
			]
		}
	}
}
```

#### 实体

你需要在实体中定义所有纹理，并使用`villager_v2_masked`材料。

```json title="RP/entity/my_entity.json"
"materials": {
	"default": "villager_v2_masked"
},
"textures": {
	"top_layer": "textures/top",
	"bottom_layer": "textures/bottom"
  //在这里添加更多纹理短名称定义。
}
```

### 带有变化的纹理分层

虽然我认为硬编码的分层纹理很酷，但真正的乐趣在于让纹理动态：

#### 实体

设置多个顶部纹理，稍后我们将进行索引。

```json title="RP/entity/my_entity.json#description"
"textures": {
	"top_1": "textures/top_1",
	"top_2": "textures/top_2",
	"top_3": "textures/top_3",
	"bottom_layer": "textures/bottom"
}
```

#### 渲染控制器

```json title="RP/render_controllers/controller.render.wool_only"
{
	"format_version": "1.10.0",
	"render_controllers": {
		"controller.render.wool_only": {
			"arrays": {
				"textures": {
					"Array.top": [
						"Texture.top_1",
						"Texture.top_2",
						"Texture.top_3"
					]
				}
			},
			"geometry": "Geometry.default",
			"materials": [
				{
					"*": "Material.default"
				}
			],
			"textures": [
				"Texture.bottom", //静态底部纹理
				"Array.top[q.variant]" //根据实体变体选择顶部纹理。
			]
		}
	}
}
```

通过使用数组和`q.variant`，我们可以根据实体的`variant`选择顶部纹理。

#### 设置变体

现在，为了选择哪个层将显示，我们只需在实体中设置变体组件：

```json title="BP/entities/my_entity.json#components"
"minecraft:variant": {
	"value": 0
}
```

请记住，像变体这样的组件是零索引的，这意味着`0`是我们的第一个纹理，然后`1`和`2`指向第二个和第三个。

#### 动态改变纹理

如果你想在游戏过程中动态改变实体的纹理，你只需改变`variant`。这可以通过组件组和事件来完成。

#### 动态分层纹理

动态分层纹理可以通过添加更多纹理列表和其他虚拟组件作为索引来实现。你可以在[这里](https://example.com)阅读关于虚拟组件的内容。

### 动态替代几何体

动态改变几何体的方式几乎与改变纹理相同。

在以下示例中，你可以看到一个渲染控制器设置为根据变体更改实体的几何体。就像在纹理中一样，你写下几何体的顺序决定了它们的编号顺序。顶部为0。
当我们改变变体时，它将使用不同的几何体。

请注意，与纹理不同，你不能分层几何体，因此不应包含“基础底层”几何体。
这仍然需要使用`villager_v2_masked`材料。

```json title="RP/render_controllers/controller.render.player.third_person.json"
{
	"format_version": "1.8.0",
	"render_controllers": {
		"controller.render.player.third_person": {
			"materials": [
				{
					"*": "Material.default"
				}
			],
			"textures": [
				"Texture.bottom",
				"Array.top[q.variant]"
			],
			"arrays": {
				"geometries": {
					"Array.geo": [
						"Geometry.default",
						"Geometry.custom_1",
						"Geometry.custom_2"
					]
				},
				"textures": {
					"Array.top": [
						"Texture.bottom",
						"Texture.top_1",
						"Texture.top_2"
					]
				}
			},
			"geometry": "Array.geo[q.variant]"
		}
	}
}
```

#### 实体

记得在实体文件中包含几何体变体。

```json title=""
"geometry": {
	"default": "geometry.entity.default",
	"custom_1": "geometry.entity.custom_1",
	"custom_2": "geometry.entity.custom_2"
}
```

## 常见错误

在渲染控制器中，你可以有多个纹理引用，但只能有一个几何体引用。这也适用于数组。

```json
"arrays": {
    "textures": {
        "array.skin": [],
        "array.dress": []
    },
    "geometries": {
        "array.geo": []
    }
}
```

接着是：

```json
"textures": [
    "array.skin[q.variant]",
    "array.dress[q.skin_id]"
],
"geometry": "array.geo[q.mark_variant]"
```