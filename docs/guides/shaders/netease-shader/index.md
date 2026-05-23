# 中国版着色器<!-- md:flag china -->

中国版提供了与国际版不同的材质和着色器工作流。你可以通过`materials`目录下的材质文件指定顶点着色器、片元着色器、宏定义、采样器状态和渲染状态，再把材质引用到原版实体、网易骨骼模型、后处理或中国版粒子特效中。

/// warning | 只适用于中国版
本页内容来自中国版API文档的材质与着色器章节。它依赖中国版资源目录、材质扩展和部分SDK接口，不能直接用于国际版资源包。
///

## 文件放在哪里

一个最小练习包可以从这些文件开始：

/// html | div.treeview
- resource_packs
    - my_shader_pack
        - materials
            - {/{file|common.json}}
            - {/{file|entity.material}}
        - shaders
            - glsl
                - {/{file|entity_reverse.fragment}}
///

`common.json`用于声明要加载的材质文件：

```json
[
  {
    "path": "materials/entity.material"
  }
]
```

如果你要区分画质开关，可以使用`sad.json`和`fancy.json`。中国版文档说明，`fancy.json`通常会比`sad.json`多加载材质或多添加`FANCY`宏；玩家打开精美图像时加载`fancy`路线，关闭时加载`sad`路线。

## 定义一个材质

材质文件基本结构如下：

```json
{
  "materials": {
    "version": "1.0.0",
    "entity_reverse:entity_alphatest_netease": {
      "fragmentShader": "shaders/glsl/entity_reverse.fragment"
    }
  }
}
```

这里的`entity_reverse:entity_alphatest_netease`表示新材质`entity_reverse`继承自`entity_alphatest_netease`。继承后，新材质会保留父材质的大部分设置，只覆盖片元着色器路径。

常用字段包括：

| 字段 | 作用 |
| --- | --- |
| `vertexShader` | 顶点着色器路径，通常是`shaders/glsl/xxx.vertex` |
| `fragmentShader` | 片元着色器路径，通常是`shaders/glsl/xxx.fragment` |
| `+defines` | 给着色器启用宏定义 |
| `+samplerStates` | 配置纹理采样器 |
| `states` | 配置混合、深度写入、剔除等渲染状态 |

## 引用材质

### 原版实体

在`vanilla_netease\entity\player.entity.json`这类客户端实体文件中，`description.materials.default`指定默认材质。把它改成自定义材质名即可让实体使用你的材质。

```json
"materials": {
  "default": "entity_reverse"
}
```

### 网易骨骼模型

在`vanilla_netease\models\netease_models.json`中给模型配置`material`字段：

```json
{
  "model_example": {
    "dy_load": true,
    "mesh": "mesh/model_example_mesh.json",
    "skeleton": "skeleton/model_example_skeleton.json",
    "material": "my_blinn_phong"
  }
}
```

如果希望同一帧用多个材质绘制同一模型，可以把`material`写成数组。文档称这种方式为多pass。

```json
"material": [
  "entity_for_skeleton",
  "netease_drawline_example"
]
```

### 后处理

后处理配置位于`vanilla_netease\graphics_settings\post_process.json`。单个pass中的`material`字段决定该pass使用哪个材质。

## 写一个反色片元着色器

这个练习只改片元颜色，不改顶点逻辑。可以复制原实体片元着色器作为模板，在最终输出前加入反色逻辑：

```glsl
color.rgb = vec3(1.0) - color.rgb;
gl_FragColor = color;
```

如果你使用的是继承父材质的方式，顶点着色器、透明度测试、蒙皮等逻辑可以继续复用父材质。

## 读取常用Uniform

中国版文档列出了一些常用头文件和Uniform：

| 头文件 | 常用内容 | 使用时机 |
| --- | --- | --- |
| `uniformWorldConstants.h` | `WORLD`、`WORLDVIEW`、`PROJ`、`WORLDVIEWPROJ` | 场景对象着色器 |
| `uniformPerFrameConstants.h` | `VIEW_POS`、`TIME`、`FOG_COLOR`、`FOG_CONTROL` | 每帧更新 |
| `uniformEntityConstants.h` | `OVERLAY_COLOR`、`TILE_LIGHT_COLOR`、`GLINT_COLOR` | 实体渲染 |
| `uniformShaderConstants.h` | `CURRENT_COLOR`、`DARKEN`、`TEXTURE_DIMENSIONS` | 通用着色器 |

头文件放在`shaders/glsl`中，着色器可通过`#include`引用。

```glsl
#include "uniformPerFrameConstants.h"
```

## 性能原则

中国版着色器会直接影响GPU负担。写效果前先记住这些规则：

- 少用大量`if`/`else`分支。简单阈值选择可以用`step()`合并。
- 循环变量必须初始化，例如`for(int i = 0; i < 5; i++)`。
- 片元着色器比顶点着色器更容易成为性能瓶颈；能放到顶点阶段的计算不要全部放到片元阶段。
- 移动端可考虑`lowp`、`mediump`和`highp`精度差异，但不要为了性能牺牲必要精度。
- 为高画质和低画质分别写`FANCY`分支，让玩家用精美图像开关选择。

## 下一步

完成反色练习后，可以继续尝试：

1. 给骨骼模型添加Blinn-Phong光照。
2. 制作只在`FANCY`宏开启时生效的高开销效果。
3. 给后处理pass编写屏幕空间效果。
4. 使用中国版SDK接口动态替换材质或设置额外Uniform。