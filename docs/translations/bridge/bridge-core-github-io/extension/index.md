# 扩展API

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/](https://bridge-core.github.io/extension-docs/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/index.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/index.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@a39ee641218cd148c6acd3348d295f541054bbf0 -->
///

这是bridge.的扩展API文档。我们仍在努力为API带来更多功能。

## 一般信息

bridge.按项目加载扩展。这意味着每个工作区可以拥有独特的扩展集。扩展由JSON、JavaScript和Vue文件组成。可以在[这里](https://bridge-core.github.io/created-extensions/)找到公开可用的扩展。

## 开始使用

导航到bridge.存储你项目的目录。选择你想要添加扩展的项目，并导航到`.bridge/extensions`文件夹。你也可以在bridge.根目录的`extensions`文件夹中全局添加扩展。

在此目录中，你可以为每个要添加的扩展创建一个新文件夹。在扩展的根目录中创建一个名为*manifest.json*的新JSON文件（`.bridge/extensions/<扩展名称>/manifest.json`）。

## 扩展清单

扩展清单存储有关你的附加包的重要数据，如版本号、扩展名称等。有关扩展清单的更多信息，请参见[这里](./extension-manifest.md)。

## 脚本

脚本从`<扩展名称>/scripts`文件夹加载。脚本使用JavaScript编写，允许扩展深入挂钩到bridge.的功能中。你可以创建新窗口、添加新标签类型等。