# <!-- md:samp ShapedRecipe -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShapedRecipe -->类型。

## 结构

```viz
digraph ShapedRecipe {
	graph [rankdir=LR];
	{
		graph [rank=max];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		11	[comment="name: \"varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		13	[comment="name: \"varint\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		17	[comment="name: \"RecipeIngredient\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=RecipeIngredient];
		20	[comment="name: \"unsigned varint\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		23	[comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemInstanceDescriptor];
		25	[comment="name: \"mce::UUID\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="mce::UUID"];
		27	[comment="name: \"string\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		29	[comment="name: \"varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	6	[comment="name: \"ShapedRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ShapedRecipe];
	7	[comment="name: \"Recipe Unique Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Recipe Unique Id"];
	6 -> 7;
	9	[comment="name: \"Ingredient Grid\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Ingredient Grid"];
	6 -> 9;
	18	[comment="name: \"Production List\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Production List"];
	6 -> 18;
	24	[comment="name: \"Recipe ID\", typeName: \"mce::UUID\", id: 24, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Recipe ID"];
	6 -> 24;
	26	[comment="name: \"Recipe Tag\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"Available ones: CARTOGRAPHY_TABLE, \
CRAFTING_TABLE, SMITHING_TABLE, STONECUTTER, FURNACE_TAG, BLAST_FURNACE_TAG, SMOKER_TAG, CAMPFIRE_TAG, SOUL_CAMPFIRE_TAG\"",
		label="Recipe Tag"];
	6 -> 26;
	28	[comment="name: \"Priority\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Priority];
	6 -> 28;
	7 -> 8;
	14	[comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	9 -> 14;
	15	[comment="name: \"example element\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	9 -> 15;
	10	[comment="name: \"Recipe Width\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Recipe Width"];
	14 -> 10;
	12	[comment="name: \"Recipe Height\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Recipe Height"];
	14 -> 12;
	10 -> 11;
	12 -> 13;
	16	[comment="name: \"Ingredient\", typeName: \"RecipeIngredient\", id: 16, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Ingredient];
	15 -> 16;
	16 -> 17;
	19	[comment="name: \"Array Size\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	18 -> 19;
	21	[comment="name: \"example element\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	18 -> 21;
	19 -> 20;
	22	[comment="name: \"Produced Item\", typeName: \"NetworkItemInstanceDescriptor\", id: 22, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Produced Item"];
	21 -> 22;
	22 -> 23;
	24 -> 25;
	26 -> 27;
	28 -> 29;
}

```

## 字段

/// define
ShapedRecipe

Recipe Unique Id：<!-- md:samp string -->

- 类型：string。

Ingredient Grid

Ingredient Grid数组的大小

Recipe Width：<!-- md:samp varint -->

- 类型：varint。

Recipe Height：<!-- md:samp varint -->

- 类型：varint。

Ingredient Grid的示例元素

Ingredient：[<!-- md:samp RecipeIngredient -->](refs/protocols/types/recipeingredient.md)

- 类型：RecipeIngredient。

Production List

Production List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Production List的示例元素

Produced Item：[<!-- md:samp NetworkItemInstanceDescriptor -->](refs/protocols/types/networkiteminstancedescriptor.md)

- 类型：NetworkItemInstanceDescriptor。

Recipe ID：[<!-- md:samp mce::UUID -->](refs/protocols/types/mce::uuid.md)

- 类型：mce::UUID。

Recipe Tag：<!-- md:samp string -->

- 类型：string。Available ones: CARTOGRAPHY_TABLE, CRAFTING_TABLE, SMITHING_TABLE, STONECUTTER, FURNACE_TAG, BLAST_FURNACE_TAG, SMOKER_TAG, CAMPFIRE_TAG, SOUL_CAMPFIRE_TAG

Priority：<!-- md:samp varint -->

- 类型：varint。


///
