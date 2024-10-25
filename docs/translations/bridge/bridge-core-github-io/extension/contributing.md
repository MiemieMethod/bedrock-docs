# 贡献扩展

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/contributing/](https://bridge-core.github.io/extension-docs/contributing/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/contributing.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/contributing.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@2288e988aa39b393169b3a4e83469928088e4f5e -->
///

## 仓库

bridge.从[bridge-core/plugins](https://github.com/bridge-core/plugins)仓库中拉取扩展。为了使你的扩展在bridge.中显示，你需要将其添加到该仓库。

## 添加扩展

_在将你的插件添加到仓库之前，请确保插件正常工作。_

要添加扩展，请将扩展的文件夹拖入`plugins`文件夹。
一旦拉取请求合并，它将**自动创建一个插件的zip文件**，并将其添加到plugins.json或extensions.json文件中，具体取决于目标版本的bridge.，因此你无需自己执行此操作。

**确保你的扩展清单包含以下信息：**

- `"author"`
- `"name"`
- `"version"`
- `"id"`
- `"description"`
- `"tags"`

未列出的属性为可选项。

如果你为bridge. v2贡献扩展，请在扩展清单中将`"target"`属性设置为`"v2"`，如果扩展与两个版本兼容，则设置为`"both"`。如果未指定，将默认为`"v1"`。