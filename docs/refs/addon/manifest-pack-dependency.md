# 包依赖架构参考

本文档对应Microsoft Learn的`minecraft:packdependency`结构。

## 字段

| 字段 | 默认值 | 类型 | 说明 |
|------|--------|------|------|
| `uuid` | *未设置* | 对象 | 被依赖包标识符字段。 |
| `version` | *未设置* | [语义版本对象](#版本对象)或字符串 | 被依赖包版本。 |

## 版本对象

| 字段 | 默认值 | 类型 |
|------|--------|------|
| `buildMeta` | *空* | 字符串 |
| `major` | `0` | 整数 |
| `minor` | `0` | 整数 |
| `patch` | `0` | 整数 |
| `preRelease` | *空* | 字符串 |

## 相关页面

- [清单依赖](manifest-dependency.md)
- [清单文件架构](manifest-schema.md)
- [版本格式](semversion.md)