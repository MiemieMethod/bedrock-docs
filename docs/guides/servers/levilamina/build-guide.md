# 项目构建指南

本指南涵盖从源代码构建LeviLamina，包括环境设置、构建命令、依赖项和版本管理。

## 前置要求

### 必需工具

- **XMake 3.0.0+** — 构建系统 ([xmake.io](https://xmake.io))
- **MSVC 2022+** — 支持C++20的Microsoft Visual C++编译器
- **Git** — 用于版本控制和版本号生成
- **Windows 10/11 x64** — 目前仅支持Windows构建

### 安装XMake

```powershell
# 使用PowerShell
Invoke-Expression (Invoke-Webrequest 'https://xmake.io/psget.text' -UseBasicParsing).Content

# 或使用Scoop
scoop install xmake
```

### 安装MSVC

安装Visual Studio 2022并选择"使用C++的桌面开发"工作负载，或安装Visual Studio 2022生成工具。

## 构建命令

### 基本构建

```powershell
# 克隆仓库
git clone https://github.com/LiteLDev/LeviLamina.git
cd LeviLamina

# 构建服务端（默认）
xmake

# 或显式指定服务端
xmake f --target_type=server
xmake
```

### 构建客户端

```powershell
xmake f --target_type=client
xmake
```

客户端构建会编译`src-client/`中的专用代码，并面向Windows版Minecraft客户端进程输出模组。它可以使用输入、客户端事件和渲染相关接口，但不能直接替代服务端构建。

### 构建并启用测试

```powershell
xmake f --tests=y
xmake
```

### 发布构建

```powershell
xmake f --publish=y
xmake
```

### 清理构建

```powershell
xmake c
xmake
```

## 构建选项

| 选项 | 值 | 默认值 | 说明 |
|------|-----|--------|------|
| `--target_type` | `server`, `client` | `server` | 构建目标类型 |
| `--tests` | `y`, `n` | `n` | 启用基于GTest的测试 |
| `--publish` | `y`, `n` | `n` | 标记为发布版本（影响版本字符串） |
| `--levimc_repo` | URL | — | 自定义xmake-repo URL |

## 构建模组

使用LeviLamina模板构建自己的模组：

```powershell
# 克隆模组模板
git clone https://github.com/LiteLDev/levilamina-mod-template.git my-mod
cd my-mod

# 更新xmake仓库
xmake repo -u

# 配置为调试构建
xmake f -m debug

# 开始构建
xmake
```

## 下一步

- 了解更多关于[命令注册](command-guide.md)
- 参考[创建第一个模组](../levilamina.md#创建第一个模组)获得详细步骤
- 查看[LeviLamina官方构建指南](https://levilamina.liteldev.com)
