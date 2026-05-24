---
comments: true
toc_depth: 2
---

# 创建您的第一个插件

/// details-info | 来源信息
- 原文仓库：[github.com/EndstoneMC/endstone](https://github.com/EndstoneMC/endstone)
- 许可说明：以原仓库或原站点公开许可声明为准。
///


## 前置条件

=== ":fontawesome-brands-python: Python"

    要使用Python API开发您的第一个插件，您需要安装以下前置条件：
    
    -   [JetBrains PyCharm]
    -   [Python] (>= 3.10)
    -   [endstone Python包]

=== ":simple-cplusplus: C++"

    要使用C++ API开发您的第一个插件，您需要安装以下前置条件：

    -   [JetBrains CLion]
    -   [CMake] (>= 3.15)
    -   C++编译器
        -   **:fontawesome-brands-windows: Windows**: [Visual Studio] 2017或更新版本
        -   **:fontawesome-brands-linux: Linux**: [LLVM工具链] 5或更新版本，带有Clang和libc++

## 创建新项目

=== ":fontawesome-brands-python: Python"

    当您启动PyCharm时，您会看到此欢迎屏幕：

    ![欢迎使用PyCharm](screenshots/pycharm-welcome.png)

    点击**新建项目**

    ![新建PyCharm项目](screenshots/pycharm-create-project.png)

    假设您想将您的插件命名为**MyPlugin**。在Endstone插件开发中，我们遵循以下命名约定：

    1. 使用`lower-case-with-dash`作为项目名称
    2. 用`endstone-`为项目名称加前缀

    因此，您应该在**名称**字段中输入`endstone-my-plugin`。

    然后，在**解释器类型**中，选择**自定义环境**。选择**选择现有**，并设置路径到您之前安装`endstone`的位置，如前置条件中所述。

    最后，点击**创建**。PyCharm工作区将弹出，您将看到这个。

    ![PyCharm工作区](screenshots/pycharm-workspace.png)

    !!! tip
        Endstone服务器要求其插件安装在同一Python环境中。**强烈建议**使用虚拟环境。

    ### 检查您的依赖

    在上一步中，您选择了安装了`endstone`包的现有解释器。目前，这是我们简单插件唯一需要的依赖。要检查其安装，请点击侧栏上的:octicons-terminal-16:图标打开终端并输入：
    ```
    pip show endstone
    ```

    您应该看到类似这样的内容：
    ```
    Name: endstone
    Version: 0.11.3
    Summary: Endstone offers a plugin API for Bedrock Dedicated Servers, supporting both Python and C++.
    Home-page:
    Author:
    Author-email: Vincent Wu <magicdroidx@gmail.com>
    License: Apache License
    ```

    ### 创建`pyproject.toml`

    现代Python包可以包含一个`pyproject.toml`文件，首次在[PEP 518]中引入。该文件包含构建系统要求和信息，pip使用这些信息来构建包。
    
    现在，右键单击项目文件夹并选择**新建> 文件**来创建一个`pyproject.toml`。 

    ![创建pyproject.toml](screenshots/pycharm-create-pyproject-toml.png)    

    复制以下内容并粘贴到文件中。
    ``` toml title="pyproject.toml" linenums="1"
    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"
    
    [project]
    name = "endstone-my-plugin"
    version = "0.1.0"
    description = "My first Python plugin for Endstone servers!"
    ```

    !!! notice
        名称字段应始终是项目名称。它必须以`endstone-`开头，这由插件加载器**强制执行**。该名称也应该使用`lower-case-with-dash`风格。

=== ":simple-cplusplus: C++"

    当您启动CLion时，您会看到此欢迎屏幕：

    ![欢迎使用CLion](screenshots/clion-welcome.png)

    点击**新建项目**

    ![新建CLion项目](screenshots/clion-create-project.png)

    在侧栏中，选择**C++库**。为**语言标准**选择**C++ 20**。为**库类型**选择**共享**。点击**创建**。CLion工作区将弹出，您将看到这个。

    ![CLion工作区](screenshots/clion-workspace.png)

    ### 文件结构
    从侧栏的项目视图中，您会注意到CLion为我们创建了几个文件。

    -   `.clang-format`: ClangFormat的配置文件
    -   `CMakeLists.txt`: CMake构建系统的清单文件
    -   `library.cpp`: 源文件
    -   `library.h`: 头文件
    
    **删除**`library.cpp`和`library.h`，因为我们不需要它们。您可以保留`.clang-format`和`CMakeLists.txt`。

    ### 更新`CMakeLists.txt`

    现在，在侧栏中打开`CMakeLists.txt`并删除所有现有内容。 
    然后，将以下内容复制并粘贴到您的`CMakeLists.txt`。

    ``` CMake title="CMakeLists.txt" linenums="1"
    cmake_minimum_required(VERSION 3.15)
    
    project(my_plugin CXX)
    
    set(CMAKE_CXX_STANDARD 20)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
    
    include(FetchContent)
    FetchContent_Declare(
        endstone
        GIT_REPOSITORY https://github.com/EndstoneMC/endstone.git
        GIT_TAG v0.11 #(1)!
    )
    FetchContent_MakeAvailable(endstone)
    ```

    1.  :warning: **重要：**这指定了目标Endstone API版本。确保在Endstone每次主要版本发布后更新它以保持最新。
    
    [JetBrains CLion]: https://www.jetbrains.com/clion/

## 创建主插件类

=== ":fontawesome-brands-python: Python"

    现在，右键单击项目文件夹并选择**新建> 目录**来创建一个`src`目录。 

    右键单击您刚创建的`src`目录，并选择**标记目录为> 源根目录**。您会注意到图标的颜色变为蓝色。

    再次右键单击`src`目录，并选择**新建> Python包**为我们的插件创建一个包。 
    由于我的项目名称是`endstone-my-plugin`，我将命名包为`endstone_my_plugin`。
    
    您应该有类似这样的东西：

    ![创建Python包](screenshots/pycharm-create-package.png)
    
    !!! tip
        对于Python包，通常的做法是使用`lower-case-with-dash`作为项目名称，`lower_case_with_underscore`作为包名称。参见[PEP 8]了解Python的样式指南。

    右键单击您刚创建的包，并选择**新建> Python文件**来创建一个`my_plugin.py`。创建一个名为`MyPlugin`的类，它扩展了来自`endstone.plugin`的`Plugin`类。

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" 
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        pass
    ```

    然后，打开同一文件夹下的`__init__.py`，从Python文件导入`MyPlugin`类并将其添加到`__all__`变量。

    ``` python title="src/endstone_my_plugin/__init__.py" linenums="1"
    from endstone_my_plugin.my_plugin import MyPlugin

    __all__ = ["MyPlugin"]
    ```

=== ":simple-cplusplus: C++"

    现在，创建两个文件：`src/my_plugin.cpp`和`include/my_plugin.h`。

    打开`CMakeLists.txt`并添加一个新目标。

    ``` CMake title="CMakeLists.txt" linenums="1" hl_lines="16"
    cmake_minimum_required(VERSION 3.15)
    
    project(my_plugin CXX)
    
    set(CMAKE_CXX_STANDARD 20)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
    
    include(FetchContent)
    FetchContent_Declare(
        endstone
        GIT_REPOSITORY https://github.com/EndstoneMC/endstone.git
        GIT_TAG v0.11
    )
    FetchContent_MakeAvailable(endstone)

    endstone_add_plugin(${PROJECT_NAME} src/my_plugin.cpp)
    ```

    您应该有类似这样的东西：

    ![更新CMakeLists](screenshots/clion-update-cmakelists.png)

    打开`include/my_plugin.h`并添加一个扩展`endstone::Plugin`类的新类`MyPlugin`。

    ``` c++ title="include/my_plugin.h" linenums="1" 
    #include <endstone/endstone.hpp>

    class MyPlugin : public endstone::Plugin {};
    ```

    然后，在`src/my_plugin.cpp`中，包含头文件。

    ``` c++ title="src/my_plugin.cpp" linenums="1"
    #include "my_plugin.h"
    ```

## 添加方法

=== ":fontawesome-brands-python: Python"

    现在我们想从基类覆盖一些方法：
    
    - `on_load`: 当插件由服务器加载时将被调用
    - `on_enable`: 当插件启用时将被调用
    - `on_disable`: 当插件被禁用时将被调用（例如，在服务器关闭期间）

    您可以使用logger在插件加载、启用和禁用时记录消息，如下所示：

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" hl_lines="4-5 7-8 10-11"
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        def on_load(self) -> None:
            self.logger.info("on_load is called!")

        def on_enable(self) -> None:
            self.logger.info("on_enable is called!")

        def on_disable(self) -> None:
            self.logger.info("on_disable is called!")
    ```

=== ":simple-cplusplus: C++"

    现在我们想从基类覆盖一些方法：
    
    - `onLoad`: 当插件由服务器加载时将被调用
    - `onEnable`: 当插件启用时将被调用
    - `onDisable`: 当插件被禁用时将被调用（例如，在服务器关闭期间）

    您可以使用logger在插件加载、启用和禁用时记录消息，如下所示：

    ``` c++ title="include/my_plugin.h" linenums="1" hl_lines="4-8 10-13 15-18"
    #include <endstone/endstone.hpp>

    class MyPlugin : public endstone::Plugin {
    public:
        void onLoad() override
        {
            getLogger().info("onLoad is called");
        }
    
        void onEnable() override
        {
            getLogger().info("onEnable is called");
        }
    
        void onDisable() override
        {
            getLogger().info("onDisable is called");
        }
    };
    ```

## 配置插件元数据

=== ":fontawesome-brands-python: Python"

    现在，该插件几乎完成了。让我们告诉服务器我们兼容的API版本。

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" hl_lines="4"
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        api_version = "0.11"

        def on_load(self) -> None:
            self.logger.info("on_load is called!")

        def on_enable(self) -> None:
            self.logger.info("on_enable is called!")

        def on_disable(self) -> None:
            self.logger.info("on_disable is called!")
    ```
    
    最后，要使插件可被服务器发现，您必须在`pyproject.toml`中指定一个入口点。

    ``` toml title="pyproject.toml" linenums="1" hl_lines="10-11"
    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"
    
    [project]
    name = "endstone-my-plugin"
    version = "0.1.0"
    description = "My first Python plugin for Endstone servers!"

    [project.entry-points."endstone"]
    my-plugin = "endstone_my_plugin:MyPlugin"
    ```

    !!! notice
    
        对于入口点，名称**必须**是您的项目名称**不带**`endstone-`前缀。例如，我们的项目名称是`endstone-my-plugin`，所以入口点的名称应该是`my-plugin`。该值只是`{module}:{class}`。

=== ":simple-cplusplus: C++"

    现在，该插件几乎完成了。让我们告诉服务器我们的名称、版本、主类和描述。

    ``` c++ title="src/my_plugin.cpp" linenums="1" hl_lines="3-6"
    #include "my_plugin.h"

    ENDSTONE_PLUGIN(/*(1)!*/"my_plugin", /*(2)!*/"0.1.0", /*(3)!*/MyPlugin)
    {
        description = "My first C++ plugin for Endstone servers";
    }
    ```

    1.  :abc: 这是插件名称！
    2.  :hash: 这是插件版本！
    3.  :white_check_mark: 这是插件的主类！

    !!! notice
         
        对于插件名称，它必须只包含**小写字母、数字和下划线**。

[JetBrains PyCharm]: https://www.jetbrains.com/pycharm/

[JetBrains CLion]: https://www.jetbrains.com/clion/

[Python]: https://www.python.org/downloads/

[endstone Python包]: ../getting-started/installation.md#with-pip

[CMake]: https://cmake.org/

[PEP 8]: https://peps.python.org/pep-0008/

[PEP 518]: https://peps.python.org/pep-0518/

[Visual Studio]: https://visualstudio.microsoft.com/

[LLVM工具链]: https://apt.llvm.org/