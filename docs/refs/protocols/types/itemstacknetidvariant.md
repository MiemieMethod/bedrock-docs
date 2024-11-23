# <!-- md:samp ItemStackNetIdVariant -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ItemStackNetIdVariant -->类型。该类型用于protocol.type.itemstacknetidvariant.description

## 结构

```viz
digraph "ItemStackNetIdVariant" {
rankdir = LR
37
37 -> 38
38 -> 39

37 [label="ItemStackNetIdVariant",comment="name: \"ItemStackNetIdVariant\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
38 [label="Raw Id (32 bit signed)",comment="name: \"Raw Id (32 bit signed)\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
39 [label="varint",comment="name: \"varint\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;39}

}

```

## 字段

```title='ItemStackNetIdVariant'
[raw_id]
```

/// html | div.result
//// define
Raw Id (32 bit signed)：<!-- md:samp varint -->

- 基本类型。protocol.type.itemstacknetidvariant.raw_id.description


////

///

