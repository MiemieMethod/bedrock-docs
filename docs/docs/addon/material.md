# 材质

**材质（Material）**是Minecraft基岩版资源包中用于定义渲染阶段配置的资源类型。材质决定模型在渲染时使用的着色器、渲染状态和顶点输入布局，是纹理与几何体能够被正确绘制的关键环节。

## 概述

材质定义文件位于资源包的`materials/`目录，扩展名通常为`.material`。实体和附着物不会直接写入底层着色器路径，而是先在客户端实体定义中声明材质短名称，再由渲染控制器通过`Material.`前缀进行选择。

材质本身不描述“使用哪张纹理”，而是描述“如何渲染”。纹理选择通常由客户端实体定义与渲染控制器完成。

## 主要作用

材质主要用于统一描述以下内容：

- 着色器入口与渲染变种。
- 渲染状态，例如混合、剔除、深度写入。
- 顶点字段布局与采样器状态。
- 某些渲染功能开关，例如覆盖色或UV动画相关定义。

## 与渲染控制器的关系

渲染控制器中的`materials`字段负责将骨骼映射到材质短名称。引擎渲染骨骼时，会先匹配到对应材质，再结合纹理与几何体完成最终绘制。因此，材质是渲染控制器资源组合链中的核心节点之一。

实体局部发光、半透明等效果通常同时依赖“正确的材质类型”与“正确的纹理内容”。仅替换纹理而不调整材质，往往无法得到预期结果。

## 旧版着色器文件

/// warning | RenderDragon不兼容
本节所述的着色器机制与RenderDragon渲染引擎不兼容。在1.16.200及以后版本的Windows和主机设备，以及1.18.30及以后版本的其他设备上，此类自定义着色器均无法生效。
///

在RenderDragon引入之前，`.material`文件可以通过`vertexShader`和`fragmentShader`字段直接引用自定义着色器源文件，实现光影级别的视觉效果修改。着色器文件分为`glsl/`和`hlsl/`两个目录；要在所有设备上生效，需同时用两种语言编写。

`.material`文件中与着色器相关的通用字段如下：

| 字段 | 说明 |
|------|------|
| `vertexShader` | 顶点着色器路径，相对于`hlsl/`或`glsl/`目录，HLSL文件会自动追加`.hlsl`后缀 |
| `fragmentShader` | 片段着色器路径，规则与`vertexShader`相同 |
| `vertexFields` | 传递给顶点着色器的字段数组，通常从原版材质复制 |
| `variants` | 材质变种定义数组 |
| `+defines` | 向着色器源码追加的`#define`指令数组 |
| `-defines` | 从继承材质中移除的`#define`指令数组 |
| `+states` | 启用的渲染状态数组，如`Blending`、`DisableDepthWrite` |
| `+samplerStates` | 纹理采样方式定义数组，包含`samplerIndex`和`textureFilter`等字段 |
| `msaaSupport` | 多重采样抗锯齿支持设置 |
| `blendSrc` | 颜色源混合因子 |
| `blendDst` | 颜色目标混合因子 |

材质支持继承，使用冒号语法（如`entity_alpha:entity_base`）声明父材质，子材质会继承父材质的所有字段并按需覆盖或追加。

材质系统在不同渲染时代存在明显差异。旧版社区资料中部分可行做法在RenderDragon渲染路径下可能失效，或仅在特定版本、特定平台生效。维护跨版本内容时，应始终以目标版本的内容日志和实际设备测试结果为准。

## 相关页面

- [纹理](texture.md)
- [渲染控制器](render-controller.md)
- [渲染控制器参考](../../refs/addon/render-controller.md)

## 原版材质列表

以下列出基岩版中供附加包引用的原版材质标识符及其已知属性。可在客户端实体定义中直接引用这些标识符名称。由于材质系统在RenderDragon时代经历了较大变化，部分材质在新渲染路径下的具体表现可能与早期测试结果存在差异，建议实际使用时在目标设备上验证效果。

/// warning | 行为不稳定
材质系统不适合轻率使用。部分材质可能导致崩溃、内容日志报错或加载缓慢。强烈建议自行实验并以实际设备测试结果为准。
///

