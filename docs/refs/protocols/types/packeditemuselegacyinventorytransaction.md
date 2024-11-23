# <!-- md:samp PackedItemUseLegacyInventoryTransaction -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp PackedItemUseLegacyInventoryTransaction -->类型。该类型用于protocol.type.packeditemuselegacyinventorytransaction.description

## 结构

```viz
digraph "PackedItemUseLegacyInventoryTransaction" {
rankdir = LR
28
28 -> 29
29 -> 33
28 -> 34
34 -> 35
35 -> 36
34 -> 37
37 -> 38
38 -> 39
39 -> 40
38 -> 41
41 -> 42
42 -> 43
41 -> 44
44 -> 45
45 -> 46
44 -> 47
47 -> 48
48 -> 49
28 -> 50
50 -> 51
51 -> 52
50 -> 53
53 -> 54
54 -> 55
28 -> 56
56 -> 57
28 -> 58
58 -> 59
28 -> 60
60 -> 61
28 -> 62
62 -> 63
28 -> 64
64 -> 65
28 -> 66
66 -> 67
28 -> 68
68 -> 69
28 -> 70
70 -> 71
28 -> 72
72 -> 73
28 -> 74
74 -> 75

28 [label="PackedItemUseLegacyInventoryTransaction",comment="name: \"PackedItemUseLegacyInventoryTransaction\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="ID",comment="name: \"ID\", typeName: \"TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>\", id: 29, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
33 [label="TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>",comment="name: \"TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
34 [label="Dependency on 'valid ID'",shape=note,comment="name: \"Dependency on 'valid ID'\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
35 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
36 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 37, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
38 [label="Container Slots",comment="name: \"Container Slots\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
39 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
40 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
42 [label="Container Enum Name",comment="name: \"Container Enum Name\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
43 [label="byte",comment="name: \"byte\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
44 [label="Slots",comment="name: \"Slots\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
45 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
46 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
47 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
48 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
49 [label="byte",comment="name: \"byte\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
50 [label="Actions",comment="name: \"Actions\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
51 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
52 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
53 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
54 [label="Action",comment="name: \"Action\", typeName: \"InventoryAction\", id: 54, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
55 [label="InventoryAction",comment="name: \"InventoryAction\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
56 [label="Action Type",comment="name: \"Action Type\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
57 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
58 [label="Trigger Type",comment="name: \"Trigger Type\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 0, notes: \"PlayerInput if it's a direct result from a player's initial button input,		SimulationTick if the player is holding down the input button started from a previous tick.\""];
59 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
60 [label="Position",comment="name: \"Position\", typeName: \"NetworkBlockPosition\", id: 60, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
61 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
62 [label="Face",comment="name: \"Face\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
63 [label="varint",comment="name: \"varint\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
64 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
65 [label="varint",comment="name: \"varint\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
66 [label="Item",comment="name: \"Item\", typeName: \"NetworkItemStackDescriptor\", id: 66, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
67 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
68 [label="From Position",comment="name: \"From Position\", typeName: \"Vec3\", id: 68, branchId: 0, recurseId: -1, attributes: 256, notes: \"Where the player thinks they are when sending this\""];
69 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
70 [label="Click Position",comment="name: \"Click Position\", typeName: \"Vec3\", id: 70, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
71 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
72 [label="Target Block Id",comment="name: \"Target Block Id\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
73 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
74 [label="Client Interact Prediction",comment="name: \"Client Interact Prediction\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
75 [label="byte",comment="name: \"byte\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;33;36;40;43;46;49;52;55;57;59;61;63;65;67;69;71;73;75}

}

```

## 字段

```title='PackedItemUseLegacyInventoryTransaction'
[id][dependency_on_valid_id][actions][action_type][trigger_type][position][face][slot][item][from_position][click_position][target_block_id][client_interact_prediction]
```

/// html | div.result
//// define
ID：[<!-- md:samp TypedClientNetId&lt;struct ItemStackLegacyRequestIdTag,int,0&gt; -->](../types/typedclientnetid_struct_itemstacklegacyrequestidtag,int,0_.md)

- 特殊类型。protocol.type.packeditemuselegacyinventorytransaction.id.description


////
> 依赖于`valid ID`

///// tab | `valid ID`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `valid ID`如果为`1`
```title='if (1)'
[container_slots]
```

