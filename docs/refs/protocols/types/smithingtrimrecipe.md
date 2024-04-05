# <!-- md:samp SmithingTrimRecipe -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SmithingTrimRecipe -->类型。

## 结构

```viz
digraph SmithingTrimRecipe {
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
		16	[comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	6	[comment="name: \"SmithingTrimRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=SmithingTrimRecipe];
	7	[comment="name: \"Recipe Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Recipe Id"];
	6 -> 7;
	9	[comment="name: \"Template Ingredient\", typeName: \"RecipeIngredient\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Template Ingredient"];
	6 -> 9;
	11	[comment="name: \"Base Ingredient\", typeName: \"RecipeIngredient\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Base Ingredient"];
	6 -> 11;
	13	[comment="name: \"Addition Ingredient\", typeName: \"RecipeIngredient\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Addition Ingredient"];
	6 -> 13;
	15	[comment="name: \"Tag\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Tag];
	6 -> 15;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
}

```

## 字段

/// define
SmithingTrimRecipe

Recipe Id：<!-- md:samp string -->

- 类型：string。

Template Ingredient：[<!-- md:samp RecipeIngredient -->](refs/protocols/types/recipeingredient.md)

- 类型：RecipeIngredient。

Base Ingredient：[<!-- md:samp RecipeIngredient -->](refs/protocols/types/recipeingredient.md)

- 类型：RecipeIngredient。

Addition Ingredient：[<!-- md:samp RecipeIngredient -->](refs/protocols/types/recipeingredient.md)

- 类型：RecipeIngredient。

Tag：<!-- md:samp string -->

- 类型：string。


///
