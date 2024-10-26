---
title: 原始文本
mention:
  - BedrockCommands
  - GTB3NW
  - SpacebarNinja
description: 理解在 /tellraw 和 /titleraw 命令中使用的原始文本 JSON 组件。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

![](/assets/images/documentation/tellrawshow.png)

原始文本用于向玩家发送和显示富文本。这可以在 `/tellraw` 或 `/titleraw` 命令中使用。

在方括号 `[]` 内，这是您将列出多个文本对象的地方。

```json
{"rawtext":[]}
```

您可以通过在组件末尾添加逗号 `,` 来组合组件。

## 文本组件

显示文本。用于引号内。

**语法：**

```json
{"text":"<您的文本在这里>"}
```

**示例：**

向所有玩家发送“大家好！”的消息：

```json
/tellraw @a {"rawtext":[{"text":"大家好！"}]}
```

### 换行、换行符和 Unicode

1. 换行符使用 `\` 访问，用于在组件中使用引号 `"`。示例：

```json
/tellraw @a {"rawtext":[{"text":"他说，\"我喜欢苹果\"..."}]}
#在聊天中的输出：
#    他说，“我喜欢苹果”...
```

2. 换行符使用 `\n` 进行换行。示例：

```json
/tellraw @a {"rawtext":[{"text":"你好\n下一行"}]}
#在聊天中的输出：
#    你好
#    下一行
```

3. Unicode 提供一个唯一的数字，用于显示图标/表情符号。示例：

```json
/tellraw @a {"rawtext":[{"text":"\u263a"}]}
```
- 在聊天中的输出：
    - ![](/assets/images/concepts/emojis/hud/food.png)
> 注意：Unicode 符号将在 Minecraft 中显示为其对应的图标/表情符号。

有关更多信息和 Bedrock 中可用的完整 Unicode 列表，请参阅 [表情符号与符号](/concepts/emojis) 页面。

## 选择器组件

显示您选择的目标的名称。允许使用目标选择器参数。

**语法：**

```json
{"selector":"<目标>"}
```

**示例：**

1. 在聊天中发送所有玩家的名称：
```json
/tellraw @a {"rawtext":[{"selector":"@a"}]}
```
2. 在聊天中发送所有标记为“winner”的玩家的名称：
```json
/tellraw @a {"rawtext":[{"selector":"@a [tag=winner]"}]}
```

## 分数组件

显示来自记分板目标的分数。

**语法：**
```json
{"score":{"name":"<名称>", "objective":"<分数>"}}
```

- **`name`** - 这可以是任何选择器，如 `@p` 或玩家的名称。
    - 您还可以使用 **`*`** 通配符来显示读者自己的分数。
- **`objective`** - 您想要显示分数的记分板的名称。

在使用分数组件时，两个字段都是必需的。

**示例：**

1. 在聊天中显示最近玩家的积分分数：
```json
/tellraw @a {"rawtext":[{"score":{"name":"@p","objective":"points"}}]}
```
2. 在聊天中显示读者的金钱分数：
```json
/titleraw @a title {"rawtext":[{"score":{"name":"*","objective":"money"}}]}
```

## 翻译组件

允许创作者向用户显示本地化文本。要翻译的字符串列表在语言文件中。有关更多信息，请参阅 [文本与翻译](https://wiki.bedrock.dev/concepts/text-and-translations) 页面。

**语法：**

```json
{"translate":"<字符串>"}
```

**示例：**

```json
/tellraw @a {"rawtext":[{"translate":"multiplayer.player.joined"}]}
#在聊天中的输出：
#    %s 加入了游戏
```

在上面的示例中，它输出“`%s 加入了游戏`”。要使名称出现在 `%s` 位置，必须指定 `with`。需要使用数组 `[]` 而不是大括号 `{}`。

```json
/tellraw @a {"rawtext":[{"translate":"multiplayer.player.joined", "with": ["Steve"]}]}
#在聊天中的输出：
#    Steve 加入了游戏
```

![](/assets/images/documentation/tellrawtranslate.png)

### %%s

`translate` 和 `%s` 可以在本地化文件中没有匹配字符串的情况下使用。例如：

```json
/tellraw @a {"rawtext":[{"translate":"Hello %%s", "with":["Steve"]}]}
#在聊天中的输出：
#    Hello Steve
```

### 多个 %%s

`%%s` 可以多次使用。它们按显示的顺序填充。

```json
/tellraw @a {"rawtext":[{"translate":"Hello %%s and %%s", "with":["Steve","Alex"]}]}
#在聊天中的输出：
#    Hello Steve and Alex
```

### 使用 %%# 的顺序

填充 `%s` 的顺序可以通过在末尾用数字替换 `s` 来更改。例如，要交换上面示例中 Steve 和 Alex 的位置：

```json
/tellraw @a {"rawtext":[{"translate":"Hello %%2 and %%1", "with":["Steve","Alex"]}]}
#在聊天中的输出：
#    Hello Alex and Steve
```

而且，您可以使用原始文本组件，如下所示。

```json
/tellraw @a {"rawtext":[{"translate":"Hello %%s and %%s","with": {"rawtext":[{"text":"Steve"},{"translate":"item.apple.name"}]}}]}
#在聊天中的输出：
#    Hello Steve and Apple
```