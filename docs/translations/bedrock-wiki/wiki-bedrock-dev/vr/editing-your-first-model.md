---
标题: 编辑你的第一个模型
类别: 教程
提及:
    - TheDoctor15
    - MedicalJewel105
    - TheItsNameless
    - SmokeyStack
标签:
    - 专家
描述: 本教程将教你如何制作你的第一个虚拟现实模型。
---

本教程将教你如何制作你的第一个虚拟现实模型。
为了本教程，我们将编辑右手模型。

:::提示
本教程使用程序[Blender](https://www.blender.org/download/)，请确保在跟随本教程之前已安装该程序。
:::

## 在Blender中查看模型

首先，你需要将模型导入Blender：

![](/assets/images/vr/tutorial-hand-right/import-1.png)
![](/assets/images/vr/tutorial-hand-right/import-2.png)
![](/assets/images/vr/tutorial-hand-right/import-3.png)

你的模型现在已导入，但缺少纹理。
要添加纹理，你需要进入Blender的着色选项卡。
在这里，你将添加一个纹理元素，如下所示：

![](/assets/images/vr/tutorial-hand-right/shading-add-texture-element.png)
![](/assets/images/vr/tutorial-hand-right/texture-element.png)

在该元素中，点击“打开”，选择你的纹理，在我们的案例中是`something\VRpackTemplate\textures\hologram_hands.png`。
确保将线性更改为最近邻，否则你的纹理会显得模糊。
最后，它将看起来像这样：

![](/assets/images/vr/tutorial-hand-right/texture-element-complete.png)

现在是时候将纹理添加到模型的材质上了。
你需要将黄色点拖动并连接到另一个黄色点，如下所示：

![](/assets/images/vr/tutorial-hand-right/texture-base-connect.png)

如果一切顺利，你的模型现在应该看起来像这样：

![](/assets/images/vr/tutorial-hand-right/texture-on-model.png)

## 编辑模型

在编辑模型时，你几乎拥有完全的自由，唯一的要求是模型只能使用一个纹理。

### 编辑模型（简单）

由于这是简单教程，我们将教你如何将手变成手臂。

首先，我们需要确定该对象的尺寸。

![](/assets/images/vr/tutorial-hand-right/model-dimensions.png)

这张图片显示3个像素在Blender中等于18.75米，一个手臂长12个像素，这意味着手臂在Blender中是`4 * 18.75 = 75米`。
编辑尺寸时，它将看起来像这样：

![](/assets/images/vr/tutorial-hand-right/edited-dimensions-1.png)

如果我们将其导入Minecraft，手臂将会太远。这是因为原始模型是为手而设计的，而不是手臂。因此，我们需要将其向下移动`3 * 18.75 = 56.25米`。

![](/assets/images/vr/tutorial-hand-right/edited-dimensions-2.png)

#### 纹理处理

由于这是一个手臂，我们将使用Steve的手臂模型，你可以像上面那样导入它。

![](/assets/images/vr/tutorial-hand-right/hologram-hands-steve.png)

![](/assets/images/vr/tutorial-hand-right/steve-texture-stretched.png)

现在你可能会注意到你的纹理被拉伸了。要解决这个问题，我们将进入UV编辑并编辑UV贴图。
UV编辑看起来几乎与Blockbench相同。

![](/assets/images/vr/tutorial-hand-right/uv-map.png)

:::提示
开启这个像磁铁一样的图标会更精确。
![](/assets/images/vr/tutorial-hand-right/magnet-icon.png)
:::

我们首先选择手的顶部和底部。

![](/assets/images/vr/tutorial-hand-right/uv-map-top-selected.png)

接下来，我们选择移动工具。

![](/assets/images/vr/tutorial-hand-right/uv-map-pos.png)

现在我们将顶部面和底部面移动到纹理的顶部。

![](/assets/images/vr/tutorial-hand-right/uv-map-top-move-up.png)

手臂的侧面也是如此。

你的新UV贴图应该看起来像这样：

![](/assets/images/vr/tutorial-hand-right/uv-map-side-up.png)

如果我们查看手臂的外观，我们会发现一切都已修复。

![](/assets/images/vr/tutorial-hand-right/uv-map-done.png)

#### 导出！

现在是时候导出你的模型了，首先将Steve的手臂纹理放入`VRpackTemplateRP\textures`。
将其命名为`hologram_hands.png`。

![](/assets/images/vr/tutorial-hand-right/export-texture.png)

现在让我们导出模型。

![](/assets/images/vr/tutorial-hand-right/export-model-1.png)

将模型命名为`hologram_hand_right.obj`。

![](/assets/images/vr/tutorial-hand-right/export-model-2.png)

#### 在游戏中测试

将包加载到Minecraft中并尝试一下，如果它看起来像这样，你就成功完成了本教程！

![](/assets/images/vr/tutorial-hand-right/export-done.png)

<Button link="https://github.com/Bedrock-OSS/wiki-addon/releases/download/download/vr_edit_model.mcpack">
    获取教程最终结果！
</Button>

## 你的进度

-   [x] 设置Minecraft VR
-   [x] 设置包
-   [x] 编辑模型