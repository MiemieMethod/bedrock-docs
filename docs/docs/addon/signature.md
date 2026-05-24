# 签名文件

**签名文件（Signatures File）**是附加包中用于提供文件签名验证的数据驱动文件，文件名硬编码为{{file|signatures.json}}，位于附加包根目录，与[清单文件](manifest.md)处于同级目录。

## 概述

签名文件为附加包内指定文件记录其SHA-256杂凑值的Base64编码。游戏在验证附加包时，会检测签名文件中所列出的每个文件的实际杂凑值是否与文件中记录的值吻合。若全部吻合，该附加包将被标记为已信任（Trusted）。签名文件可为附加包开发者提供一定的防篡改保护。

对于来源于用户自行加载的附加包，签名文件并非必须存在。

/// html | div.treeview
- {{file|pack}} 附加包
    - {{file|signatures.json}}
///

## 结构

签名文件的根是一个数组，每个元素为一个签名条目，记录包内某一文件的相对路径及其杂凑值：

/// html | div.treeview
- {{json|array|}}：根数组。
    - {{json|object|}}：一个签名条目。
        - {{json|string|path|required=1}}：相对于附加包根目录的文件路径。
        - {{json|string|hash|required=1}}：该文件SHA-256杂凑值的Base64编码。
///