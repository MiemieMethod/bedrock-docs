# <!-- md:samp Packet Header -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp Packet Header -->类型。该类型用于protocol.type.packet_header.description

## 结构

```viz
digraph "Packet Header" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="Packet Header",comment="name: \"Packet Header\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Packet ID",comment="name: \"Packet ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"The first 10 value bits are the packet id, the next 2 value bits are the Sender SubClientID, and the next 2 value bits are the Target SubClientID\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='Packet Header'
[packet_id]
```

/// html | div.result
//// define
Packet ID：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.packet_header.packet_id.descriptionThe first 10 value bits are the packet 'id', the next 2 value bits are the Sender SubClientID, and the next 2 value bits are the Target SubClientID


////

///

