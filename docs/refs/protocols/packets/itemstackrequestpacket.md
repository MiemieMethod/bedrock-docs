# <!-- md:samp ItemStackRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackRequestPacket -->数据包，数字ID是`147`。该数据包用于protocol.packet.itemstackrequestpacket.description

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

- 基本类型。protocol.packet.itemstackrequestpacket.数组大小.description


/////
```title='示例元素'
[client_request_id][actions][strings_to_filter][stringstofilterorigin]
```

///// html | div.result
////// define
Client Request Id：[<!-- md:samp TypedClientNetId&lt;struct ItemStackRequestIdTag,int,0&gt; -->](../types/typedclientnetid_struct_itemstackrequestidtag,int,0_.md)

- 特殊类型。protocol.packet.itemstackrequestpacket.client_request_id.description


//////
```title='Actions'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.itemstackrequestpacket.数组大小.description


///////
```title='示例元素'
[action_type][amount][source][destination]
```

/////// html | div.result
//////// define
Action type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.itemstackrequestpacket.action_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Take`|`0`|protocol.enum.take|
  |`Place`|`1`|protocol.enum.place|
  |`Swap`|`2`|protocol.enum.swap|
  |`Drop`|`3`|protocol.enum.drop|
  |`Destroy`|`4`|protocol.enum.destroy|
  |`Consume`|`5`|protocol.enum.consume|
  |`Create`|`6`|protocol.enum.create|
  |`PlaceInItemContainer`|`7`|protocol.enum.placeinitemcontainer|
  |`TakeFromItemContainer`|`8`|protocol.enum.takefromitemcontainer|
  |`ScreenLabTableCombine`|`9`|protocol.enum.screenlabtablecombine|
  |`ScreenBeaconPayment`|`10`|protocol.enum.screenbeaconpayment|
  |`ScreenHUDMineBlock`|`11`|protocol.enum.screenhudmineblock|
  |`CraftRecipe`|`12`|protocol.enum.craftrecipe|
  |`CraftRecipeAuto`|`13`|protocol.enum.craftrecipeauto|
  |`CraftCreative`|`14`|protocol.enum.craftcreative|
  |`CraftRecipeOptional`|`15`|protocol.enum.craftrecipeoptional|
  |`CraftRepairAndDisenchant`|`16`|protocol.enum.craftrepairanddisenchant|
  |`CraftLoom`|`17`|protocol.enum.craftloom|
  |`CraftNonImplemented_DEPRECATEDASKTYLAING`|`18`|protocol.enum.craftnonimplemented_deprecatedasktylaing|
  |`CraftResults_DEPRECATEDASKTYLAING`|`19`|protocol.enum.craftresults_deprecatedasktylaing|
  |`ifdef`|`20`|protocol.enum.ifdef|
  |`TEST_INFRASTRUCTURE_ENABLED`|`21`|protocol.enum.test_infrastructure_enabled|
  |`Test`|`22`|protocol.enum.test|
  |`endif`|`23`|protocol.enum.endif|



////////
//////// define
Amount：<!-- md:samp byte -->

- 基本类型。protocol.packet.itemstackrequestpacket.amount.description


////////
//////// define
Source：[<!-- md:samp ItemStackRequestSlotInfo -->](../types/itemstackrequestslotinfo.md)

- 特殊类型。protocol.packet.itemstackrequestpacket.source.description


////////
//////// define
Destination：[<!-- md:samp ItemStackRequestSlotInfo -->](../types/itemstackrequestslotinfo.md)

- 特殊类型。protocol.packet.itemstackrequestpacket.destination.description


////////

///////

//////
```title='Strings To Filter'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.itemstackrequestpacket.数组大小.description


///////
```title='示例元素'
[string_to_filter]
```

/////// html | div.result
//////// define
String To Filter：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.itemstackrequestpacket.string_to_filter.descriptionIndivdiual string that needs checking


////////

///////

//////
////// define
StringsToFilterOrigin：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.itemstackrequestpacket.stringstofilterorigin.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`unknown`|`-1`|protocol.enum.unknown|
  |`ServerChatPublic`|`0`|protocol.enum.serverchatpublic|
  |`ServerChatWhisper`|`1`|protocol.enum.serverchatwhisper|
  |`SignText`|`2`|protocol.enum.signtext|
  |`AnvilText`|`3`|protocol.enum.anviltext|
  |`BookAndQuillText`|`4`|protocol.enum.bookandquilltext|
  |`CommandBlockText`|`5`|protocol.enum.commandblocktext|
  |`BlockActorDataText`|`6`|protocol.enum.blockactordatatext|
  |`JoinEventText`|`7`|protocol.enum.joineventtext|
  |`LeaveEventText`|`8`|protocol.enum.leaveeventtext|
  |`SlashCommandChat`|`9`|protocol.enum.slashcommandchat|
  |`CartographyText`|`10`|protocol.enum.cartographytext|
  |`KickCommand`|`11`|protocol.enum.kickcommand|
  |`TitleCommand`|`12`|protocol.enum.titlecommand|
  |`SummonCommand`|`13`|protocol.enum.summoncommand|
  |`ServerForm`|`14`|protocol.enum.serverform|
  |`COUNT`|`15`|protocol.enum.count|



//////

/////

////

///

