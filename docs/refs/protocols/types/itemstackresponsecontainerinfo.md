# <!-- md:samp ItemStackResponseContainerInfo -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ItemStackResponseContainerInfo -->类型。该类型用于protocol.type.itemstackresponsecontainerinfo.description

## 结构

```viz
digraph "ItemStackResponseContainerInfo" {
rankdir = LR
18
18 -> 19
19 -> 20
18 -> 21
21 -> 22
22 -> 23
21 -> 24
24 -> 25
25 -> 42

18 [label="ItemStackResponseContainerInfo",comment="name: \"ItemStackResponseContainerInfo\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
19 [label="Full Container Name",comment="name: \"Full Container Name\", typeName: \"FullContainerName\", id: 19, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
20 [label="FullContainerName",comment="name: \"FullContainerName\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Slots",comment="name: \"Slots\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
22 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
23 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
24 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
25 [label="Slot Info",comment="name: \"Slot Info\", typeName: \"ItemStackResponseSlotInfo\", id: 25, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
42 [label="ItemStackResponseSlotInfo",comment="name: \"ItemStackResponseSlotInfo\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;20;23;42}

}

```

## 字段

```title='ItemStackResponseContainerInfo'
[full_container_name][slots]
```

/// html | div.result
//// define
Full Container Name：[<!-- md:samp FullContainerName -->](../types/fullcontainername.md)

- 特殊类型。protocol.type.itemstackresponsecontainerinfo.full_container_name.description


////
```title='Slots'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.itemstackresponsecontainerinfo.slots.array_size.description


/////
```title='示例元素'
[slot_info]
```

///// html | div.result
////// define
Slot Info：[<!-- md:samp ItemStackResponseSlotInfo -->](../types/itemstackresponseslotinfo.md)

- 特殊类型。protocol.type.itemstackresponsecontainerinfo.slots.example_element.slot_info.description


//////

/////

////

///

