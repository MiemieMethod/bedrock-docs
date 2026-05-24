# 粒子与音效关键帧

/// details-info | 源文档
该页面翻译自[Blockbench官方文档](https://blockbench.net/wiki/guides/minecraft-particles-sounds)
///

Blockbench允许用户向动画添加粒子效果和音效，预览它们，并将它们导出到Minecraft：基岩版。本指南将教你如何做到这一点。

## 添加效果关键帧

通过关键帧来触发音效和粒子效果。要启用效果动画器，请按时间线上方的"Animate Effects"按钮。在效果动画器中，你可以添加各种类型的关键帧

- **粒子关键帧**播放粒子效果
- **音效关键帧**播放音效
- **指令关键帧**允许你在动画期间的任何时间在实体上运行任意Molang表达式。
  这可用于修改变量以切换纹理或更改其他渲染属性。

![Blockbench中的效果动画器](/assets/images/guides/tools/blockbench/effects-keyframes/effect-animator.png)
<!-- 这个图片应显示Blockbench中的效果动画器 -->

## 预览效果

添加关键帧后，使用关键帧面板中的"Select Keyframe File"按钮来选择预览文件。

对于音效，这必须是`.ogg`音频文件。对于粒子文件，它必须是`.json`粒子文件。

加载后，效果将在Blockbench内预览。

对于粒子效果，你还可以在关键帧面板中从模型中选择定位器。即使定位器的位置有动画，粒子效果也将附着到该特定定位器。对于粒子效果，你还可以定义脚本。此脚本将在创建粒子效果时运行。请注意，在游戏中，查询命名空间与实体相关，而变量命名空间仅引用粒子发射器上的变量。

粒子效果将在你编辑粒子文件后自动重新加载。如果你想重新加载音效，或者你正在使用网络版本，只需再次选择文件以重新加载它。

## 在游戏中使用效果

为了在游戏中使用效果，需要额外步骤：

### 效果标识符

效果标识符用于在资源包中的任何地方引用粒子效果或音效

- 对于粒子效果，标识符是在粒子文件中或在Snowstorm中指定的标识符。
  只要粒子文件位于资源包的`particles`文件夹中或其子文件夹之一中，粒子效果就可以正常工作。

- 对于音效，标识符在应该位于资源包sounds文件夹内的文件`sound_definitions.json`中定义。
  此文件定义了包中的所有自定义音效。每个音效链接到资源包中的一个或多个`.ogg`文件。
  有关定义音效的更多信息，请参阅此处：[音效 - 基岩Wiki](https://wiki.bedrock.dev/concepts/sounds.html)

```json
{
	"format_version": "1.14.0",
	"sound_definitions": {
		"rainbow.bling": {
			"category": "ui",
			"sounds": [ "sounds/rainbow/bling" ]
		}
	}
}
```

### 分配短名称

1. 打开你正在制作动画的自定义实体的客户端实体文件。客户端实体文件可在资源包的`entity`文件夹中找到。
2. 在"description"内，添加列出效果的新对象。对于音效，添加一个称为`"sound_effects"`的对象。对于粒子效果，添加一个称为`"particle_effects"`的对象。
3. 现在，将你的效果作为键值对添加到此对象中。
	键是我们从现在起将在实体范围内使用以引用效果的效果的**短名称**。
	值是效果的完整**标识符**。

```json
{
	"format_version": "1.10.0",
	"minecraft:client_entity": {
		"description": {
			
			// 其他信息，如标识符、模型和纹理
			[...]

			"particle_effects": {
				"rainbow": "snowstorm:rainbow"
			},
			"sound_effects": {
				"pling": "rainbow.pling"
			}
		}
	}
}
```

### 在Blockbench中使用短名称

现在短名称已定义，我们可以在动画中使用它。只需在Blockbench的关键帧面板中的"Effect"输入中输入短名称即可。

![Blockbench中的关键帧面板，其中短名称被放入效果输入](/assets/images/guides/tools/blockbench/effects-keyframes/keyframe-panel.png)
<!-- 这个图片应显示Blockbench中的关键帧面板 -->

现在音效或粒子效果应该在Minecraft中工作！