////// html | div.result
```title='Container Slots'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.packeditemuselegacyinventorytransaction.dependency_on_valid_id.if_1.container_slots.array_size.description


////////
```title='示例元素'
[container_enum_name][slots]
```

//////// html | div.result
///////// define
Container Enum Name：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.packeditemuselegacyinventorytransaction.dependency_on_valid_id.if_1.container_slots.example_element.container_enum_name.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`AnvilInputContainer`|`0`|protocol.enum.anvilinputcontainer|
  |`AnvilMaterialContainer`|`1`|protocol.enum.anvilmaterialcontainer|
  |`AnvilResultPreviewContainer`|`2`|protocol.enum.anvilresultpreviewcontainer|
  |`SmithingTableInputContainer`|`3`|protocol.enum.smithingtableinputcontainer|
  |`SmithingTableMaterialContainer`|`4`|protocol.enum.smithingtablematerialcontainer|
  |`SmithingTableResultPreviewContainer`|`5`|protocol.enum.smithingtableresultpreviewcontainer|
  |`ArmorContainer`|`6`|protocol.enum.armorcontainer|
  |`LevelEntityContainer`|`7`|protocol.enum.levelentitycontainer|
  |`BeaconPaymentContainer`|`8`|protocol.enum.beaconpaymentcontainer|
  |`BrewingStandInputContainer`|`9`|protocol.enum.brewingstandinputcontainer|
  |`BrewingStandResultContainer`|`10`|protocol.enum.brewingstandresultcontainer|
  |`BrewingStandFuelContainer`|`11`|protocol.enum.brewingstandfuelcontainer|
  |`CombinedHotbarAndInventoryContainer`|`12`|protocol.enum.combinedhotbarandinventorycontainer|
  |`CraftingInputContainer`|`13`|protocol.enum.craftinginputcontainer|
  |`CraftingOutputPreviewContainer`|`14`|protocol.enum.craftingoutputpreviewcontainer|
  |`RecipeConstructionContainer`|`15`|protocol.enum.recipeconstructioncontainer|
  |`RecipeNatureContainer`|`16`|protocol.enum.recipenaturecontainer|
  |`RecipeItemsContainer`|`17`|protocol.enum.recipeitemscontainer|
  |`RecipeSearchContainer`|`18`|protocol.enum.recipesearchcontainer|
  |`RecipeSearchBarContainer`|`19`|protocol.enum.recipesearchbarcontainer|
  |`RecipeEquipmentContainer`|`20`|protocol.enum.recipeequipmentcontainer|
  |`RecipeBookContainer`|`21`|protocol.enum.recipebookcontainer|
  |`EnchantingInputContainer`|`22`|protocol.enum.enchantinginputcontainer|
  |`EnchantingMaterialContainer`|`23`|protocol.enum.enchantingmaterialcontainer|
  |`FurnaceFuelContainer`|`24`|protocol.enum.furnacefuelcontainer|
  |`FurnaceIngredientContainer`|`25`|protocol.enum.furnaceingredientcontainer|
  |`FurnaceResultContainer`|`26`|protocol.enum.furnaceresultcontainer|
  |`HorseEquipContainer`|`27`|protocol.enum.horseequipcontainer|
  |`HotbarContainer`|`28`|protocol.enum.hotbarcontainer|
  |`InventoryContainer`|`29`|protocol.enum.inventorycontainer|
  |`ShulkerBoxContainer`|`30`|protocol.enum.shulkerboxcontainer|
  |`TradeIngredient1Container`|`31`|protocol.enum.tradeingredient1container|
  |`TradeIngredient2Container`|`32`|protocol.enum.tradeingredient2container|
  |`TradeResultPreviewContainer`|`33`|protocol.enum.traderesultpreviewcontainer|
  |`OffhandContainer`|`34`|protocol.enum.offhandcontainer|
  |`CompoundCreatorInput`|`35`|protocol.enum.compoundcreatorinput|
  |`CompoundCreatorOutputPreview`|`36`|protocol.enum.compoundcreatoroutputpreview|
  |`ElementConstructorOutputPreview`|`37`|protocol.enum.elementconstructoroutputpreview|
  |`MaterialReducerInput`|`38`|protocol.enum.materialreducerinput|
  |`MaterialReducerOutput`|`39`|protocol.enum.materialreduceroutput|
  |`LabTableInput`|`40`|protocol.enum.labtableinput|
  |`LoomInputContainer`|`41`|protocol.enum.loominputcontainer|
  |`LoomDyeContainer`|`42`|protocol.enum.loomdyecontainer|
  |`LoomMaterialContainer`|`43`|protocol.enum.loommaterialcontainer|
  |`LoomResultPreviewContainer`|`44`|protocol.enum.loomresultpreviewcontainer|
  |`BlastFurnaceIngredientContainer`|`45`|protocol.enum.blastfurnaceingredientcontainer|
  |`SmokerIngredientContainer`|`46`|protocol.enum.smokeringredientcontainer|
  |`Trade2Ingredient1Container`|`47`|protocol.enum.trade2ingredient1container|
  |`Trade2Ingredient2Container`|`48`|protocol.enum.trade2ingredient2container|
  |`Trade2ResultPreviewContainer`|`49`|protocol.enum.trade2resultpreviewcontainer|
  |`GrindstoneInputContainer`|`50`|protocol.enum.grindstoneinputcontainer|
  |`GrindstoneAdditionalContainer`|`51`|protocol.enum.grindstoneadditionalcontainer|
  |`GrindstoneResultPreviewContainer`|`52`|protocol.enum.grindstoneresultpreviewcontainer|
  |`StonecutterInputContainer`|`53`|protocol.enum.stonecutterinputcontainer|
  |`StonecutterResultPreviewContainer`|`54`|protocol.enum.stonecutterresultpreviewcontainer|
  |`CartographyInputContainer`|`55`|protocol.enum.cartographyinputcontainer|
  |`CartographyAdditionalContainer`|`56`|protocol.enum.cartographyadditionalcontainer|
  |`CartographyResultPreviewContainer`|`57`|protocol.enum.cartographyresultpreviewcontainer|
  |`BarrelContainer`|`58`|protocol.enum.barrelcontainer|
  |`CursorContainer`|`59`|protocol.enum.cursorcontainer|
  |`CreatedOutputContainer`|`60`|protocol.enum.createdoutputcontainer|
  |`SmithingTableTemplateContainer`|`61`|protocol.enum.smithingtabletemplatecontainer|
  |`CrafterLevelEntityContainer`|`62`|protocol.enum.crafterlevelentitycontainer|
  |`DynamicContainer`|`63`|protocol.enum.dynamiccontainer|



/////////
```title='Slots'
[array_size][[example_element]..]
```

///////// html | div.result
////////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.packeditemuselegacyinventorytransaction.dependency_on_valid_id.if_1.container_slots.example_element.slots.array_size.description


//////////
```title='示例元素'
[slot]
```

////////// html | div.result
/////////// define
Slot：<!-- md:samp byte -->

- 基本类型。protocol.type.packeditemuselegacyinventorytransaction.dependency_on_valid_id.if_1.container_slots.example_element.slots.example_element.slot.description


///////////

//////////

/////////

////////

///////

//////

/////
```title='Actions'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.packeditemuselegacyinventorytransaction.actions.array_size.description


