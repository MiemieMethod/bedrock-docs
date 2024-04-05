# <!-- md:samp SetPlayerGameTypePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetPlayerGameTypePacket -->数据包，数字ID是`62`。

## 结构

```viz
digraph "SetPlayerGameTypePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetPlayerGameTypePacket",comment="name: \"SetPlayerGameTypePacket\", typeName: \"\", id: 0, branchId: 62, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player Game Type",comment="name: \"Player Game Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameType\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

/// define
SetPlayerGameTypePacket

Player Game Type：<!-- md:samp varint -->

- 类型：varint。enumeration: GameType


///
