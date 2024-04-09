# <!-- md:samp ItemStackRequestSlotInfo -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackRequestSlotInfo -->类型。该类型用于protocol.type.itemstackrequestslotinfo.description

## 结构

```viz
digraph "ItemStackRequestSlotInfo" {
rankdir = LR
95
95 -> 96
96 -> 97
95 -> 98
98 -> 99
95 -> 100
100 -> 101

95 [label="ItemStackRequestSlotInfo",comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
96 [label="Open container net id",comment="name: \"Open container net id\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerEnumName\""];
97 [label="byte",comment="name: \"byte\", typeName: \"\", id: 97, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
98 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
99 [label="byte",comment="name: \"byte\", typeName: \"\", id: 99, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
100 [label="Raw Id (32 bit signed)",comment="name: \"Raw Id (32 bit signed)\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
101 [label="varint",comment="name: \"varint\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;97;99;101}

}

```

## 字段

```title='ItemStackRequestSlotInfo'
[open_container_net_id][slot][raw_id]
```

/// html | div.result
//// define
Open container net id：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.itemstackrequestslotinfo.open_container_net_id.description枚举值如下：

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



////
//// define
Slot：<!-- md:samp byte -->

- 基本类型。protocol.type.itemstackrequestslotinfo.slot.description


////
//// define
Raw Id (32 bit signed)：<!-- md:samp varint -->

- 基本类型。protocol.type.itemstackrequestslotinfo.raw_id.description


////

///

