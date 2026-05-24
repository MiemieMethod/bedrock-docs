---
title: 变更日志索引
---

# 变更日志索引

本页整理`.knowledge\基岩版协议库`中的协议变更日志Markdown来源脉络。

## 扫描范围

- 变更日志文件总数：61
- 协议版本覆盖范围：407至1001
- 目录分布：
    - 根目录：`changelog_1001_05_18_26.md`
    - 历史目录：`previous_changelogs\*.md`（60个）

## 年度文件数量（按文件名年份后缀统计）

| 年份 | 文件数 |
|---|---:|
| 2020 | 10 |
| 2021 | 13 |
| 2022 | 9 |
| 2023 | 9 |
| 2024 | 9 |
| 2025 | 7 |
| 2026 | 4 |

## 近期版本链路

| 协议版本 | 来源文件 |
|---:|---|
| 893 | `.knowledge\基岩版协议库\previous_changelogs\changelog_893_11_07_25.md` |
| 924 | `.knowledge\基岩版协议库\previous_changelogs\changelog_924_01_21_26.md` |
| 944 | `.knowledge\基岩版协议库\previous_changelogs\changelog_944_03_04_26.md` |
| 975 | `.knowledge\基岩版协议库\previous_changelogs\changelog_975_04_22_26.md` |
| 1001 | `.knowledge\基岩版协议库\changelog_1001_05_18_26.md` |

## 阅读建议

1. 先确定目标协议版本。
2. 从该版本文件向前追溯相邻2至4个版本，定位破坏性迁移点。
3. 对出现`Converted to Cereal`、`Modified Packets`、`Modified Enums`的版本优先做回归验证。
