# <!-- md:samp UpdateEquipPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp UpdateEquipPacket -->数据包，数字ID是`81`。该数据包用于protocol.packet.updateequippacket.description

## 结构

```viz
digraph "UpdateEquipPacket" {
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

0 [label="UpdateEquipPacket",comment="name: \"UpdateEquipPacket\", typeName: \"\", id: 0, branchId: 81, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Container Type",comment="name: \"Container Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Size",comment="name: \"Size\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
8 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Data Tags",comment="name: \"Data Tags\", typeName: \"CompoundTag\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='UpdateEquipPacket'
[container_id][container_type][size][target_actor_id][data_tags]
```

/// html | div.result
//// define
Container ID：<!-- md:samp byte -->

- 基本类型。protocol.packet.updateequippacket.container_id.description


////
//// define
Container Type：<!-- md:samp byte -->

- 基本类型。protocol.packet.updateequippacket.container_type.description


////
//// define
Size：<!-- md:samp varint -->

- 基本类型。protocol.packet.updateequippacket.size.description


////
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.updateequippacket.target_actor_id.description


////
//// define
Data Tags：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.updateequippacket.data_tags.description


////

///

