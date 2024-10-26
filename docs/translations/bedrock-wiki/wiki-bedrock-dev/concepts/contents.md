---
标题：contents.json
提及：
    - MedicalJewel105
    - Osaxely
    - SirLich
    - solvedDev
    - Joelant05
    - Jorginhor
    - TheItsNameless
描述：contents.json 是一个文件，可能用于游戏更轻松地处理包文件。它可能是为市场内容创作者和Mojang准备的，包正常工作并不需要这个文件。
---

`contents.json` 是一个文件，_可能_ 用于游戏更轻松地处理包文件。它 _可能_ 是为市场内容创作者和Mojang准备的，包正常工作并不需要这个文件。

您将在此找到有关此文件使用的说明。

## 文件结构

`contents.json` 位于附加包目录的根目录。它包含包中包含的文件列表。
示例：

<CodeHeader>RP/contents.json</CodeHeader>

```json
{
	"content": [
		{
			"path": "texts/en_US.lang"
		},
		{
			"path": "contents.json"
		},
		{
			"path": "manifest.json"
		},
		{
			"path": "animations/my_animation.animation.json"
		},
		{
			"path": "animation_controllers/my_ac.ac.json"
		},
		{
			"path": "entity/my_entity.entity.json"
		},
		{
			"path": "textures/textures_list.json"
		},
		{
			"path": "textures/blocks/my_block.png"
		}
	]
}
```

<FolderView
	:paths="[
    'RP/texts/en_US.lang',
    'RP/manifest.json',
    'RP/contents.json',
    'RP/animations/my_animation.animation.json',
    'RP/animation_controllers/my_ac.ac.json',
    'RP/entity/my_entity.entity.json',
    'RP/textures/texture_list.json',
    'RP/textures/blocks/my_block.png'
]"
> </FolderView>

## 自动化过程

`contents.json` 文件可以由游戏自动生成，强烈建议这样做以减少出错的风险。然而，文件必须先准备好。在您的附加包根目录中创建一个名为 `contents.json` 的新空文件，并添加空括号。

<CodeHeader>BP|RP/contents.json</CodeHeader>

```json
{}
```

文件内容将在下次启动游戏时自动写入。

## 附加信息

-   无论包的位置（开发文件夹或正常文件夹），都可以实现自动化过程。
-   不要为子包创建多个 `contents.json`，包根目录中的文件就足够了。
-   此文件不是附加包正常工作的必要条件。