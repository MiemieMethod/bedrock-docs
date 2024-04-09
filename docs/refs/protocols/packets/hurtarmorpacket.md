# <!-- md:samp HurtArmorPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp HurtArmorPacket -->数据包，数字ID是`38`。该数据包用于protocol.packet.hurtarmorpacket.description

## 结构

```viz
digraph "HurtArmorPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="HurtArmorPacket",comment="name: \"HurtArmorPacket\", typeName: \"\", id: 0, branchId: 38, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Cause",comment="name: \"Cause\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Damage",comment="name: \"Damage\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Armor Slots",comment="name: \"Armor Slots\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Bitset\""];
6 [label="unsigned varint64",comment="name: \"unsigned varint64\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='HurtArmorPacket'
[cause][damage][armor_slots]
```

/// html | div.result
//// define
Cause：<!-- md:samp varint -->

- 基本类型。protocol.packet.hurtarmorpacket.cause.description


////
//// define
Damage：<!-- md:samp varint -->

- 基本类型。protocol.packet.hurtarmorpacket.damage.description


////
//// define
Armor Slots：<!-- md:samp unsigned varint64 -->

- 基本类型。protocol.packet.hurtarmorpacket.armor_slots.descriptionBitset


////

///

