# 着色器系列教程

基岩版的“着色器”不是一个单一技术。国际版当前面向创作者公开的是PBR、延迟渲染/Vibrant Visuals和RTX光线追踪资源包；中国版还提供材质文件、GLSL着色器和若干运行时接口；社区又有BetterRTX这类第三方方案。把它们混在一起学习很容易走错路，所以本系列先按平台和管线分开。

## 你应该先读哪一页

| 目标 | 建议页面 |
| --- | --- |
| 想知道材质、着色器、PBR和延迟渲染的关系 | [认识着色器](understanding-shaders.md) |
| 想做最新版国际版PBR资源包 | [使用并自定义延迟渲染](getting-started-with-deferred-lighting.md) |
| 想维护RTX光线追踪包 | [启用光线追踪并制作PBR包](getting-started-with-ray-tracing.md) |
| 想学习中国版GLSL材质 | [中国版着色器](netease-shader/index.md) |
| 想了解BetterRTX在文档站中的定位 | [BetterRTX](betterrtx.md) |

## 不同路线的差异

| 路线 | 主要文件 | 运行环境 | 推荐程度 |
| --- | --- | --- | --- |
| Vibrant Visuals/延迟渲染<!-- md:flag vanilla --> | `*.texture_set.json`、`lighting/global.json`、`water/water.json`等 | 支持该图形模式的国际版设备 | 新项目优先 |
| RTX光线追踪<!-- md:flag vanilla --> | `*.texture_set.json`和PBR纹理 | Windows、支持硬件光线追踪的GPU | 维护旧RTX包时使用 |
| 中国版材质与着色器<!-- md:flag china --> | `materials/*.material`、`shaders/glsl/*.vertex`、`*.fragment` | 中国版OpenGL材质管线 | 中国版项目使用 |
| BetterRTX<!-- md:flag vanilla --> | 知识库未收录具体资料 | 依赖社区方案和玩家环境 | 仅作为兼容性话题记录 |

## 学习建议

1. 先读概念页，不要直接复制完整着色器。渲染管线错误往往比JSON语法错误更难排查。
2. 国际版新资源包优先学习PBR和Vibrant Visuals。官方文档已经提示RTX仍受支持，但很大程度上被Vibrant Visuals取代。
3. 中国版GLSL教程只面向中国版工作流。不要把中国版`materials`和`shaders/glsl`直接放进国际版资源包。
4. 第三方方案只用于理解生态和兼容性，不作为本站最新版主线教程的基础。