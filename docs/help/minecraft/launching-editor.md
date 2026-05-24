# 启动Minecraft编辑器<!-- md:flag vanilla -->

Minecraft编辑器是Windows版Minecraft基岩版提供的创作者工具模式。它需要键盘和鼠标，主要用于创建、编辑、测试和导出世界项目。

使用编辑器前，应先确保设备满足启动器最低要求，并已在启动器中安装Minecraft基岩版。

## 通过启动器打开

推荐使用Minecraft启动器打开编辑器：

1. 打开Minecraft启动器。
2. 进入**Creator Tools**页。
3. 安装或选择Minecraft基岩版。
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
- [官方反馈站中的编辑器分区](https://feedback.minecraft.net/hc/en-us/community/topics/31501891355661)
