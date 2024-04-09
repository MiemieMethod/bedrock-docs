# <!-- md:samp DimensionDefinitionGroup::DimensionDefinition -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DimensionDefinitionGroup::DimensionDefinition -->类型。该类型用于protocol.type.dimensiondefinitiongroup::dimensiondefinition.description

## 结构

```viz
digraph "DimensionDefinitionGroup::DimensionDefinition" {
rankdir = LR
10
10 -> 11
11 -> 12
10 -> 13
13 -> 14
10 -> 15
15 -> 16

10 [label="DimensionDefinitionGroup::DimensionDefinition",comment="name: \"DimensionDefinitionGroup::DimensionDefinition\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="Height Maximum",comment="name: \"Height Maximum\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="varint",comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Height Minimum",comment="name: \"Height Minimum\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="varint",comment="name: \"varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Generator Type",comment="name: \"Generator Type\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="varint",comment="name: \"varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;12;14;16}

}

```

## 字段

```title='DimensionDefinitionGroup::DimensionDefinition'
[height_maximum][height_minimum][generator_type]
```

/// html | div.result
//// define
Height Maximum：<!-- md:samp varint -->

- 基本类型。protocol.type.dimensiondefinitiongroup::dimensiondefinition.height_maximum.description


////
//// define
Height Minimum：<!-- md:samp varint -->

- 基本类型。protocol.type.dimensiondefinitiongroup::dimensiondefinition.height_minimum.description


////
//// define
Generator Type：<!-- md:samp varint -->

- 基本类型。protocol.type.dimensiondefinitiongroup::dimensiondefinition.generator_type.description


////

///

