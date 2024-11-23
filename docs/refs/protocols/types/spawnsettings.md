# <!-- md:samp SpawnSettings -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp SpawnSettings -->类型。该类型用于protocol.type.spawnsettings.description

## 结构

```viz
digraph "SpawnSettings" {
rankdir = LR
27
27 -> 28
28 -> 29
27 -> 30
30 -> 31
27 -> 32
32 -> 33

27 [label="SpawnSettings",comment="name: \"SpawnSettings\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
28 [label="Type",comment="name: \"Type\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="short",comment="name: \"short\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="User Defined Biome Name",comment="name: \"User Defined Biome Name\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
31 [label="string",comment="name: \"string\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
32 [label="Dimension",comment="name: \"Dimension\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently 0 for Overworld, 1 for Nether, 2 for The End, 3 Undefined\""];
33 [label="varint",comment="name: \"varint\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;29;31;33}

}

```

## 字段

```title='SpawnSettings'
[type][user_defined_biome_name][dimension]
```

/// html | div.result
//// define
Type：<!-- md:samp short -->

- 基本类型枚举。protocol.type.spawnsettings.type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Default`|`0`|protocol.enum.default|
  |`UserDefined`|`1`|protocol.enum.userdefined|



////
//// define
User Defined Biome Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.spawnsettings.user_defined_biome_name.description


////
//// define
Dimension：<!-- md:samp varint -->

- 基本类型。protocol.type.spawnsettings.dimension.descriptionCurrently 0 for Overworld, 1 for Nether, 2 for The End, 3 Undefined


////

///

