---
title: 附加包
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - ChilRx
    - SmokeyStack
    - MedicalJewel105
    - TheItsNameless
description: 附加包允许您在不同的附加包“配置”之间进行选择。
---

## 什么是附加包？

附加包允许您在不同的附加包“配置”之间进行选择。

它们旨在根据不同的内存容量加载纹理分辨率，但也可以用于创建行为和资源包的文件变体。这些变体可以通过点击齿轮图标并调整滑块来选择。

## 附加包如何工作？

放置在您的附加包文件夹中的文件将覆盖放置在主附加包文件夹中的文件，前提是选择了该附加包。例如，如果您的附加包同时包含 `RP/textures/entities/ghost.png` 和 `RP/subpacks/pack_1/textures/ghost.png`，则第二个图像文件将在选择附加包 `pack_1` 时替换第一个。

有关文件如何相互覆盖的更多信息，请参见我们关于 [覆盖原版资源](../concepts/overwriting-assets.md) 的页面。

## 创建附加包

-   要开始添加附加包，您需要在 `BP`/`RP` 的根目录下创建一个 `subpacks` 文件夹。
-   然后在 `subpacks` 文件夹内为每个您想要的附加包添加一个文件夹，例如：

<FolderView :paths="[
	'RP/subpacks/subpack_1',
	'RP/subpacks/subpack_2'
]"></FolderView>

-   在这些文件夹内，您可以添加每个附加包的内容。
    这可以是通常放在您的行为包或资源包中的任何内容。
    例如：

<FolderView :paths="[
	'RP/subpacks/subpack_1/textures/blocks/dirt.png',
	'RP/subpacks/subpack_1/textures/items/example_item.png',
	'RP/subpacks/subpack_2/textures/blocks/dirt.png',
	'RP/subpacks/subpack_2/textures/items/example_item.png'
]"></FolderView>

## 清单部分

要在清单中注册附加包，您需要添加 `subpacks`，并且这包含一个附加包数组。

示例：

<CodeHeader>RP/manifest.json</CodeHeader>

```json
{
	"format_version": 2,
	"header": {
		"name": "包名称",
		"description": "包描述",
		"uuid": "2fc2dd6f-86cb-4370-af70-21490a1ae471",
		"version": [1, 0, 0],
		"min_engine_version": [1, 13, 0]
	},
	"modules": [
		{
			"type": "resources",
			"uuid": "f6821b4a-1854-44fc-a8a4-0c2847ffda46",
			"version": [1, 0, 0]
		}
	],
	"subpacks": [
		{
			"folder_name": "subpack_1",
			"name": "第一个附加包",
			"memory_tier": 0
		},
		{
			"folder_name": "subpack_2",
			"name": "第二个附加包",
			"memory_tier": 1
		}
	]
}
```

-   `name` - 在选择附加包时显示的名称。

-   `memory_tier` - 设备必须具备的RAM数量，以启用此附加包。1个内存级别 = 0.25 GB。

-   `folder_name` - 用于此附加包的文件夹名称，例如在上述示例中，这将是 `subpack_1` 或 `subpack_2`。

## 已知事项

如果您只添加一个附加包，附加包选择部分将有两个选项，但第二个分辨率（实际上没有附加包）并不会使根文件夹中的内容覆盖附加包。