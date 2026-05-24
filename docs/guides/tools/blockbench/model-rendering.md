# 模型渲染

/// details-info | 源文档
该页面翻译自[Blockbench官方文档](https://blockbench.net/wiki/guides/model-rendering)
///

要获得Blockbench模型具有逼真光照的图像，需要在外部程序中渲染它。本文将介绍最流行的渲染程序，并解释如何创建模型的渲染。

![Blockbench预览与最终渲染的对比](/assets/images/guides/tools/blockbench/model-rendering/preview-vs-render.png)
<!-- 该图片应显示Blockbench预览（左）与最终渲染（右）之间的差异 -->

## 软件选择

选择渲染程序是第一步。通常，渲染质量越高、需要的选项越多，程序就越难学。

| | 3D Viewer | Sketchfab | Light Tracer | Blender |
|---|---|---|---|---|
| **难度** | 非常简单 | 简单 | 中等 | 困难 |
| **质量** | 低 | 中等 | 高 | 高 |
| **功能** | 1/10 | 4/10 | 6/10 | 10/10 |
| **光线追踪** | — | — | 是 | 是，通过Cycles |
| **透明背景** | 是 | 是 | （付费） | 是 |
| **平台** | Windows | 网页 | Windows、Mac | Windows、Linux、Mac |
| **价格** | 免费 | 免费 | 免费增值 | 免费 |

/// note | 光线追踪
光线追踪是一种渲染技术，其中光线从光源发出，在模型周围反弹，并被场景中的对象反射和遮挡。在常规实时渲染器中，阴影是根据对象形状计算并在边缘模糊，而环境光遮挡则是根据模型的形状虚拟的。相比之下，光线追踪产生了更加逼真和吸引人的结果，因为它密切模拟了光在现实世界中的工作方式。
///

### Windows 3D Viewer

默认Windows 3D Viewer是一个易于使用但功能有限的3D模型查看和渲染程序。你可以从不同角度渲染模型，并在模型周围设置光源。

### Sketchfab

Sketchfab是一个用于共享3D模型的在线平台，类似于YouTube之于视频。上传模型时，你有许多选项来配置模型的呈现方式，包括背景、光照和渲染效果。

由于3D编辑器的功能，Sketchfab也是渲染模型的绝佳选择。

### Light Tracer

Light Tracer是一个专注于渲染的应用程序。与Sketchfab和3D Viewer相比，它在质量上有很大进步，但使用起来仍然很简单。

Light Tracer有一个免费的浏览器应用程序，功能受限但仍能产生很好的效果。具有完整功能集的桌面应用程序可作为订阅或49美元的一次性购买提供。

### Blender

Blender是一个专业的3D建模和渲染软件。它本质上有无限的选项，但也伴随陡峭的学习曲线。Blender具有与付费3D程序（如Cinema 4D、3ds Max和Maya）相似的功能集。如果你拥有其中一个程序，也可以用它们进行渲染。

## 如何渲染

在将模型导入所选的渲染程序之前，需要以兼容的格式导出它。建议使用格式glTF，因为它与列表中的所有程序兼容，将所有内容保存到一个文件中，甚至支持模型层级和动画。通过**File**>`Export`>`Export as glTF**导出模型。

### Windows 3D Viewer

右键单击导出的glTF文件，然后选择**Open with**>`3D Viewer**。

你可以在侧边栏中选择光照预设。在下方，你可以微调每个光源的参数。

![Windows 3D Viewer](/assets/images/guides/tools/blockbench/model-rendering/3d-viewer.png)
<!-- 这个图片应显示Windows 3D Viewer的界面 -->

对光照和相机角度满意后，进入**File**>`Export Image**。选择所需的分辨率和导出选项，然后按**Export**。

### Sketchfab

将模型上传到Sketchfab是Blockbench的内置功能。进入**File**>`Upload to Sketchfab...**，填写模型元数据，然后按照说明获取访问令牌。

![Blockbench中的Sketchfab上传对话框](/assets/images/guides/tools/blockbench/model-rendering/sketchfab-upload.png)
<!-- 该图片应显示Blockbench中的Sketchfab上传对话框 -->

上传模型后，点击**Edit 3D Settings**以访问3D编辑器。

在3D编辑器中，你可以配置模型的光照、背景和效果。要了解有关Sketchfab上光照和阴影微调的更多信息，请阅读[How to Fine-tune your Lighting and Shadows on Sketchfab](https://sketchfab.com/blogs/community/how-to-fine-tune-your-lighting-and-shadows-on-sketchfab/)。

![Sketchfab 3D设置](/assets/images/guides/tools/blockbench/model-rendering/sketchfab-editor.png)
<!-- 该图片应显示Sketchfab 3D编辑器的界面 -->

对结果满意后，导出图像的一种方法是简单地截图。大多数网络浏览器都有内置的截图功能。你也可以在Windows上按`Windows Key + Shift + S`或在macOS上按`Command + Shift + 4`来截图。

如果这还不够，你也可以使用Sketchfab的[Screenshot工具](https://labs.sketchfab.com/experiments/screenshots/)。这允许你指定图像分辨率或以透明背景导出。

### Light Tracer

打开[Light Tracer浏览器应用](https://lighttracer.org/app.html)或桌面应用（如果你有的话），然后从文件浏览器将模型glTF文件拖入程序。在弹出的对话框中，按**Replace**。

![Light Tracer界面](/assets/images/guides/tools/blockbench/model-rendering/light-tracer.png)
<!-- 该图片应显示Light Tracer的界面 -->

你可以使用左右鼠标按钮定位相机。在左侧栏的Scene Explorer中，按**Make floor**创建一个地面平面以捕捉模型下的阴影。

在地图编辑器中，你可以创建环境地图，基本上是围绕模型的图像，用于控制光线来自何处。你可以调整地图的旋转和强度，并添加其他光源。

在付费版本中，你也可以配置背景板，一个与环境地图不同的自定义背景。选择**Gradient**并将两种颜色的alpha值都降低到0以获得透明背景。

对角度和光照满意后，按位于模型上方中心的**Save render to image**按钮。这将把你的模型导出为图像。

### Blender

你可以从[Blender.org - Download](https://www.blender.org/download/)下载Blender。

打开Blender后，通过按Delete并确认弹出窗口来确保删除默认立方体。现在导航到**File**>`Import**>`glTF 2.0**，然后打开模型文件。

![Blender界面](/assets/images/guides/tools/blockbench/model-rendering/blender.png)
<!-- 该图片应显示Blender的界面 -->

本文不会深入讨论在Blender中设置相机和光照，但这里有一个很好的[教程视频](https://youtu.be/5UCc3Z_-ibs)。

对光照满意后，按**F12**渲染模型。进入**Image**>`Save**以将渲染导出为PNG图像。
