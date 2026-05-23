# 闪烁标语文件

**闪烁标语文件（Splashes File）**是资源包中用于定义主菜单**闪烁标语（Splash）**的数据驱动文件，文件名硬编码为{{file|splashes.json}}，位于资源包根目录。

## 概述

闪烁标语是Minecraft主菜单中标题文字旁边以黄色文字随机显示的短句。资源包可通过提供闪烁标语文件向游戏注入自定义标语文本，或控制其是否与其他资源层（如父包或子包）中的标语合并显示。

/// html | div.treeview
- {{file|rp}} 资源包
    - {{file|splashes.json}}
///

## 结构

/// html | div.treeview
- {{json|object|}}：根对象。
    - {{json|bool|canMerge}}：是否允许本文件的标语列表与其他资源层（如父包或子包）中的闪烁标语合并。省略时默认不合并。
    - {{json|array|splashes}}：无条件显示的闪烁标语列表。每个元素为一个字符串，支持本地化键。
    - {{json|array|conditional}}：需要满足特定条件才可显示的闪烁标语列表。
        - {{json|object|}}：一组带条件的标语项。
            - {{json|object|requires|required=1}}：触发该组标语所需满足的条件。
                - {{json|array|platforms}}：需要满足的平台名称列表，如`"Android"`、`"iOS"`等。
                - {{json|array|treatments}}：需要满足的处理包（Treatment Pack）列表。
                - {{json|array|stores}}：需要满足的商店列表。
            - {{json|array|splashes}}：条件满足时可被随机选取的标语列表，每个元素为字符串，支持本地化键。
///

## 参考阅读

- [[闪烁文字|mcwzh:闪烁文字]]（Minecraft Wiki）
