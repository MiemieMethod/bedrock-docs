# <!-- md:samp InventorySlotPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

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
0 -> 7
7 -> 8
0 -> 9
9 -> 10

0 [label="InventorySlotPacket",comment="name: \"InventorySlotPacket\", typeName: \"\", id: 0, branchId: 50, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Full Container Name",comment="name: \"Full Container Name\", typeName: \"FullContainerName\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"Used to reference a specific container within a given screen container context\""];
6 [label="FullContainerName",comment="name: \"FullContainerName\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Dynamic Container Size",comment="name: \"Dynamic Container Size\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Size of the container if it is dynamic, zero otherwise\""];
8 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Item",comment="name: \"Item\", typeName: \"NetworkItemStackDescriptor\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='InventorySlotPacket'
[container_id][slot][full_container_name][dynamic_container_size][item]
```

/// html | div.result
//// define
Container ID：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.packet.inventoryslotpacket.container_id.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`CONTAINER_ID_NONE`|`-1`|protocol.enum.container_id_none|
  |`CONTAINER_ID_INVENTORY`|`0`|protocol.enum.container_id_inventory|
  |`CONTAINER_ID_FIRST`|`1`|protocol.enum.container_id_first|
  |`CONTAINER_ID_LAST`|`100`|protocol.enum.container_id_last|
  |`CONTAINER_ID_OFFHAND`|`119`|protocol.enum.container_id_offhand|
  |`CONTAINER_ID_ARMOR`|`120`|protocol.enum.container_id_armor|
  |`CONTAINER_ID_SELECTION_SLOTS`|`122`|protocol.enum.container_id_selection_slots|
  |`CONTAINER_ID_PLAYER_ONLY_UI`|`124`|protocol.enum.container_id_player_only_ui|
  |`CONTAINER_ID_REGISTRY`|`125`|protocol.enum.container_id_registry|
  |`CONTAINER_ID_REGISTRY_INVENTORY`|`126`|protocol.enum.container_id_registry_inventory|



////
//// define
Slot：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.inventoryslotpacket.slot.description


////
//// define
Full Container Name：[<!-- md:samp FullContainerName -->](../types/fullcontainername.md)

- 特殊类型。protocol.packet.inventoryslotpacket.full_container_name.descriptionUsed to reference a specific container within a given screen container context


////
//// define
Dynamic Container Size：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.inventoryslotpacket.dynamic_container_size.descriptionSize of the container if it is dynamic, zero otherwise


////
//// define
Item：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.packet.inventoryslotpacket.item.description


////

///

