# <!-- md:samp PropertySyncData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PropertySyncData -->类型。

## 结构

```viz
digraph "PropertySyncData" {
rankdir = LR
61
61 -> 62
62 -> 63
63 -> 64
62 -> 65
65 -> 66
66 -> 67
65 -> 68
68 -> 69
61 -> 70
70 -> 71
71 -> 72
70 -> 73
73 -> 74
74 -> 75
73 -> 76
76 -> 77

61 [label="PropertySyncData",comment="name: \"PropertySyncData\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
62 [label="Int Entries List",comment="name: \"Int Entries List\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
63 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
64 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
65 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
66 [label="Property Index",comment="name: \"Property Index\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
67 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
68 [label="Data",comment="name: \"Data\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
69 [label="varint",comment="name: \"varint\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
70 [label="Float Entries List",comment="name: \"Float Entries List\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
71 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
72 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
73 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
74 [label="Property Index",comment="name: \"Property Index\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
75 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
76 [label="Data",comment="name: \"Data\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
77 [label="float",comment="name: \"float\", typeName: \"\", id: 77, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;64;67;69;72;75;77}

}

```

## 字段

```title='PropertySyncData'
[int_entries_list][float_entries_list]
```

/// html | div.result
```title='Int Entries List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 类型：<!-- md:samp unsigned varint -->。


/////
```title='示例元素'
[property_index][data]
```

///// html | div.result
////// define
Property Index：<!-- md:samp unsigned varint -->

- 类型：<!-- md:samp unsigned varint -->。


//////
////// define
Data：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。


//////

/////

////
```title='Float Entries List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 类型：<!-- md:samp unsigned varint -->。


/////
```title='示例元素'
[property_index][data]
```

///// html | div.result
////// define
Property Index：<!-- md:samp unsigned varint -->

- 类型：<!-- md:samp unsigned varint -->。


//////
////// define
Data：<!-- md:samp float -->

- 类型：<!-- md:samp float -->。


//////

/////

////

///

