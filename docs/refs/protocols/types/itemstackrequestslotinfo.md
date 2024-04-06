# <!-- md:samp ItemStackRequestSlotInfo -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackRequestSlotInfo -->类型。

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

- <!-- md:samp byte -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`AnvilInputContainer`|`0`||
  |`AnvilMaterialContainer`|`1`||
  |`AnvilResultPreviewContainer`|`2`||
  |`SmithingTableInputContainer`|`3`||
  |`SmithingTableMaterialContainer`|`4`||
  |`SmithingTableResultPreviewContainer`|`5`||
  |`ArmorContainer`|`6`||
  |`LevelEntityContainer`|`7`||
  |`BeaconPaymentContainer`|`8`||
  |`BrewingStandInputContainer`|`9`||
  |`BrewingStandResultContainer`|`10`||
  |`BrewingStandFuelContainer`|`11`||
  |`CombinedHotbarAndInventoryContainer`|`12`||
  |`CraftingInputContainer`|`13`||
  |`CraftingOutputPreviewContainer`|`14`||
  |`RecipeConstructionContainer`|`15`||
  |`RecipeNatureContainer`|`16`||
  |`RecipeItemsContainer`|`17`||
  |`RecipeSearchContainer`|`18`||
  |`RecipeSearchBarContainer`|`19`||
  |`RecipeEquipmentContainer`|`20`||
  |`RecipeBookContainer`|`21`||
  |`EnchantingInputContainer`|`22`||
  |`EnchantingMaterialContainer`|`23`||
  |`FurnaceFuelContainer`|`24`||
  |`FurnaceIngredientContainer`|`25`||
  |`FurnaceResultContainer`|`26`||
  |`HorseEquipContainer`|`27`||
  |`HotbarContainer`|`28`||
  |`InventoryContainer`|`29`||
  |`ShulkerBoxContainer`|`30`||
  |`TradeIngredient1Container`|`31`||
  |`TradeIngredient2Container`|`32`||
  |`TradeResultPreviewContainer`|`33`||
  |`OffhandContainer`|`34`||
  |`CompoundCreatorInput`|`35`||
  |`CompoundCreatorOutputPreview`|`36`||
  |`ElementConstructorOutputPreview`|`37`||
  |`MaterialReducerInput`|`38`||
  |`MaterialReducerOutput`|`39`||
  |`LabTableInput`|`40`||
  |`LoomInputContainer`|`41`||
  |`LoomDyeContainer`|`42`||
  |`LoomMaterialContainer`|`43`||
  |`LoomResultPreviewContainer`|`44`||
  |`BlastFurnaceIngredientContainer`|`45`||
  |`SmokerIngredientContainer`|`46`||
  |`Trade2Ingredient1Container`|`47`||
  |`Trade2Ingredient2Container`|`48`||
  |`Trade2ResultPreviewContainer`|`49`||
  |`GrindstoneInputContainer`|`50`||
  |`GrindstoneAdditionalContainer`|`51`||
  |`GrindstoneResultPreviewContainer`|`52`||
  |`StonecutterInputContainer`|`53`||
  |`StonecutterResultPreviewContainer`|`54`||
  |`CartographyInputContainer`|`55`||
  |`CartographyAdditionalContainer`|`56`||
  |`CartographyResultPreviewContainer`|`57`||
  |`BarrelContainer`|`58`||
  |`CursorContainer`|`59`||
  |`CreatedOutputContainer`|`60`||
  |`SmithingTableTemplateContainer`|`61`||
  |`CrafterLevelEntityContainer`|`62`||



////
//// define
Slot：<!-- md:samp byte -->

- <!-- md:samp byte -->类型。


////
//// define
Raw Id (32 bit signed)：<!-- md:samp varint -->

- <!-- md:samp varint -->类型。


////

///

