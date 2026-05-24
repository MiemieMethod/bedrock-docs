# 图标文件

**图标文件（Icon File）**是附加包中用于在游戏界面中代表该包的视觉标识图像，文件名硬编码为{{file|pack_icon.png}}，位于附加包根目录。此外，针对存在已知漏洞的包，可在根目录下额外提供{{file|bug_pack_icon.png}}作为替代显示图标。

## 概述

在游戏的附加包管理界面、关联世界的包列表等位置，每个附加包条目左侧会显示其图标文件。当游戏检测到该附加包存在已知漏洞时，将改为显示{{file|bug_pack_icon.png}}；若后者不存在，则仍显示{{file|pack_icon.png}}。

图标文件格式须为PNG格式。建议图标为正方形图像，推荐分辨率为128×128像素。图标应能清晰代表该包的主题或品牌，以便用户在包列表中快速辨认。

/// html | div.treeview
- {{file|pack}} 附加包
    - {{file|pack_icon.png}}
    - {{file|bug_pack_icon.png}}
///