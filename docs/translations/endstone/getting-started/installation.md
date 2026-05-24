---
comments: true
---

# 快速开始

/// details-info | 来源信息
- 原文仓库：[github.com/EndstoneMC/endstone](https://github.com/EndstoneMC/endstone)
- 许可说明：以原仓库或原站点公开许可声明为准。
///


Endstone为基岩版专用服务器提供了强大的插件API，这是Minecraft：基岩版的官方服务器软件。如果您熟悉Python，可以使用Python包管理器[`pip`](#with-pip)来安装Endstone。如果没有，我们建议使用[`docker`](#with-docker)。

## 安装

### 环境 <small>可选</small> { #environment data-toc-label="环境" }

我们建议使用[虚拟环境]，这是一个隔离的Python运行时。
如果您在虚拟环境中，任何您安装或升级的包都将是该环境的本地包。
如果遇到问题，您可以直接删除并重新创建环境。设置非常简单：

-   使用以下命令创建新的虚拟环境：

    ```
    python3 -m venv venv
    ```

-   使用以下命令激活环境：

    === ":fontawesome-brands-windows: Windows"

        ``` sh
        . venv/Scripts/activate
        ```

    === ":fontawesome-brands-linux: Linux"

        ``` sh
        . venv/bin/activate
        ```


    您的终端现在应该在提示符前打印`(venv)`，这是您在刚创建的虚拟环境中的标志。

-   使用以下命令退出环境：

    ```
    deactivate
    ```

### 使用pip <small>推荐</small> { #with-pip data-toc-label="使用pip" }

Endstone作为[Python包]发布，可以使用`pip`安装，最好是通过使用上一步的[虚拟环境](#environment)。打开终端并使用以下命令安装Endstone：

=== "最新版本"

    ``` sh
    pip install endstone
    ```

### 使用docker

官方的[Docker镜像]是在几分钟内启动并运行Endstone服务器的一个不错的方式。打开终端并使用以下命令拉取镜像：

=== "最新版本"

    ```
    docker pull endstone/endstone
    ```

[Python包]: https://pypi.org/project/endstone/

[虚拟环境]: https://realpython.com/what-is-pip/#using-pip-in-a-python-virtual-environment

[Docker镜像]: https://hub.docker.com/r/endstone/endstone/