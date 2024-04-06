# <!-- md:samp ContainerOpenPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ContainerOpenPacket -->数据包，数字ID是`46`。

## 结构

```viz
digraph "ContainerOpenPacket" {
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

0 [label="ContainerOpenPacket",comment="name: \"ContainerOpenPacket\", typeName: \"\", id: 0, branchId: 46, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Container Type",comment="name: \"Container Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerType\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Position",comment="name: \"Position\", typeName: \"NetworkBlockPosition\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
8 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='ContainerOpenPacket'
[container_id][container_type][position][target_actor_id]
```

/// html | div.result
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
//// define
Container Type：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NONE`|`-9`||
  |`INVENTORY`|`-1`||
  |`CONTAINER`|`0`||
  |`WORKBENCH`|`1`||
  |`FURNACE`|`2`||
  |`ENCHANTMENT`|`3`||
  |`BREWING_STAND`|`4`||
  |`ANVIL`|`5`||
  |`DISPENSER`|`6`||
  |`DROPPER`|`7`||
  |`HOPPER`|`8`||
  |`CAULDRON`|`9`||
  |`MINECART_CHEST`|`10`||
  |`MINECART_HOPPER`|`11`||
  |`HORSE`|`12`||
  |`BEACON`|`13`||
  |`STRUCTURE_EDITOR`|`14`||
  |`TRADE`|`15`||
  |`COMMAND_BLOCK`|`16`||
  |`JUKEBOX`|`17`||
  |`ARMOR`|`18`||
  |`HAND`|`19`||
  |`COMPOUND_CREATOR`|`20`||
  |`ELEMENT_CONSTRUCTOR`|`21`||
  |`MATERIAL_REDUCER`|`22`||
  |`LAB_TABLE`|`23`||
  |`LOOM`|`24`||
  |`LECTERN`|`25`||
  |`GRINDSTONE`|`26`||
  |`BLAST_FURNACE`|`27`||
  |`SMOKER`|`28`||
  |`STONECUTTER`|`29`||
  |`CARTOGRAPHY`|`30`||
  |`HUD`|`31`||
  |`JIGSAW_EDITOR`|`32`||
  |`SMITHING_TABLE`|`33`||
  |`CHEST_BOAT`|`34`||
  |`DECORATED_POT`|`35`||
  |`CRAFTER`|`36`||



////
//// define
Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。


////
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。


////

///

