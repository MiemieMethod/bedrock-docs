# Blockbench

Blockbench是基岩版创作者最常用的方块风格三维编辑器。它的优势不是“能做任意复杂模型”，而是把Minecraft需要的几何体、骨骼、UV、纹理和动画放进同一个工作区，并能导出基岩版能读取的几何体和动画文件。

本小节会先带你认识Blockbench的工作方式，再通过若干实践页面完成基础操作：

- [使用指南](how-to-use.md)：制作一个能导出到资源包的简单实体视觉资源。
- [选择项目格式](formats.md)：判断什么时候使用`Bedrock Model`、`Generic Model`或旧格式。
- [界面与工作流](workflow-and-tips.md)：熟悉界面模式、轴心点、骨骼层级、绘制和截图。
- [动画表达式](animation-expressions.md)：在Blockbench动画中使用Molang风格表达式。
- [粒子与音效关键帧](effects-keyframes.md)：用效果动画器预览并导出粒子和音效。
- [Minecraft美术风格](minecraft-style.md)：检查模型、UV、纹理和像素风问题。
- [制作Minecraft风格标题](creating-minecraft-style-title.md)：用Blockbench制作像素风标题或展示图资产。
- [绘制皮肤](skin-tool.md)：使用Blockbench内置的皮肤项目格式绘制并导出Minecraft皮肤。
- [Minecraft Entity Wizard](entity-wizard.md)：通过官方插件分步骤生成一个完整的自定义实体附加包。
- [Minecraft Block Wizard](block-wizard.md)：通过官方插件分步骤生成一个完整的自定义方块附加包。

/// note | 网页版和桌面版
Blockbench既有桌面端，也有网页版和可安装的PWA。做基岩版项目时，桌面端在文件保存、资源路径和大型项目稳定性上通常更省心；如果只是临时查看或绘制小模型，网页版也能完成很多工作。
///

## 先理解四个模式

Blockbench的界面按创作阶段分成不同模式。后续教程会频繁切换它们。

/// define
编辑模式

- 用来创建立方体、骨骼和定位器，调整位置、大小、旋转、轴心点和UV映射。

绘制模式

- 用来创建或导入纹理，并直接在三维预览或UV面板上绘制。

动画模式

- 用来创建关键帧动画。基岩版模型可以导出动画JSON，实体再通过客户端实体定义和动画控制器播放它。

展示模式

- 主要用于Minecraft方块或物品格式，定义模型在手持、物品展示框、物品栏等场景中的显示方式。
///

## 基岩版创作时要避开的坑

### 选错格式

新建项目时要选择`Bedrock Model`或与目标匹配的基岩版格式。Java版方块/物品模型和基岩版几何体不是同一套格式，直接导出给基岩版使用通常会失败。

### 骨骼命名随意

动画和客户端实体文件会按骨骼名引用模型部件。骨骼名应使用小写字母、数字和下划线，尽量保持`root`、`body`、`head`这类清晰结构。

### 轴心点放错

骨骼围绕轴心点旋转。门、手臂、头部、轮子这类部件的轴心点必须放在真实关节或旋转中心，否则动画会像“整块飞出去”一样不自然。

### 纹理比例不一致

Minecraft美术风格依赖像素和模型单位之间的稳定比例。不要把一部分纹理画成16像素风，另一部分画成64像素细节；这种混合分辨率会让模型显得不像原版内容。

## 建议的文件分工

Blockbench自己的工程文件通常保存为`.bbmodel`，这是继续编辑时最重要的源文件。导入游戏时还需要导出或保存这些文件：

/// html | div.treeview
- 资源包
    - {/{file|models/entity/xxx.geo.json}}：几何体。
    - {/{file|textures/entity/xxx.png}}：颜色纹理。
    - {/{file|animations/xxx.animation.json}}：动画。
    - {/{file|animation_controllers/xxx.animation_controller.json}}：动画控制器，通常也会手动编辑。
    - {/{file|entity/xxx.entity.json}}：客户端实体定义，负责把模型、纹理、材质和动画关联起来。
///

进入[使用指南](how-to-use.md)后，我们会按这个文件分工完成一个最小可用流程。