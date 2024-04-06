# <!-- md:samp MobEquipmentPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MobEquipmentPacket -->数据包，数字ID是`31`。

## 结构

```viz
digraph "MobEquipmentPacket" {
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

0 [label="MobEquipmentPacket",comment="name: \"MobEquipmentPacket\", typeName: \"\", id: 0, branchId: 31, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Item",comment="name: \"Item\", typeName: \"NetworkItemStackDescriptor\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Selected Slot",comment="name: \"Selected Slot\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\""];
10 [label="byte",comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='MobEquipmentPacket'
[target_runtime_id][item][slot][selected_slot][container_id]
```

/// html | div.result
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。


////
//// define
Item：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。


////
//// define
Slot：<!-- md:samp byte -->

- 基本类型。


////
//// define
Selected Slot：<!-- md:samp byte -->

- 基本类型。


////
//// define
Container ID：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

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

///
