---
comments: true
toc_depth: 2
---

# 更新日志

该页面用于跟踪Endstone项目的版本变更。为避免构建时的snippet路径解析错误，本站不再通过`--8<--`直接内嵌外部文件。

- 官方原始更新日志：<https://github.com/EndstoneMC/endstone/blob/main/CHANGELOG.md>
- 版本对比入口：<https://github.com/EndstoneMC/endstone/releases>

## 最近版本摘要

### 0.11.3（2026-04-02）

- 新增对BDS1.26.12的支持。
- 注册表API新增`BlockType`。
- 长矛附魔新增`Lunge`类型。
- 修复了`PacketReceiveEvent`报错信息、若干数据包序列化和指标模块相关问题。

### 0.11.2（2026-03-02）

- 新增对BDS1.26.3.1的支持。
- 新增`BlockExplodeEvent`与`Player.send_map()`。
- 修复了RakNet相关崩溃和多个事件导出问题。

### 0.11.1（2026-02-20）

- 新增对BDS1.26.1.1的支持。
- 新增NBT树转原生Python结构方法，导出更多顶层子模块。
- 修复了多项事件触发、附魔哈希与地图API稳定性问题。

### 0.11.0（2026-02-13）

- 新增对BDS1.26.0的支持。
- 引入完整NBT API、地图API、注册表系统、更多事件和`endstone.asyncio`、`endstone.metrics`模块。
- 包含若干破坏性变更（如`NamespacedKey`替换为`Identifier<T>`等），升级前需先核对官方更新日志。
