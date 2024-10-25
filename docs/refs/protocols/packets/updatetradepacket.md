# <!-- md:samp UpdateTradePacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp UpdateTradePacket -->数据包，数字ID是`80`。该数据包用于protocol.packet.updatetradepacket.description

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
1 [label="Container Id",comment="name: \"Container Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Container Type",comment="name: \"Container Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 基本类型枚举。protocol.packet.updatetradepacket.container_id.description枚举值如下：

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
Container Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.updatetradepacket.container_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NONE`|`-9`|无|
  |`INVENTORY`|`-1`|protocol.enum.inventory|
  |`CONTAINER`|`0`|protocol.enum.container|
  |`WORKBENCH`|`1`|protocol.enum.workbench|
  |`FURNACE`|`2`|protocol.enum.furnace|
  |`ENCHANTMENT`|`3`|protocol.enum.enchantment|
  |`BREWING_STAND`|`4`|protocol.enum.brewing_stand|
  |`ANVIL`|`5`|protocol.enum.anvil|
  |`DISPENSER`|`6`|protocol.enum.dispenser|
  |`DROPPER`|`7`|protocol.enum.dropper|
  |`HOPPER`|`8`|protocol.enum.hopper|
  |`CAULDRON`|`9`|protocol.enum.cauldron|
  |`MINECART_CHEST`|`10`|protocol.enum.minecart_chest|
  |`MINECART_HOPPER`|`11`|protocol.enum.minecart_hopper|
  |`HORSE`|`12`|protocol.enum.horse|
  |`BEACON`|`13`|protocol.enum.beacon|
  |`STRUCTURE_EDITOR`|`14`|protocol.enum.structure_editor|
  |`TRADE`|`15`|protocol.enum.trade|
  |`COMMAND_BLOCK`|`16`|protocol.enum.command_block|
  |`JUKEBOX`|`17`|protocol.enum.jukebox|
  |`ARMOR`|`18`|protocol.enum.armor|
  |`HAND`|`19`|protocol.enum.hand|
  |`COMPOUND_CREATOR`|`20`|protocol.enum.compound_creator|
  |`ELEMENT_CONSTRUCTOR`|`21`|protocol.enum.element_constructor|
  |`MATERIAL_REDUCER`|`22`|protocol.enum.material_reducer|
  |`LAB_TABLE`|`23`|protocol.enum.lab_table|
  |`LOOM`|`24`|protocol.enum.loom|
  |`LECTERN`|`25`|protocol.enum.lectern|
  |`GRINDSTONE`|`26`|protocol.enum.grindstone|
  |`BLAST_FURNACE`|`27`|protocol.enum.blast_furnace|
  |`SMOKER`|`28`|protocol.enum.smoker|
  |`STONECUTTER`|`29`|protocol.enum.stonecutter|
  |`CARTOGRAPHY`|`30`|protocol.enum.cartography|
  |`HUD`|`31`|protocol.enum.hud|
  |`JIGSAW_EDITOR`|`32`|protocol.enum.jigsaw_editor|
  |`SMITHING_TABLE`|`33`|protocol.enum.smithing_table|
  |`CHEST_BOAT`|`34`|protocol.enum.chest_boat|
  |`DECORATED_POT`|`35`|protocol.enum.decorated_pot|
  |`CRAFTER`|`36`|protocol.enum.crafter|



////
//// define
Size：<!-- md:samp varint -->

- 基本类型。protocol.packet.updatetradepacket.size.description


////
//// define
Trade Tier：<!-- md:samp varint -->

- 基本类型。protocol.packet.updatetradepacket.trade_tier.description


////
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.updatetradepacket.target_actor_id.description


////
//// define
Last Trading Player ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.updatetradepacket.last_trading_player_id.description


////
//// define
Display Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.updatetradepacket.display_name.description


////
//// define
Use New Trade UI：<!-- md:samp bool -->

- 基本类型。protocol.packet.updatetradepacket.use_new_trade_ui.description


////
//// define
Using Economy Trade：<!-- md:samp bool -->

- 基本类型。protocol.packet.updatetradepacket.using_economy_trade.descriptionWhen set to false, it means the packet comes from the old Trade Component.


////
//// define
Data Tags：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.updatetradepacket.data_tags.description


////

///

