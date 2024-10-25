# <!-- md:samp ContainerOpenPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ContainerOpenPacket -->数据包，数字ID是`46`。该数据包用于protocol.packet.containeropenpacket.description

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
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Container Type",comment="name: \"Container Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 基本类型枚举。protocol.packet.containeropenpacket.container_id.description枚举值如下：

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

- 基本类型枚举。protocol.packet.containeropenpacket.container_type.description枚举值如下：

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
Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.containeropenpacket.position.description


////
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.containeropenpacket.target_actor_id.description


////

///

