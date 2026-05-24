---
title: 构建指南
---

# 构建指南

## 前置要求

- XMake 3.0.0或更高版本。
- MSVC 2022或更高版本。
- Git。
- Windows 10/11 x64。

## 基本构建

```powershell
git clone https://github.com/LiteLDev/LeviLamina.git
cd LeviLamina
xmake
```

## 客户端构建

```powershell
xmake f --target_type=client
xmake
```

## 常用选项

- `--target_type`：`server`或`client`。
- `--tests`：是否启用测试。
- `--publish`：是否标记为发布构建。
- `--levimc_repo`：自定义xmake-repo地址。

