# <!-- md:samp SubChunkPacket::SubChunkPosOffset -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SubChunkPacket::SubChunkPosOffset -->类型。

## 结构

```viz
digraph "SubChunkPacket::SubChunkPosOffset" {
rankdir = LR
19
19 -> 20
20 -> 21
19 -> 22
22 -> 23
19 -> 24
24 -> 25

19 [label="SubChunkPacket::SubChunkPosOffset",comment="name: \"SubChunkPacket::SubChunkPosOffset\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="Offset X",comment="name: \"Offset X\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="byte",comment="name: \"byte\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="Offset Y",comment="name: \"Offset Y\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
23 [label="byte",comment="name: \"byte\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
24 [label="Offset Z",comment="name: \"Offset Z\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="byte",comment="name: \"byte\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;21;23;25}

}

```

## 字段

```title='SubChunkPacket::SubChunkPosOffset'
[offset_x][offset_y][offset_z]
```

/// html | div.result
//// define
Offset X：<!-- md:samp byte -->

- <!-- md:samp byte -->类型。


////
//// define
Offset Y：<!-- md:samp byte -->

- <!-- md:samp byte -->类型。


////
//// define
Offset Z：<!-- md:samp byte -->

- <!-- md:samp byte -->类型。


////

///

