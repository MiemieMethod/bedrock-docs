# <!-- md:samp ItemStackResponseInfo -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ItemStackResponseInfo -->类型。该类型用于protocol.type.itemstackresponseinfo.description

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
7 [label="Result",comment="name: \"Result\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 基本类型枚举。protocol.type.itemstackresponseinfo.result.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Success`|`0`|protocol.enum.success|
  |`Error`|`1`|protocol.enum.error|
  |`InvalidRequestActionType`|`2`|protocol.enum.invalidrequestactiontype|
  |`ActionRequestNotAllowed`|`3`|protocol.enum.actionrequestnotallowed|
  |`ScreenHandlerEndRequestFailed`|`4`|protocol.enum.screenhandlerendrequestfailed|
  |`ItemRequestActionHandlerCommitFailed`|`5`|protocol.enum.itemrequestactionhandlercommitfailed|
  |`InvalidRequestCraftActionType`|`6`|protocol.enum.invalidrequestcraftactiontype|
  |`InvalidCraftRequest`|`7`|protocol.enum.invalidcraftrequest|
  |`InvalidCraftRequestScreen`|`8`|protocol.enum.invalidcraftrequestscreen|
  |`InvalidCraftResult`|`9`|protocol.enum.invalidcraftresult|
  |`InvalidCraftResultIndex`|`10`|protocol.enum.invalidcraftresultindex|
  |`InvalidCraftResultItem`|`11`|protocol.enum.invalidcraftresultitem|
  |`InvalidItemNetId`|`12`|protocol.enum.invaliditemnetid|
  |`MissingCreatedOutputContainer`|`13`|protocol.enum.missingcreatedoutputcontainer|
  |`FailedToSetCreatedItemOutputSlot`|`14`|protocol.enum.failedtosetcreateditemoutputslot|
  |`RequestAlreadyInProgress`|`15`|protocol.enum.requestalreadyinprogress|
  |`FailedToInitSparseContainer`|`16`|protocol.enum.failedtoinitsparsecontainer|
  |`ResultTransferFailed`|`17`|protocol.enum.resulttransferfailed|
  |`ExpectedItemSlotNotFullyConsumed`|`18`|protocol.enum.expecteditemslotnotfullyconsumed|
  |`ExpectedAnywhereItemNotFullyConsumed`|`19`|protocol.enum.expectedanywhereitemnotfullyconsumed|
  |`ItemAlreadyConsumedFromSlot`|`20`|protocol.enum.itemalreadyconsumedfromslot|
  |`ConsumedTooMuchFromSlot`|`21`|protocol.enum.consumedtoomuchfromslot|
  |`MismatchSlotExpectedConsumedItem`|`22`|protocol.enum.mismatchslotexpectedconsumeditem|
  |`MismatchSlotExpectedConsumedItemNetIdVariant`|`23`|protocol.enum.mismatchslotexpectedconsumeditemnetidvariant|
  |`FailedToMatchExpectedSlotConsumedItem`|`24`|protocol.enum.failedtomatchexpectedslotconsumeditem|
  |`FailedToMatchExpectedAllowedAnywhereConsumedItem`|`25`|protocol.enum.failedtomatchexpectedallowedanywhereconsumeditem|
  |`ConsumedItemOutOfAllowedSlotRange`|`26`|protocol.enum.consumeditemoutofallowedslotrange|
  |`ConsumedItemNotAllowed`|`27`|protocol.enum.consumeditemnotallowed|
  |`PlayerNotInCreativeMode`|`28`|protocol.enum.playernotincreativemode|
  |`InvalidExperimentalRecipeRequest`|`29`|protocol.enum.invalidexperimentalreciperequest|
  |`FailedToCraftCreative`|`30`|protocol.enum.failedtocraftcreative|
  |`FailedToGetLevelRecipe`|`31`|protocol.enum.failedtogetlevelrecipe|
  |`FailedToFindRecipeByNetId`|`32`|protocol.enum.failedtofindrecipebynetid|
  |`MismatchedCraftingSize`|`33`|protocol.enum.mismatchedcraftingsize|
  |`MissingInputSparseContainer`|`34`|protocol.enum.missinginputsparsecontainer|
  |`MismatchedRecipeForInputGridItems`|`35`|protocol.enum.mismatchedrecipeforinputgriditems|
  |`EmptyCraftResults`|`36`|protocol.enum.emptycraftresults|
  |`FailedToEnchant`|`37`|protocol.enum.failedtoenchant|
  |`MissingInputItem`|`38`|protocol.enum.missinginputitem|
  |`InsufficientPlayerLevelToEnchant`|`39`|protocol.enum.insufficientplayerleveltoenchant|
  |`MissingMaterialItem`|`40`|protocol.enum.missingmaterialitem|
  |`MissingActor`|`41`|protocol.enum.missingactor|
  |`UnknownPrimaryEffect`|`42`|protocol.enum.unknownprimaryeffect|
  |`PrimaryEffectOutOfRange`|`43`|protocol.enum.primaryeffectoutofrange|
  |`PrimaryEffectUnavailable`|`44`|protocol.enum.primaryeffectunavailable|
  |`SecondaryEffectOutOfRange`|`45`|protocol.enum.secondaryeffectoutofrange|
  |`SecondaryEffectUnavailable`|`46`|protocol.enum.secondaryeffectunavailable|
  |`DstContainerEqualToCreatedOutputContainer`|`47`|protocol.enum.dstcontainerequaltocreatedoutputcontainer|
  |`DstContainerAndSlotEqualToSrcContainerAndSlot`|`48`|protocol.enum.dstcontainerandslotequaltosrccontainerandslot|
  |`FailedToValidateSrcSlot`|`49`|protocol.enum.failedtovalidatesrcslot|
  |`FailedToValidateDstSlot`|`50`|protocol.enum.failedtovalidatedstslot|
  |`InvalidAdjustedAmount`|`51`|protocol.enum.invalidadjustedamount|
  |`InvalidItemSetType`|`52`|protocol.enum.invaliditemsettype|
  |`InvalidTransferAmount`|`53`|protocol.enum.invalidtransferamount|
  |`CannotSwapItem`|`54`|protocol.enum.cannotswapitem|
  |`CannotPlaceItem`|`55`|protocol.enum.cannotplaceitem|
  |`UnhandledItemSetType`|`56`|protocol.enum.unhandleditemsettype|
  |`InvalidRemovedAmount`|`57`|protocol.enum.invalidremovedamount|
  |`InvalidRegion`|`58`|protocol.enum.invalidregion|
  |`CannotDropItem`|`59`|protocol.enum.cannotdropitem|
  |`CannotDestroyItem`|`60`|protocol.enum.cannotdestroyitem|
  |`InvalidSourceContainer`|`61`|protocol.enum.invalidsourcecontainer|
  |`ItemNotConsumed`|`62`|protocol.enum.itemnotconsumed|
  |`InvalidNumCrafts`|`63`|protocol.enum.invalidnumcrafts|
  |`InvalidCraftResultStackSize`|`64`|protocol.enum.invalidcraftresultstacksize|
  |`CannotRemoveItem`|`65`|protocol.enum.cannotremoveitem|
  |`CannotConsumeItem`|`66`|protocol.enum.cannotconsumeitem|
  |`ScreenStackError`|`67`|protocol.enum.screenstackerror|



////
//// define
Client Request Id：[<!-- md:samp TypedClientNetId&lt;struct ItemStackRequestIdTag,int,0&gt; -->](../types/typedclientnetid_struct_itemstackrequestidtag,int,0_.md)

- 特殊类型。protocol.type.itemstackresponseinfo.client_request_id.description


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

- 基本类型。protocol.type.itemstackresponseinfo.dependency_on_itemstacknetresult.if_0.containers.array_size.description


////////
```title='示例元素'
[container_info]
```

//////// html | div.result
///////// define
Container Info：[<!-- md:samp ItemStackResponseContainerInfo -->](../types/itemstackresponsecontainerinfo.md)

- 特殊类型。protocol.type.itemstackresponseinfo.dependency_on_itemstacknetresult.if_0.containers.example_element.container_info.description


/////////

////////

///////

//////

/////

///// tab | `ItemStackNetResult`如果为`1`
////// define
if (1)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///

