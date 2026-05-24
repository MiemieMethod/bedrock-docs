---
comments: true
---

# 安装您的插件

在安装您的第一个插件之前，您需要构建它。

=== ":fontawesome-brands-python: Python"

    点击侧栏上的:octicons-terminal-16:图标打开终端并输入：

    ```bash
    pip install pipx
    pipx run build --wheel
    ```

    您应该在控制台中看到类似这样的内容：

    ![PyCharm构建插件](screenshots/pycharm-build-plugin.png)

    然后，将构建的wheel包`endstone_my_plugin.whl`从`dist`文件夹复制到{{file|plugins}}目录`path/to/bedrock_server/plugins`。

    现在，[再次启动您的服务器]。您应该看到您的插件已成功加载。
    
    ![使用插件启动服务器](screenshots/start-server-with-plugin.png)

    **:partying_face: 恭喜！** 您已经为Endstone服务器创建了您的第一个插件！

    ## 开发模式（也称为可编辑安装）
    
    创建插件时，开发者通常想在切割发布和准备发布存档之前迭代实现和测试更改。在正常情况下，这可能非常繁琐，需要开发者不断重新构建和重新安装插件。

    **但我们为您服务！** Endstone也允许开发者直接从项目文件夹加载开发中的代码，而无需将`whl`文件复制到`plugins`文件夹。

    为此，您需要激活[虚拟环境]。请确保Endstone也安装在环境中。

    === ":fontawesome-brands-windows: Windows"

        ``` sh
        . venv/Scripts/activate
        ```

    === ":fontawesome-brands-linux: Linux"

        ``` sh
        . venv/bin/activate
        ```
    
    您现在可以通过在虚拟环境中执行[可编辑安装]来进入此"开发模式"，使用pip的`-e/--editable`标志，如下所示：

    ``` sh title="(venv)"
    pip install --editable .
    ```

    现在，如果您更改磁盘上的源代码，您可以在Endstone中运行`/reload`命令，您的更改将立即生效。

    完成给定的开发任务后，您可以简单地卸载您的包（如您通常使用`pip uninstall <package name>`所做的那样）。

=== ":simple-cplusplus: C++"

    点击顶部栏上的菜单图标，选择**构建> 构建项目**来构建您的插件。

    ![CLion构建插件](screenshots/clion-build-plugin.png)
    
    然后，将构建的共享库`endstone_my_plugin.dll`复制到{{file|plugins}}目录`path/to/bedrock_server/plugins`。

    现在，[再次启动您的服务器]。您应该看到您的插件已成功加载。
    
    ![使用插件启动服务器](screenshots/start-server-with-plugin.png)

    **:partying_face: 恭喜！** 您已经为Endstone服务器创建了您的第一个插件！


[再次启动您的服务器]: ../getting-started/start-your-server.md

[可编辑安装]: https://pip.pypa.io/en/latest/topics/local-project-installs/

[虚拟环境]: ../../getting-started/installation/#environment