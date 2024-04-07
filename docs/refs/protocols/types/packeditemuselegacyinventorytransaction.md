# <!-- md:samp PackedItemUseLegacyInventoryTransaction -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PackedItemUseLegacyInventoryTransaction -->类型。

## 结构

```viz
digraph "PackedItemUseLegacyInventoryTransaction" {
rankdir = LR
32
32 -> 33
33 -> 37
32 -> 38
38 -> 39
39 -> 40
38 -> 41
41 -> 42
42 -> 43
43 -> 44
42 -> 45
45 -> 46
46 -> 47
45 -> 48
48 -> 49
49 -> 50
48 -> 51
51 -> 52
52 -> 53
32 -> 54
54 -> 55
55 -> 56
54 -> 57
57 -> 58
58 -> 59
32 -> 60
60 -> 61
32 -> 62
62 -> 63
32 -> 64
64 -> 65
32 -> 66
66 -> 67
32 -> 68
68 -> 69
32 -> 70
70 -> 71
32 -> 72
72 -> 73
32 -> 74
74 -> 75

32 [label="PackedItemUseLegacyInventoryTransaction",comment="name: \"PackedItemUseLegacyInventoryTransaction\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
33 [label="ID",comment="name: \"ID\", typeName: \"TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>\", id: 33, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
37 [label="TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>",comment="name: \"TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
38 [label="Dependency on 'valid ID'",shape=note,comment="name: \"Dependency on 'valid ID'\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
39 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
40 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 41, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
42 [label="Container Slots",comment="name: \"Container Slots\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
43 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
44 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
45 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
46 [label="Container Enum Name",comment="name: \"Container Enum Name\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerEnumName\""];
47 [label="byte",comment="name: \"byte\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
48 [label="Slots",comment="name: \"Slots\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
49 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
50 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
51 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
52 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
53 [label="byte",comment="name: \"byte\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
54 [label="Actions",comment="name: \"Actions\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
55 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
56 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
57 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
58 [label="Action",comment="name: \"Action\", typeName: \"InventoryAction\", id: 58, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
59 [label="InventoryAction",comment="name: \"InventoryAction\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
60 [label="Action Type",comment="name: \"Action Type\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ItemUseInventoryTransaction::ActionType\""];
61 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
62 [label="Position",comment="name: \"Position\", typeName: \"NetworkBlockPosition\", id: 62, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
63 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
64 [label="Face",comment="name: \"Face\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
65 [label="varint",comment="name: \"varint\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
66 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
67 [label="varint",comment="name: \"varint\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
68 [label="Item",comment="name: \"Item\", typeName: \"NetworkItemStackDescriptor\", id: 68, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
69 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
70 [label="From Position",comment="name: \"From Position\", typeName: \"Vec3\", id: 70, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
71 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
72 [label="Click Position",comment="name: \"Click Position\", typeName: \"Vec3\", id: 72, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
73 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
74 [label="Target Block Id",comment="name: \"Target Block Id\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
75 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;37;40;44;47;50;53;56;59;61;63;65;67;69;71;73;75}

}

```

## 字段

```title='PackedItemUseLegacyInventoryTransaction'
[id][dependency_on_valid_id][actions][action_type][position][face][slot][item][from_position][click_position][target_block_id]
```

/// html | div.result
//// define
ID：[<!-- md:samp TypedClientNetId&lt;struct ItemStackLegacyRequestIdTag,int,0&gt; -->](../types/typedclientnetid_struct_itemstacklegacyrequestidtag,int,0_.md)

- 特殊类型。


////
> 依赖于`valid ID`

///// tab | `valid ID`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据。


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

- 基本类型。


////////
```title='示例元素'
[container_enum_name][slots]
```

//////// html | div.result
///////// define
Container Enum Name：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

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



/////////
```title='Slots'
[array_size][[example_element]..]
```

///////// html | div.result
////////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。


//////////
```title='示例元素'
[slot]
```

////////// html | div.result
/////////// define
Slot：<!-- md:samp byte -->

- 基本类型。


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

- 基本类型。


/////
```title='示例元素'
[action]
```

///// html | div.result
////// define
Action：[<!-- md:samp InventoryAction -->](../types/inventoryaction.md)

- 特殊类型。


//////

/////

////
//// define
Action Type：<!-- md:samp unsigned varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Place`|`0`||
  |`Use`|`1`||
  |`Destroy`|`2`||



////
//// define
Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。


////
//// define
Face：<!-- md:samp varint -->

- 基本类型。


////
//// define
Slot：<!-- md:samp varint -->

- 基本类型。


////
//// define
Item：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。


////
//// define
From Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。


////
//// define
Click Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。


////
//// define
Target Block Id：<!-- md:samp unsigned varint -->

- 基本类型。


////

///

