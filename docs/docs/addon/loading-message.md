# 加载消息文件

**加载消息文件（Loading Messages File）**是资源包中用于自定义加载界面提示文字的数据驱动文件，文件名硬编码为{{file|loading_messages.json}}，位于资源包根目录。

## 概述

**加载消息（Loading Message）**，又称**加载提示（Loading Tip）**，是Minecraft在进入世界或切换场景时加载界面上随机显示的提示文字。通过在资源包中提供加载消息文件，开发者可以添加自定义的加载消息文本，分别针对正常游戏模式和[编辑器](../../help/bedrock/editor.md)模式配置不同的消息列表。

/// html | div.treeview
- {{file|rp}} 资源包
    - {{file|loading_messages.json}}
///

## 结构

/// html | div.treeview
- {{json|object|}}：根对象。
    - {{json|array|loading_messages}}：正常游戏模式下显示的加载消息列表。每个元素为一个字符串，支持本地化键。
    - {{json|array|editor_loading_messages}}：编辑器模式下显示的加载消息列表。每个元素为一个字符串，支持本地化键。
///

## 参考阅读

- [[加载提示|mcwzh:加载提示]]（Minecraft Wiki）
