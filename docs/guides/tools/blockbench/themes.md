# 自定义主题

/// details-info | 源文档
该页面翻译自[Blockbench文档](https://blockbench.net/wiki/blockbench/themes)
///

主题允许你改变Blockbench的视觉外观。你可以将`.bbtheme`文件拖放到Blockbench中来加载它们。

## 创建主题

主题可以使用Blockbench中的主题编辑器创建。你可以通过进入`File`>`Preferences`>`Theme...`来打开它。

### 颜色和字体

你可以通过点击彩色矩形并选择颜色来改变基本界面颜色。你还可以改变字体。

* 主字体是默认字体。
* 标题字体用于标题和大型文本，如面板标签。
* 代码字体用于代码框和编辑器内。

要选择字体，请输入系统中已安装字体的完整字体名称。如果你与他人共享带有自定义字体的主题，需要确保使用该主题的所有人也安装了该字体。如果你想定义一个或多个备用字体，以防第一个字体未安装，你可以创建一个字体名称列表，用逗号分隔。

### 自定义CSS

Blockbench使用网络技术构建。如果你想进一步自定义Blockbench的外观，你可以使用网络的样式语言：CSS。

你可以在主题对话框底部的自定义CSS编辑器中输入CSS规则。例如，使用以下代码为对话框提供磨砂玻璃背景：

```css
dialog {
  background-color: rgba(20, 22, 30, 0.7);
  backdrop-filter: blur(5px);
}
```

为了检查界面并找出要使用的CSS选择器，请进入`Help`>`Developer`>`Open Dev Tools`。你可以在[这篇关于使用Chrome开发工具查看和更改CSS的文章](https://developer.chrome.com/docs/devtools/css/)中了解更多信息。

如果你是CSS新手，想了解更多，请查看[W3Schools CSS教程](https://www.w3schools.com/css/)。

## 共享主题

一旦你对主题满意，你可以使用对话框操作栏中的`Export Theme`按钮将其导出为文件。你可以与朋友个人分享该文件。

如果你想与Blockbench社区分享该主题，你可以在[Blockbench Discord服务器](https://discord.gg/blockbench)的#bb-themes频道中发布它。确保包括名称、描述和预览图像。