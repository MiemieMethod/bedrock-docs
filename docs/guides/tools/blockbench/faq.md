# 常见问题

/// details-info | 源文档
该页面翻译自[Blockbench文档](https://blockbench.net/wiki/blockbench/faq)
///

## Blockbench是免费的吗？

是的。Blockbench完全免费，适用于所有用户和所有用途！该项目是开源的，由社区支持，并通过捐赠和赞助商资金维持。

## 我能在（商业）项目中使用Blockbench的模型吗？

你用Blockbench制作的一切都是你的作品。Blockbench只是一款工具。这意味着你可以自由使用和重新发布用Blockbench制作的任何内容，甚至用于商业用途。

## 我该如何开始？

[快速入门向导](https://blockbench.net/quickstart)会告诉你应该选择哪种格式，并为你的具体需求提供有用的信息、教程和资源。

## Mojang使用Blockbench吗？

Mojang在内部使用Blockbench作为建模和制作生物及其他资产动画的工具。一些用Blockbench设计的生物示例包括美西螈、山羊、骆驼和探路者。

Mojang还支持Blockbench的开发，既用于内部用途，也用于Minecraft社区。

## 我应该在哪里报告错误？

你可以在Github上的[Blockbench漏洞追踪器](https://github.com/JannisX11/blockbench/issues)报告问题。在报告漏洞前，请确保该漏洞尚未被报告。

## 我在哪里可以找到错误消息？

如果Blockbench或插件出现问题，你可以在Blockbench控制台中看到错误消息。要查看控制台，同时按下Control + Shift + I。在某些情况下，你可能不会直接看到控制台，所以需要点击"Console"选项卡。在漏洞报告中包含错误消息的截图。

## 网页应用预览无法加载。我该怎么办？

请确保你的浏览器支持WebGL。访问[get.webgl.org](https://get.webgl.org)并检查是否出现立方体。如果没有，请更新或切换浏览器。Chrome、Edge、Firefox和Opera的最新版本应该可以工作。

如果这没有帮助，可能是你的图形驱动程序的个别问题。

## 网页应用有哪些限制？

网页应用是应用程序的完整功能版本。由于浏览器中的安全限制，只有某些导入/导出功能需要额外步骤。模型导入仍然可能，但在许多情况下必须手动加载纹理。

## Blockbench可作为移动应用使用吗？

Blockbench可作为渐进式网络应用使用。这意味着你可以直接从浏览器安装它，无需使用APK或应用商店。你可以在[下载页面](https://blockbench.net/downloads/)找到安装说明。

## 我如何添加参考图像/蓝图？

你可以向Blockbench添加参考图像。它们可以放置为模型后面的背景，或在UI上方。在正交相机角度下，图像可用作蓝图。要添加新的参考图像，在预览中单击右键，然后点击"Add Reference Image"。右键单击参考图像可更改其设置、将其移到不同图层，或为蓝图启用清晰模式。退出参考图像编辑模式后，你可以双击参考图像再次编辑它。

## Blockbench是用什么技术和编程语言构建的？

Blockbench是用网络技术构建的。这允许它在不同平台上无缝工作，甚至在Android、iOS和Chromebook上作为网络应用工作。

该程序主要用JavaScript和TypeScript编写。3D预览使用WebGL和THREE.JS渲染。可自定义界面主要用JavaScript和TypeScript编写，部分动态组件（如Outliner）使用Vue.js 2进行动态渲染。

Windows、Linux和Mac上的桌面应用是通过Electron创建的。

Blockbench还使用多种其他开源库。可在"帮助">"关于"中找到完整列表。

## 为什么Blockbench界面闪烁和模糊？

这是你的图形设置的问题。如果你使用Nvidia显卡，请打开Nvidia控制面板，选择"3D Settings">"Manage 3D Settings"并禁用"Antialiasing - FXAA"。点击"Apply"。重新启动Blockbench后更改将显示。

## Discord服务器

更多常见问题，包括关于建模的问题，在[Blockbench Discord服务器](https://discord.gg/WVHg5kH)上解答。