# <!-- md:samp String -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp String -->类型。

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

/// define
String

Byte Array

//// define
Byte Array数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Byte Array的示例元素

String Data：<!-- md:samp byte -->

- 类型：byte。


////



///
