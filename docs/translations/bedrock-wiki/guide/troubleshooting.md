# 故障排除

/// details-info | 来源信息
- 原文仓库：[github.com/Bedrock-OSS/bedrock-wiki](https://github.com/Bedrock-OSS/bedrock-wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///


为Minecraft基岩版创建附加包是一个相对直接的过程——_一旦掌握窍门后_。但初次尝试通常充满挫折，极易出现各种错误。本文档包含修复这些棘手问题的技巧与最佳实践建议。

在深入特定领域的故障排除之前，请完整阅读本页内容。

## 重新加载游戏

首先，你应当始终尝试完全重载Minecraft。这意味着彻底关闭游戏后重新启动。这可以解决许多错误，特别是那些与通过文件路径访问的资产相关的问题（如纹理材质或战利品表）。

## 开发环境配置

避免棘手错误的最佳方式是配置正确的开发环境。建议回顾[软件准备文档](./software-preparation.md)获取编辑器推荐。最重要的是配置JSON语法检查器（[或使用在线JSON校验工具](https://jsonlint.com/)），并将资源包存放在`development_behavior_packs`和`development_resource_packs`目录。

如果将附加包存放在常规文件夹中，可能会遇到"包缓存"问题——即你编辑了某处的文件，但游戏仍在读取旧文件。

## 内容日志

/// warning | 善用内容日志！
内容日志是你调试附加包的最佳工具。请勿跳过此步骤！
///

/// tip | 提示
错误信息不会在多次运行间自动清除，因此内容日志中显示的错误可能是_之前运行_遗留的旧错误。
///

'内容日志'是游戏检测到的附加包问题清单。Minecraft会在每次加载世界时生成该列表。它可以捕获以下类型的问题：
    - 错误的纹理路径
    - 拼写错误的组件名称
    - 不正确的JSON结构

内容日志可在`设置 > 创作者`中启用。游戏加载时会显示初始日志，游戏过程中新出现的错误也会实时更新。

![](/assets/images/guide/content_log.png)

### 日志文件位置

内容日志以`.txt`格式保存在以下路径：

- *Windows*: `C:\Users\用户名\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\logs`
- *Android:* `/storage/emulated/0/Android/data/com.mojang.minecraftpe/files/games/com.mojang/logs`

## 使用原版资源

建议下载原版资源包和行为包。你可以在[官方附加包页面](https://www.minecraft.net/en-us/addons/)找到这些资源。遇到问题时可以与原版文件进行对比！

## JSON模式校验

JSON模式是验证文件有效性的重要工具。了解更多关于JSON模式的使用方法，请参阅[配置JSON架构校验](../../../guides/tools/json-schemas.md)。

# 附加包故障排查

## 实体

[实体问题排查](/entities/troubleshooting-entities){ .md-button }

## 方块

[方块问题排查](/blocks/troubleshooting-blocks){ .md-button }