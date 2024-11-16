---
title: 使用架构
mentions:
    - SirLich
    - MedicalJewel105
    - 7dev7urandom
    - KalmeMarq
description: 在VSCode中进行附加包开发时使用架构。
---

JSON架构为你提供了两样东西：验证以确保你的JSON具有正确的结构，以及（取决于编辑器的支持）IntelliSense来帮助你正确编写JSON。架构的好处在于，当你出错时，它们会立即给出反馈，但它们并不能捕捉到所有问题。

JSON架构本身就是JSON文件，并不会单独执行任何操作。你可以编写自己的架构或使用他人的架构。目前已经有一些适用于基岩版的架构。由于我所知，没有任何架构是“官方的”，而且基岩版是一个不断变化的目标，因此你找到的任何架构可能都会存在一些不准确之处。因此，请记住：有时问题出在你的代码中，有时架构可能是错误的。如果你发现了错误的架构，请考虑改进它，并向作者提交一个拉取请求，以便我们共同受益。

要使验证工作，你需要一个验证器。这里有很多选择，包括特定于编辑器的选项。

## 架构

存在许多架构，且有许多细微的差别。尝试不同的架构，看看哪个最适合你：

| 作者                                                                   | 支持                                                                                                          | 备注                                             |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [Assassin](https://github.com/aexer0e/bedrock-schema)                 | 行为包实体文件                                                                                              | 本文所写的原始架构                               |
| [Tschrock's](https://github.com/bedrock-studio/bedrock-json-schemas/) | 清单、角色动画控制器、角色动画、角色资源定义、渲染控制器、几何体                                            |                                                  |
| [stirante](https://github.com/stirante/bedrock-shader-schema/)        | 着色器                                                                                                      |                                                  |
| [KalmeMarq](https://github.com/KalmeMarq/Bugrock-JSON-UI-Schemas/)    | JSON UI文件（包括_ui_defs.json和_global_variables.json）                                                    |                                                  |

## VSCode

要在VSCode中的JSON文件中使用此架构，只需将以下行添加到你的根对象中：

`"$schema": "https://aexer0e.github.io/bedrock-schema/"`

它应该看起来像这样：

<CodeHeader></CodeHeader>

```json
"format_version": "1.14.0",
"$schema": "https://aexer0e.github.io/bedrock-schema/"
```

### 将架构添加到工作区

如果你想在工作区内的所有文件中使用此架构，可以将其添加到VS Code工作区的设置中。

为此，请确保你在工作区中，然后按`Ctrl+Shift+P`，输入并选择`>Preferences: Open Workspace Settings (JSON)`。之后，将以下内容添加到根对象中：

<CodeHeader></CodeHeader>

```json
"settings": {
    "json.schemas": [
        {
            "fileMatch": [
                "*.json"
            ],
            "url": "https://aexer0e.github.io/bedrock-schema/"
        }
    ]
}
```

要测试它是否有效，请创建一个`.json`文件，打开一个对象，看看是否会出现自动完成选项。（你也可以按`Ctrl+Space`强制显示可用选项。）