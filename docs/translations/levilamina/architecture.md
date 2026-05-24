---
title: 项目架构
---

# 项目架构

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

## 构建差异

LeviLamina通过`--target_type`区分服务端与客户端构建。服务端构建加载到`bedrock_server_mod.exe`，客户端构建加载到`Minecraft.Windows.exe`。

