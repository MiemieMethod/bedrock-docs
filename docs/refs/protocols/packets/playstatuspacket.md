# <!-- md:samp PlayStatusPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayStatusPacket -->数据包，数字ID是`2`。该数据包用于protocol.packet.playstatuspacket.description

## 结构

```viz
digraph "PlayStatusPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="PlayStatusPacket",comment="name: \"PlayStatusPacket\", typeName: \"\", id: 0, branchId: 2, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Status",comment="name: \"Status\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="big endian int",comment="name: \"big endian int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='PlayStatusPacket'
[status]
```

/// html | div.result
//// define
Status：<!-- md:samp big endian int -->

- 基本类型。protocol.packet.playstatuspacket.status.description


////

///

