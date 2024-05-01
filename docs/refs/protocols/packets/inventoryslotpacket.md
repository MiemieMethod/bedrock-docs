# <!-- md:samp InventorySlotPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp InventorySlotPacket -->数据包，数字ID是`50`。该数据包用于protocol.packet.inventoryslotpacket.description

## 结构

```viz
digraph "InventorySlotPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="InventorySlotPacket",comment="name: \"InventorySlotPacket\", typeName: \"\", id: 0, branchId: 50, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Item",comment="name: \"Item\", typeName: \"NetworkItemStackDescriptor\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='InventorySlotPacket'
[container_id][slot][item]
```

/// html | div.result
//// define
Container ID：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.inventoryslotpacket.container_id.description


////
//// define
Slot：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.inventoryslotpacket.slot.description


////
//// define
Item：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.packet.inventoryslotpacket.item.description


////

///