/////
```title='示例元素'
[action]
```

///// html | div.result
////// define
Action：[<!-- md:samp InventoryAction -->](../types/inventoryaction.md)

- 特殊类型。protocol.type.packeditemuselegacyinventorytransaction.actions.example_element.action.description


//////

/////

////
//// define
Action Type：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.type.packeditemuselegacyinventorytransaction.action_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Place`|`0`|protocol.enum.place|
  |`Use`|`1`|protocol.enum.use|
  |`Destroy`|`2`|protocol.enum.destroy|



////
//// define
Trigger Type：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.type.packeditemuselegacyinventorytransaction.trigger_type.descriptionPlayerInput if it's a direct result from a player's initial button input,		SimulationTick if the player is holding down the input button started from a previous tick.枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`0`|protocol.enum.unknown|
  |`PlayerInput`|`1`|protocol.enum.playerinput|
  |`SimulationTick`|`2`|protocol.enum.simulationtick|



////
//// define
Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.type.packeditemuselegacyinventorytransaction.position.description


////
//// define
Face：<!-- md:samp varint -->

- 基本类型。protocol.type.packeditemuselegacyinventorytransaction.face.description


////
//// define
Slot：<!-- md:samp varint -->

- 基本类型。protocol.type.packeditemuselegacyinventorytransaction.slot.description


////
//// define
Item：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.type.packeditemuselegacyinventorytransaction.item.description


////
//// define
From Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.type.packeditemuselegacyinventorytransaction.from_position.descriptionWhere the player thinks they are when sending this


////
//// define
Click Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.type.packeditemuselegacyinventorytransaction.click_position.description


////
//// define
Target Block Id：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.packeditemuselegacyinventorytransaction.target_block_id.description


////
//// define
Client Interact Prediction：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.packeditemuselegacyinventorytransaction.client_interact_prediction.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Failure`|`0`|protocol.enum.failure|
  |`Success`|`1`|protocol.enum.success|



////

///

