# 认识着色器

在进入具体教程前，先把几个词分清楚：纹理决定“表面画了什么”，材质决定“表面怎样被渲染”，着色器决定“渲染时具体怎么算颜色”。不同平台公开的能力不一样，所以同一个“光影效果”在国际版和中国版里可能完全不是同一套文件。

## 从渲染管线理解

游戏渲染可以粗略分成三个阶段：

1. CPU准备数据：加载模型、纹理、动画、相机和光照信息。
2. GPU处理几何：顶点着色器把模型顶点变换到屏幕空间，也可以做逐顶点动画或光照。
3. GPU处理片元：片元着色器根据纹理、光照、雾、透明度等信息计算候选像素颜色，再经过深度测试、透明度测试和混合输出到屏幕。

中国版文档把这类流程称为图形管线，并说明着色器通常包括顶点着色器和片元着色器。顶点着色器按顶点计算，开销相对低但表现较粗；片元着色器按片元或像素计算，表现更细但开销更高。

## 材质和着色器的关系

中国版材质文件会指定顶点着色器、片元着色器、宏、采样器和渲染状态。例如一个材质可以继承另一个材质，只替换片元着色器，从而复用原有透明、蒙皮和附魔等逻辑。

国际版最新版主线则不公开这种通用GLSL材质替换方式。创作者更多通过数据驱动资源控制PBR纹理、光照、天空、水、色彩分级等效果。

/// warning | 不要跨平台套用文件
中国版的`materials/*.material`和`shaders/glsl`教程不能直接用于国际版。国际版Vibrant Visuals资源包也不能直接当作中国版材质包使用。
///

## PBR是什么

PBR是一套模拟材料如何响应真实光照的渲染思路。普通颜色纹理只说明“这个像素是什么颜色”，PBR还会说明：

- 金属度：像不像金属。
- 自发光：是否自己发光。
- 粗糙度：反射是清晰还是模糊。
- 法线或高度：表面细节如何影响光照。
- 次表面散射：Vibrant Visuals中可用，用来描述光进入非金属材质内部再散出的效果。

在基岩版资源中，这些数据通常由`*.texture_set.json`和对应纹理图提供。MER纹理把金属度放在红色通道，自发光放在绿色通道，粗糙度放在蓝色通道；MERS会额外把次表面散射放进Alpha通道。

## 延迟渲染、Vibrant Visuals和RTX

Vibrant Visuals是国际版新的图形升级，提供方向光、体积雾、大气效果等，并基于PBR管线工作。官方文档说明它只改变本地画面，不改变玩法，因此玩家可以按自己的设备选择是否启用。

RTX光线追踪仍受支持，但官方文档提示它很大程度上已被Vibrant Visuals取代。RTX路线需要Windows和支持硬件光线追踪的GPU，且PBR支持范围比Vibrant Visuals窄。

延迟渲染技术预览是Vibrant Visuals正式化前后文档中经常出现的名称。读旧教程时，你会看到“Render Dragon Features for Creators”“Deferred Technical Preview”等开关；读新教程时，则更多看到“Vibrant Visuals”和`"pbr"`功能声明。

## 中国版GLSL路线

中国版允许通过材质和GLSL着色器实现更底层的渲染效果。常见文件包括：

/// html | div.treeview
- 资源包
    - materials
        - {/{file|common.json}}
        - {/{file|fancy.json}}
        - {/{file|sad.json}}
        - {/{file|entity.material}}
    - shaders
        - glsl
            - {/{file|example.vertex}}
            - {/{file|example.fragment}}
            - {/{file|uniformPerFrameConstants.h}}
///

它的学习门槛更高，因为你需要理解OpenGL、GLSL、uniform、varying、attribute、宏和移动端GPU性能。进入[中国版着色器](netease-shader/index.md)前，最好已经能读懂简单C系语言代码。
