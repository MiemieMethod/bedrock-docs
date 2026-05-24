# 编辑器<!-- md:flag vanilla -->

Minecraft编辑器是基岩版内置的多方块编辑体验。它不是一个新的游戏模式，而是一个帮助创作者搭建、编辑和测试世界的工具框架；在界面上，它像是在普通游戏画面上叠加了一套专用编辑器窗口和工具栏。

/// warning | 平台限制
现行说明将编辑器描述为面向Windows电脑、键盘和鼠标的Preview工作流，不适用于移动端或主机。若后续页面调整入口，也应先确认当前启动路径，而不要假定所有版本都共享同一入口。
///

/// note | 不要与MC Studio混淆
旧版中国版MC Studio提供过地图编辑器、关卡编辑器、逻辑编辑器、特效编辑器、界面编辑器和调试工具<!-- md:flag china -->。这些工具面向中国版旧版作品维护，不是本教程所讲的国际版Minecraft编辑器；相关历史资料见[旧版中国版MC Studio工具链](../outdated/china-legacy-mc-studio.md)。
///

## 打开编辑器

先确认已经安装Minecraft Preview。官方帮助中心当前给出的Windows安装路径是：

1. 打开Minecraft启动器。
2. 在左侧选择**Minecraft: Bedrock Edition**。
3. 打开**Latest release**菜单。
4. 选择**Latest preview**。
5. 点击**Install**或**Play**。

安装完成后，再进入编辑器。现行说明给出的最短路径是：

1. 打开Minecraft启动器。
2. 安装Minecraft Preview。
3. 创建桌面快捷方式。
4. 通过快捷方式以编辑器模式启动游戏。

如果你想做桌面快捷方式，可以创建一个Windows快捷方式。不同入口说明对协议写法存在版本差异，常见写法包括以下两种：

```text
minecraft-preview:?Editor=true
```

或：

```text
minecraft-preview://creator/?Editor=true
```

如果其中一种写法无法拉起编辑器，应优先检查当前官方来源页面使用的是哪一种协议写法，再检查Windows默认应用是否把`minecraft:`或`minecraft-preview:`协议绑定到了正确版本。

## 三步快启流程

如果你希望按最短路径启动，可以直接按这三步执行：

1. 在启动器中安装Minecraft Preview。
2. 在Windows桌面创建编辑器快捷方式。
3. 通过该快捷方式启动，并确认看到“创建项目”或“打开项目”的界面。

这个流程适合快速验证设备环境是否可用。若你平时同时维护多个Minecraft安装版本，建议分别保留普通启动入口和编辑器入口，避免误开到普通游玩模式。

## 创建项目

启动后会看到创建新项目的界面。项目不是普通可游玩的世界本身，而是编辑器保存编辑状态和导出设置的工作空间。创建时需要设置项目名、世界选项和导出选项。导出时，编辑器会根据这些设置生成可游玩的`.mcworld`。

进入项目后，建议先做三件事：

1. 打开**File**菜单中的**UI Settings**，调整界面缩放、字体和主题。
2. 浏览欢迎或快速开始窗口，确认移动方式和常用工具入口。
3. 新建一个很小的测试区域，不要一开始就编辑正式地图。

## 移动和视角

编辑器有工具模式和准星模式。刚上手时记住这几条就够了：

- 在工具模式下，按住鼠标右键再用++w++、++a++、++s++、++d++移动。
- ++space++向上，++shift++向下。
- 在工具模式下，对准远处方块按++g++可以传送到视线位置。
- 右上角指南针可以帮助你确认朝向，也可以点击方向快速对齐视角。

## 认识常用窗口

编辑器窗口可以拖动、折叠和关闭。关闭后，部分窗口可以通过菜单或快捷键重新打开。初学者最常接触的是这些区域：

| 区域 | 用途 |
| --- | --- |
| 左侧工具栏 | 选择笔刷、填充、选择、挤出等编辑工具 |
| 顶部操作栏 | 放置常用动作，方便快速执行 |
| 方块快捷栏 | 选择当前编辑使用的方块 |
| 项目设置 | 修改项目和导出相关选项 |
| 工具窗口 | 调整当前工具的尺寸、模式和参数 |

## 一个安全的编辑流程

1. 创建新项目。
2. 在小范围内试用选择工具，确认选区边界。
3. 使用填充或笔刷工具放置少量方块。
4. 保存项目。
5. 导出为世界并用普通游戏方式打开测试。
6. 确认没有问题后，再扩大编辑范围。

/// tip | 编辑器适合地图，不适合替代资源包编辑器
编辑器擅长处理世界内容，例如建筑、地形、结构和测试路线。行为包、资源包、脚本和纹理仍建议在bridge.、Visual Studio Code或其他文件编辑器中维护。
///

## 扩展开发入口

如果你想在编辑器里做自定义工具，不要只停留在内置面板，建议直接接入扩展生态：

- [Script API文档](https://learn.microsoft.com/minecraft/creator/scriptapi/)：通用脚本接口说明。
- [Editor API文档](https://aka.ms/EditorAPI)：编辑器专用接口说明。
- [Editor Extension Starter Kit](https://github.com/Mojang/minecraft-editor-extension-starter-kit)：扩展工程模板与构建管线。
- [Editor Extension Samples](https://github.com/Mojang/minecraft-editor-extension-samples)：可运行示例。
- [minecraft-editor讨论区](https://github.com/Mojang/minecraft-editor/discussions)：问题反馈与路线讨论。

另外，如果你做的是“编辑器外”的普通脚本测试，记得在实验性玩法中开启Beta APIs开关；这是当前文档给出的前置提醒。

## 与基岩版专用服务器配合

Windows版基岩版专用服务器也能以编辑器项目方式启动。文档给出的命令形式是：

```powershell
.\bedrock_server.exe Editor=true
```

这种方式只适合从头创建编辑器项目。已有编辑器项目也可以复制到服务器的`worlds`目录，并在`server.properties`中设置正确世界名。客户端连接时，版本必须与服务器匹配，否则会被拒绝。