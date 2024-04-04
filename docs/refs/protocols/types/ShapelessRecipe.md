# <!-- md:samp ShapelessRecipe -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShapelessRecipe -->类型。

## 结构

```viz
digraph ShapelessRecipe {
	graph [rankdir=LR];
	{
		graph [rank=max];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		11	[comment="name: \"unsigned varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		19	[comment="name: \"RecipeIngredient\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=RecipeIngredient];
		22	[comment="name: \"unsigned varint\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		41	[comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemInstanceDescriptor];
		48	[comment="name: \"mce::UUID\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="mce::UUID"];
		50	[comment="name: \"string\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		52	[comment="name: \"varint\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	6	[comment="name: \"ShapelessRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ShapelessRecipe];
	7	[comment="name: \"Recipe Unique Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Recipe Unique Id"];
	6 -> 7;
	9	[comment="name: \"Ingredient List\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Ingredient List"];
	6 -> 9;
	20	[comment="name: \"Production List\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Production List"];
	6 -> 20;
	42	[comment="name: \"Recipe ID\", typeName: \"mce::UUID\", id: 42, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Recipe ID"];
	6 -> 42;
	49	[comment="name: \"Recipe Tag\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 0, notes: \"Available ones: CARTOGRAPHY_TABLE, \
CRAFTING_TABLE, SMITHING_TABLE, STONECUTTER, FURNACE_TAG, BLAST_FURNACE_TAG, SMOKER_TAG, CAMPFIRE_TAG, SOUL_CAMPFIRE_TAG\"",
		label="Recipe Tag"];
	6 -> 49;
	51	[comment="name: \"Priority\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Priority];
	6 -> 51;
	7 -> 8;
	10	[comment="name: \"Array Size\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	9 -> 10;
	12	[comment="name: \"example element\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	9 -> 12;
	10 -> 11;
	13	[comment="name: \"Ingredient\", typeName: \"RecipeIngredient\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Ingredient];
	12 -> 13;
	13 -> 19;
	21	[comment="name: \"Array Size\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	20 -> 21;
	23	[comment="name: \"example element\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	20 -> 23;
	21 -> 22;
	24	[comment="name: \"Produced Item\", typeName: \"NetworkItemInstanceDescriptor\", id: 24, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Produced Item"];
	23 -> 24;
	24 -> 41;
	42 -> 48;
	49 -> 50;
	51 -> 52;
}

```

## 字段

/// define
ShapelessRecipe

Recipe Unique Id：<!-- md:samp string -->

- 类型：string。

Ingredient List

Ingredient List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Ingredient List的示例元素

Ingredient：[<!-- md:samp RecipeIngredient -->](refs/protocols/types/RecipeIngredient.md)

- 类型：RecipeIngredient。

Production List

Production List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Production List的示例元素

Produced Item：[<!-- md:samp NetworkItemInstanceDescriptor -->](refs/protocols/types/NetworkItemInstanceDescriptor.md)

- 类型：NetworkItemInstanceDescriptor。

Recipe ID：[<!-- md:samp mce::UUID -->](refs/protocols/types/mce::UUID.md)

- 类型：mce::UUID。

Recipe Tag：<!-- md:samp string -->

- 类型：string。Available ones: CARTOGRAPHY_TABLE, CRAFTING_TABLE, SMITHING_TABLE, STONECUTTER, FURNACE_TAG, BLAST_FURNACE_TAG, SMOKER_TAG, CAMPFIRE_TAG, SOUL_CAMPFIRE_TAG

Priority：<!-- md:samp varint -->

- 类型：varint。


///
