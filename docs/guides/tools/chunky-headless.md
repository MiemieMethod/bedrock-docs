# Chunky无头渲染

Chunky可以在没有GUI的情况下继续渲染已经配置好的场景。这种模式通常叫“无头渲染”，适合夜间挂机、远程主机或批处理脚本。

## 先理解启动器和Chunky本体的区别

命令行里调用的往往不是Chunky本体，而是Chunky Launcher。文档特别强调了参数前缀的区别：

- 单横杠参数，例如`-render`、`-snapshot`，会传给Chunky本体。
- 双横杠参数，例如`--update`、`--verbose`，会传给Launcher。

这也是很多命令“看起来没报错但没生效”的常见原因。

## JVM参数放在哪里

如果你在启动`ChunkyLauncher.jar`时写了JVM参数，这些参数默认只作用于Launcher本身，不会自动作用到真正的Chunky渲染进程。

需要传给Chunky本体的Java参数，应写进设置目录根部的`chunky-launcher.json`中的`javaOptions`。如果想查看Launcher最终到底用什么命令启动Chunky，可以加`--verbose`。

## 自定义设置目录

如果你想同时维护多套场景、多个配置，或希望把场景目录放到更方便备份的位置，可以使用`-Dchunky.home=`指定设置目录：

```powershell
java -Dchunky.home="D:\ChunkyHome" -jar "C:\path\to\ChunkyLauncher.jar" --update
```

要注意，这个参数必须写在`-jar`之前。

自定义设置目录常见用途包括：

- 同一台机器跑多套独立配置。
- 把场景和插件放到更大的磁盘。
- 给自动化脚本固定一个可控目录。

## 无头渲染前要先准备什么

通常至少要先完成这些步骤：

1. 下载`ChunkyLauncher.jar`。
2. 运行`--update`下载Chunky版本本体。
3. 运行`-download-mc <版本>`下载对应Java版的`version.jar`，让Chunky拿到纹理。
4. 在GUI中先把场景、相机、资源包和目标SPP都配置好。
5. 确认场景文件已经在设置目录的`scenes`文件夹里。

换句话说，无头模式更像“接着跑”，而不是“从零开始搭场景”。

## 最常用的三个命令

列出场景：

```powershell
java -jar "C:\path\to\ChunkyLauncher.jar" -list-scenes
```

渲染场景：

```powershell
java -jar "C:\path\to\ChunkyLauncher.jar" -render SceneName
```

导出当前快照：

```powershell
java -jar "C:\path\to\ChunkyLauncher.jar" -snapshot SceneName snapshot.png
```

`-render`会一直运行到场景文件里设定的目标SPP。中途按++ctrl+C++停掉时，最近一次自动保存之后的进度可能会丢失。

## 常见命令行选项

| 选项 | 用途 |
| --- | --- |
| `-render <SCENE>` | 以无头模式渲染场景。 |
| `-snapshot <SCENE> <PNG>` | 从场景导出一张PNG快照。 |
| `-list-scenes` | 列出当前场景目录中的场景。 |
| `-scene-dir <DIR>` | 指定场景目录。 |
| `-threads <NUM>` | 指定渲染线程数。 |
| `-tile-width <NUM>` | 调整分块宽度。 |
| `-spp-per-pass <NUM>` | 每次分块处理的SPP数，更适合无头模式。 |
| `-target <NUM>` | 临时覆盖当前无头渲染的目标SPP。 |
| `-download-mc <VERSION>` | 下载指定Minecraft Java版资源。 |
| `--update` | 让Launcher下载最新Chunky。 |
| `--verbose` | 输出更详细的启动信息。 |

## `-spp-per-pass`为什么更适合无头

文档指出，`-spp-per-pass`提高后可能改善渲染性能，但会破坏一部分GUI交互体验。因此它更适合本来就不看GUI、只想让机器持续跑的无头场景。

## 一个常见工作流

比较稳妥的流程通常是：

1. 在GUI里完成世界选择、选区、相机、光照、资源包和材质设置。
2. 保存场景。
3. 用`-list-scenes`确认场景名。
4. 夜间或远程主机上执行`-render SceneName`。
5. 需要中途查看结果时，执行`-snapshot`导出一张图。

如果你只是想把GUI里做好的场景继续跑到更高SPP，这个流程最省心。

## 什么时候值得单独建一个Chunky主目录

下列情况都建议考虑`-Dchunky.home`：

- 同一台机器同时渲染多个项目。
- 不希望默认用户目录越来越乱。
- 想把插件、场景和设置一起打包迁移到另一台机器。

这样做还能避免不同项目的插件和场景混在一起。