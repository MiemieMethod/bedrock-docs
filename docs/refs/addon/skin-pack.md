# 皮肤包架构参考

本文档汇总Microsoft Learn的SkinPacksReference中与皮肤包相关的JSON结构、本地化键命名和校验约束。

## `skins.json`根结构

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| `serialize_name` | 字符串 | 是 | 皮肤包的序列化键，同时作为皮肤包和皮肤名称本地化键的前缀。 |
| `localization_name` | 字符串 | 是 | 皮肤包本地化名称字段。实践中应与`serialize_name`保持一致，避免键名歧义。 |
| `skins` | 数组 | 是 | 皮肤条目列表。每个元素为一个皮肤对象。 |

## `skins`数组元素结构

| 字段 | 类型 | 必选 | 说明 | 取值约束 |
|------|------|------|------|----------|
| `localization_name` | 字符串 | 是 | 单个皮肤的本地化名称字段。 | 应为可稳定复用的标识符。 |
| `geometry` | 字符串 | 是 | 玩家模型几何体标识符。 | `geometry.humanoid.custom`或`geometry.humanoid.customSlim`。 |
| `texture` | 字符串 | 是 | 皮肤纹理文件名。 | 必须与包根目录中的PNG文件名一致。 |
| `type` | 字符串 | 是 | 皮肤可用类型。 | `free`或`paid`。 |

## 本地化键命名

皮肤包语言文件通常位于`texts/*.lang`。SkinPacksReference给出的键名模式如下：

| 键名模式 | 用途 |
|----------|------|
| `skinpack.<serialize_name>=<显示名>` | 皮肤包显示名。 |
| `skinpack.<serialize_name>.by=<创作者名>` | 皮肤包署名。 |
| `skin.<serialize_name>.<skin_localization_name>=<显示名>` | 单个皮肤显示名。 |

## 序列化键关联关系

- `serialize_name`是皮肤包跨文件关联的核心键。
- `serialize_name`同时参与`skins.json`和`.lang`中的键名拼接。
- 皮肤包清单模块类型应为`skin_pack`，用于声明该包为皮肤包。

## 校验要点

- `skins.json`必须存在且满足JSON语法要求。
- `texture`引用的PNG文件必须实际存在于皮肤包根目录。
- 几何体与纹理体型应一致，避免模型显示异常。
- 本地化键必须与`serialize_name`和各皮肤`localization_name`严格对应。

## 相关页面

- [皮肤包](../../docs/addon/skin-pack.md)
- [制作皮肤包](../../guides/addons/creating-skin-packs.md)
- [清单模块架构参考](manifest-module.md)