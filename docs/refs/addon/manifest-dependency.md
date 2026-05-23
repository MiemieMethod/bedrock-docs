# 清单依赖架构参考

本文档对应Microsoft Learn的`minecraft:dependency`结构。

## 字段

| 字段 | 默认值 | 类型 | 说明 |
|------|--------|------|------|
| `module_name` | *未设置* | 字符串 | 原生模块依赖名。 |
| `uuid` | *未设置* | 对象 | 包依赖标识符字段。 |
| `version` | *未设置* | [语义版本对象](#版本对象)或字符串 | 依赖版本。 |

## 版本对象

`version`对象在该结构中的字段默认值均为*未设置*：

| 字段 | 默认值 | 类型 |
|------|--------|------|
| `buildMeta` | *未设置* | 字符串 |
| `major` | *未设置* | 整数 |
| `minor` | *未设置* | 整数 |
| `patch` | *未设置* | 整数 |
| `preRelease` | *未设置* | 字符串 |

## 依赖分流

- 使用`uuid+version`时，可按[包依赖](manifest-pack-dependency.md)结构理解。
- 使用`module_name+version`时，可按[原生模块依赖](manifest-native-module-dependency.md)结构理解。

## 相关页面

- [清单文件架构](manifest-schema.md)
- [包依赖](manifest-pack-dependency.md)
- [原生模块依赖](manifest-native-module-dependency.md)
- [版本格式](semversion.md)
