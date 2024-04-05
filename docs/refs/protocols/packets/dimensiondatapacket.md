# <!-- md:samp DimensionDataPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DimensionDataPacket -->数据包，数字ID是`180`。

## 结构

```viz
digraph "DimensionDataPacket" {
rankdir = LR
0
0 -> 1
1 -> 18

0 [label="DimensionDataPacket",comment="name: \"DimensionDataPacket\", typeName: \"\", id: 0, branchId: 180, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Dimension Definition Group",comment="name: \"Dimension Definition Group\", typeName: \"DimensionDefinitionGroup\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
18 [label="DimensionDefinitionGroup",comment="name: \"DimensionDefinitionGroup\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;18}

}

```

## 字段

/// define
DimensionDataPacket

Dimension Definition Group：[<!-- md:samp DimensionDefinitionGroup -->](../types/dimensiondefinitiongroup.md)

- 类型：DimensionDefinitionGroup。


///
