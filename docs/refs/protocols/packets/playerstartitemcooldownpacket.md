# <!-- md:samp PlayerStartItemCooldownPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayerStartItemCooldownPacket -->数据包，数字ID是`176`。该数据包用于protocol.packet.playerstartitemcooldownpacket.description

## 结构

```viz
digraph "PlayerStartItemCooldownPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="PlayerStartItemCooldownPacket",comment="name: \"PlayerStartItemCooldownPacket\", typeName: \"\", id: 0, branchId: 176, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Item Category",comment="name: \"Item Category\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Duration Ticks",comment="name: \"Duration Ticks\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='PlayerStartItemCooldownPacket'
[item_category][duration_ticks]
```

/// html | div.result
//// define
Item Category：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.playerstartitemcooldownpacket.item_category.description


////
//// define
Duration Ticks：<!-- md:samp varint -->

- 基本类型。protocol.packet.playerstartitemcooldownpacket.duration_ticks.description


////

///

