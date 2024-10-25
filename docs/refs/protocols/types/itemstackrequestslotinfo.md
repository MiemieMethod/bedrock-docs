# <!-- md:samp ItemStackRequestSlotInfo -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ItemStackRequestSlotInfo -->类型。该类型用于protocol.type.itemstackrequestslotinfo.description

## 结构

```viz
digraph "ItemStackRequestSlotInfo" {
rankdir = LR
99
99 -> 100
100 -> 101
99 -> 102
102 -> 103
99 -> 104
104 -> 105

99 [label="ItemStackRequestSlotInfo",comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 99, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
100 [label="Full container name.",comment="name: \"Full container name.\", typeName: \"FullContainerName\", id: 100, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
101 [label="FullContainerName",comment="name: \"FullContainerName\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
102 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
103 [label="byte",comment="name: \"byte\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
104 [label="Raw Id (32 bit signed)",comment="name: \"Raw Id (32 bit signed)\", typeName: \"\", id: 104, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
105 [label="varint",comment="name: \"varint\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;101;103;105}

}

```

## 字段

```title='ItemStackRequestSlotInfo'
[full_container_name.][slot][raw_id]
```

/// html | div.result
//// define
Full container name.：[<!-- md:samp FullContainerName -->](../types/fullcontainername.md)

- 特殊类型。protocol.type.itemstackrequestslotinfo.full_container_name..description


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

