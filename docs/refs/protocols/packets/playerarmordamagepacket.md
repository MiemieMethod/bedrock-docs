# <!-- md:samp PlayerArmorDamagePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerArmorDamagePacket -->数据包，数字ID是`149`。

## 结构

```viz
digraph "PlayerArmorDamagePacket" {
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

0 [label="PlayerArmorDamagePacket",comment="name: \"PlayerArmorDamagePacket\", typeName: \"\", id: 0, branchId: 149, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Slots Bitset",comment="name: \"Slots Bitset\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Damage For Slot (Only Gets Written If Bit Is Set)",comment="name: \"Damage For Slot (Only Gets Written If Bit Is Set)\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Damage For Slot (Only Gets Written If Bit Is Set)",comment="name: \"Damage For Slot (Only Gets Written If Bit Is Set)\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Damage For Slot (Only Gets Written If Bit Is Set)",comment="name: \"Damage For Slot (Only Gets Written If Bit Is Set)\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="varint",comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Damage For Slot (Only Gets Written If Bit Is Set)",comment="name: \"Damage For Slot (Only Gets Written If Bit Is Set)\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='PlayerArmorDamagePacket'
[slots_bitset][damage_for_slot_(only_gets_written_if_bit_is_set)][damage_for_slot_(only_gets_written_if_bit_is_set)][damage_for_slot_(only_gets_written_if_bit_is_set)][damage_for_slot_(only_gets_written_if_bit_is_set)]
```

/// html | div.result
//// define
Slots Bitset：<!-- md:samp byte -->

- 类型：<!-- md:samp byte -->。


////
//// define
Damage For Slot (Only Gets Written If Bit Is Set)：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。


////
//// define
Damage For Slot (Only Gets Written If Bit Is Set)：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。


////
//// define
Damage For Slot (Only Gets Written If Bit Is Set)：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。


////
//// define
Damage For Slot (Only Gets Written If Bit Is Set)：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。


////

///

