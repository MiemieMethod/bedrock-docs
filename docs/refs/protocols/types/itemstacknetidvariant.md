# <!-- md:samp ItemStackNetIdVariant -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackNetIdVariant -->类型。

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

/// define
ItemStackNetIdVariant

Raw Id (32 bit signed)：<!-- md:samp varint -->

- 类型：varint。


///
