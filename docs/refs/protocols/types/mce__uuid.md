# <!-- md:samp mce::UUID -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp mce::UUID -->类型。该类型用于protocol.type.mce::uuid.description

## 结构

```viz
digraph "mce::UUID" {
rankdir = LR
43
43 -> 44
44 -> 45
43 -> 46
46 -> 47

43 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
44 [label="Most Significant Bits",comment="name: \"Most Significant Bits\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
45 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
46 [label="Least Significant Bits",comment="name: \"Least Significant Bits\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
47 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;45;47}

}

```

## 字段

```title='mce::UUID'
[most_significant_bits][least_significant_bits]
```

/// html | div.result
//// define
Most Significant Bits：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.type.mce::uuid.most_significant_bits.description


////
//// define
Least Significant Bits：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.type.mce::uuid.least_significant_bits.description


////

///

