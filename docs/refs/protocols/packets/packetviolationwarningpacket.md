# <!-- md:samp PacketViolationWarningPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PacketViolationWarningPacket -->数据包，数字ID是`156`。该数据包用于protocol.packet.packetviolationwarningpacket.description

## 结构

```viz
digraph "PacketViolationWarningPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8

0 [label="PacketViolationWarningPacket",comment="name: \"PacketViolationWarningPacket\", typeName: \"\", id: 0, branchId: 156, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Violation Type",comment="name: \"Violation Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Violation Severity",comment="name: \"Violation Severity\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Violating packet id",comment="name: \"Violating packet id\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Violation context",comment="name: \"Violation context\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='PacketViolationWarningPacket'
[violation_type][violation_severity][violating_packet_id][violation_context]
```

/// html | div.result
//// define
Violation Type：<!-- md:samp varint -->

- 基本类型。protocol.packet.packetviolationwarningpacket.violation_type.description


////
//// define
Violation Severity：<!-- md:samp varint -->

- 基本类型。protocol.packet.packetviolationwarningpacket.violation_severity.description


////
//// define
Violating packet id：<!-- md:samp varint -->

- 基本类型。protocol.packet.packetviolationwarningpacket.violating_packet_id.description


////
//// define
Violation context：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.packetviolationwarningpacket.violation_context.description


////

///

