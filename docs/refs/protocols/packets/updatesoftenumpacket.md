# <!-- md:samp UpdateSoftEnumPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateSoftEnumPacket -->数据包，数字ID是`114`。

## 结构

```viz
digraph "UpdateSoftEnumPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
3 -> 6
6 -> 7
7 -> 8
0 -> 9
9 -> 10

0 [label="UpdateSoftEnumPacket",comment="name: \"UpdateSoftEnumPacket\", typeName: \"\", id: 0, branchId: 114, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Enum Name",comment="name: \"Enum Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Values",comment="name: \"Values\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Enum Value",comment="name: \"Enum Value\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Update Type",comment="name: \"Update Type\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SoftEnumUpdateType\""];
10 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8;10}

}

```

## 字段

```title='UpdateSoftEnumPacket'
[enum_name][values][update_type]
```

/// html | div.result
//// define
Enum Name：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
```title='Values'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 类型：<!-- md:samp unsigned varint -->。


/////
```title='示例元素'
[enum_value]
```

///// html | div.result
////// define
Enum Value：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


//////

/////

////
//// define
Update Type：<!-- md:samp unsigned int -->

- 类型：<!-- md:samp unsigned int -->。enumeration: SoftEnumUpdateType


////

///

