# <!-- md:samp CodeBuilderSourcePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CodeBuilderSourcePacket -->数据包，数字ID是`178`。

## 结构

```viz
digraph "CodeBuilderSourcePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="CodeBuilderSourcePacket",comment="name: \"CodeBuilderSourcePacket\", typeName: \"\", id: 0, branchId: 178, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Operation",comment="name: \"Operation\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CodeBuilderStorageQueryOptions::Operation\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Category",comment="name: \"Category\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CodeBuilderStorageQueryOptions::Category\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Value",comment="name: \"Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='CodeBuilderSourcePacket'
[operation][category][value]
```

/// html | div.result
//// define
Operation：<!-- md:samp byte -->

- 类型：<!-- md:samp byte -->。enumeration: CodeBuilderStorageQueryOptions::Operation


////
//// define
Category：<!-- md:samp byte -->

- 类型：<!-- md:samp byte -->。enumeration: CodeBuilderStorageQueryOptions::Category


////
//// define
Value：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////

///

