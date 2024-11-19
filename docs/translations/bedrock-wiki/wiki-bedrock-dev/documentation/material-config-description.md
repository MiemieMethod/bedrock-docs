---
title: 材质配置说明
tags:
  - 专家
mentions:
  - MedicalJewel105
  - SmokeyStack
description: 本文将详细介绍材质文件的结构和配置。
---

/// warning
材质并非胆小者所能应对。请准备好可能的崩溃、内容日志错误和较长的加载时间。
///

## 前言

本文译自 [https://mc.163.com/dev/mcmanual/mc-dev/mcguide/](https://mc.163.com/dev/mcmanual/mc-dev/mcguide/) —— 由网易提供，中国版的开发者。本文将详细介绍材质文件的结构和配置。

## 材质文件

我们将解释微软原生的材质文件。首先，目录下的文件基本上是以“.material”为后缀的文件。此外，还有三个重要的json文件，即 common.json、fancy.json、sad.json。

首先让我们看看 sad.json 和 fancy.json。它们用于控制图像质量性能。每个文件定义了一系列材质文件。fancy.json 通常定义的材质文件比 sad.json 多，可能在某些材质文件中添加了一些额外的宏，着色器可以通过判断这些宏来进行特殊处理：

```json title="sad.json"
[
	{"path":"materials/sad.material"},
	{"path":"materials/entity.material"},
	{"path":"materials/terrain.material"},
	{"path":"materials/portal.material"},
	{"path":"materials/barrier.material"},
	{"path":"materials/wireframe.material"}
]
```

```json title="fancy.json"
[
	{"path":"materials/fancy.material", "+defines":["FANCY"]},
	{"path":"materials/entity.material", "+defines":["FANCY"]},
	{"path":"materials/terrain.material", "+defines":["FANCY"]},
	{"path":"materials/hologram.material"},
	{"path":"materials/portal.material", "+defines":["FANCY"]},
	{"path":"materials/barrier.material"},
	{"path":"materials/wireframe.material"}
]
```

可以看出，fancy.json 定义的材质文件比 sad.json 多了 fancy.material 和 hologram.material，并且为多个材质文件定义了 FANCY 宏。游戏内设置/视频/精美纹理的切换就是控制 sad 和 fancy 之间的切换。当开启精美纹理开关时，fancy.json 中的材质文件将生效，关闭时则使用 sad.json 中的材质文件。

为了实现更好的性能，fancy.json 中的材质文件通常具有更复杂的操作，而 sad.json 中的材质通常会稍微牺牲一些渲染性能以换取更好的性能。如果开发者需要编写更复杂的着色器，建议同时编写一个低成本版本，并分别在 fancy 和 sad 中定义，让玩家通过游戏中的精美纹理选项控制是否开启相应的效果。

```json title="common.json"
[
	{"path":"materials/particles.material"},
	{"path":"materials/shadows.material"},
	{"path":"materials/sky.material"},
	{"path":"materials/ui.material"},
	{"path":"materials/ui3D.material"},
	{"path":"materials/portal.material"},
	{"path":"materials/barrier.material"},
	{"path":"materials/wireframe.material"}
]
```

与 sad 和 fancy 相比，它们可以相互切换。common.json 中定义的材质文件将在进入游戏后加载。除 common.json、sad.json、fancy.json 中声明的材质文件外，其他材质文件不会被加载。

## 材质语法

我们以材质文件 entity.material 为例来说明，打开文件，可以看到文件以 materials 开头，然后定义了版本号 version 为 1.0.0，这些是固定格式，用于标识该材质文件的解析方式，我们可以暂时忽略它并不进行修改。

你可以看到材质中每个字段的定义都是以键值对的形式，例如：

```json
[
	"vertexShader": "shaders/entity.vertex",
]
```

冒号左侧代表键为 vertexShader，右侧代表值为 shaders/entity.vertex；

也有列表形式的定义：

```json
[
	"vertexFields": [
        { "field": "Position" },
        { "field": "Normal" },
        { "field": "UV0" }
    ],
]
```

带有 [ ] 符号的声明是一个列表，内部是每个子元素的 json 定义。

## 材质所有属性字段概览

### 渲染状态

#### `states`

配置渲染环境，可以有以下取值：

- `EnableAlphaToCoverage`：用于半透明物体的无序渲染方法。此开关仅在支持 MSAA 的环境中有用。启用后，物体的边缘将根据透明度更准确地软化和过渡。也可用于一些网格重叠较多的复杂场景。

- `Wireframe`：绘制线框模式

- `Blending`: 启用颜色混合模式，常用于渲染半透明物体。声明后，通常需要声明混合因子 blendSrc、blendDst

- `DisableColorWrite`：不将颜色值写入颜色缓冲区，不写入任何 RGBA 通道

- `DisableAlphaWrite`：不将透明度 alpha 值写入颜色缓冲区，允许写入 RGB 值

- `DisableRGBWrite`：不将透明 RGB 值写入颜色缓冲区，允许写入 alpha 值

- `DisableDepthTest`：关闭深度测试

- `DisableDepthWrite`：关闭深度写入

- `DisableCulling`: 同时渲染前后面

- `InvertCulling`：使用前裁剪。默认是背裁剪。声明后，将渲染背面并裁剪前面。

- `StencilWrite`: 启用模板掩码写入

- `EnableStencilTest`：启用模板掩码测试

### 着色器路径

#### `vertexShader`

顶点着色器的路径，通常为 shaders/XXX.vertex。

#### `vrGeometryShader` 或 `geometryShader`

几何着色器的路径，通常为 shaders/XXX.geometry，移动端不使用，无需修改。

#### `fragmentShader`

片段着色器的路径，通常为 shaders/XXX.fragment。

### 着色器宏定义

#### `defines`

为使用的着色器定义宏。为了代码复用，我们为许多不同的材质使用相同的着色器。这时，如果你想根据当前材质在着色器中执行不同的逻辑，可以通过材质 defines 中声明的宏进行判断。我们可以用材质 entity_for_skeleton 作为说明。在这里我们可以看到定义了三个宏 USE_SKINNING、USE_OVERLAY 和 NETEASE_SKINNING。

```json
"entity_for_skeleton": {
	"vertexShader": "shaders/entity.vertex",
	"vrGeometryShader": "shaders/entity.geometry",
	"fragmentShader": "shaders/entity.fragment",
	"+defines": [ "USE_SKINNING", "USE_OVERLAY", "NETEASE_SKINNING" ],
	"vertexFields": [
		{ "field": "Position" },
		{ "field": "Normal" },
		{ "field": "BoneId0" },
		{ "field": "UV0" }
	],
	"msaaSupport": "Both",
	"+samplerStates": [
		{
			"samplerIndex": 0,
			"textureFilter": "Point"
		}
	]
}
```

查看顶点着色器 entity.vertex，会有 #ifdef、#else、#endif 来判断宏并执行不同的逻辑分支。这些宏的判断语句是在编译时处理的，不同于传统着色器中的 if。否则，编译时处理的逻辑分支在实际运行中不会生成，且不会因分支而降低性能。此外，可以看到宏还可以进行多层判断。首先判断 NETEASE_SKINNING 宏，然后在内部执行逻辑中判断 LARGE_VERTEX_SHADER_UNIFORMS 宏：

```glsl
#ifdef NETEASE_SKINNING
		MAT4 boneMat = transpose(mat3x4ToMat4(BONES_70[int(BONEID_0)]));
		entitySpacePosition = boneMat * POSITION;
		entitySpaceNormal = boneMat * NORMAL;
#else
	#if defined(LARGE_VERTEX_SHADER_UNIFORMS)
		entitySpacePosition = BONES[int(BONEID_0)] * POSITION;
		entitySpaceNormal = BONES[int(BONEID_0)] * NORMAL;
	#else
		entitySpacePosition = BONE * POSITION;
		entitySpaceNormal = BONE * NORMAL;
	#endif
#endif
```

### 运行时状态

#### 深度测试

##### `depthFunc`

深度检测通过函数可以使用以下值：

- `Always`: 总是通过

- `Equal`：当深度值等于缓冲区值时通过

- `NotEqual`：当深度值不等于缓冲区值时通过

- `Less`：当深度值小于缓冲区值时通过

- `Greater`：当深度值大于缓冲区值时通过

- `GreaterEqual`：当深度值大于或等于缓冲区值时通过

- `LessEqual`：当深度值小于或等于缓冲区值时通过

关联的状态渲染环境配置：

- `DisableDepthTest`：关闭深度测试

- `DisableDepthWrite`：关闭深度写入

#### 模板掩码测试

##### `stencilRef`

与模板掩码缓冲区比较或写入的值

##### `stencilRefOverride`

是否使用缓冲区的当前值作为 stencilRef，支持 0 或 1：

- `1`：使用配置的 stencilRef。如果配置了 stencilRef，stencilRefOverride 会自动取 1

- `0`：使用缓冲区的当前值作为 stencilRef，此时不配置 stencilRef

##### `stencilReadMask`

在比较前，将缓冲区值和 stencilRef 值与 stencilReadMask 进行按位与操作

##### `stencilWriteMask`

在写入前，将 stencilRef 值与 stencilWriteMask 进行按位与操作

##### `frontFace` 和 `backFace`

配置在网格的前面或背面使用哪种掩码测试函数。此外，判断顺序是先做掩码检测，然后是深度检测。需要配置以下操作：

- `stencilFunc`: 在比较 stencilRef 与掩码缓冲区时使用的方法，支持以下值：
    - `Always`: 总是通过
    - `Equal`：当 stencilRef 等于缓冲区值时通过
    - `NotEqual`：当 stencilRef 不等于缓冲区值时通过
    - `Less`：当 stencilRef 小于缓冲区值时通过
    - `Greater`：当 stencilRef 大于缓冲区值时通过
    - `GreaterEqual`：当 stencilRef 大于或等于缓冲区值时通过
    - `LessEqual`：当 stencilRef 小于或等于缓冲区值时通过

- `stencilFailOp`：当 stencilFunc 比较函数未通过时执行的操作，支持以下值：
    - `Keep`：保持缓冲区的原始值
    - `Replace`：将 stencilRef 位和 stencilWriteMask 的值写入缓冲区

- `stencilDepthFailOp` : stencilFunc 比较函数通过，但深度测试失败时执行的操作，支持以下值：
    - `Keep`：保持缓冲区的原始值
    - `Replace`：将 stencilRef 位和 stencilWriteMask 的值写入缓冲区

- `stencilPassOp`: stencilFunc 比较函数通过，并且深度测试成功时执行的操作，支持以下值：
    - `Keep`：保持缓冲区的原始值
    - `Replace`：将 stencilRef 位和 stencilWriteMask 的值写入缓冲区

关联的状态渲染环境配置：

- `StencilWrite`：启用模板写入

- `EnableStencilTest`: 启用模板测试

最后，让我们看一个示例：

```json
    "shadow_back": {
      "+states": [
        "StencilWrite",
        "DisableColorWrite",
        "DisableDepthWrite",
        "InvertCulling",
        "EnableStencilTest"
      ],

      "vertexShader": "shaders/position.vertex",
      "vrGeometryShader": "shaders/position.geometry",
      "fragmentShader": "shaders/flat_white.fragment",

      "frontFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "backFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "stencilRef": 1,
      "stencilReadMask": 255,
      "stencilWriteMask": 1,

      "vertexFields": [
        { "field": "Position" }
      ],
      "msaaSupport": "Both"
    }
```

在示例中，StencilWrite 表示支持写入模板缓冲区，EnableStencilTest 表示开启模板测试，frontFace 的配置表示在渲染前面时模板测试总是通过。如果深度测试失败，缓冲区值保持不变。如果也通过，stencil 位和 stencilWriteMask 的值将写入缓冲区，即 1 & 1 = 1 值。backFace 的配置也类似。

#### 混合半透明物体颜色混合

渲染半透明物体需要配置混合因子。最终输出的 RGB 颜色值 = 当前颜色值 * 源混合因子 + 缓冲区中的颜色值 * 目标混合因子

##### `blendSrc`

源混合因子

##### `blendDst`

目标混合因子

##### `alphaSrc`

计算 alpha 时的源混合因子，通常不配置使用默认值

##### `alphaDst`

计算 alpha 时的目标混合因子，通常不配置使用默认值

总体来说，混合因子可以取以下值：

- `DestColor`：缓冲区颜色值

- `SourceColor`：当前颜色值

- `Zero`： (0,0,0)

- `One`： (1,1,1)

- `OneMinusDestColor`: (1,1,1) - 缓冲区颜色值

- `OneMinusSrcColor`: (1,1,1) - 当前颜色值

- `SourceAlpha`：当前颜色中的 alpha 值

- `DestAlpha`：缓冲区颜色中的 alpha 值

- `OneMinusSrcAlpha`：1 - 当前颜色值中的 alpha 值

在引擎中的默认值为：

- `blendSrc`：SourceAlpha

- `blendDst`：OneMinusSrcAlpha

- `alphaSrc`：One

- `alphaDst`：OneMinusSrcAlpha

关联的状态渲染环境配置：

- `Blending`: 启用颜色混合模式，常用于渲染半透明物体。声明后，通常需要声明混合因子 blendSrc、blendDst

- `DisableColorWrite`：不将颜色值写入颜色缓冲区，不写入任何 RGBA 通道

- `DisableAlphaWrite`：不将透明度 alpha 值写入颜色缓冲区，允许写入 RGB 值

- `DisableRGBWrite`：不将透明 RGB 值写入颜色缓冲区，允许写入 alpha 值

#### 采样纹理样本

##### `samplerStates`

配置采样状态，值为一个列表，根据需要采样的纹理数量配置每个纹理。通常，如果顶点属性中声明了 UV0 和 UV1，意味着需要采样两个纹理，需要在此配置两个元素。让我们看看子元素的定义：

```json
{
	"samplerIndex": 0,
	"textureFilter": "Point",
	"textureWrap": "Repeat"
}
```

每个属性的定义如下：

##### `samplerIndex`

数字，表示当前设置的纹理的属性，从 0 开始

##### `textureFilter`

纹理过滤模式（默认是 Point），当实际显示的纹理图与原始图像相比被放大或缩小时，新分辨率图与原始分辨率图上的像素的映射关系可以有以下值：

- `Point`：点采样

- `Bilinear`: 双线性采样

- `Trilinear`: 三线性采样

- `MipMapBilinear`：MipMap 双线性采样

- `TexelAA`：纹理元素抗锯齿（并非所有设备都支持，不推荐）

- `PCF`：通过比较函数采样（并非所有设备都支持，不推荐）

##### `textureWrap`

纹理环绕模式，控制当 uv 超出 [0,1] 时应采样什么样的纹理。可以有以下值：

- `Repeat`：重复，即对采样值取模至 [0, 1]

- `Clamp`：边缘采样，采样最接近边缘的值，即如果 1.1 更接近 1，则取 1；如果 -0.1 更接近 0，则取 0。

#### 顶点

##### `vertexFields`

顶点属性，用于声明使用此材质渲染的网格每个顶点所拥有的属性。这在美术制作资源时决定。可能使用的值如下：

- `Position`：模型空间坐标

- `Color`：颜色

- `Normal`：法线

- `UV0`: 纹理采样坐标

- `UV1`：纹理采样坐标

- `UV2`：纹理采样坐标

- `BoneId0`：骨骼 ID，用于骨骼模型

#### 光栅化环境配置

##### `msaaSupport`

配置 MSAA（多重采样抗锯齿）支持（引擎中的默认值是 NonMSAA）

- `NonMSAA`: 在未启用 MSAA 时允许材质

- `MSAA`: 在启用 MSAA 时允许材质

- `Both`：在启用或未启用 MSAA 时均允许材质。通常使用此值。

##### `depth offset`

深度偏移主要用于解决 Z-fighting 问题，即当两个物体具有相似深度时，渲染时某些帧可能显示该物体，某些帧显示另一个物体。深度偏移的原理是将其中一个物体在深度的大小或小方向上偏移，使它们的深度不再相同。可以配置以下四个变量：

- depthBias

- slopeScaledDepthBias

- depthBiasOGL

- slopeScaledDepthBiasOGL

具体的偏移深度为：

`offset = (slopeScaledDepthBias * m) + (depthBias * r)`

在 OGL 平台上为：

`offset = (slopeScaledDepthBiasOGL * m) + (depthBiasOGL * r)`

m 是多边形深度斜率的最大值（在光栅化阶段计算）。多边形越平行于近裁剪面，m 越接近 0。r 是在窗口坐标系中产生可辨别深度差异的最小值，r 是由实现 OpenGL 的平台指定的常数。

关联的状态渲染环境配置：

- `Wireframe`：绘制线框模式

- `DisableCulling`: 同时渲染前后面

- `InvertCulling`：使用前裁剪。默认是背裁剪。声明后，将渲染背面并裁剪前面。

#### 基元

##### `primitiveMode`

基元渲染模式（引擎中的默认值是 TriangleList）：

- `None`：不渲染，通常不使用

- `QuadList`：四边形模式

- `TriangleList`: 每三个顶点绘制一个三角形，例如第一个三角形使用顶点 v0, v1, v2，第二个使用 v3, v4, v5

- `TriangleStrip`: 每个顶点将与前两个顶点形成一个三角形，结构稍复杂，但可以节省数据量

- `LineList`: 每两个顶点绘制一条线段

- `Line`：每个顶点与其前面的一个顶点形成一条线段

### 材质变体

#### `variants`

用于基于大部分相同定义快速实现多个子材质。参见下方的实际示例 entity_static：

```json
    "entity_static": {
      "vertexShader": "shaders/entity.vertex",
      "vrGeometryShader": "shaders/entity.geometry",
      "fragmentShader": "shaders/entity.fragment",
      "vertexFields": [
        { "field": "Position" },
        { "field": "Normal" },
        { "field": "UV0" }
      ],
      "variants": [
        {
          "skinning": {
            "+defines": [ "USE_SKINNING" ],
            "vertexFields": [
              { "field": "Position" },
              { "field": "BoneId0" },
              { "field": "Normal" },
              { "field": "UV0" }
            ]
          }
        },
        {
          "skinning_color": {
            "+defines": [ "USE_SKINNING", "USE_OVERLAY" ],
            "+states": [ "Blending" ],
            "vertexFields": [
              { "field": "Position" },
              { "field": "BoneId0" },
              { "field": "Color" },
              { "field": "Normal" },
              { "field": "UV0" }
            ]
          }
        }
      ],
      "msaaSupport": "Both",
      "+samplerStates": [
        {
          "samplerIndex": 0,
          "textureFilter": "Point"
        }
      ]
    }
```

变体是材质变体的声明。上述声明定义了两个子变体，skinning 和 skinning_color。在子变体中重写了一些外部字段。实际使用时，相当于快速定义了两个材质。主体和变体通过点 "." 连接。两个材质分别为 entity_static.skinning 和 entity_static.skinning_color。

此外，如果有其他材质继承自 entity_static，例如 entity_dynamic，此材质也将继承这两个变体，entity_dynamic.skinning 和 entity_dynamic.skinning_color。

## 材质合并规则

当不同目录文件中声明了相同的材质时，加载后将根据以下规则进行合并：1. 通常，后加载文件的材质字段会覆盖先前加载的字段。2. 以下字段为特殊字段。支持通过 "+" 进行添加属性，通过 "-" 进行删除属性的操作：

- defines
- states
- samplerStates

例如，有这样的材质在包体文件中声明（省略不相关代码），定义了三个宏：

```json
"testMat": {
	"defines": [ "MACRO_1", "MACRO_2", "MACRO_3" ],
}
```

此时，mod 也声明了该材质，定义了另外三个宏：

```json
"testMat": {
	"defines": [ "MACRO_4", "MACRO_5", "MACRO_6" ],
}
```

在上述情况下，最终运行时相当于 defines 字段被覆盖，实际运行时生效的宏只有：MACRO_4、MACRO_5、MACRO_6

如果在 MOD 中定义时使用 "+" 符号：

```json
"testMat": {
	"+defines": [ "MACRO_4", "MACRO_5", "MACRO_6" ],
}
```

相当于在原有基础上添加定义，实际运行时生效的宏为：MACRO_1、MACRO_2、MACRO_3、MACRO_4、MACRO_5、MACRO_6

如果在 MOD 中定义时使用 "-" 符号：

```json
"testMat": {
	"-defines": [ "MACRO_3"],
}
```

相当于在原有基础上删除部分定义，实际运行时唯一生效的宏为：MACRO_1、MACRO_2

如果多个文件定义了相同的材质，并且涉及覆盖、添加和删除操作，它们生效的顺序为：首先进行所有覆盖操作，然后进行所有添加操作，最后进行所有删除操作。

即，如果某个材质文件声明了删除 MACRO_3 的操作：

```json
"testMat": {
	"-defines": [ "MACRO_3"],
}
```

那么无论其他文件如何覆盖、添加 MACRO_3，这个材质在最终合成后必须没有 MACRO_3 宏。