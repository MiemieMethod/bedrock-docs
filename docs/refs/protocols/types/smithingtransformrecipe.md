# <!-- md:samp SmithingTransformRecipe -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SmithingTransformRecipe -->类型。

## 结构

```viz
digraph "SmithingTransformRecipe" {
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
6 -> 17
17 -> 18

6 [label="SmithingTransformRecipe",comment="name: \"SmithingTransformRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="Recipe Id",comment="name: \"Recipe Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Template Ingredien",comment="name: \"Template Ingredien\", typeName: \"RecipeIngredient\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Base Ingredien",comment="name: \"Base Ingredien\", typeName: \"RecipeIngredient\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Addition Ingredien",comment="name: \"Addition Ingredien\", typeName: \"RecipeIngredient\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Result",comment="name: \"Result\", typeName: \"NetworkItemInstanceDescriptor\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
16 [label="NetworkItemInstanceDescriptor",comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Tag",comment="name: \"Tag\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="string",comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;8;10;12;14;16;18}

}

```

## 字段

```title='SmithingTransformRecipe'
[recipe_id][template_ingredien][base_ingredien][addition_ingredien][result][tag]
```

/// html | div.result
//// define
Recipe Id：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Template Ingredien：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 类型：<!-- md:samp RecipeIngredient -->。


////
//// define
Base Ingredien：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 类型：<!-- md:samp RecipeIngredient -->。


////
//// define
Addition Ingredien：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 类型：<!-- md:samp RecipeIngredient -->。


////
//// define
Result：[<!-- md:samp NetworkItemInstanceDescriptor -->](../types/networkiteminstancedescriptor.md)

- 类型：<!-- md:samp NetworkItemInstanceDescriptor -->。


////
//// define
Tag：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////

///