| 材质标识符 | 主要属性 |
|-----------|---------|
| `alpha_block` | 背面剔除、完全不透明 |
| `alpha_block_color` | 背面剔除、Alpha通道（半透明） |
| `banner` | 无特殊属性（透明物体后方渲染不稳定） |
| `banner_pole` | 背面剔除、透明效果（透明物体后方渲染不稳定） |
| `beacon_beam` | 完全不透明 |
| `beacon_beam_transparent` | Alpha通道（后方粒子呈"正面剔除"效果） |
| `charged_creeper` | 自发光、固定透明度（透明物体后方渲染不稳定） |
| `conduit_wind` | 透明效果、Alpha通道（半透明） |
| `entity` | 完全不透明、背面剔除 |
| `entity_alphablend` | 背面剔除、Alpha通道（透明物体后方渲染不稳定） |
| `entity_alphablend_nocolorentity_static` | 未知属性，可能导致崩溃 |
| `entity_alphatest` | 透明效果、Alpha通道（半透明） |
| `entity_alphatest_change_color` | 透明效果、Alpha通道（不透明） |
| `entity_alphatest_change_color_glint` | 未知属性 |
| `entity_alphatest_glint` | 未知属性 |
| `entity_alphatest_glint_item` | 未知属性 |
| `entity_alphatest_multicolor_tint` | 灰度处理、背面剔除、透明效果（不透明） |
| `entity_beam` | 透明效果、Alpha通道（半透明） |
| `entity_beam_additive` | 透明效果、自发光、背面剔除、固定透明度（始终渲染在最上层） |
| `entity_change_color` | 完全不透明 |
| `entity_change_color_glint` | 未知属性 |
| `entity_custom` | 背面剔除、Alpha通道（透明物体后方渲染不稳定） |
| `entity_dissolve_layer0` | 未知属性（透明物体后方渲染不稳定） |
| `entity_dissolve_layer1` | 未知属性 |
| `entity_emissive` | 自发光、完全不透明、背面剔除 |
| `entity_emissive_alpha` | 自发光、Alpha通道、透明效果 |
| `entity_emissive_alpha_one_sided` | 自发光、Alpha通道、透明效果、背面剔除 |
| `entity_flat_color_line` | 背面剔除、完全不透明 |
| `entity_glint` | 未知属性 |
| `entity_lead_base` | Alpha通道（透明物体后方渲染不稳定） |
| `entity_loyalty_rope` | 未知属性 |
| `entity_multitexture` | 未知属性 |
| `entity_multitexture_alpha_test` | 未知属性 |
| `entity_multitexture_alpha_test_color_mask` | 未知属性 |
| `entity_multitexture_color_mask` | 未知属性 |
| `entity_multitexture_masked` | 未知属性 |
| `entity_multitexture_multiplicative_blend` | 未知属性 |
| `entity_nocull` | 完全不透明（无背面剔除） |
| `guardian_ghost` | 未知属性 |
| `item_in_hand` | 完全不透明、背面剔除 |
| `item_in_hand_entity_alphatest` | 透明效果、Alpha通道（半透明） |
| `item_in_hand_entity_alphatest_color` | 未知属性 |
| `item_in_hand_glint` | 未知属性 |
| `item_in_hand_multicolor_tint` | 灰度处理、背面剔除、透明效果 |
| `map` | 未知属性 |
| `map_decoration` | 未知属性 |
| `map_marker` | 未知属性 |
| `moving_block` | 完全不透明 |
| `moving_block_alpha` | Alpha通道（半透明） |
| `moving_block_alpha_seasons` | Alpha通道（半透明） |
| `moving_block_alpha_single_side` | 背面剔除、Alpha通道（半透明） |
| `moving_block_blend` | 混合透明 |
| `moving_block_double_side` | 完全不透明（无背面剔除） |
| `moving_block_seasons` | 完全不透明 |
| `opaque_block` | 完全不透明、背面剔除 |
| `opaque_block_color` | 完全不透明、背面剔除（带颜色叠加） |
| `opaque_block_color_uv2` | 完全不透明、背面剔除（带颜色叠加及UV2） |
