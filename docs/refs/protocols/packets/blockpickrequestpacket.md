# <!-- md:samp BlockPickRequestPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp BlockPickRequestPacket -->数据包，数字ID是`34`。该数据包用于protocol.packet.blockpickrequestpacket.description

## 结构

```viz
digraph "BlockPickRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="BlockPickRequestPacket",comment="name: \"BlockPickRequestPacket\", typeName: \"\", id: 0, branchId: 34, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="With Data?",comment="name: \"With Data?\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Max Slots",comment="name: \"Max Slots\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='BlockPickRequestPacket'
[position][with_data][max_slots]
```

/// html | div.result
//// define
Position：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.packet.blockpickrequestpacket.position.description


////
//// define
With Data?：<!-- md:samp bool -->

- 基本类型。protocol.packet.blockpickrequestpacket.with_data.description


////
//// define
Max Slots：<!-- md:samp byte -->

- 基本类型。protocol.packet.blockpickrequestpacket.max_slots.description


////

///

