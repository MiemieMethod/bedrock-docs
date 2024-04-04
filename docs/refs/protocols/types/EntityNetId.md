# <!-- md:samp EntityNetId -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EntityNetId -->类型。

## 结构

```dot
digraph EntityNetId {
	graph [rankdir=LR];
	{
		graph [rank=max];
		4	[comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
	}
	2	[comment="name: \"EntityNetId\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=EntityNetId];
	3	[comment="name: \"Raw Entity Id\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Raw Entity Id"];
	2 -> 3;
	3 -> 4;
}

```

## 字段

/// define
EntityNetId

Raw Entity Id：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


///
