# <!-- md:samp ShapelessChemistryRecipe -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShapelessChemistryRecipe -->类型。

## 结构

```viz
digraph ShapelessChemistryRecipe {
	graph [rankdir=LR];
	{
		graph [rank=max];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		11	[comment="name: \"unsigned varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		14	[comment="name: \"RecipeIngredient\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=RecipeIngredient];
		17	[comment="name: \"unsigned varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		20	[comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemInstanceDescriptor];
		22	[comment="name: \"mce::UUID\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="mce::UUID"];
		24	[comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		26	[comment="name: \"varint\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	6	[comment="name: \"ShapelessChemistryRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ShapelessChemistryRecipe];
	7	[comment="name: \"Recipe Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Recipe Id"];
	6 -> 7;
	9	[comment="name: \"Ingredients\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Ingredients];
	6 -> 9;
	15	[comment="name: \"Results\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Results];
	6 -> 15;
	21	[comment="name: \"Id\", typeName: \"mce::UUID\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Id];
	6 -> 21;
	23	[comment="name: \"Tag\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"As string\"",
		label=Tag];
	6 -> 23;
	25	[comment="name: \"Priority\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Priority];
	6 -> 25;
	7 -> 8;
	10	[comment="name: \"Array Size\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	9 -> 10;
	12	[comment="name: \"example element\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	9 -> 12;
	10 -> 11;
	13	[comment="name: \"Entry\", typeName: \"RecipeIngredient\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Entry];
	12 -> 13;
	13 -> 14;
	16	[comment="name: \"Array Size\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	15 -> 16;
	18	[comment="name: \"example element\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	15 -> 18;
	16 -> 17;
	19	[comment="name: \"Entry\", typeName: \"NetworkItemInstanceDescriptor\", id: 19, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Entry];
	18 -> 19;
	19 -> 20;
	21 -> 22;
	23 -> 24;
	25 -> 26;
}

```

## 字段

/// define
ShapelessChemistryRecipe

Recipe Id：<!-- md:samp string -->

- 类型：string。

Ingredients

//// define
Ingredients数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Ingredients的示例元素

Entry：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 类型：RecipeIngredient。


////


Results

//// define
Results数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Results的示例元素

Entry：[<!-- md:samp NetworkItemInstanceDescriptor -->](../types/networkiteminstancedescriptor.md)

- 类型：NetworkItemInstanceDescriptor。


////


Id：[<!-- md:samp mce::UUID -->](../types/mce::uuid.md)

- 类型：mce::UUID。

Tag：<!-- md:samp string -->

- 类型：string。As string

Priority：<!-- md:samp varint -->

- 类型：varint。


///
