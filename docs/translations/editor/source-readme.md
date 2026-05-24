# 欢迎使用Minecraft基岩版编辑器

/// details-info | 来源信息
- 原文标题：Welcome to the Minecraft: Bedrock Editor!
- 原始仓库：<https://github.com/Mojang/minecraft-editor>
- 对应来源：`.knowledge\基岩版编辑器\README.md`
///

本文为来源README的中文整理译文，保留原始段落结构与信息重心，用于资料追溯与历史语境核对。

## 概览

Minecraft编辑器是运行在游戏引擎内部的多方块编辑体验，目标是让不同技能层级的创作者都能更容易构建高质量基岩版内容。

编辑器通过“游戏内原生工具+JavaScript脚本API”组合提供创作框架，使创作者可以构建用于增强编辑体验的“编辑器扩展”。

## 说明事项

- 编辑器仍处于早期开发阶段，能力会持续增加并根据反馈调整。
- 该来源将编辑器定位为Windows平台、键盘鼠标工作流，并强调预览版入口。
- 编辑器不是新的游戏模式，而是用于世界构建流程的工具。

## 开发阶段说明

来源强调编辑器仍在持续开发中，团队会通过更早频次的公开发布与社区反馈迭代功能。

## 可扩展性

来源指出，编辑器API是重点建设方向之一。除核心体验迭代外，官方也希望通过API向第三方开放能力，以便开发自定义编辑工具（扩展）。

来源列出的扩展开发资源如下：

| 资源 | 说明 |
| --- | --- |
| [Script API Docs](https://learn.microsoft.com/minecraft/creator/scriptapi/) | 创作者脚本API官方文档 |
| [Editor API Docs](https://aka.ms/EditorAPI) | 编辑器API官方文档 |
| [Editor Extension Starter Kit](https://github.com/Mojang/minecraft-editor-extension-starter-kit) | 扩展开发模板、类型与构建管线 |
| [Editor Extension Samples](https://github.com/Mojang/minecraft-editor-extension-samples) | 可参考的扩展示例集合 |

来源补充说明：若进行“编辑器外”的脚本探索，应在实验性玩法中启用Beta APIs开关，并建议提前掌握JavaScript与TypeScript基础。

## 访问编辑器

来源给出的快速路径为：

1. 通过启动器安装Minecraft基岩版预览版。
2. 创建桌面快捷方式，目标填写`minecraft-preview://creator/?Editor=true`。
3. 通过该快捷方式打开编辑器。

若快捷方式无法打开编辑器，来源建议先检查默认应用是否将`minecraft:`协议错误绑定到非预览版应用。

## 资源入口

来源列出的常用入口包括：

- 编辑器学习入口：<https://aka.ms/LearnEditor>
- 预览版更新日志：<https://feedback.minecraft.net/hc/en-us/sections/360001185332-Beta-and-Preview-Information-and-Changelogs>
- 仓库讨论区：<https://github.com/Mojang/minecraft-editor/discussions>

## 故障排除（来源流程）

若桌面快捷方式无法拉起编辑器，来源建议在Windows中按以下顺序检查：

1. 按++windows+i++打开设置。
2. 进入**应用**并打开**默认应用**。
3. 搜索并进入Minecraft应用设置。
4. 找到`MINECRAFT`（`URL:minecraft`）关联项。
5. 将其关联应用改为Minecraft Preview。
