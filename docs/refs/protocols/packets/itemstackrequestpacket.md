# <!-- md:samp ItemStackRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackRequestPacket -->数据包，数字ID是`147`。

## 结构

```viz
digraph "ItemStackRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6
4 -> 7
7 -> 8
8 -> 9
7 -> 10
10 -> 11
11 -> 12
10 -> 13
13 -> 14
10 -> 15
15 -> 16
10 -> 17
17 -> 18
4 -> 19
19 -> 20
20 -> 21
19 -> 22
22 -> 23
23 -> 24
4 -> 25
25 -> 26

0 [label="ItemStackRequestPacket",comment="name: \"ItemStackRequestPacket\", typeName: \"\", id: 0, branchId: 147, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Requests",comment="name: \"Requests\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Client Request Id",comment="name: \"Client Request Id\", typeName: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="TypedClientNetId<struct ItemStackRequestIdTag,int,0>",comment="name: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Actions",comment="name: \"Actions\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"There are a variety of possible actions each with their own schema; this (Take) is just one example. Refer to the Item Stack Net Manager documentation.\""];
8 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="Action type",comment="name: \"Action type\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ItemStackRequestActionType\""];
12 [label="byte",comment="name: \"byte\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Amount",comment="name: \"Amount\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="byte",comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Source",comment="name: \"Source\", typeName: \"ItemStackRequestSlotInfo\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
16 [label="ItemStackRequestSlotInfo",comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Destination",comment="name: \"Destination\", typeName: \"ItemStackRequestSlotInfo\", id: 17, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
18 [label="ItemStackRequestSlotInfo",comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Strings To Filter",comment="name: \"Strings To Filter\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 8, notes: \"Array of strings to submit to profanity filtering service\""];
20 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
23 [label="String To Filter",comment="name: \"String To Filter\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"Indivdiual string that needs checking\""];
24 [label="string",comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="StringsToFilterOrigin",comment="name: \"StringsToFilterOrigin\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: TextProcessingEventOrigin\""];
26 [label="int",comment="name: \"int\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6;9;12;14;16;18;21;24;26}

}

```

## 字段

```title='ItemStackRequestPacket'
[requests]
```

/// html | div.result
```title='Requests'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


/////
```title='示例元素'
[client_request_id][actions][strings_to_filter][stringstofilterorigin]
```

///// html | div.result
////// define
Client Request Id：[<!-- md:samp TypedClientNetId&lt;struct ItemStackRequestIdTag,int,0&gt; -->](../types/typedclientnetid_struct_itemstackrequestidtag,int,0_.md)

- <!-- md:samp TypedClientNetId&lt;struct ItemStackRequestIdTag,int,0&gt; -->类型。


//////
```title='Actions'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


///////
```title='示例元素'
[action_type][amount][source][destination]
```

/////// html | div.result
//////// define
Action type：<!-- md:samp byte -->

- <!-- md:samp byte -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Take`|`0`||
  |`Place`|`1`||
  |`Swap`|`2`||
  |`Drop`|`3`||
  |`Destroy`|`4`||
  |`Consume`|`5`||
  |`Create`|`6`||
  |`PlaceInItemContainer`|`7`||
  |`TakeFromItemContainer`|`8`||
  |`ScreenLabTableCombine`|`9`||
  |`ScreenBeaconPayment`|`10`||
  |`ScreenHUDMineBlock`|`11`||
  |`CraftRecipe`|`12`||
  |`CraftRecipeAuto`|`13`||
  |`CraftCreative`|`14`||
  |`CraftRecipeOptional`|`15`||
  |`CraftRepairAndDisenchant`|`16`||
  |`CraftLoom`|`17`||
  |`CraftNonImplemented_DEPRECATEDASKTYLAING`|`18`||
  |`CraftResults_DEPRECATEDASKTYLAING`|`19`||
  |`ifdef`|`20`||
  |`TEST_INFRASTRUCTURE_ENABLED`|`21`||
  |`Test`|`22`||
  |`endif`|`23`||



////////
//////// define
Amount：<!-- md:samp byte -->

- <!-- md:samp byte -->类型。


////////
//////// define
Source：[<!-- md:samp ItemStackRequestSlotInfo -->](../types/itemstackrequestslotinfo.md)

- <!-- md:samp ItemStackRequestSlotInfo -->类型。


////////
//////// define
Destination：[<!-- md:samp ItemStackRequestSlotInfo -->](../types/itemstackrequestslotinfo.md)

- <!-- md:samp ItemStackRequestSlotInfo -->类型。


////////

///////

//////
```title='Strings To Filter'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


///////
```title='示例元素'
[string_to_filter]
```

/////// html | div.result
//////// define
String To Filter：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。Indivdiual string that needs checking


////////

///////

//////
////// define
StringsToFilterOrigin：<!-- md:samp int -->

- <!-- md:samp int -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`unknown`|`-1`||
  |`ServerChatPublic`|`0`||
  |`ServerChatWhisper`|`1`||
  |`SignText`|`2`||
  |`AnvilText`|`3`||
  |`BookAndQuillText`|`4`||
  |`CommandBlockText`|`5`||
  |`BlockActorDataText`|`6`||
  |`JoinEventText`|`7`||
  |`LeaveEventText`|`8`||
  |`SlashCommandChat`|`9`||
  |`CartographyText`|`10`||
  |`KickCommand`|`11`||
  |`TitleCommand`|`12`||
  |`SummonCommand`|`13`||
  |`ServerForm`|`14`||
  |`COUNT`|`15`||



//////

/////

////

///

