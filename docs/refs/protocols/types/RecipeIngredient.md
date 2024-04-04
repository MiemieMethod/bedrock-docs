# <!-- md:samp RecipeIngredient -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RecipeIngredient -->类型。

## 结构

```dot
digraph RecipeIngredient {
	graph [rankdir=LR];
	{
		graph [rank=max];
		16	[comment="name: \"byte\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		18	[comment="name: \"varint\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	14	[comment="name: \"RecipeIngredient\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=RecipeIngredient];
	15	[comment="name: \"InternalType\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ItemDescriptor::InternalType\"",
		label=InternalType];
	14 -> 15;
	17	[comment="name: \"StackSize\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=StackSize];
	14 -> 17;
	15 -> 16;
	17 -> 18;
}

```

## 字段

/// define
RecipeIngredient

InternalType：<!-- md:samp byte -->

- 类型：byte。enumeration: ItemDescriptor::InternalType

StackSize：<!-- md:samp varint -->

- 类型：varint。


///
