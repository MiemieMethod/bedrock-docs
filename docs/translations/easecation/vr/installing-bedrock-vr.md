# 启用VR模式

/// details-info | 来源信息
- 原文仓库：[github.com/EaseCation/netease-modsdk-wiki](https://github.com/EaseCation/netease-modsdk-wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///


/// details-info | 署名信息
- 该页面整理自[EaseCation Wiki](https://mcwiki.easecation.net/wiki/vr/installing-bedrock-vr)
///

在Windows上，最新版本Minecraft的VR入口通常通过`minecraft://Mode/?OpenXR=true`启动。旧版Oculus商店客户端不再是当前方案，因此本文只说明通用的Windows启动方式。

/// warning | 适用范围
PlayStation用户无需使用本页步骤。
///

## 创建桌面快捷方式

1. 在桌面空白处右键，创建一个新的快捷方式。
2. 将目标位置设置为`minecraft://Mode/?OpenXR=true`。
3. 为快捷方式命名，例如“Minecraft VR”。
4. 保存后，桌面上会出现一个指向VR入口的快捷方式。

## 启动游戏

1. 确认头戴设备已正确连接，并完成系统层面的配置。
2. 双击快捷方式启动Minecraft。
3. 如果设备和运行时正常，游戏将进入VR模式。

/// tip | 提示
如果未能进入VR模式，优先检查头戴设备驱动、OpenXR运行时和系统级VR设置，而不是游戏本身。
///