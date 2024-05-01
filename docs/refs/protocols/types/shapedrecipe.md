# <!-- md:samp ShapedRecipe -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ShapedRecipe -->类型。该类型用于protocol.type.shapedrecipe.description

## 结构

```viz
digraph "ShapedRecipe" {
rankdir = LR
6
6 -> 7
7 -> 8
6 -> 9
9 -> 14
14 -> 10
10 -> 11
14 -> 12
12 -> 13
9 -> 15
15 -> 16
16 -> 17
6 -> 18
18 -> 19
19 -> 20
18 -> 21
21 -> 22
22 -> 23
6 -> 24
24 -> 25
6 -> 26
26 -> 27
6 -> 28
28 -> 29
6 -> 30
30 -> 31

6 [label="ShapedRecipe",comment="name: \"ShapedRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="Recipe Unique Id",comment="name: \"Recipe Unique Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Ingredient Grid",comment="name: \"Ingredient Grid\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
14 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="Recipe Width",comment="name: \"Recipe Width\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="varint",comment="name: \"varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="Recipe Height",comment="name: \"Recipe Height\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
13 [label="varint",comment="name: \"varint\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
16 [label="Ingredient",comment="name: \"Ingredient\", typeName: \"RecipeIngredient\", id: 16, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
17 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="Production List",comment="name: \"Production List\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
19 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
22 [label="Produced Item",comment="name: \"Produced Item\", typeName: \"NetworkItemInstanceDescriptor\", id: 22, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
23 [label="NetworkItemInstanceDescriptor",comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
24 [label="Recipe ID",comment="name: \"Recipe ID\", typeName: \"mce::UUID\", id: 24, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
25 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="Recipe Tag",comment="name: \"Recipe Tag\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"Available ones: CARTOGRAPHY_TABLE, CRAFTING_TABLE, SMITHING_TABLE, STONECUTTER, FURNACE_TAG, BLAST_FURNACE_TAG, SMOKER_TAG, CAMPFIRE_TAG, SOUL_CAMPFIRE_TAG\""];
27 [label="string",comment="name: \"string\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="Priority",comment="name: \"Priority\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="varint",comment="name: \"varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="Assume Symmetry",comment="name: \"Assume Symmetry\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
31 [label="bool",comment="name: \"bool\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;8;11;13;17;20;23;25;27;29;31}

}

```

## 字段

```title='ShapedRecipe'
[recipe_unique_id][ingredient_grid][production_list][recipe_id][recipe_tag][priority][assume_symmetry]
```

/// html | div.result
//// define
Recipe Unique Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.shapedrecipe.recipe_unique_id.description


////
```title='Ingredient Grid'
[array_size][[example_element]..]
```

//// html | div.result
```title='数组大小'
[recipe_width][recipe_height]
```

///// html | div.result
////// define
Recipe Width：<!-- md:samp varint -->

- 基本类型。protocol.type.shapedrecipe.recipe_width.description


//////
////// define
Recipe Height：<!-- md:samp varint -->

- 基本类型。protocol.type.shapedrecipe.recipe_height.description


//////

/////
```title='示例元素'
[ingredient]
```

///// html | div.result
////// define
Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 特殊类型。protocol.type.shapedrecipe.ingredient.description


//////

/////

////
```title='Production List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.shapedrecipe.数组大小.description


/////
```title='示例元素'
[produced_item]
```

///// html | div.result
////// define
Produced Item：[<!-- md:samp NetworkItemInstanceDescriptor -->](../types/networkiteminstancedescriptor.md)

- 特殊类型。protocol.type.shapedrecipe.produced_item.description


//////

/////

////
//// define
Recipe ID：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- 特殊类型。protocol.type.shapedrecipe.recipe_id.description


////
//// define
Recipe Tag：[<!-- md:samp string -->](../types/string.md)

- 特殊类型枚举。protocol.type.shapedrecipe.recipe_tag.description枚举值如下：

  |值|描述|
  |---|---|
  |`CARTOGRAPHY_TABLE`|protocol.enum.cartography_table|
  |`CRAFTING_TABLE`|protocol.enum.crafting_table|
  |`SMITHING_TABLE`|protocol.enum.smithing_table|
  |`STONECUTTER`|protocol.enum.stonecutter|
  |`FURNACE_TAG`|protocol.enum.furnace_tag|
  |`BLAST_FURNACE_TAG`|protocol.enum.blast_furnace_tag|
  |`SMOKER_TAG`|protocol.enum.smoker_tag|
  |`CAMPFIRE_TAG`|protocol.enum.campfire_tag|
  |`SOUL_CAMPFIRE_TAG`|protocol.enum.soul_campfire_tag|



////
//// define
Priority：<!-- md:samp varint -->

- 基本类型。protocol.type.shapedrecipe.priority.description


////
//// define
Assume Symmetry：<!-- md:samp bool -->

- 基本类型。protocol.type.shapedrecipe.assume_symmetry.description


////

///

