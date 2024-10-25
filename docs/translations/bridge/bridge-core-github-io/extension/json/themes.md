# 主题

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/json/themes/](https://bridge-core.github.io/extension-docs/json/themes/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/json/themes.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/json/themes.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@4ec6002ba312583b1a86a0e98d897b87dd8e220a -->
///

## 概述

主题可以以多种方式改变bridge.的外观。这包括更改亮色模式和暗色模式、语法高亮器以及bridge.用户界面的许多其他部分。

## 扩展集成

扩展也可以通过在`<扩展名称>/themes`文件夹中提供新主题来添加主题。每个要添加的主题创建一个JSON文件。单个文件名无关紧要。

## 加载行为

bridge.首先应用默认颜色主题，然后用你提供的主题覆盖它。这意味着你只需定义在自定义主题中应更改的颜色。此行为的一个例外是文件高亮器定义。你必须明确设置所有颜色，否则bridge.将使用默认文本颜色（白色/黑色）。

## 格式

### 主要

| 名称          | 类型                      | 描述                                         |
| ------------- |-------------------------| -------------------------------------------- |
| `name`        | `String`                | 主题名称                                    |
| `id`          | `String`                | 主题的UUID                                  |
| `colorScheme` | `String<light|dark>`    | 主题的颜色方案                              |
| `colors`      | `Object<ThemeDefinition>`          | 主题的颜色                                  |
| `highlighter` | `Object<HighlighterDefinition>`         | 你的bridge.主题的语法高亮器颜色           |
| `monaco`      | `Record<string, string>` | Monaco编辑器的颜色方案                      |

### 主题定义

| 名称                      | 类型     | 描述                                                                          |
| ------------------------- | -------- | ------------------------------------------------------------------------------ |
| `primary`                 |   `String` | 颜色；影响菜单图标、活动标签、MoLang编辑图标等                              |
| `secondary`               |   `String` | 颜色                                                                          |
| `accent`                  |   `String` | 颜色；影响工具栏图标                                                          |
| `error`                   |   `String` | 颜色；影响悬停错误、!错误标记、关闭提示框上的关闭按钮等                     |
| `info`                    |   `String` | 颜色                                                                          |
| `success`                 |   `String` | 颜色；影响关闭提示框上的保存按钮                                            |
| `warning`                 |   `String` | 颜色                                                                          |
| `background`              |   `String` | 颜色；影响编辑器的背景                                                        |
| `sidebarNavigation`       |   `String` | 颜色；影响导航侧边栏                                                          |
| `expandedSidebar`         |   `String` | 颜色；影响包含文件夹和文件的侧边栏                                          |
| `sidebarSelection`        |   `String` | 颜色                                                                          |
| `menu`                    |   `String` | 颜色；影响菜单                                                                |
| `toolbar`                 |   `String` | 颜色；影响带下拉菜单的顶部栏                                                |
| `footer`                  |   `String` | 颜色；影响包含通知的底部栏                                                  |
| `tooltip`                 |   `String` | 颜色；影响当你悬停在按钮上时显示的工具提示                                  |
| `tabActive`               |   `String` | 颜色                                                                          |
| `tabInactive`             |   `String` | 颜色                                                                          |
| `lineHighlightBackground` |   `String` | 颜色                                                                          |
| `scrollbarThumb`          |   `String` | 颜色                                                                          |
| `behaviorPack`            |   `String` | 颜色                                                                          |
| `resourcePack`            |   `String` | 颜色                                                                          |
| `skinPack`                |   `String` | 颜色                                                                          |
| `worldTemplate`           |   `String` | 颜色                                                                          |

### 高亮器定义

| 名称                | 类型                  | 描述                                                          |
| ------------------- | --------------------- | -------------------------------------------------------------- |
| `property`          |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `keyword`           |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `definition`        |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `atom`              |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `number`            |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `string`            |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `variable`          |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `variableStrong`    |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `meta`              |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `comment`           |   `Object<StyleObject>`     | 语法高亮器的自定义样式                                        |
| `colorCode.<Color>` |   `Object<StyleObject>`     | 语法高亮器的自定义样式；影响Minecraft颜色代码               |

### 样式对象

| 名称             | 类型                                              | 描述        |
| ---------------- | ------------------------------------------------- | ----------- |
| `color`          |   `String`                                          | 颜色        |
| `textDecoration` | `String<underline|overline|line-through|blink>` | 文本装饰     |
| `isItalic`       | `Boolean`                                         | 设置斜体文本 |

## 示例

```json
{
  "id": "bridge.default.dark",
  "name": "默认暗色",
  "colorScheme": "dark",
  "colors": {
    "text": "#fff",
    "primary": "#0073FF",
    "secondary": "#0073FF",
    "accent": "#0073FF",
    "error": "#ff5252",
    "info": "#2196f3",
    "warning": "#fb8c00",
    "success": "#4caf50",
    "background": "#121212",
    "sidebarNavigation": "#1F1F1F",
    "expandedSidebar": "#1F1F1F",
    "sidebarSelection": "#151515",
    "menu": "#252525",
    "footer": "#111111",
    "tooltip": "#1F1F1F",
    "toolbar": "#000000",
    "tabActive": "#121212",
    "tabInactive": "#1F1F1F",
    "lineHighlightBackground": "#1F1F1F"
  },
  "highlighter": {
    "type": {
      "color": "#a6e22e"
    },
    "keyword": {
      "color": "#f92672"
    },
    "definition": {
      "color": "#fd971f"
    },
    "atom": {
      "color": "#ae81ff"
    },
    "number": {
      "color": "#ae81ff"
    },
    "string": {
      "color": "#e6db74"
    },
    "variable": {
      "color": "#9effff"
    },
    "variableStrong": {
      "color": "#9effff"
    },
    "meta": {
      "color": "white"
    },
    "comment": {
      "color": "#75715e"
    },
    "colorCode.darkRed": {
      "color": "#AA0000"
    },
    "colorCode.red": {
      "color": "#FF5555"
    },
    "colorCode.gold": {
      "color": "#FFAA00"
    },
    "colorCode.yellow": {
      "color": "#FFFF55"
    },
    "colorCode.darkGreen": {
      "color": "#00AA00"
    },
    "colorCode.green": {
      "color": "#55FF55"
    },
    "colorCode.aqua": {
      "color": "#55FFFF"
    },
    "colorCode.darkAqua": {
      "color": "#00AAAA"
    },
    "colorCode.darkBlue": {
      "color": "#0000AA"
    },
    "colorCode.blue": {
      "color": "#5555FF"
    },
    "colorCode.lightPurple": {
      "color": "#FF55FF"
    },
    "colorCode.darkPurple": {
      "color": "#AA00AA"
    },
    "colorCode.white": {
      "color": "#FFFFFF"
    },
    "colorCode.gray": {
      "color": "#AAAAAA"
    },
    "colorCode.darkGray": {
      "color": "#555555"
    },
    "colorCode.black": {
      "color": "#000000"
    },
    "colorCode.minecoinGold": {
      "color": "#ff0000"
    },
    "colorCode.bold": {
      "color": "#fff",
      "textDecoration": "bold"
    },
    "colorCode.italic": {
      "color": "#fff",
      "textDecoration": "italic"
    },
    "colorCode.underline": {
      "color": "#fff",
      "textDecoration": "underline"
    }
  }
}
```

### 更多示例：

-   [`内置主题`](https://github.com/bridge-core/editor-packages/tree/main/packages/common/themes)
-   [`主题架构`](https://github.com/bridge-core/editor-packages/blob/main/packages/common/schema/bridge/theme/main.json)