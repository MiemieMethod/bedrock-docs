# <!-- md:samp InventorySlotPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InventorySlotPacket -->数据包，数字ID是`50`。

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
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\""];
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

- <!-- md:samp unsigned varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`CONTAINER_ID_NONE`|`-1`||
  |`CONTAINER_ID_INVENTORY`|`0`||
  |`CONTAINER_ID_FIRST`|`1`||
  |`CONTAINER_ID_LAST`|`100`||
  |`CONTAINER_ID_OFFHAND`|`119`||
  |`CONTAINER_ID_ARMOR`|`120`||
  |`CONTAINER_ID_SELECTION_SLOTS`|`122`||
  |`CONTAINER_ID_PLAYER_ONLY_UI`|`124`||



////
//// define
Slot：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


////
//// define
Item：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- <!-- md:samp NetworkItemStackDescriptor -->类型。


////

///

