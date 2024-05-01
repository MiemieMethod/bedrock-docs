# <!-- md:samp PlayerToggleCrafterSlotRequestPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayerToggleCrafterSlotRequestPacket -->数据包，数字ID是`306`。该数据包用于protocol.packet.playertogglecrafterslotrequestpacket.description

## 结构

```viz
digraph "PlayerToggleCrafterSlotRequestPacket" {
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
0 -> 9
9 -> 10

0 [label="PlayerToggleCrafterSlotRequestPacket",comment="name: \"PlayerToggleCrafterSlotRequestPacket\", typeName: \"\", id: 0, branchId: 306, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Pos X",comment="name: \"Pos X\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="int",comment="name: \"int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Pos Y",comment="name: \"Pos Y\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="int",comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Pos Z",comment="name: \"Pos Z\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="int",comment="name: \"int\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Slot Index",comment="name: \"Slot Index\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Is Disabled",comment="name: \"Is Disabled\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="bool",comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='PlayerToggleCrafterSlotRequestPacket'
[pos_x][pos_y][pos_z][slot_index][is_disabled]
```

/// html | div.result
//// define
Pos X：<!-- md:samp int -->

- 基本类型。protocol.packet.playertogglecrafterslotrequestpacket.pos_x.description


////
//// define
Pos Y：<!-- md:samp int -->

- 基本类型。protocol.packet.playertogglecrafterslotrequestpacket.pos_y.description


////
//// define
Pos Z：<!-- md:samp int -->

- 基本类型。protocol.packet.playertogglecrafterslotrequestpacket.pos_z.description


////
//// define
Slot Index：<!-- md:samp byte -->

- 基本类型。protocol.packet.playertogglecrafterslotrequestpacket.slot_index.description


////
//// define
Is Disabled：<!-- md:samp bool -->

- 基本类型。protocol.packet.playertogglecrafterslotrequestpacket.is_disabled.description


////

///

