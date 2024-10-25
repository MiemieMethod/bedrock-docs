# <!-- md:samp BlockEventPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp BlockEventPacket -->数据包，数字ID是`26`。该数据包用于protocol.packet.blockeventpacket.description

## 结构

```viz
digraph "BlockEventPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="BlockEventPacket",comment="name: \"BlockEventPacket\", typeName: \"\", id: 0, branchId: 26, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Block Position",comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Event Type",comment="name: \"Event Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Event Value",comment="name: \"Event Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='BlockEventPacket'
[block_position][event_type][event_value]
```

/// html | div.result
//// define
Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.blockeventpacket.block_position.description


////
//// define
Event Type：<!-- md:samp varint -->

- 基本类型。protocol.packet.blockeventpacket.event_type.description


////
//// define
Event Value：<!-- md:samp varint -->

- 基本类型。protocol.packet.blockeventpacket.event_value.description


////

///

