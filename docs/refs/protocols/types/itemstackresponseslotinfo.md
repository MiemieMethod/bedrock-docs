# <!-- md:samp ItemStackResponseSlotInfo -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ItemStackResponseSlotInfo -->类型。该类型用于protocol.type.itemstackresponseslotinfo.description

## 结构

```viz
digraph "ItemStackResponseSlotInfo" {
rankdir = LR
26
26 -> 27
27 -> 28
26 -> 29
29 -> 30
26 -> 31
31 -> 32
26 -> 33
33 -> 37
26 -> 38
38 -> 39
26 -> 40
40 -> 41

26 [label="ItemStackResponseSlotInfo",comment="name: \"ItemStackResponseSlotInfo\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
27 [label="Requested slot",comment="name: \"Requested slot\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
28 [label="byte",comment="name: \"byte\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
29 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
30 [label="byte",comment="name: \"byte\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="Amount",comment="name: \"Amount\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="byte",comment="name: \"byte\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Item Stack Net Id",comment="name: \"Item Stack Net Id\", typeName: \"TypedServerNetId<struct ItemStackNetIdTag,int,0>\", id: 33, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
37 [label="TypedServerNetId<struct ItemStackNetIdTag,int,0>",comment="name: \"TypedServerNetId<struct ItemStackNetIdTag,int,0>\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
38 [label="Custom Name",comment="name: \"Custom Name\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 0, notes: \"Allows you to filter for profanity on the server and return the updated name\""];
39 [label="string",comment="name: \"string\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
40 [label="Durability Correction",comment="name: \"Durability Correction\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
41 [label="varint",comment="name: \"varint\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;28;30;32;37;39;41}

}

```

## 字段

```title='ItemStackResponseSlotInfo'
[requested_slot][slot][amount][item_stack_net_id][custom_name][durability_correction]
```

/// html | div.result
//// define
Requested slot：<!-- md:samp byte -->

- 基本类型。protocol.type.itemstackresponseslotinfo.requested_slot.description


////
//// define
Slot：<!-- md:samp byte -->

- 基本类型。protocol.type.itemstackresponseslotinfo.slot.description


////
//// define
Amount：<!-- md:samp byte -->

- 基本类型。protocol.type.itemstackresponseslotinfo.amount.description


////
//// define
Item Stack Net Id：[<!-- md:samp TypedServerNetId&lt;struct ItemStackNetIdTag,int,0&gt; -->](../types/typedservernetid_struct_itemstacknetidtag,int,0_.md)

- 特殊类型。protocol.type.itemstackresponseslotinfo.item_stack_net_id.description


////
//// define
Custom Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.itemstackresponseslotinfo.custom_name.descriptionAllows you to filter for profanity on the server and return the updated 'name'


////
//// define
Durability Correction：<!-- md:samp varint -->

- 基本类型。protocol.type.itemstackresponseslotinfo.durability_correction.description


////

///

