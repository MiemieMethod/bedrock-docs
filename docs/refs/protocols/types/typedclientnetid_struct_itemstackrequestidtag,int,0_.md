# <!-- md:samp TypedClientNetId&lt;struct ItemStackRequestIdTag,int,0&gt; -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp TypedClientNetId&lt;struct ItemStackRequestIdTag,int,0&gt; -->类型。该类型用于protocol.type.typedclientnetid&lt;struct_itemstackrequestidtag,int,0&gt;.description

## 结构

```viz
digraph "TypedClientNetId<struct ItemStackRequestIdTag,int,0>" {
rankdir = LR
82
82 -> 83
83 -> 84

82 [label="TypedClientNetId<struct ItemStackRequestIdTag,int,0>",comment="name: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
83 [label="Raw Id (32 bit signed)",comment="name: \"Raw Id (32 bit signed)\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
84 [label="varint",comment="name: \"varint\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;84}

}

```

## 字段

```title='TypedClientNetId&lt;struct ItemStackRequestIdTag,int,0&gt;'
[raw_id]
```

/// html | div.result
//// define
Raw Id (32 bit signed)：<!-- md:samp varint -->

- 基本类型。protocol.type.typedclientnetid&lt;struct_itemstackrequestidtag,int,0&gt;.raw_id.description


////

///

