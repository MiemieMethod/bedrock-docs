# <!-- md:samp PlayerHotbarPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayerHotbarPacket -->数据包，数字ID是`48`。该数据包用于protocol.packet.playerhotbarpacket.description

## 结构

```viz
digraph "PlayerHotbarPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="PlayerHotbarPacket",comment="name: \"PlayerHotbarPacket\", typeName: \"\", id: 0, branchId: 48, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Selected Slot",comment="name: \"Selected Slot\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Should select slot?",comment="name: \"Should select slot?\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='PlayerHotbarPacket'
[selected_slot][container_id][should_select_slot]
```

/// html | div.result
//// define
Selected Slot：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.playerhotbarpacket.selected_slot.description


////
//// define
Container ID：<!-- md:samp byte -->

- 基本类型。protocol.packet.playerhotbarpacket.container_id.description


////
//// define
Should select slot?：<!-- md:samp bool -->

- 基本类型。protocol.packet.playerhotbarpacket.should_select_slot.description


////

///

