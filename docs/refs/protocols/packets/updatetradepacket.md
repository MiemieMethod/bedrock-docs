# <!-- md:samp UpdateTradePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateTradePacket -->数据包，数字ID是`80`。

## 结构

```viz
digraph "UpdateTradePacket" {
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
0 -> 13
13 -> 14
0 -> 15
15 -> 16
0 -> 17
17 -> 18
0 -> 19
19 -> 20

0 [label="UpdateTradePacket",comment="name: \"UpdateTradePacket\", typeName: \"\", id: 0, branchId: 80, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Container Id",comment="name: \"Container Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Container Type",comment="name: \"Container Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerType\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Size",comment="name: \"Size\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Trade Tier",comment="name: \"Trade Tier\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="varint",comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Last Trading Player ID",comment="name: \"Last Trading Player ID\", typeName: \"ActorUniqueID\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Display Name",comment="name: \"Display Name\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Use New Trade UI",comment="name: \"Use New Trade UI\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="bool",comment="name: \"bool\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Using Economy Trade",comment="name: \"Using Economy Trade\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"When set to false, it means the packet comes from the old Trade Component.\""];
18 [label="bool",comment="name: \"bool\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Data Tags",comment="name: \"Data Tags\", typeName: \"CompoundTag\", id: 19, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
20 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14;16;18;20}

}

```

## 字段

```title='UpdateTradePacket'
[container_id][container_type][size][trade_tier][target_actor_id][last_trading_player_id][display_name][use_new_trade_ui][using_economy_trade][data_tags]
```

/// html | div.result
//// define
Container Id：<!-- md:samp byte -->

- <!-- md:samp byte -->类型枚举。枚举值如下：

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

- <!-- md:samp byte -->类型枚举。枚举值如下：

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
Size：<!-- md:samp varint -->

- <!-- md:samp varint -->类型。


////
//// define
Trade Tier：<!-- md:samp varint -->

- <!-- md:samp varint -->类型。


////
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- <!-- md:samp ActorUniqueID -->类型。


////
//// define
Last Trading Player ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- <!-- md:samp ActorUniqueID -->类型。


////
//// define
Display Name：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////
//// define
Use New Trade UI：<!-- md:samp bool -->

- <!-- md:samp bool -->类型。


////
//// define
Using Economy Trade：<!-- md:samp bool -->

- <!-- md:samp bool -->类型。When set to false, it means the packet comes from the old Trade Component.


////
//// define
Data Tags：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- <!-- md:samp CompoundTag -->类型。


////

///

