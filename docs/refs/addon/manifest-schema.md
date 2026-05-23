# 清单文件架构参考

本文档对应Microsoft Learn的`minecraft:packmanifestdocument`结构，描述{{file|manifest.json}}根对象的字段。

## 顶层字段

| 字段 | 默认值 | 类型 | 说明 |
|------|--------|------|------|
| `capabilities` | *未设置* | 字符串数组 | 声明包请求的功能。 |
| `dependencies` | *未设置* | 字符串数组 | 依赖字段入口。依赖项结构见[清单依赖](manifest-dependency.md)。 |
| `format_version` | *未设置* | 整数 | 清单格式版本。 |
| `has_education_metadata` | *未设置* | 布尔值 | 是否包含教育版元数据。<!-- md:flag edu --> |
| `header` | *未设置* | [Header](manifest-header.md)对象 | 包标头。 |
| `metadata` | *未设置* | [Metadata](manifest-metadata.md)对象 | 包元数据。 |
| `modules` | *未设置* | [Module](manifest-module.md)项 | 模块声明入口。 |
| `settings` | *未设置* | 字符串数组 | 世界设置入口。具体结构见[世界设置](world-setting.md)。 |
| `subpacks` | *未设置* | [Subpack](manifest-subpack.md)项 | 子包声明入口。 |

## 字段关联

- `header`：定义包身份、版本和兼容性信息。
- `modules`：定义包包含的数据模块、资源模块或脚本模块。
- `dependencies`：定义包依赖或原生模块依赖。
- `settings`：定义世界创建界面可配置的设置项。
- `subpacks`：定义可选子包和性能分级。

## 备注

ManifestReference自动导出的`dependencies`与`settings`在顶层表中显示为字符串数组；同目录同时提供了依赖对象与设置对象的独立结构定义。参考页按结构页拆分呈现，便于逐字段查阅。
