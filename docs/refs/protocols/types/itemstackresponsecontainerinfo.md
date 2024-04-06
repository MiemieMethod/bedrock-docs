# <!-- md:samp ItemStackResponseContainerInfo -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackResponseContainerInfo -->类型。

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
19 [label="Open Container Net Id",comment="name: \"Open Container Net Id\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="byte",comment="name: \"byte\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
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
[open_container_net_id][slots]
```

/// html | div.result
//// define
Open Container Net Id：<!-- md:samp byte -->

- 基本类型。


////
```title='Slots'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。


/////
```title='示例元素'
[slot_info]
```

///// html | div.result
////// define
Slot Info：[<!-- md:samp ItemStackResponseSlotInfo -->](../types/itemstackresponseslotinfo.md)

- 特殊类型。


//////

/////

////

///

