# <!-- md:samp MaterialReducerDataEntry -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp MaterialReducerDataEntry -->类型。该类型用于protocol.type.materialreducerdataentry.description

## 结构

```viz
digraph "MaterialReducerDataEntry" {
rankdir = LR
44
44 -> 45
45 -> 46
44 -> 47
47 -> 48
48 -> 49
47 -> 50
50 -> 51
51 -> 52
50 -> 53
53 -> 54

44 [label="MaterialReducerDataEntry",comment="name: \"MaterialReducerDataEntry\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
45 [label="From Item (Key): Input",comment="name: \"From Item (Key): Input\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
46 [label="varint",comment="name: \"varint\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
47 [label="Item Ids and Counts",comment="name: \"Item Ids and Counts\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
48 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
49 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
50 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
51 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
52 [label="varint",comment="name: \"varint\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
53 [label="Item Count",comment="name: \"Item Count\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
54 [label="varint",comment="name: \"varint\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;46;49;52;54}

}

```

## 字段

```title='MaterialReducerDataEntry'
[from_item:_input][item_ids_and_counts]
```

/// html | div.result
//// define
From Item (Key): Input：<!-- md:samp varint -->

- 基本类型。protocol.type.materialreducerdataentry.from_item:_input.description


////
```title='Item Ids and Counts'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.materialreducerdataentry.数组大小.description


/////
```title='示例元素'
[item_id][item_count]
```

///// html | div.result
////// define
Item Id：<!-- md:samp varint -->

- 基本类型。protocol.type.materialreducerdataentry.item_id.description


//////
////// define
Item Count：<!-- md:samp varint -->

- 基本类型。protocol.type.materialreducerdataentry.item_count.description


//////

/////

////

///

