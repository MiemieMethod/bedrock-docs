# 文件定义

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/json/file-definitions/](https://bridge-core.github.io/extension-docs/json/file-definitions/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/json/file-definitions.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/json/file-definitions.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@4ec6002ba312583b1a86a0e98d897b87dd8e220a -->
///

## 一般信息

文件定义允许你将新文件类型注册到bridge.。文件定义仅通过位于`<packageName>/fileDefinitions`或`<EXTENSION NAME>/fileDefinitions`下的JSON文件加载。

## 格式

以下接口描述了文件定义文件的JSON格式。

```typescript
interface IFileType {
  type?: 'json' | 'text' | 'nbt'
  id: string
  icon?: string
  detect?: {
    scope?: string | string[]
    matcher?: string | string[]
    fileContent?: string[]
    fileExtensions?: string[]
  }

  schema: string
  types: (string | [string, { targetVersion: [CompareOperator, string] }])[]
  packSpider: string
  lightningCache: string
  definitions: IDefinitions
  formatOnSaveCapable: boolean
  documentation?: {
    baseUrl: string
    supportsQuerying?: boolean // 默认: true
  }
  meta?: {
    commandsUseSlash?: boolean
  }
  highlighterConfiguration?: {
    keywords?: string[]
    typeIdentifiers?: string[]
    variables?: string[]
    definitions?: string[]
  }
}
interface IDefinitions {
  [key: string]: IDefinition | IDefinition[]
}
interface IDefinition {
  directReference?: boolean
  from: string
  match: string
}
```

### `type`

此文件定义应定义的文件类型。用于帮助bridge.确定如何加载文件。
示例：`#!json "type": "json"`

### `id`

文件定义的唯一标识符。
示例：`#!json "id": "entity"`

### `icon`

应与此文件类型关联的[Material Design Icon](https://materialdesignicons.com/)。
示例：`#!json "icon": "mdi-minecraft"`

### `detect`

用于检测此文件的属性。

-   `scope` - 文件将位于的项目文件夹范围，例如`#!json "scope": "BP/entities/"`
-   `matcher` - 使用glob模式匹配更精确文件位置的单一路径或路径列表。例如`#!json "matcher": ["BP/entities/**/*.json", "BP/entities/*.json"]`
-   `fileContent` - 文件的顶级属性，可用于猜测文件类型，例如`#!json "fileContent": ["minecraft:entity"]`
-   `fileExtensions` - 此文件可以使用的文件扩展名。用于帮助猜测文件类型。例如`#!json "fileExtensions": [".mcstructure"]`

### `schema`

此项可以定义JSON架构的路径，以提供自动补全和文件验证。
示例：`#!json "schema": "file:///data/packages/minecraftBedrock/schema/entity/main.json"`

### `types`

此项可用于定义TypeScript声明文件的路径，以便在JavaScript或TypeScript文件中提供自动补全和验证。你可以选择性地指定目标版本以过滤类型声明文件。
示例：`#!json "types": ["types/scriptingApi/common.d.ts","types/scriptingApi/client.d.ts"]`

### `packSpider`

此项可以引用一个包蜘蛛定义文件，以便将此文件类型链接到其他文件类型。
示例：`#!json "packSpider": "entity.json"`

### `lightningCache`

此项可以引用一个闪电缓存定义文件，以便从此文件类型收集数据，用于架构和其他bridge.功能。

### `definitions`

此属性用于提供数据给bridge.在JSON文件中的跳转定义功能。
示例：

```json
{
  "definitions": {
    "identifier": [
      {
        "from": "clientEntity",
        "match": "identifier"
      },
      {
        "from": "spawnRule",
        "match": "identifier"
      }
    ],
    "lootTablePath": {
      "directReference": true
    }
  }
}
```

在此示例中，`"identifier"`和`"lootTablePath"`是来自此文件的闪电缓存键。
`"match"`指定此键应匹配的闪电缓存键，`"from"`指定要搜索此键的文件ID。
当缓存键的值是直接指向定义文件的文件路径时，`"directReference"`应设置为true。

### `formatOnSaveCapable`

如果文件能够在保存时由monaco自动格式化，则应设置为true。
示例：`#!json "formatOnSaveCapable": false`

### `documentation`

-   `"baseUrl"` - 应为此文件的文档基础URL。
-   `"supportsQuerying"` - 文档是否支持查询特定字符串。

示例：

```json
{
  "documentation": {
    "baseUrl": "https://bedrock.dev/docs/stable/Entities"
  }
}
```

### `meta`

文件类型的附加元数据。

-   `commandsUseSlash` - 此文件中的内联命令是否在前面使用斜杠。如果为false，则将自动从文件中编写的命令中删除斜杠。

示例：

```json
{
  "meta": {
    "commandsUseSlash": true
  }
}
```

### `highlighterConfiguration`

此项定义了此文件的语法高亮配置，以及哪些字符串应使用特定颜色名称进行着色。

示例：

```json
{
  "highlighterConfiguration": {
    "variables": [
      "description",
      "component_groups",
      "permutations",
      "components",
      "events"
    ],
    "typeIdentifiers": ["format_version", "event"],
    "definitions": [
      "animations",
      "scripts",
      "filters",
      "add",
      "remove",
      "run_command"
    ]
  }
}
```

## 示例

-   [`内置文件定义`](https://github.com/bridge-core/editor-packages/tree/main/packages/minecraftBedrock/fileDefinition)