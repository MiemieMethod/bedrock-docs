# <!-- md:samp TypedServerNetId<struct RecipeNetIdTag,unsigned int,0> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp TypedServerNetId<struct RecipeNetIdTag,unsigned int,0> -->类型。

## 结构

```dot
digraph "TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		57	[comment="name: \"unsigned varint\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
	}
	55	[comment="name: \"TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 0, \
notes: \"\"",
		label="TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>"];
	56	[comment="name: \"Raw Id (32 bit unsigned)\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Raw Id (32 bit unsigned)"];
	55 -> 56;
	56 -> 57;
}

```

## 字段

/// define
TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>

Raw Id (32 bit unsigned)：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


///
