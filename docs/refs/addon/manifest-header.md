# 清单标头架构参考

本文档对应Microsoft Learn的`minecraft:header`结构。

## 字段

| 字段 | 默认值 | 类型 | 说明 |
|------|--------|------|------|
| `allow_random_seed` | *未设置* | 布尔值 | 是否允许随机种子。 |
| `base_game_version` | *未设置* | 字符串 | 基游戏版本。 |
| `description` | *未设置* | 字符串 | 包描述。 |
| `lock_template_options` | *未设置* | 布尔值 | 是否锁定模板选项。 |
| `min_engine_version` | *未设置* | 字符串 | 最低引擎版本。 |
| `name` | *未设置* | 字符串 | 包名称。 |
| `pack_optimization_version` | *未设置* | [语义版本对象](#包优化版本对象)或字符串 | 包优化版本。 |
| `pack_scope` | *未设置* | 字符串 | 包作用域。 |
| `platform_locked` | *未设置* | 布尔值 | 是否平台锁定。 |
| `uuid` | *未设置* | 对象 | 包标识符字段。 |
| `version` | *未设置* | [语义版本对象](#版本对象)或字符串 | 包版本。 |

## 包优化版本对象

`pack_optimization_version`使用以下字段：

| 字段 | 默认值 | 类型 |
|------|--------|------|
| `buildMeta` | *空* | 字符串 |
| `major` | `0` | 整数 |
| `minor` | `0` | 整数 |
| `patch` | `0` | 整数 |
| `preRelease` | *空* | 字符串 |

## 版本对象

`version`对象结构与[包优化版本对象](#包优化版本对象)一致。

## 相关页面

- [清单文件架构](manifest-schema.md)
- [版本格式](semversion.md)