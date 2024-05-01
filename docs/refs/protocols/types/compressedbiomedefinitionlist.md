# <!-- md:samp CompressedBiomeDefinitionList -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp CompressedBiomeDefinitionList -->类型，数字ID是`301`。该类型用于protocol.packet.compressedbiomedefinitionlist.description

## 结构

```viz
digraph "CompressedBiomeDefinitionList" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="CompressedBiomeDefinitionList",comment="name: \"CompressedBiomeDefinitionList\", typeName: \"\", id: 0, branchId: 301, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Compressed BiomeData",comment="name: \"Compressed BiomeData\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='CompressedBiomeDefinitionList'
[compressed_biomedata]
```

/// html | div.result
//// define
Compressed BiomeData：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.compressedbiomedefinitionlist.compressed_biomedata.description


////

///

