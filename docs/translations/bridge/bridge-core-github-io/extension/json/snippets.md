# 代码片段

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/json/snippets/](https://bridge-core.github.io/extension-docs/json/snippets/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/json/snippets.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/json/snippets.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@26fe9f8bcdd01f1bc2c37bc3a4fcb3fac3ff85b1 -->
///

## 概述

代码片段允许bridge.用户快速将大量代码片段插入到当前活动的编辑器中。代码片段API设计为能够自动适用于所有文件类型，包括.mcfunction、.molang、.js、.ts和.json文件，适用于文本编辑器和树形编辑器。bridge. v2提供了这一功能。

## 扩展集成

扩展可以通过在`<扩展名称>/snippets`文件夹中提供新的代码片段来添加它们。为每个要添加的代码片段创建一个JSON文件。单个文件名不重要。

## 格式

| 名称                  | 类型                      | 描述                                                                                       |
| --------------------- |-------------------------|------------------------------------------------------------------------------------------|
| `name`                | `String`                | 代码片段的名称                                                                                  |
| `description`         | `String`                | 代码片段的描述。用于补全项目菜单中                                                                        | 
| `fileTypes`           | `String[]`              | 代码片段兼容的文件类型，完整列表请参见我们的[文件类型文档](../other/default-file-types.md)                           |
| `locations`           | `String[]`              | JSON文件中可以插入代码片段的位置，例如`minecraft:entity/components`或`minecraft:entity/component_groups/*` |
| `targetFormatVersion` | `ITargetFormatVersion`  | 描述代码片段所需的格式版本范围                                                                          |
| `data`                | `String\|Object\|String[]` | 用户选择应用代码片段时插入的数据，这些数据可以是JSON文件的对象，也可以是字符串或字符串数组，字符串数组用换行符(`\n`)连接，以插入到文本文件中              |

### ITargetFormatVersion

```typescript
interface ITargetFormatVersion {
  // 代码片段所需的最低格式版本
  min: string
  // 代码片段所需的最高格式版本
  max: string
}
```

## 示例

```json
{
  "name": "我的第一个代码片段",
  "description": "这是我创建的第一个代码片段",
  "fileTypes": ["entity"],
  "locations": ["minecraft:entity/events"],
  "data": {
    "新事件": {
      "add": {
        "component_groups": []
      },
      "remove": {
        "component_groups": []
      }
    }
  }
}
```

```json
{
  "name": "你好，世界",
  "description": "显示“你好，世界”",
  "fileTypes": ["function"],
  "data": "say 你好，世界"
}
```

```json
{
  "name": "数字",
  "description": "显示值1-5",
  "fileTypes": ["function"],
  "data": ["say 1", "say 2", "say 3", "say 4", "say 5"]
}
```