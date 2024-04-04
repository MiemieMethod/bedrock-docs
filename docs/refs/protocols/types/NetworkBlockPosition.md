# <!-- md:samp NetworkBlockPosition -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkBlockPosition -->类型。

## 结构

```dot
digraph NetworkBlockPosition {
	graph [rankdir=LR];
	{
		graph [rank=max];
		44	[comment="name: \"varint\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		46	[comment="name: \"unsigned varint\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		48	[comment="name: \"varint\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	42	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=NetworkBlockPosition];
	43	[comment="name: \"X\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=X];
	42 -> 43;
	45	[comment="name: \"Y\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Y];
	42 -> 45;
	47	[comment="name: \"Z\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Z];
	42 -> 47;
	43 -> 44;
	45 -> 46;
	47 -> 48;
}

```

## 字段

/// define
NetworkBlockPosition

X：<!-- md:samp varint -->

- 类型：varint。

Y：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Z：<!-- md:samp varint -->

- 类型：varint。


///
