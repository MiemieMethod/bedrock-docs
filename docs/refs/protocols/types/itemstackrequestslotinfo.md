# <!-- md:samp ItemStackRequestSlotInfo -->

> 文档版本：r/20_u8<br/>协议版本：671

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
96 [label="Open container net id",comment="name: \"Open container net id\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 基本类型。protocol.type.itemstackrequestslotinfo.open_container_net_id.description


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

