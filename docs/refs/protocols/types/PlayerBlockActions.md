# <!-- md:samp PlayerBlockActions -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerBlockActions -->类型。

## 结构

```viz
digraph PlayerBlockActions {
	graph [rankdir=LR];
	{
		graph [rank=max];
		121	[comment="name: \"varint\", typeName: \"\", id: 121, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		158	[comment="name: \"PlayerBlockActionData\", typeName: \"\", id: 158, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=PlayerBlockActionData];
	}
	118	[comment="name: \"PlayerBlockActions\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerBlockActions];
	119	[comment="name: \"Player Block Actions\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Player Block Actions"];
	118 -> 119;
	120	[comment="name: \"Player Block Actions count\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player Block Actions count"];
	119 -> 120;
	122	[comment="name: \"example element\", typeName: \"\", id: 122, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	119 -> 122;
	120 -> 121;
	123	[comment="name: \"Player Block Action\", typeName: \"PlayerBlockActionData\", id: 123, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player Block Action"];
	122 -> 123;
	123 -> 158;
}

```

## 字段

/// define
PlayerBlockActions

Player Block Actions

Player Block Actions count：<!-- md:samp varint -->

- 类型：varint。

Player Block Actions的示例元素

Player Block Action：[<!-- md:samp PlayerBlockActionData -->](refs/protocols/types/playerblockactiondata.md)

- 类型：PlayerBlockActionData。


///
