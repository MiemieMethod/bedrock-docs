---
标题: Minecraft Beta & Preview - 1.21.40.25
日期: 2024-10-02T08:24:19Z
更新: 2024-10-03T15:23:09Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/30728854635533-Minecraft-Beta-Preview-1-21-40-25
哈希:
  用户内容-特性和漏洞修复: features-and-bug-fixes
  用户内容-图形: graphical
  用户内容-技术更新: technical-updates
  用户内容-组件: components
---

**发布时间:** 2024年10月3日

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

我们对Minecraft LIVE上展示的新特性感到兴奋。这些特性目前可在Java快照中测试，并将很快在基岩预览和Beta中推出！您可以在这里阅读更多关于这些特性的内容: [minecraft.net/en-us/article/the-pale-garden](https://www.minecraft.net/en-us/article/the-pale-garden)。

以下是本周更新的新内容。请在 [feedback.minecraft.net](https://feedback.minecraft.net/) 告诉我们您的想法，并在 [bugs.mojang.com](https://bugs.mojang.com/) 报告任何漏洞。

# 特性和漏洞修复

## 图形

- 修复了某些Android设备渲染透明物品为纯黑色的问题 ([MCPE-185038](https://bugs.mojang.com/browse/MCPE-185038))

# 技术更新

## 组件

- 移除了“minecraft:looked_at 组件”中的“allow_invulnerable”字段的支持
  - 此字段从未具有任何功能，因此此更改不会以任何方式影响现有或未来的内容
  - 对于格式版本低于1.21.40的任何内容，此字段将被忽略
  - 对于格式版本等于或高于1.21.40但仍使用此字段的任何内容，将发出内容错误