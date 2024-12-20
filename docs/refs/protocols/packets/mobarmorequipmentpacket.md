# <!-- md:samp MobArmorEquipmentPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp MobArmorEquipmentPacket -->数据包，数字ID是`32`。该数据包用于protocol.packet.mobarmorequipmentpacket.description

## 结构

```viz
digraph "MobArmorEquipmentPacket" {
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
0 -> 11
11 -> 12

0 [label="MobArmorEquipmentPacket",comment="name: \"MobArmorEquipmentPacket\", typeName: \"\", id: 0, branchId: 32, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Head",comment="name: \"Head\", typeName: \"NetworkItemStackDescriptor\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Torso",comment="name: \"Torso\", typeName: \"NetworkItemStackDescriptor\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Legs",comment="name: \"Legs\", typeName: \"NetworkItemStackDescriptor\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
8 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Feet",comment="name: \"Feet\", typeName: \"NetworkItemStackDescriptor\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Body",comment="name: \"Body\", typeName: \"NetworkItemStackDescriptor\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12}

}

```

## 字段

```title='MobArmorEquipmentPacket'
[target_runtime_id][head][torso][legs][feet][body]
```

/// html | div.result
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.mobarmorequipmentpacket.target_runtime_id.description


////
//// define
Head：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.packet.mobarmorequipmentpacket.head.description


////
//// define
Torso：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.packet.mobarmorequipmentpacket.torso.description


////
//// define
Legs：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.packet.mobarmorequipmentpacket.legs.description


////
//// define
Feet：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.packet.mobarmorequipmentpacket.feet.description


////
//// define
Body：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.packet.mobarmorequipmentpacket.body.description


////

///

