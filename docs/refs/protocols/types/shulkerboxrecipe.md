# <!-- md:samp ShulkerBoxRecipe -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ShulkerBoxRecipe -->类型。该类型用于protocol.type.shulkerboxrecipe.description

## 结构

```viz
digraph "ShulkerBoxRecipe" {
rankdir = LR
6
6 -> 7
7 -> 8
6 -> 9
9 -> 10
10 -> 11
9 -> 12
12 -> 13
13 -> 14
6 -> 15
15 -> 16
16 -> 17
15 -> 18
18 -> 19
19 -> 20
6 -> 21
21 -> 22
6 -> 23
23 -> 24
6 -> 25
25 -> 26

6 [label="ShulkerBoxRecipe",comment="name: \"ShulkerBoxRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="Recipe Unique Id",comment="name: \"Recipe Unique Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Ingredient List",comment="name: \"Ingredient List\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
10 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
13 [label="Ingredient",comment="name: \"Ingredient\", typeName: \"RecipeIngredient\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Production List",comment="name: \"Production List\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
16 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
19 [label="Produced Item",comment="name: \"Produced Item\", typeName: \"NetworkItemInstanceDescriptor\", id: 19, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
20 [label="NetworkItemInstanceDescriptor",comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Recipe ID",comment="name: \"Recipe ID\", typeName: \"mce::UUID\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
22 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Recipe Tag",comment="name: \"Recipe Tag\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"Available ones: CARTOGRAPHY_TABLE, CRAFTING_TABLE, SMITHING_TABLE, STONECUTTER, FURNACE_TAG, BLAST_FURNACE_TAG, SMOKER_TAG, CAMPFIRE_TAG, SOUL_CAMPFIRE_TAG\""];
24 [label="string",comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Priority",comment="name: \"Priority\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="varint",comment="name: \"varint\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;8;11;14;17;20;22;24;26}

}

```

## 字段

```title='ShulkerBoxRecipe'
[recipe_unique_id][ingredient_list][production_list][recipe_id][recipe_tag][priority]
```

/// html | div.result
//// define
Recipe Unique Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.shulkerboxrecipe.recipe_unique_id.description


////
```title='Ingredient List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.shulkerboxrecipe.ingredient_list.array_size.description


/////
```title='示例元素'
[ingredient]
```

///// html | div.result
////// define
Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 特殊类型。protocol.type.shulkerboxrecipe.ingredient_list.example_element.ingredient.description


//////

/////

////
```title='Production List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.shulkerboxrecipe.production_list.array_size.description


/////
```title='示例元素'
[produced_item]
```

///// html | div.result
////// define
Produced Item：[<!-- md:samp NetworkItemInstanceDescriptor -->](../types/networkiteminstancedescriptor.md)

- 特殊类型。protocol.type.shulkerboxrecipe.production_list.example_element.produced_item.description


//////

/////

////
//// define
Recipe ID：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- 特殊类型。protocol.type.shulkerboxrecipe.recipe_id.description


////
//// define
Recipe Tag：[<!-- md:samp string -->](../types/string.md)

- 特殊类型枚举。protocol.type.shulkerboxrecipe.recipe_tag.description枚举值如下：

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

- 基本类型。protocol.type.shulkerboxrecipe.priority.description


////

///

