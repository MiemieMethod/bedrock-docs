# <!-- md:samp TypedServerNetId<struct ItemStackNetIdTag,int,0> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp TypedServerNetId<struct ItemStackNetIdTag,int,0> -->类型。

## 结构

```viz
digraph "TypedServerNetId<struct ItemStackNetIdTag,int,0>" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		36	[comment="name: \"varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	34	[comment="name: \"TypedServerNetId<struct ItemStackNetIdTag,int,0>\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="TypedServerNetId<struct ItemStackNetIdTag,int,0>"];
	35	[comment="name: \"Raw Id (32 bit signed)\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Raw Id (32 bit signed)"];
	34 -> 35;
	35 -> 36;
}

```

## 字段

/// define
TypedServerNetId<struct ItemStackNetIdTag,int,0>

Raw Id (32 bit signed)：<!-- md:samp varint -->

- 类型：varint。


///
