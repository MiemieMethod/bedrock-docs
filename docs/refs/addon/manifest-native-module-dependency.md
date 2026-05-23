# 原生模块依赖架构参考

本文档对应Microsoft Learn的`minecraft:nativemoduledependency`结构。

## 字段

| 字段 | 默认值 | 类型 | 说明 |
|------|--------|------|------|
| `module_name` | *未设置* | 字符串 | 原生模块名。 |
| `optional` | `false` | 布尔值 | 是否可选依赖。 |
| `version` | *未设置* | 对象 | 模块版本字段。 |

## 常见模块名

| 模块名 | 说明 |
|--------|------|
| `@minecraft/server` | 服务端脚本模块。 |
| `@minecraft/server-ui` | UI脚本模块。 |
| `@minecraft/server-gametest` | GameTest脚本模块。 |

## 相关页面

- [清单依赖](manifest-dependency.md)
- [清单文件架构](manifest-schema.md)
