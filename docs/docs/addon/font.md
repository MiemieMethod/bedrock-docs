# 字体

**字体（Font）**是资源包中用于控制文本字形显示的客户端资源。基岩版可以通过位图字形、TTF字体和MSDF字体显示文本，资源包可以替换原版字形，也可以注册新的字体供JSON UI等界面文件引用。

## 概述

字体资源通常位于资源包的{{file|font}}目录中。原版资源包含多种字体资源，例如ASCII字形、标准银河字母字形、Unicode字形页、TTF字体文件和MSDF字体文件。

在资源包中修改字体通常有两类目标：

- 替换原版字体资源，使游戏内已有文本呈现为新的字形风格。
- 注册新的字体名称或字体别名，并在JSON UI文件中通过`font_type`引用。

## 位图字形

基岩版的传统字体资源使用按Unicode码位分组的位图字形页。常见文件包括{{file|default8.png}}、{{file|ascii_sga.png}}和一系列形如{{file|glyph_00.png}}至{{file|glyph_ff.png}}的字形页。

每个{{file|glyph_xx.png}}文件对应**基本多文种平面（Basic Multilingual Plane）**中的一段字符。例如，{{file|glyph_4e.png}}对应`U+4E00`至`U+4EFF`范围内的字符。每张字形页通常按16×16网格排列字符图像。

## 字体元数据

{{file|font_metadata.json}}用于注册字体文件和字体别名。它通常包含`fonts`数组和`font_aliases`数组：

```json title="font_metadata.json"
{
  "version": 1,
  "fonts": [
    {
      "font_format": "ttf",
      "font_name": "ExampleFont",
      "version": 1,
      "font_file": "font/example_font",
      "lowPerformanceCompatible": false
    }
  ],
  "font_aliases": [
    {
      "alias": "ExampleAlias",
      "fonts": [
        {
          "font_reference": "ExampleFont"
        }
      ]
    }
  ]
}
```

/// define
`font_format`

- 字体格式。常见值包括`ttf`和`msdf`。

`font_name`

- 字体的注册名称。其他字体别名或界面文件可以引用该名称。

`font_file`

- 字体文件路径，不包含扩展名。

`font_aliases`

- 字体别名列表。别名可以组合多个字体，并通过字符范围指定回退关系。

`font_ranges`

- 字体适用的Unicode码位范围，范围端点使用十进制整数表示。

///

## 在界面中引用

JSON UI控件可以通过`font_type`指定字体名称或字体别名：

```json
{
  "namespace": "example",
  "example_label": {
    "type": "label",
    "font_type": "ExampleFont",
    "text": "示例文本"
  }
}
```

字体引用只改变文本渲染方式，不改变[本地化](localization.md)文本本身。若一行文本中存在当前字体无法显示的字符，游戏可能回退到其他字体或使用缺字图像。

## 性能与兼容性

自定义字体可能显著增加文本渲染成本，尤其是在字体覆盖范围很大、界面文本很多或设备性能较低时。为减少问题，资源包应尽量限制字体覆盖范围，避免注册过多大型字体，并在低端设备上测试界面、聊天、物品名称和长文本页面的显示表现。

