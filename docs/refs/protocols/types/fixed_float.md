# <!-- md:samp fixed float -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp fixed float -->类型。该类型用于protocol.type.fixed_float.description

## 结构

```viz
digraph "Fixed Float" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="Fixed Float",comment="name: \"Fixed Float\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Modified float value",comment="name: \"Modified float value\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Float value multiplied by 32\""];
2 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='fixed float'
[modified_float_value]
```

/// html | div.result
//// define
Modified float value：<!-- md:samp varint64 -->

- 基本类型。protocol.type.fixed_float.modified_float_value.descriptionFloat value multiplied by 32


////

///

