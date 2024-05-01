# <!-- md:samp TrimDataPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp TrimDataPacket -->数据包，数字ID是`302`。该数据包用于protocol.packet.trimdatapacket.description

## 结构

```viz
digraph "TrimDataPacket" {
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
0 -> 9
9 -> 10
10 -> 11
9 -> 12
12 -> 13
13 -> 14
12 -> 15
15 -> 16
12 -> 17
17 -> 18

0 [label="TrimDataPacket",comment="name: \"TrimDataPacket\", typeName: \"\", id: 0, branchId: 302, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="TrimPattern List",comment="name: \"TrimPattern List\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Item Name",comment="name: \"Item Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Pattern Id",comment="name: \"Pattern Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="TrimMaterial List",comment="name: \"TrimMaterial List\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
10 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
13 [label="Material Id",comment="name: \"Material Id\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Color",comment="name: \"Color\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="string",comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Item Name",comment="name: \"Item Name\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="string",comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6;8;11;14;16;18}

}

```

## 字段

```title='TrimDataPacket'
[trimpattern_list][trimmaterial_list]
```

/// html | div.result
```title='TrimPattern List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.trimdatapacket.数组大小.description


/////
```title='示例元素'
[item_name][pattern_id]
```

///// html | div.result
////// define
Item Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.trimdatapacket.item_name.description


//////
////// define
Pattern Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.trimdatapacket.pattern_id.description


//////

/////

////
```title='TrimMaterial List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.trimdatapacket.数组大小.description


/////
```title='示例元素'
[material_id][color][item_name]
```

///// html | div.result
////// define
Material Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.trimdatapacket.material_id.description


//////
////// define
Color：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.trimdatapacket.color.description


//////
////// define
Item Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.trimdatapacket.item_name.description


//////

/////

////

///

