# 自发光纹理与渲染

/// details-info | 源文档
该页面翻译自[Blockbench文档](https://blockbench.net/wiki/guides/emissive-textures-renders)
///

## 介绍

你可能见过一些模型的渲染效果很突出，因为它们的部分会发光。也许你甚至想在自己的一些模型上尝试这个效果。本文将向你展示如何做到这一点。

要创建任何类型的渲染，你需要决定使用哪种渲染软件。如果你想探索不同的渲染软件并查看每个软件的优缺点，请参阅[模型渲染](model-rendering.md)指南，因为本指南不会深入讨论一般渲染。

本指南将为两个最流行的软件[Blender](https://www.blender.org/)和[Sketchfab](https://sketchfab.com/)提供深入的步骤，但在使用其他软件创建自发光纹理时可能会有重叠。这里以详细的步骤解释了每个软件所需的步骤，你可以通过向下滚动或导航到页面右侧的目录来访问。除了解释所需的步骤外，本指南还有一个示例可供你跟随，以帮助可视化过程。我们将在Blender和Sketchfab中都创建一个台灯的渲染。

请注意，本文推荐的方法不是实现自发光纹理的唯一方法，而是应该提供关于如何实现它们的常见见解。我们鼓励你进行实验并找到最适合你的工作流程。

在此示例中，我们将使用以下台灯模型。

![基础台灯模型](/assets/images/guides/tools/blockbench/emissive-textures-renders/base-lamp-model.png)
<!-- 这个图片应显示Blockbench中的台灯模型 -->

## Blender

### 1. 制作自发光纹理

在Blender中，你可以通过着色选项卡中的节点更改纹理属性。与Sketchfab不同，Blender要求用户为自发光元素和非自发光元素创建单独的纹理，因为我们打算编辑每个纹理作为一个整体的属性。如果你想让多个部分以不同的强度发光，你需要为要具有不同发射强度的每个对象创建单独的纹理。

![Blockbench中的模型](/assets/images/guides/tools/blockbench/emissive-textures-renders/blender-model-in-bb.png)
<!-- 这个图片应显示Blockbench中的台灯模型 -->

### 2. 导出到Blender

将模型、纹理和动画导入Blender的最简单方法是通过File>`Export`>`Export glTF model`导出模型作为.gltf文件。要将导出的glTF导入Blender，请选择File>`Import`>`glTF 2.0`，然后选择你的文件。你的模型将显示为灰色；要查看纹理，请确保在右上角启用视口着色。

![Blender导入选项](/assets/images/guides/tools/blockbench/emissive-textures-renders/blender-import.png)
<!-- 这个图片应显示Blender的导入选项 -->

![Blender视口着色](/assets/images/guides/tools/blockbench/emissive-textures-renders/blender-shading.png)
<!-- 这个图片应显示Blender视口着色选项 -->

### 3. 配置

对于此示例，我们将启用Cycles而不是EEVEE，因为它具有光路追踪。如果你想了解有关EEVEE和Cycles之间差异的更多信息，请查看[Blender Wiki](https://docs.blender.org/manual/en/latest/render/eevee/introduction.html)。

导航到着色选项卡，然后点击你想要自发光的对象。节点应该出现在底部（如果没有，请确保启用了"Use Nodes"切换）。接下来，将基色节点的颜色输出拖到PrincipledBSDF节点上的自发光输入，这将使对象发光！如果需要，调整你想要的发射强度，你可以在自发光输入下找到它。

![处理节点](/assets/images/guides/tools/blockbench/emissive-textures-renders/blender-nodes.png)
<!-- 这个图片应显示Blender中的节点设置 -->

完成后，将相机定位到你喜欢的位置，然后按F12进行渲染，并下载最终结果。

![最终结果](/assets/images/guides/tools/blockbench/emissive-textures-renders/blender-final.png)
<!-- 这个图片应显示Blender中的最终渲染结果 -->

## Sketchfab

### 1. 制作自发光纹理

为了让Sketchfab知道哪些部分需要发光，你需要创建一个称为自发光纹理的东西。此纹理将告诉Sketchfab需要考虑自发光的部分，以及不应该的部分。

要制作自发光纹理，请首先复制你的纹理。我们将对这个新纹理进行更改，同时保持主纹理不变。为了区分它们，建议重命名自发光纹理（例如，你可以在纹理名称中追加`-emissive`）。

重要提示：在复制之前，请确保纹理的尺寸是2的幂。否则它将无法正确工作！（如果不是，你可以通过右键单击它并选择`Resize`来调整纹理大小，并创建新的模板纹理以确保UV正常。）

![复制纹理](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-duplicate-texture.png)
<!-- 这个图片应显示Blockbench中的复制纹理选项 -->

为了在视觉上看到我们对纹理所做更改在模型上的效果，我们需要告诉Blockbench将纹理应用于模型，因为目前它仍然应用主纹理。要做到这一点，使用`Ctrl + A`选择整个模型，然后右键单击大纲中的立方体。然后，选择`Texture > [Your Emissive Texture Name]`，如屏幕截图所示。现在，我们对自发光纹理所做的所有更改都将在模型上直观地反映出来。

![将自发光纹理应用于模型](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-apply-emissive-texture.png)
<!-- 这个图片应显示Blockbench中应用自发光纹理的选项 -->

我们的自发光纹理与我们的常规纹理完全相同（这就是为什么我们复制了我们的原始纹理），但只会突出我们想要自发光的部分。有很多方法可以做到这一点；本指南涵盖了使用内置且通常首选的方式制作自发光纹理。

首先，我们需要告诉Blockbench复制的纹理需要自发光。要做到这一点，只需右键单击复制的纹理并将`Render Mode`设置为`Emissive`。

![将渲染模式设置为自发光](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-render-mode.png)
<!-- 这个图片应显示Blockbench中设置自发光渲染模式的选项 -->

接下来，我们需要标记要自发光的元素。要做到这一点，请在顶部工具栏中选择橡皮擦工具，将不透明度降低到1-24之间的任何地方（不透明度越高，你在Blockbench中看到自发光效果的强度就越强），然后擦除你想自发光的像素。这将导致像素点亮。非常重要的是你降低橡皮擦的不透明度，否则你会意外完全擦除自发光像素！

![橡皮擦设置](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-eraser.png)
<!-- 这个图片应显示Blockbench中的橡皮擦设置 -->

提示：为了更好地看到对自发光纹理的更改，请在`File > Preferences > Settings`中降低Blockbench预览的亮度。

如果前面的设置正确，模型中需要发光的部分现在应该会比其他部分更亮。

![Blockbench中的自发光预览](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-bb-emissive.png)
<!-- 该图片应为Blockbench里应用自发光纹理后的台灯截图，发光区域明显更亮 -->

最后，右键自发光纹理并选择`Export Emission Map`导出发射贴图。其余设置通常保持默认即可，但要额外勾选`Flip Y-Axis`，因为Sketchfab会对常规纹理自动执行这一翻转。

![导出发射贴图](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-export-emission.png)
<!-- 该图片应为Blockbench中右键纹理并选择导出发射贴图的截图 -->

![发射贴图导出设置](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-emission-settings.png)
<!-- 该图片应为Emission Map导出设置对话框，并突出显示Flip Y-Axis选项 -->

### 2. 导出到Sketchfab

此时模型仍然应用着自发光纹理。上传到Sketchfab前，需要把模型重新切回原始纹理，否则常规底色也会被错误替换。做法与前面相同：按++ctrl+a++选中整个模型，右键大纲中的立方体，然后选择`Texture > [原始纹理名]`。

![切回原始纹理](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-apply-default.png)
<!-- 该图片应为Blockbench中把模型从自发光纹理切回原始纹理的截图 -->

接下来即可直接从Blockbench上传：打开**File**→**Export**→**Upload to Sketchfab**，填写标题、描述等必填信息后点击**Confirm**。完成后，Blockbench会给出一个跳转提示，用于在Sketchfab网页中继续配置模型。

![上传到Sketchfab](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-export.png)
<!-- 该图片应为Blockbench的Upload to Sketchfab对话框或确认界面截图 -->

### 3. 在Sketchfab中配置

进入Sketchfab后，先点击右上角的**Edit 3D Settings**。这里会看到模型预览以及大量渲染面板。自发光相关设置主要位于**Materials**页签中。

![Sketchfab中的模型](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-model-uploaded.png)
<!-- 该图片应为模型刚上传到Sketchfab后的默认预览界面截图 -->

在**Materials**面板里向下找到**Emission**分类。点击颜色选择器，切换到**Texture**页签，再选择**Manage Textures**，导入刚才从Blockbench导出的发射贴图。

![自发光设置入口](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-emissive-feature.png)
<!-- 该图片应为Sketchfab的Materials面板，并标出Emission分类位置 -->

![管理纹理](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-manage-textures.png)
<!-- 该图片应为Sketchfab中Manage Textures按钮和导入纹理界面的截图 -->

导入完成后，模型就会按照发射贴图发光。之后可以继续调整背景、泛光、阴影等效果。示例中给发光材质额外加入了Bloom，因此灯光边缘会更柔和。

![启用自发光与Bloom后的结果](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-bloom.png)
<!-- 该图片应为Sketchfab中导入发射贴图并启用Bloom后的效果截图 -->

如果想保留像素风边缘，可以把默认的三线性过滤改成最近邻过滤。这样发光区域边缘会更接近Minecraft常见的像素观感。

![不同过滤模式的效果](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-nearest.png)
<!-- 该图片应为Sketchfab中把发射纹理过滤方式从trilinear切换为nearest的对比截图 -->

最后导出或截图即可得到成品。

![Sketchfab最终效果](/assets/images/guides/tools/blockbench/emissive-textures-renders/sketchfab-finished.png)
<!-- 该图片应为Sketchfab中完成全部设置后的最终渲染截图 -->