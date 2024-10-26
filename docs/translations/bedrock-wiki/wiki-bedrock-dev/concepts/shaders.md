---
title: 着色器
mentions:
    - SirLich
    - Dreamedc2015
    - yanasakana
    - MedicalJewel
    - SIsilicon
description: MCBE的着色器。
---

:::warning
本页面上的着色器与[Render Dragon](https://help.minecraft.net/hc/en-us/articles/360052771272-About-the-1-16-200-Update-for-Windows-10-)不兼容。这意味着它们在1.16.200及之后的Windows和主机设备上无法使用，也无法在1.18.30及之后的其他设备上使用！
:::

## 概述

着色器分为两个文件夹：`glsl`和`hlsl`。为了使着色器在所有设备上都能正常工作，您需要使用这两种语言编写着色器。在Windows上进行测试时，使用`hlsl`就足够了。当将着色器从一种语言重写为另一种语言时，需要更改的内容很少，例如HLSL中的`float3`在GLSL中对应`vec3`。这两种语言之间的映射可以在[这里](https://anteru.net/blog/2016/mapping-between-HLSL-and-GLSL/)找到。

## 材料

顶点、片段和有时的几何着色器与一些选项结合在一起作为材料，是自定义着色器所必需的。要创建新的材料，您需要创建一个文件，其名称与原版资源包中的.material文件名称匹配。例如：`materials/particles.material`。材料支持通过在冒号后添加父材料来实现继承。例如：`entity_alpha:entity_base`。

### 常见材料定义字段

| **字段名称**     | **描述**                                                         | **示例值**                                              | **备注**                                                                                                                                         |
|------------------|------------------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `vertexShader`   | 相对于hlsl/glsl文件夹的着色器路径                               |                                                        | 对于HLSL着色器，添加`.hlsl`后缀。                                                                                                             |
| `fragmentShader` | 相对于hlsl/glsl文件夹的着色器路径                               |                                                        | 对于HLSL着色器，添加`.hlsl`后缀。                                                                                                             |
| `vertexFields`   | 传递给顶点着色器的字段数组                                       |                                                        | 最好从原版材料中复制此字段。                                                                                                                   |
| `variants`       | 定义材料变体的对象数组                                           |                                                        | 最好从原版材料中复制此字段。                                                                                                                   |
| `+defines`       | 要添加到着色器源代码中的`#define`指令数组                       |                                                        | 适用于重用着色器，但更改一些小设置。                                                                                                           |
| `+states`        | 要启用的状态数组                                                 | `["Blending", "DisableAlphaWrite", "DisableDepthWrite"]` | 对于OpenGL实现，相当于[glEnable](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glEnable.xml)调用。                          |
| `-defines`       | 从继承的`+defines`中删除的`#defines`指令数组                   |                                                        |                                                                                                                                                   |
| `+samplerStates` | 定义特定索引的纹理如何处理的对象数组                             | `{ "samplerIndex": 0, "textureFilter": "Point" }`    | `textureFilter`指定如何采样纹理，`textureWrap`指定在访问纹理维度外部时的行为。                                                               |
| `msaaSupport`    | 多重采样抗锯齿支持                                               | `Both`                                                 |                                                                                                                                                   |
| `blendSrc`       | 指定颜色源混合因子的计算方式                                     | `One`                                                  | 对于OpenGL实现，相当于[glBlendFunc](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendFunc.xhtml)调用。                     |
| `blendDst`       | 指定颜色目标混合因子的计算方式                                   | `One`                                                  | 对于OpenGL实现，相当于[glBlendFunc](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendFunc.xhtml)调用。                     |

示例：

<CodeHeader></CodeHeader>

```json
{
	"materials": {
		"version": "1.0.0",
		"particle_debug": {
			"vertexShader": "shaders/particle_generic.vertex",
			"fragmentShader": "shaders/particle_debug.fragment",

			"vertexFields": [
				{ "field": "Position" },
				{ "field": "Color" },
				{ "field": "UV0" }
			],

			"+samplerStates": [
				{
					"samplerIndex": 0,
					"textureFilter": "Point"
				}
			],

			"msaaSupport": "Both"
		}
	}
}
```

有关材料文件和可能字段值的所有详细信息，请查看[材料文件JSON架构](https://github.com/stirante/bedrock-shader-schema/blob/master/materials.schema.json)。

## 故障排除

### 着色器没有变化

每次着色器发生更改时，您需要重启Minecraft以完全重新编译着色器。

### 编译错误

当出现着色器编译错误时，通常会指定错误发生的行号。您需要检查错误行上方的几行，因为Minecraft在编译之前会添加`#define`指令。

### 找不到常量缓冲区名：$Globals

我无法准确找到此错误的实际原因，但似乎与全局变量有关。删除它们（在`main`函数中初始化或将其更改为`#define`指令）似乎可以解决问题。

## 提示与技巧

### 将变量传递给着色器

您可以通过更改实体颜色将变量从粒子或实体传递给着色器。输入颜色被限制在`<0.0, 1.0>`之间。要传递更显著的值，您需要除以最大值（或至少某个较大的数字）。

### 在着色器中使用时间

`TIME`变量是以`float`表示的秒数，并且对所有着色器都是全局的。对于基于粒子生命周期的时间，您需要传递以下内容：

<CodeHeader></CodeHeader>

```json
"minecraft:particle_appearance_tinting": {
    "color": ["variable.particle_age/variable.particle_lifetime", 0, 0, 1]
}
```

然后在着色器中，使用`PSInput.color.r`作为时间，其中`0.0`表示粒子出生，`1.0`表示粒子死亡。

### 相机方向朝向实体

对于实体着色器，您可以使着色器依赖于相机朝向实体的方向。

- 在顶点和片段着色器的`PS_Input`中添加新字段

<CodeHeader></CodeHeader>

```
float3 viewDir: POSITION;
```

- 然后，在顶点着色器中添加这一行

<CodeHeader></CodeHeader>

```
PSInput.viewDir = normalize((mul(WORLD, mul(BONES[VSInput.boneId], float4(VSInput.position, 1)))).xyz);
```

- 在片段着色器中，使用`PSInput.viewDir`根据相机旋转进行更改。

### 调试值

调试值的最简单方法是将其转换为颜色并像这样渲染。

<CodeHeader></CodeHeader>

```
PSOutput.color = float4(PSInput.uv, 0., 1.);
```

这应该会创建一个红绿渐变，显示`uv`的值在`<0, 0>`和`<1, 1>`之间。

您可以使用我编写的调试着色器[基于此着色器](http://mew.cx/drawtext/drawtext)。现在，这个着色器将显示传递给着色器的颜色值。要显示其他值，请将hlsl着色器中的第70行更改为

<CodeHeader></CodeHeader>

```
int ascii = getFloatCharacter( cellIndex, <float4 vector here> );
```

GLSL版本的调试着色器可能会导致Minecraft崩溃，仅用于调试。

[下载调试着色器](http://files.stirante.com/debugShader.zip)

![](/assets/images/knowledge/shaders/debugShader.gif)