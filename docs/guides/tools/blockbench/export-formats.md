# 三维导出格式

/// details-info | 源文档
该页面翻译自[Blockbench官方文档](https://blockbench.net/wiki/guides/export-formats)
///

## 介绍

你已在Blockbench中创建了模型，现在想在其他程序中使用它？Blockbench附带了与外部应用兼容的多种3D导出格式。无论你想创建模型的渲染、在自己的Unity、Unreal或Godot游戏中使用它，甚至进行3D打印，都很可能有适合你的格式！

所有导出格式都可从菜单中的File>`Export`获得。但格式之间存在差异。每个格式都有其独特的优缺点，因此你需要找到最适合你的用例的格式。

本文将介绍常见导出格式，帮助你找到合适的格式，并解释如何将模型导入一些常见程序。

有关如何将模型导出到专门格式的指南，例如个别游戏（如Minecraft）的3D模型，请查看[快速入门指南](https://blockbench.net/quickstart/)。

## 按用例推荐格式

通常每个应用都有理想的格式：

| 应用 | 推荐格式 |
|------|---------|
| Blender（用于建模） | DAE |
| Blender（用于渲染） | glTF |
| Unity游戏 | FBX、DAE |
| Unreal Engine游戏 | FBX |
| Godot游戏 | glTF |
| Sketchfab | glTF（File>`Export`>`Upload to Sketchfab`） |

## 三维格式

### OBJ

OBJ可能是最广泛支持的3D模型格式。然而，尽管它得到支持，但它也极其有限。如果你想要任何类型的层级或动画支持，这不是你的格式。

#### 优点

* 几乎普遍支持
* 简单易手动编辑

#### 缺点

* 无层级
* 无动画
* 材质选项有限

### glTF / glb

glTF或其二进制编码的对应物glb是3D导出的现代且广泛采用的标准。然而，就其对3D导出的效果而言，它在不同3D编辑器之间交换文件时确实存在一些缺点。

#### 优点

* 广泛支持
* 对层级和动画的强大支持
* 对材质的良好支持，包括像素完美过滤
* 嵌入式纹理

#### 缺点

* 不针对进一步编辑进行优化。四边形转换为三角形，顶点不再在不同面之间共享
* Unreal Engine和Unity中无原生支持

### FBX

FBX是Autodesk的专有3D格式。它广泛用于3D游戏和电影。然而，格式的闭源性质使得开源应用支持它变得困难。

#### 优点

* 支持Unity和Unreal Engine
* 支持所有重要特性
* 嵌入式纹理

#### 缺点

* 与Blender不兼容，因为Blender只能导入二进制FBX，而Blockbench只能导出ASCII FBX

### DAE (Collada)

Collada是一个开源3D格式，旨在在不同3D程序之间交换文件。它支持层级和动画。

#### 优点

* 支持所有重要特性
* 与Blender、Unity和许多其他程序兼容

#### 缺点

* 与glTF相比，材质选项更受限

## 导入指南

导出后，将模型导入目标应用通常很简单。但它可能需要一些调整才能正确渲染。除非你使用glTF和兼容程序，否则你的纹理可能看起来完全模糊，透明度可能无法工作。以下是在一些最常见的应用中如何解决此问题的指南。

### Blender

* 通过File>`Import`导入模型
* 使用视口顶部右角的视口着色选项切换到材质预览选项，以便可以看到纹理
* 确保你的对象被选中，然后在屏幕右下角的属性面板中切换到材质属性选项卡
* 在Surface下，按Base Color旁边的箭头按钮展开选项，并将第二个选项从Linear更改为Closest
* 向下滚动并将Roughness设置为1.000
* 向下滚动到Settings并将Blend Mode设置为Alpha Clip。或者，如果你的纹理具有半透明（半透明）部分，请将其设置为Alpha Blend
* 在这里，你还可以根据你的偏好启用或禁用Backface Culling。如果启用，你将看不到面的背面

### Unity

* 将模型拖放到Unity文件浏览器中的首选文件夹中
* 从某些文件类型加载时，所有几何体、材质和纹理都被烘焙为一个预制件，因此你无法更改它们。要解决此问题，请在项目浏览器中找到并展开模型。右键单击纹理并点击从预制件中提取。对所有纹理和材质执行此操作
* 接下来，选择材质并将Rendering Mode设置为Cutout
* 现在，选择纹理，将Filter Mode设置为Point（无过滤），并在底部将Format设置为RGBA 32位
* 别忘了按Apply！

![在Unity中配置材质选项](/assets/images/guides/tools/blockbench/export-formats/unity-material.png)
<!-- 这个图片应显示Unity中材质选项的配置 -->
