# <!-- md:samp ShapedChemistryRecipe -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShapedChemistryRecipe -->类型。该类型用于protocol.type.shapedchemistryrecipe.description

## 结构

```viz
digraph "ShapedChemistryRecipe" {
rankdir = LR
6
6 -> 7
7 -> 8
6 -> 9
9 -> 10
6 -> 11
11 -> 12
6 -> 13
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

6 [label="ShapedChemistryRecipe",comment="name: \"ShapedChemistryRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="Recipe Id",comment="name: \"Recipe Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Width",comment="name: \"Width\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Height",comment="name: \"Height\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="varint",comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Ingredient",comment="name: \"Ingredient\", typeName: \"RecipeIngredient\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Result Items",comment="name: \"Result Items\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
16 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
19 [label="Entry",comment="name: \"Entry\", typeName: \"NetworkItemInstanceDescriptor\", id: 19, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
20 [label="NetworkItemInstanceDescriptor",comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Id",comment="name: \"Id\", typeName: \"mce::UUID\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
22 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Tag",comment="name: \"Tag\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"As string\""];
24 [label="string",comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Priority",comment="name: \"Priority\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="varint",comment="name: \"varint\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;8;10;12;14;17;20;22;24;26}

}

```

## 字段

```title='ShapedChemistryRecipe'
[recipe_id][width][height][ingredient][result_items][id][tag][priority]
```

/// html | div.result
//// define
Recipe Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.shapedchemistryrecipe.recipe_id.description


////
//// define
Width：<!-- md:samp varint -->

- 基本类型。protocol.type.shapedchemistryrecipe.width.description


////
//// define
Height：<!-- md:samp varint -->

- 基本类型。protocol.type.shapedchemistryrecipe.height.description


////
//// define
Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 特殊类型。protocol.type.shapedchemistryrecipe.ingredient.description


////
```title='Result Items'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.shapedchemistryrecipe.数组大小.description


/////
```title='示例元素'
[entry]
```

///// html | div.result
////// define
Entry：[<!-- md:samp NetworkItemInstanceDescriptor -->](../types/networkiteminstancedescriptor.md)

- 特殊类型。protocol.type.shapedchemistryrecipe.entry.description


//////

/////

////
//// define
Id：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- 特殊类型。protocol.type.shapedchemistryrecipe.id.description


////
//// define
Tag：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.shapedchemistryrecipe.tag.descriptionAs string


////
//// define
Priority：<!-- md:samp varint -->

- 基本类型。protocol.type.shapedchemistryrecipe.priority.description


////

///

