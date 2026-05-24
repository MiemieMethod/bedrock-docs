# 启动Minecraft编辑器<!-- md:flag vanilla -->

Minecraft编辑器是Windows版Minecraft基岩版提供的创作者工具模式。它需要键盘和鼠标，主要用于创建、编辑、测试和导出世界项目。

使用编辑器前，应先确保设备满足启动器最低要求，并已在启动器中安装Minecraft基岩版。

## 使用范围与定位

- 编辑器不是新的游戏模式，而是用于世界创作流程的工具框架。
- 编辑器仍在持续迭代，功能、界面和入口名称可能随版本调整。
- 现行说明将其定位为Windows电脑与键盘鼠标工作流，并以Minecraft Preview为主要入口。
- Microsoft Learn当前的重定向配置仍保留`EditorOverview`、`EditorInstallation`、`EditorTutorial`与`EditorExtensionsIntroduction`等页面入口；若不同页面用语存在差异，应优先以当前Learn页面说明为准。

## 先安装Minecraft Preview

官方帮助中心当前给出的Windows端Preview安装路径为：

1. 打开Minecraft启动器。
2. 在左侧选择**Minecraft: Bedrock Edition**。
3. 打开**Latest release**菜单。
4. 选择**Latest preview**。
5. 点击**Install**或**Play**。

如果启动器界面与上述描述不同，应先确认当前启动器版本的页面布局，再查阅对应的官方入口说明。

## 通过启动器或快捷方式打开

相关材料对编辑器入口给出了两类写法：

1. 通过启动器中的编辑器入口直接启动。
2. 通过桌面快捷方式以协议方式启动。

启动后，编辑器会显示创建项目或打开已有项目的界面。若只想了解编辑器的概念和工作方式，请参阅[编辑器](../../docs/general/editor.md)。

## 通过快捷方式打开

也可以创建Windows桌面快捷方式。不同入口说明存在两种常见协议写法：

```text
minecraft-preview:?Editor=true
```

或：

```text
minecraft-preview://creator/?Editor=true
```

协议地址区分大小写。若快捷方式打开了普通游戏而不是编辑器，应先检查当前参考来源使用的是哪一种协议写法，再检查地址是否拼写正确。

## 启动后检查项

正常启动编辑器后，通常应看到“创建项目”或“打开已有项目”的入口页面。若界面仍为普通游玩界面，应优先检查以下内容：

1. 是否已经安装Minecraft Preview。
2. 快捷方式协议是否包含`?Editor=true`参数。
3. 当前参考的官方入口说明与本机启动器版本是否一致。

## 排查默认应用

如果预览版快捷方式无法启动编辑器，Windows可能把`minecraft:`或`minecraft-preview:`协议绑定到了其他应用。可以按以下步骤检查：

1. 按++windows+i++打开Windows设置。
2. 进入**应用**。
3. 打开**默认应用**。
4. 搜索**Minecraft**。
5. 找到与`MINECRAFT`、`MINECRAFT-PREVIEW`、`URL:minecraft`或`URL:minecraft-preview`相关的条目。
6. 将其默认应用改为需要启动的Minecraft版本。

/// warning | 预览版风险
预览版可能包含尚未稳定的编辑器功能。编辑正式项目之前，应先备份项目或导出世界副本。
///

## 与普通脚本测试的关系

若当前工作并不在编辑器中运行，而是在普通世界中测试脚本功能，应在实验性玩法中按需开启Beta APIs开关。编辑器入口本身不替代实验性开关管理。

## 相关资源

- [Minecraft Bedrock Editor概览（Microsoft Learn）](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockeditor/editoroverview?view=minecraft-bedrock-stable)
- [官方Editor API文档](https://aka.ms/EditorAPI)
- [Editor Extension Starter Kit](https://github.com/Mojang/minecraft-editor-extension-starter-kit)
- [Editor Extension Samples](https://github.com/Mojang/minecraft-editor-extension-samples)
- [minecraft-editor仓库与讨论区](https://github.com/Mojang/minecraft-editor)
- [官方反馈站中的编辑器分区](https://feedback.minecraft.net/hc/en-us/community/topics/31501891355661)