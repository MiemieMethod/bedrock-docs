# <!-- md:samp LecternUpdatePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp LecternUpdatePacket -->数据包，数字ID是`125`。该数据包用于protocol.packet.lecternupdatepacket.description

## 结构

```viz
digraph "LecternUpdatePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="LecternUpdatePacket",comment="name: \"LecternUpdatePacket\", typeName: \"\", id: 0, branchId: 125, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="New page to show",comment="name: \"New page to show\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Total Pages",comment="name: \"Total Pages\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Position of Lectern to update",comment="name: \"Position of Lectern to update\", typeName: \"NetworkBlockPosition\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='LecternUpdatePacket'
[new_page_to_show][total_pages][position_of_lectern_to_update]
```

/// html | div.result
//// define
New page to show：<!-- md:samp byte -->

- 基本类型。protocol.packet.lecternupdatepacket.new_page_to_show.description


////
//// define
Total Pages：<!-- md:samp byte -->

- 基本类型。protocol.packet.lecternupdatepacket.total_pages.description


////
//// define
Position of Lectern to update：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.lecternupdatepacket.position_of_lectern_to_update.description


////

///

