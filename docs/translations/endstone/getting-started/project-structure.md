# 项目结构

本章提供了项目的高级概览，以便更轻松地进行导航、构建和使用。

## CMake项目和依赖关系

[GitHub仓库](https://github.com/EndstoneMC/endstone)包含以下CMake项目：

- **Endstone API** (`include/endstone`)
    - 这是开发者用来创建插件的**仅头文件**API层。
    - 它提供了一套标准化的方法和抽象来与Minecraft交互，确保插件可以跨不同Minecraft版本以最少的调整工作。
    - 它抽象了Minecraft的内部部分，允许插件以版本无关的方式与游戏交互，而无需直接与Mojang的代码接触。

- **Endstone Python绑定** (`src/endstone_python`)
    - 这是Endstone API的Python绑定。
    - 它允许开发者通过将API调用从Python转换为底层C++调用来使用Python创建插件。

- **Endstone Core** (`src/endstone_core`)
    - 这是Endstone API的实现。它位于API和游戏本身之间。
    - 它通过直接与基岩版专用服务器(BDS)交互来为API方法提供实际行为，将来自插件的抽象API调用转换为特定的BDS内部调用。

- **Endstone运行时** (`src/endstone_runtime`)
    - 这包括应用于基岩版专用服务器的可执行文件二进制的挂钩，以修改或扩展功能，提供仅通过API不可能实现的bug修复和功能。
    - 这些挂钩是必要的，因为原始软件被编译成二进制，Minecraft的更新经常会破坏现有代码的兼容性。

- **Endstone开发工具** (`src/endstone_devtools`)
    - 这提供了一个图形用户界面(GUI)，允许高级用户从原版软件转储有用的数据供其他目的使用，例如第三方服务器软件。
    - 目前仅在Windows上启用，并需要系统上可用的OpenGL功能。

## Python项目

Endstone作为PyPI上的Python包发布，它包含了几个用纯Python编写的实用程序，以及CMake项目的编译库和Endstone API的Python绑定。这些Python代码位于`python/src`文件夹下，单元测试位于`python/tests`。