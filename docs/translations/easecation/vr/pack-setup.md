# 设置资源包

/// details-info | 署名信息
- 该页面整理自[EaseCation Wiki](https://mcwiki.easecation.net/wiki/vr/pack_setup)
///

VR资源包负责提供全息模型与对应纹理。制作VR内容前，通常需要先获取一个基础模板，再将其并入自己的资源包结构中。

## 模板包含哪些内容

模板通常包含两个可编辑目录：

- `holograms`：存放全息模型。
- `textures`：存放模型使用的纹理贴图。

## 需要注意的文件

模板依赖`contents.json`和`textures_list.json`运行。前者用于声明可用内容，后者用于列出纹理资源。删除这两个文件会导致模板失效。

/// warning | 文件合并
如果你的自有资源包中已经存在同名文件，必须手动合并，不可直接覆盖。
///

## 合并方式

1. 将模板中的全息模型和纹理复制到自己的资源包。
2. 检查`contents.json`和`textures_list.json`中的条目是否重复。
3. 将所有需要被游戏调用的资源都登记到对应文件中。
4. 确认资源路径与文件名一致。
