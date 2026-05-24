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

## 常用构建选项

- `--target_type`：`server`或`client`。
- `--tests`：是否启用测试。
- `--publish`：是否标记为发布构建。
- `--levimc_repo`：自定义xmake-repo地址。

## 客户端构建

```powershell
xmake f --target_type=client
xmake
```

## 构建模组

如果要按照官方模板构建自己的模组，可以先更新xmake仓库，再切换到调试模式：

```powershell
git clone https://github.com/LiteLDev/levilamina-mod-template.git my-mod
cd my-mod
xmake repo -u
xmake f -m debug
xmake
```

如果需要在Visual Studio Code中生成`compile_commands.json`，可以执行：

```powershell
xmake project -k compile_commands
```

## 其他构建命令

```powershell
xmake f --tests=y
xmake f --publish=y
xmake c
```

测试构建、发布构建和清理构建分别对应测试启用、发布标记和彻底重新构建。
