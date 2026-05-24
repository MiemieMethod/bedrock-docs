# 清单元数据架构参考

本文档对应Microsoft Learn的`minecraft:metadata`结构。

## 字段

| 字段 | 默认值 | 类型 | 说明 |
|------|--------|------|------|
| `authors` | *未设置* | 字符串数组 | 作者列表。 |
| `generated_with` | *未设置* | 对象 | 生成工具信息。 |
| `license` | *未设置* | 字符串 | 许可证文本。 |
| `product_type` | *未设置* | 字符串 | 产品类型。 |
| `url` | *未设置* | 字符串 | 项目地址。 |

## `generated_with`说明

`generated_with`通常用于记录生成工具与版本号。例如键为工具名，值为版本字符串。

## 相关页面

- [清单文件架构](manifest-schema.md)