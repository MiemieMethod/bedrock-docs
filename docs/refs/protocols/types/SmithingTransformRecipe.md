# <!-- md:samp SmithingTransformRecipe -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SmithingTransformRecipe -->类型。

## 结构

```dot
digraph SmithingTransformRecipe {
	graph [rankdir=LR];
	{
		graph [rank=max];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"RecipeIngredient\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=RecipeIngredient];
		12	[comment="name: \"RecipeIngredient\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=RecipeIngredient];
		14	[comment="name: \"RecipeIngredient\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=RecipeIngredient];
		16	[comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemInstanceDescriptor];
		18	[comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	6	[comment="name: \"SmithingTransformRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=SmithingTransformRecipe];
	7	[comment="name: \"Recipe Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Recipe Id"];
	6 -> 7;
	9	[comment="name: \"Template Ingredien\", typeName: \"RecipeIngredient\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Template Ingredien"];
	6 -> 9;
	11	[comment="name: \"Base Ingredien\", typeName: \"RecipeIngredient\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Base Ingredien"];
	6 -> 11;
	13	[comment="name: \"Addition Ingredien\", typeName: \"RecipeIngredient\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Addition Ingredien"];
	6 -> 13;
	15	[comment="name: \"Result\", typeName: \"NetworkItemInstanceDescriptor\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Result];
	6 -> 15;
	17	[comment="name: \"Tag\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Tag];
	6 -> 17;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	17 -> 18;
}

```

## 字段

/// define
SmithingTransformRecipe

Recipe Id：<!-- md:samp string -->

- 类型：string。

Template Ingredien：[<!-- md:samp RecipeIngredient -->](refs/protocols/types/RecipeIngredient.md)

- 类型：RecipeIngredient。

Base Ingredien：[<!-- md:samp RecipeIngredient -->](refs/protocols/types/RecipeIngredient.md)

- 类型：RecipeIngredient。

Addition Ingredien：[<!-- md:samp RecipeIngredient -->](refs/protocols/types/RecipeIngredient.md)

- 类型：RecipeIngredient。

Result：[<!-- md:samp NetworkItemInstanceDescriptor -->](refs/protocols/types/NetworkItemInstanceDescriptor.md)

- 类型：NetworkItemInstanceDescriptor。

Tag：<!-- md:samp string -->

- 类型：string。


///
