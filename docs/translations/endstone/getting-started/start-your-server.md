---
comments: true
---

# 启动您的服务器

[安装]了Endstone后，您可以使用`endstone`可执行文件引导您的服务器。进入您想要服务器所在的目录并输入：

```
endstone
```

或者，如果您在Docker中运行Endstone，请使用：

=== ":fontawesome-brands-linux: Linux / :fontawesome-brands-windows: Powershell"

    ```
    docker run --rm -it -v ${PWD}:/home/endstone -p 19132:19132/udp endstone/endstone
    ```

=== ":fontawesome-brands-windows: 命令提示符"

    ```
    docker run --rm -it -v "%cd%":/home/endstone -p 19132:19132/udp endstone/endstone
    ```

您应该在您的控制台中看到：

![启动您的服务器](start-your-server.png)

!!! tip
    首次运行引导程序时，它需要从官方镜像下载[基岩版专用服务器]。按++y++和++enter++继续。


[安装]: installation.md

[基岩版专用服务器]: https://www.minecraft.net/en-us/download/server/bedrock
