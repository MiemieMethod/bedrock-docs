# 扩展清单

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/extension-manifest/](https://bridge-core.github.io/extension-docs/extension-manifest/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/extension-manifest.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/extension-manifest.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@594c381b198a963354203dcec0674a112db4ec85 -->
///

扩展清单用于存储有关你的扩展的数据。它应位于扩展的根目录，并且必须命名为`manifest.json`。

## 字段

### `icon`

**类型：字符串**

图标应为以`mdi-`开头的[Material Design Icon](https://materialdesignicons.com/)的ID，例如：`mdi-apple`。

### `author`

**类型：字符串**

作者可以是任何字符串，用于在bridge.的用户界面中显示扩展的作者。

### `id`

**类型：字符串**

ID应为唯一的UUID V4，你可以从[UUIDGenerator](https://www.uuidgenerator.net/)生成。

### `version`

**类型：字符串**

版本应为`X.X.X`格式的版本，例如`1.2.3`。在更新扩展时，此版本号需要递增。

### `name`

**类型：字符串**

名称字段应简单地包含要在bridge.的用户界面中显示的扩展名称。

### `link`

**类型：字符串**

链接可以是与扩展或创建者相关的网页链接。用户可以通过bridge.的用户界面中的按钮访问该链接。

### `target`

**类型：字符串**

目标可以是三种选项之一：`v1`、`v2`或`both`。这在你将扩展发布到扩展商店时用于选择是将扩展发布到bridge. v1、bridge. v2还是两者。

### `description`

**类型：字符串**

扩展的描述应简要概述你的扩展的功能。这将在bridge.的用户界面中显示。

### `api_version`

**类型：整数**

API版本仅与bridge. v1相关，可以是`1`或`2`。它告诉bridge.扩展是用于新扩展API还是旧扩展API。如果省略，将默认为最新版本。

### `tags`

**类型：数组<string>**

标签列表应为扩展标签ID的数组。可用的标签ID可以在[这里](https://github.com/bridge-core/editor-packages/blob/main/packages/common/extensionTags.json)找到。

### `compiler`

**类型：对象**

编译器字段应用于编译器插件，以指定插件的ID和文件位置。

结构：

```json
{
  "compiler": {
    "plugins": {
      "<ID>": "<LOCATION>"
    }
  }
}
```

示例：

```json
{
  "compiler": {
    "plugins": {
      "jsonEncoder": "compiler/jsonEncoder.js"
    }
  }
}
```

### `contributeFiles`

**类型：对象**

贡献文件字段用于在安装扩展时将文件或文件夹安装到项目中。这可以用于将自定义组件和命令安装到`BP/commands`和`BP/components`文件夹。

你可以像这样添加单个文件：

```json
{
  "contributeFiles": {
    "<FILE_SOURCE>": "<FILE_DESTINATION>"
  }
}
```

```json
{
  "contributeFiles": {
    "components/item/myComponent.js": "BP/components/item/myComponent.js"
  }
}
```

并像这样添加文件夹：

```json
{
  "contributeFiles": {
    "<FOLDER_SOURCE>": "<FOLDER_DESTINATION>"
  }
}
```

```json
{
  "contributeFiles": {
    "components/item": "BP/components/item/"
  }
}
```

### `readme`

**类型：字符串**

指向你扩展的自述文件的URL。在扩展商店中为你的扩展创建一个按钮，以访问你设置的URL。

### `compatibleAppVersions`

**类型：对象**

一个具有`min`和`max`字段的对象，用于指定你的扩展支持的bridge.版本范围。

## 示例

```json
{
  "author": "solvedDev",
  "icon": "mdi-code-braces",
  "id": "aad1d7ec-a32e-4732-ad2b-abb770e38202",
  "version": "1.0.0",
  "name": "我的扩展",
  "link": "www.my_homepage.com/me",
  "target": "v2",
  "description": "我的第一个bridge.扩展",
  "api_version": 2,
  "tags": ["实用工具"]
}
```