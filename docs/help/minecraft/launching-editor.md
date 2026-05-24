# 启动Minecraft编辑器<!-- md:flag vanilla -->

Minecraft编辑器是Windows版Minecraft基岩版提供的创作者工具模式。它需要键盘和鼠标，主要用于创建、编辑、测试和导出世界项目。

使用编辑器前，应先确保设备满足启动器最低要求，并已在启动器中安装Minecraft基岩版。

## 使用范围与定位

- 编辑器不是新的游戏模式，而是用于世界创作流程的工具框架。
- 编辑器仍在持续迭代，功能、界面和入口名称可能随版本调整。
- 来源README将编辑器定位为Windows电脑与键盘鼠标工作流，并以启动器中的预览版路径为主要入口。

## 通过启动器打开

推荐使用Minecraft启动器打开编辑器：

1. 打开Minecraft启动器。
2. 进入**Creator Tools**页。
3. 安装或选择Minecraft基岩版（常见为预览版分发路径）。
4. 点击**Launch Editor**启动编辑器。

启动后，编辑器会显示创建项目或打开已有项目的界面。若只想了解编辑器的概念和工作方式，请参阅[编辑器](../../docs/general/editor.md)。

## 通过快捷方式打开

也可以创建Windows桌面快捷方式，并将目标设置为以下地址之一：

```text
minecraft://creator/?Editor=true
```

预览版可以使用：

```text
minecraft-preview://creator/?Editor=true
```

协议地址区分大小写。若快捷方式打开了普通游戏而不是编辑器，应先检查地址是否拼写正确。

## 启动后检查项

正常启动编辑器后，通常应看到“创建项目”或“打开已有项目”的入口页面。若界面仍为普通游玩界面，应优先检查以下内容：

1. 启动器入口是否为Creator Tools路径。
2. 快捷方式协议是否包含`?Editor=true`参数。
3. 当前版本是否支持编辑器入口。

## 排查默认应用

如果预览版快捷方式无法启动编辑器，Windows可能把`minecraft:`协议绑定到了正式版或其他应用。可以按以下步骤检查：

1. 按++windows+i++打开Windows设置。
2. 进入**应用**。
3. 打开**默认应用**。
4. 搜索**Minecraft**。
5. 找到与`MINECRAFT`或`URL:minecraft`相关的条目。
6. 将其默认应用改为需要启动的Minecraft版本。

/// warning | 预览版风险
预览版可能包含尚未稳定的编辑器功能。编辑正式项目之前，应先备份项目或导出世界副本。
///

## 相关资源

- [Minecraft Bedrock Editor概览（Microsoft Learn）](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockeditor/editoroverview?view=minecraft-bedrock-stable)
- [官方Editor API文档](https://aka.ms/EditorAPI)
- [Editor Extension Starter Kit](https://github.com/Mojang/minecraft-editor-extension-starter-kit)
- [Editor Extension Samples](https://github.com/Mojang/minecraft-editor-extension-samples)
- [minecraft-editor仓库与讨论区](https://github.com/Mojang/minecraft-editor)
- [官方反馈站中的编辑器分区](https://feedback.minecraft.net/hc/en-us/community/topics/31501891355661)
