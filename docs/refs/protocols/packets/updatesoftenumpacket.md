# <!-- md:samp UpdateSoftEnumPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp UpdateSoftEnumPacket -->数据包，数字ID是`114`。该数据包用于protocol.packet.updatesoftenumpacket.description

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
9 [label="Update Type",comment="name: \"Update Type\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="byte",comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8;10}

}

```

## 字段

```title='UpdateSoftEnumPacket'
[enum_name][values][update_type]
```

/// html | div.result
//// define
Enum Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.updatesoftenumpacket.enum_name.description


////
```title='Values'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.updatesoftenumpacket.values.array_size.description


/////
```title='示例元素'
[enum_value]
```

///// html | div.result
////// define
Enum Value：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.updatesoftenumpacket.values.example_element.enum_value.description


//////

/////

////
//// define
Update Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.updatesoftenumpacket.update_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Add`|`0`|protocol.enum.add|
  |`Remove`|`1`|protocol.enum.remove|
  |`Replace`|`2`|protocol.enum.replace|



////

///

