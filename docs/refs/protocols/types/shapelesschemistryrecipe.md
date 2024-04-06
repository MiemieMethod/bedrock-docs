# <!-- md:samp ShapelessChemistryRecipe -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShapelessChemistryRecipe -->类型。

## 结构

```viz
digraph "ShapelessChemistryRecipe" {
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

6 [label="ShapelessChemistryRecipe",comment="name: \"ShapelessChemistryRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="Recipe Id",comment="name: \"Recipe Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Ingredients",comment="name: \"Ingredients\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
10 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
13 [label="Entry",comment="name: \"Entry\", typeName: \"RecipeIngredient\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Results",comment="name: \"Results\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
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
{ rank = max;8;11;14;17;20;22;24;26}

}

```

## 字段

```title='ShapelessChemistryRecipe'
[recipe_id][ingredients][results][id][tag][priority]
```

/// html | div.result
//// define
Recipe Id：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////
```title='Ingredients'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


/////
```title='示例元素'
[entry]
```

///// html | div.result
////// define
Entry：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- <!-- md:samp RecipeIngredient -->类型。


//////

/////

////
```title='Results'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


/////
```title='示例元素'
[entry]
```

///// html | div.result
////// define
Entry：[<!-- md:samp NetworkItemInstanceDescriptor -->](../types/networkiteminstancedescriptor.md)

- <!-- md:samp NetworkItemInstanceDescriptor -->类型。


//////

/////

////
//// define
Id：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- <!-- md:samp mce::UUID -->类型。


////
//// define
Tag：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。As string


////
//// define
Priority：<!-- md:samp varint -->

- <!-- md:samp varint -->类型。


////

///

