# <!-- md:samp ItemStackResponseInfo -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackResponseInfo -->类型。

## 结构

```viz
digraph "ItemStackResponseInfo" {
rankdir = LR
6
6 -> 7
7 -> 8
6 -> 9
9 -> 10
6 -> 11
11 -> 12
12 -> 13
13 -> 14
14 -> 15
13 -> 16
16 -> 17
17 -> 43
11 -> 44
44 -> 45

6 [label="ItemStackResponseInfo",comment="name: \"ItemStackResponseInfo\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="Result",comment="name: \"Result\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ItemStackNetResult\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Client Request Id",comment="name: \"Client Request Id\", typeName: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="TypedClientNetId<struct ItemStackRequestIdTag,int,0>",comment="name: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Dependency on 'ItemStackNetResult'",shape=note,comment="name: \"Dependency on 'ItemStackNetResult'\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
12 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
13 [label="Containers",comment="name: \"Containers\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
14 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
17 [label="Container Info",comment="name: \"Container Info\", typeName: \"ItemStackResponseContainerInfo\", id: 17, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
43 [label="ItemStackResponseContainerInfo",comment="name: \"ItemStackResponseContainerInfo\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
44 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 44, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
45 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;8;10;15;43;45}

}

```

## 字段

```title='ItemStackResponseInfo'
[result][client_request_id][dependency_on_itemstacknetresult]
```

/// html | div.result
//// define
Result：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Success`|`0`||
  |`Error`|`1`||
  |`InvalidRequestActionType`|`2`||
  |`ActionRequestNotAllowed`|`3`||
  |`ScreenHandlerEndRequestFailed`|`4`||
  |`ItemRequestActionHandlerCommitFailed`|`5`||
  |`InvalidRequestCraftActionType`|`6`||
  |`InvalidCraftRequest`|`7`||
  |`InvalidCraftRequestScreen`|`8`||
  |`InvalidCraftResult`|`9`||
  |`InvalidCraftResultIndex`|`10`||
  |`InvalidCraftResultItem`|`11`||
  |`InvalidItemNetId`|`12`||
  |`MissingCreatedOutputContainer`|`13`||
  |`FailedToSetCreatedItemOutputSlot`|`14`||
  |`RequestAlreadyInProgress`|`15`||
  |`FailedToInitSparseContainer`|`16`||
  |`ResultTransferFailed`|`17`||
  |`ExpectedItemSlotNotFullyConsumed`|`18`||
  |`ExpectedAnywhereItemNotFullyConsumed`|`19`||
  |`ItemAlreadyConsumedFromSlot`|`20`||
  |`ConsumedTooMuchFromSlot`|`21`||
  |`MismatchSlotExpectedConsumedItem`|`22`||
  |`MismatchSlotExpectedConsumedItemNetIdVariant`|`23`||
  |`FailedToMatchExpectedSlotConsumedItem`|`24`||
  |`FailedToMatchExpectedAllowedAnywhereConsumedItem`|`25`||
  |`ConsumedItemOutOfAllowedSlotRange`|`26`||
  |`ConsumedItemNotAllowed`|`27`||
  |`PlayerNotInCreativeMode`|`28`||
  |`InvalidExperimentalRecipeRequest`|`29`||
  |`FailedToCraftCreative`|`30`||
  |`FailedToGetLevelRecipe`|`31`||
  |`FailedToFindRecipeByNetId`|`32`||
  |`MismatchedCraftingSize`|`33`||
  |`MissingInputSparseContainer`|`34`||
  |`MismatchedRecipeForInputGridItems`|`35`||
  |`EmptyCraftResults`|`36`||
  |`FailedToEnchant`|`37`||
  |`MissingInputItem`|`38`||
  |`InsufficientPlayerLevelToEnchant`|`39`||
  |`MissingMaterialItem`|`40`||
  |`MissingActor`|`41`||
  |`UnknownPrimaryEffect`|`42`||
  |`PrimaryEffectOutOfRange`|`43`||
  |`PrimaryEffectUnavailable`|`44`||
  |`SecondaryEffectOutOfRange`|`45`||
  |`SecondaryEffectUnavailable`|`46`||
  |`DstContainerEqualToCreatedOutputContainer`|`47`||
  |`DstContainerAndSlotEqualToSrcContainerAndSlot`|`48`||
  |`FailedToValidateSrcSlot`|`49`||
  |`FailedToValidateDstSlot`|`50`||
  |`InvalidAdjustedAmount`|`51`||
  |`InvalidItemSetType`|`52`||
  |`InvalidTransferAmount`|`53`||
  |`CannotSwapItem`|`54`||
  |`CannotPlaceItem`|`55`||
  |`UnhandledItemSetType`|`56`||
  |`InvalidRemovedAmount`|`57`||
  |`InvalidRegion`|`58`||
  |`CannotDropItem`|`59`||
  |`CannotDestroyItem`|`60`||
  |`InvalidSourceContainer`|`61`||
  |`ItemNotConsumed`|`62`||
  |`InvalidNumCrafts`|`63`||
  |`InvalidCraftResultStackSize`|`64`||
  |`CannotRemoveItem`|`65`||
  |`CannotConsumeItem`|`66`||
  |`ScreenStackError`|`67`||



////
//// define
Client Request Id：[<!-- md:samp TypedClientNetId&lt;struct ItemStackRequestIdTag,int,0&gt; -->](../types/typedclientnetid_struct_itemstackrequestidtag,int,0_.md)

- 特殊类型。


////
> 依赖于`ItemStackNetResult`

///// tab | `ItemStackNetResult`如果为`0`
```title='if (0)'
[containers]
```

////// html | div.result
```title='Containers'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。


////////
```title='示例元素'
[container_info]
```

//////// html | div.result
///////// define
Container Info：[<!-- md:samp ItemStackResponseContainerInfo -->](../types/itemstackresponsecontainerinfo.md)

- 特殊类型。


/////////

////////

///////

//////

/////

///// tab | `ItemStackNetResult`如果为`1`
////// define
if (1)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///

