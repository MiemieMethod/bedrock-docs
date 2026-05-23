# 版本格式参考

本文档对应Microsoft Learn的`minecraft:semversionproxy`结构。

## 语义版本对象字段

| 字段 | 默认值 | 类型 | 说明 |
|------|--------|------|------|
| `buildMeta` | *空* | 字符串 | 构建元数据。 |
| `major` | `0` | 整数 | 主版本号。 |
| `minor` | `0` | 整数 | 次版本号。 |
| `patch` | `0` | 整数 | 补丁版本号。 |
| `preRelease` | *空* | 字符串 | 预发布标识。 |

## 表示形式

- 对象形式：使用上述五个字段。
- 字符串形式：`major.minor.patch`，也可附加预发布和构建元数据。

## 相关页面

- [清单标头](manifest-header.md)
- [清单模块](manifest-module.md)
- [清单依赖](manifest-dependency.md)
