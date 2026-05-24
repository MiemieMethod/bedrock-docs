---
title: 基岩版命令更新记录
---

# 基岩版命令更新记录

本页基于ProjectXero维护的《Minecraft基岩版命令更新日志》进行中文整理，面向命令迁移、函数兼容性校验与教程版本标注。

- 原始项目：<https://github.com/XeroAlpha/Minecraft-Bedrock-Command-Log>
- 当前整理来源：`.knowledge\基岩版命令更新记录\README.md`

## 最新收录版本

按来源文档当前状态：

- 正式版：`26.1.1`
- 预览版：`26.10.25`

## 近期关键变更

| 游戏版本 | 变更摘要 |
| --- | --- |
| 26.10.25 | `camera attach_to_entity`、`camera detach_from_entity`和`camera play_spline`不再需要特定实验性玩法。 |
| 26.0.27 | `camera`新增`play_spline`子命令（实验性）。 |
| 26.0.23 | 新增`packstack`命令。 |
| 1.21.120.24 | `camera`新增`attach_to_entity`和`detach_from_entity`子命令（实验性）。 |
| 1.21.100.25 | `camera fov_clear`和`camera fov_set`不再需要特定实验性玩法。 |
| 1.21.90.23 | `controlscheme`命令不再需要特定实验性玩法。 |
| 1.21.60.24 | `script diagnostics startcapture`和`script diagnostics stopcapture`子命令加入。 |
| 1.21.50.20 | `schedule delay`子命令加入。 |

## 使用建议

- 在撰写教程时，为命令语法标注最低可用版本。
- 在迁移旧工程时，先核对实验性要求是否已解除，再决定是否保留旧兼容写法。
- 对于命令方块、函数和脚本调用链，优先结合命令版本与目标构建进行实机验证。

## 相关页面

- [命令版本参考](../../refs/commands/version.md)
- [命令](../../docs/general/command.md)
- [版本](../../docs/general/version.md#命令版本)
