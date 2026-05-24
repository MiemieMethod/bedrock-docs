---
comments: true
toc_depth: 2
---

# 贡献

👍🎉 首先，感谢您花时间做出贡献！🎉👍

## 从哪里开始？

如果您在寻找一个好的问题来开始，请检查以下内容：

- [好的第一个问题](https://github.com/EndstoneMC/endstone/labels/good%20first%20issue) - 应该相当容易实现的问题，
- [需要帮助](https://github.com/EndstoneMC/endstone/labels/help%20wanted) - 通常比初学者问题涉及更多的问题，
- [高优先级](https://github.com/EndstoneMC/endstone/labels/high%20priority) - 需要尽快修复的东西，但通常复杂性较高。

## 源代码

要在本地机器上从源代码构建，请按照以下说明进行操作：

### 克隆仓库

```shell
git clone https://github.com/EndstoneMC/endstone.git
cd endstone
```

### 安装包管理器(conan)

开发**Endstone**所需的依赖项由Conan包管理器(`>=2.0`)提供。要安装包管理器，请在Python环境中运行以下命令。

```shell
pip install conan
conan profile detect
```

### 安装依赖

首先，运行以下命令来安装该项目的依赖项：

=== ":fontawesome-brands-windows: 命令提示符"
```shell
conan install . --build=missing -s compiler.cppstd=20 -c tools.cmake.cmaketoolchain:generator=Ninja
```

=== ":fontawesome-brands-windows: Powershell"
```shell
conan install . --build=missing -s compiler.cppstd=20 -c tools.cmake.cmaketoolchain:generator=Ninja -c tools.env.virtualenv:powershell=True
```

=== ":fontawesome-brands-linux: Linux"

    ```shell
    conan install . --build=missing -s compiler.cppstd=20 -s compiler.libcxx=libc++ -c tools.cmake.cmaketoolchain:generator=Ninja
    ```

现在，激活由conan创建的构建虚拟环境。

=== ":fontawesome-brands-windows: 命令提示符"
```cmd
.\build\Release\generators\conanbuild.bat
```

=== ":fontawesome-brands-windows: Powershell"
```cmd
.\build\Release\generators\conanbuild.ps1
```

=== ":fontawesome-brands-linux: Linux"

    ```shell
    source ./build/Release/generators/conanbuild.sh
    ```

运行`cmake`并检查版本：

```shell
$ cmake --version
cmake version 3.31.2
```

### 使用CMake构建

```shell
cmake --preset conan-release
cmake --build --preset conan-release
```

### 安装

要从本地源安装**Endstone**，只需运行：

```shell
pip install -U .
```

## 文档

我们使用[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)构建文档。
安装所有必需依赖项的最简单方法是使用`pip`：

```shell
pip install -r docs/requirements.txt
```

之后，您可以选择：

- [启动实时服务器以在编写时预览文档](https://squidfunk.github.io/mkdocs-material/creating-your-site/#previewing-as-you-write)，或

```shell
mkdocs serve
```

- [构建文档](https://squidfunk.github.io/mkdocs-material/creating-your-site/#building-your-site)

```shell
mkdocs build
```
