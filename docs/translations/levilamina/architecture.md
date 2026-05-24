---
title: 官方项目架构
---

# 官方项目架构

/// details-info | 来源信息
- 原文仓库：[github.com/LiteLDev/LeviLamina](https://github.com/LiteLDev/LeviLamina)
- 许可说明：以原仓库或原站点公开许可声明为准。
///



本页保留LeviLamina官方架构说明的原始脉络摘要。若需要站内术语统一后的概念总览，应优先阅读[LeviLamina](../../docs/server/levilamina.md)；若需要实践性的开发步骤，则继续阅读[LeviLamina开发者指南](../../guides/servers/levilamina/index.md)。

## 目录结构

- `src/`：通用与服务端代码。
- `src-client/`：客户端专用代码。
- `src-server/`：服务端专用代码。
- `src-test/`：测试代码。
- `docs/`：文档。
- `scripts/`：构建与工具脚本。
- `builder/`：头文件生成脚本。

## 分层

- `mc/`：基岩版引擎头文件。
- `ll/core/`：内部实现。
- `ll/api/`：公开API。

在官方架构中，`mc`头文件来自对基岩版专用服务器与客户端的分析，用于描述引擎内部C++接口；它们不是官方稳定SDK。`ll/core`负责模组注册、原生模组加载、内置命令、崩溃记录和内部调整等核心功能，`ll/api`则向开发者公开事件、命令、表单、配置、服务、协程、日志、数据、反射、网络和钩子等接口。

## 构建差异

LeviLamina通过`--target_type`区分服务端与客户端构建。服务端构建加载到`bedrock_server_mod.exe`，客户端构建加载到`Minecraft.Windows.exe`。两者共享部分通用API，但并非所有模块都能在两个环境中同时使用。