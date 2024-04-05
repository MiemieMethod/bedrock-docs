# <!-- md:samp PlayerEnchantOptionsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerEnchantOptionsPacket -->数据包，数字ID是`146`。

## 结构

```viz
digraph PlayerEnchantOptionsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"unsigned varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		35	[comment="name: \"ItemEnchants\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ItemEnchants];
		37	[comment="name: \"string\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		39	[comment="name: \"TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 512, \
notes: \"\"",
			label="TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>"];
	}
	0	[comment="name: \"PlayerEnchantOptionsPacket\", typeName: \"\", id: 0, branchId: 146, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerEnchantOptionsPacket];
	1	[comment="name: \"Options\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Options];
	0 -> 1;
	2	[comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"Cost\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Cost];
	4 -> 5;
	7	[comment="name: \"Enchants\", typeName: \"ItemEnchants\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Enchants];
	4 -> 7;
	36	[comment="name: \"Enchant Name\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enchant Name"];
	4 -> 36;
	38	[comment="name: \"Enchant Net Id\", typeName: \"TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>\", id: 38, branchId: 0, recurseId: -1, \
attributes: 256, notes: \"\"",
		label="Enchant Net Id"];
	4 -> 38;
	5 -> 6;
	7 -> 35;
	36 -> 37;
	38 -> 39;
}

```

## 字段

/// define
PlayerEnchantOptionsPacket

Options

Options数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Options的示例元素

Cost：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Enchants：[<!-- md:samp ItemEnchants -->](refs/protocols/types/itemenchants.md)

- 类型：ItemEnchants。

Enchant Name：<!-- md:samp string -->

- 类型：string。

Enchant Net Id：[<!-- md:samp TypedServerNetId<struct RecipeNetIdTag,unsigned int,0> -->](refs/protocols/types/typedservernetid<struct_recipenetidtag,unsigned_int,0>.md)

- 类型：TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>。


///
