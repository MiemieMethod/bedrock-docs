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

## 依赖项

LeviLamina依赖25+个外部库，由XMake自动管理。

### 核心库

| 库 | 版本 | 用途 |
|----|------|------|
| **entt** | v3.15.0 | 实体组件系统 |
| **fmt** | 11.2.0 | 字符串格式化 |
| **nlohmann_json** | v3.11.3 | JSON解析 |
| **rapidjson** | v1.1.0 | 快速JSON解析 |
| **leveldb** | 1.23 | 键值数据库 |
| **gsl** | v4.2.0 | 指南支持库 |

### 性能库

| 库 | 版本 | 用途 |
|----|------|------|
| **mimalloc** | v2.1.7 | 高性能内存分配器 |
| **parallel-hashmap** | v2.0.0 | 快速哈希表 |
| **concurrentqueue** | v1.0.4 | 无锁队列 |

### 工具库

| 库 | 版本 | 用途 |
|----|------|------|
| **ctre** | 3.8.1 | 编译期正则表达式 |
| **magic_enum** | v0.9.7 | 枚举反射 |
| **type_safe** | v0.2.4 | 类型安全工具 |
| **expected-lite** | v0.8.0 | Expected/Result类型 |
| **glm** | 1.0.1 | 数学库 |

### LeviLamina专用库

| 库 | 版本 | 用途 |
|----|------|------|
| **pcg_cpp** | v1.0.0 | 随机数生成 |
| **pfr** | 2.1.1 | 反射 |
| **demangler** | v17.0.7 | C++名称反修饰 |
| **levibuildscript** | 0.4.1 | 构建脚本 |
| **preloader** | v1.15.7 | DLL预加载 |
| **symbolprovider** | v1.2.0 | 符号解析 |
| **trampoline** | 2024.11.7 | 函数钩子 |

### 平台特定库

| 库 | 版本 | 平台 | 用途 |
|----|------|------|------|
| **libhat** | 0.4.0 | Windows | 内存操作 |
| **bedrockdata** | v1.21.132 | - | BDS头文件（server.8或client.9） |

## 版本号生成

LeviLamina的版本号从Git标签自动生成。

### 版本格式

```
v{major}.{minor}.{patch}{-prerelease}+{commit_hash}
```

### 示例

- **正式版**：`v1.8.0`
- **预发布版**：`v1.8.0-rc.2`
- **开发版**：`v1.8.0-rc.2+ce09050f05`（`--publish=n`时包含提交哈希）

### 版本来源优先级

1. **Git标签** — 如果当前提交有匹配`v*.*.*`的标签。
2. **tooth.json** — 回退到`tooth.json`中的`version`字段。

### 版本注入

版本会在构建期间注入到`src/ll/core/Version.h.in`：

```cpp
// Generated Version.h
#define LL_VERSION_MAJOR 1
#define LL_VERSION_MINOR 8
#define LL_VERSION_PATCH 0
#define LL_VERSION_PRERELEASE "rc.2"
#define LL_VERSION_BUILD "ce09050f05"
```

## 编译器设置

### C++标准

- **C++20**必需。
- **C++23**特性通过`_HAS_CXX23=1`启用。

### MSVC标志

- **运行时**：`/MD`（动态，非调试）。
- **异常**：`/EHa`（SEH+C++异常）。
- **警告**：`/W4`并配合以下升级项：
  - `/w44265` — 虚函数无`override`
  - `/w44289` — 循环变量在循环外使用
  - `/w44296` — 表达式始终为真或假
  - `/w45263` — 对临时对象调用`std::move`
  - `/w44738` — 在内存中存储浮点数

## 构建输出

### 目录结构

```
LeviLamina/
├── build/
│   └── windows/
│       └── x64/
│           └── release/
│               └── LeviLamina.dll
└── bin/
    └── LeviLamina/
        ├── LeviLamina.dll
        └── manifest.json
```

### 产物

- **LeviLamina.dll** — 主加载器DLL。
- **manifest.json** — 包含版本信息的模组元数据。

## CI/CD

LeviLamina使用GitHub Actions进行持续集成。

### 自动化构建

- **触发器**：推送到主分支或拉取请求。
- **平台**：Windows x64。
- **目标**：服务端和客户端。
- **测试**：`--tests=y`时运行。

### 发布流程

1. 为提交打标签：`git tag v1.8.0`
2. 推送标签：`git push origin v1.8.0`
3. CI使用`--publish=y`构建。
4. 产物上传到GitHub Releases。

## 故障排除

### XMake缓存问题

```powershell
xmake c -a  # 清理所有
xmake f -c  # 重新配置
```

### 依赖下载失败

```powershell
# 使用镜像
xmake g --proxy_pac=github_mirror.lua
```

### 找不到MSVC

确保已安装Visual Studio 2022或生成工具，并从“VS 2022开发人员命令提示符”运行。

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