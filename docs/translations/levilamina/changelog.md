---
title: 更新日志
---

# 更新日志

/// info | 来源信息
- 原文仓库：[`LiteLDev/LeviLamina`](https://github.com/LiteLDev/LeviLamina)
- 对应来源：`.knowledge\LeviLamina源码及文档\CHANGELOG.md`
- 原始更新日志：<https://github.com/LiteLDev/LeviLamina/blob/HEAD/CHANGELOG.md>
- 发布页：<https://github.com/LiteLDev/LeviLamina/releases>
///

该页面用于记录LeviLamina项目的近期版本变更。由于原始更新日志较长，本站仅摘录最近版本摘要；完整历史请参阅原始文件。

## 阅读提示

- 升级LeviLamina前，应先对照[支持的版本](versions.md)确认BDS版本、客户端版本与LeviLamina版本是否匹配。
- `CHANGELOG.md`不仅记录新功能，也会记录兼容性修复、运行时数据升级和安全相关修复，因此不应只看最新标签号。
- 历史变更中已有多项高风险修复，例如`1.9.6`中对Mojang修改版RakNet导致的`MCPE-228407`崩溃风险进行绕过、`1.9.4`中修复`SubChunkRequestPacket`漏洞，以及`1.9.3`中修复`Certificate::validate`崩溃。

如需从法律、许可和发布边界的角度整体理解这些文件，可继续参阅[法律与发布说明](legal-release-notes.md)。

## 近期版本摘要

### 26.10.11（2026-05-09）

- 新增控制台输出事件。
- 将`bedrock-runtime-data`升级至`v26.10.4-server.14`与`v26.10.4-client.14`。

### 26.10.10（2026-05-03）

- 将`bedrock-runtime-data`升级至`v26.10.4-server.13`与`v26.10.4-client.13`。
- 移除`makeI18nStringError`中的`constexpr`。
- 修复模组卸载时的重载工厂与清理分配问题。

### 26.10.9（2026-04-22）

- 修复`Block::tryGetFromRegistry`与`BlockType::tryGetFromRegistry`的函数调用歧义。
- 修复`KeyInputEvent`。

### 26.10.8（2026-04-18）

- 增强跨模块的国际化支持与错误处理，完成[#1806](https://github.com/LiteLDev/LeviLamina/issues/1806)。
- 新增`mayPrintCommandError`，用于改进命令执行时的错误处理。
- 将`bedrock-runtime-data`升级至`v26.10.4-server.12`与`v26.10.4-client.12`。
- 更新错误消息处理与参数类型，以提升可读性。
- 更新`nbt at()`方法。
- 修复`ll::getWorldDataRoot()`与`ll::getWorldConfigRoot()`崩溃。
- 修复`TypeTraits.h`中的缺失`include`。

### 26.10.7（2026-04-13）

- 将`bedrock-runtime-data`升级至`v26.10.4-server.11`与`v26.10.4-client.11`。
- 修正方块放置触发器，并补充`BlockPos`测试。

### 26.10.6（2026-04-12）

- 新增代码覆盖率测试。
- 同步客户端的`MCPE-228407`修复。
- 将`bedrock-runtime-data`升级至`v26.10.4-server.10`与`v26.10.4-client.10`。
- 修复`Generator ElementsOf`。

### 26.10.5（2026-04-11）

- 为`Generator`新增`ElementsOf`。
- 引入`gtest`。
- 新增命令执行辅助与`gtest`覆盖。
- 将`FileReference`、`Identifier`与`Reference`的模板参数改为`int`，以适配官方头文件。

### 26.10.4（2026-04-10）

- 将`bedrock-runtime-data`升级至`v26.10.4-server.8`与`v26.10.4-client.8`。
- 修复虚函数匹配。

### 26.10.3（2026-04-09）

- 为服务器端新增`VillageFeature`与`PoolElementStructurePiece`构造函数。
- 在`mc/deps/shared_types/util/`中实现`FileReference`、`Identifier`与`Reference`。
- 新增可移除模组生命周期回调。
- 新增`AABB::shrink(Vec3 const& offset)`。
- 更新`DefaultEntitySystemsCollection`至`26.0`。
- 将`bedrock-runtime-data`升级至`v26.10.4-server.7`与`v26.10.4-client.7`。
- 更新Minecraft头文件。
- 修复`uncachedResolve`方法崩溃。

### 26.10.2（2026-04-08）

- 将`bedrock-runtime-data`升级至`v26.10.4-server.5`与`v26.10.4-client.5`。
- 更新Minecraft头文件。
- 修复统计中的Minecraft版本。

### 26.10.1（2026-04-07）

- 将`bedrock-runtime-data`升级至`v26.10.4-server.3`与`v26.10.4-client.3`。

### 26.10.0（2026-04-07）

- 新增常用工具函数与符号缓存。
- 新增`ActorDamageSource`与`RedactableString`默认构造函数。
- 新增`CommandRegistrar`实例获取快捷方式。
- 适配`26.10`。
- 将内置命令注册迁移到事件，并重新对齐其生命周期。
- 调整客户端启用与停用时机。
- 修复`ActorHurtEvent`、`ll::getGameVersion()`与客户端协程问题。
- 同步并优化`MCPE-228407`临时修复。

## 历史关键条目

以下条目虽然不属于当前`26.10.x`系列，但仍然直接影响兼容性判断、安全排查与客户端能力理解：

### 1.9.9（2026-04-02）

- 为`RuntimeOverload`新增`modify`方法。
- 将`bedrock-runtime-data`升级至`v1.21.132-server.10`与`v1.21.132-client.11`，并同步更新Minecraft头文件。
- 修复因旧版头文件连带包含而导致的特定头文件编译失败问题。

### 1.9.6（2026-02-25）

- 新增从服务端模组对应目录加载包的能力。
- 修复`MolangVariable`复制中的空指针解引用。
- 绕过因Mojang修改版RakNet而引发的`MCPE-228407`崩溃路径：在异常短数据包进入脆弱代码前直接丢弃。

### 1.9.4（2026-02-03）

- 修复`SubChunkRequestPacket`漏洞。

### 1.9.3（2026-02-03）

- 修复`Certificate::validate`崩溃。
- 同步更新对应的服务端与客户端运行时数据及Minecraft头文件。

### 1.9.0（2026-01-25）

- 正式加入客户端支持。
- 新增鼠标输入事件、键盘输入事件、自定义快捷键、客户端关卡生命周期事件与自定义数据包能力。
- 新增`ll::isClient`、数据库存储服务，以及世界路径与世界数据目录相关接口。

### 1.7.5与1.7.4（2025-11-18至2025-11-19）

- 默认启用数据包速率限制与RakNet连接频率限制，以减轻数据包洪泛。
- 修复恶意客户端在连接关闭后继续发包的问题。
- 修复超长证书链`LoginPacket`可导致服务端崩溃的问题。
- 修复畸形`InventoryTransactionPacket`可导致服务端卡死的问题。

原始文件还包含更早版本的完整记录；若需要逐条核对历史变更，请直接参阅来源文件。
