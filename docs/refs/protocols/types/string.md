# <!-- md:samp string -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp string -->类型。该类型用于protocol.type.string.description

## 结构

```viz
digraph "String" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6

0 [label="String",comment="name: \"String\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Byte Array",comment="name: \"Byte Array\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="String Data",comment="name: \"String Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6}

}

```

## 字段

```title='string'
[byte_array]
```

/// html | div.result
```title='Byte Array'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.string.byte_array.array_size.description


/////
```title='示例元素'
[string_data]
```

///// html | div.result
////// define
String Data：<!-- md:samp byte -->

- 基本类型。protocol.type.string.byte_array.example_element.string_data.description


//////

/////

////

///

