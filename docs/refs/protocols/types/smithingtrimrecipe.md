# <!-- md:samp SmithingTrimRecipe -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SmithingTrimRecipe -->类型。

## 结构

```viz
digraph "SmithingTrimRecipe" {
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

6 [label="SmithingTrimRecipe",comment="name: \"SmithingTrimRecipe\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="Recipe Id",comment="name: \"Recipe Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Template Ingredient",comment="name: \"Template Ingredient\", typeName: \"RecipeIngredient\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Base Ingredient",comment="name: \"Base Ingredient\", typeName: \"RecipeIngredient\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Addition Ingredient",comment="name: \"Addition Ingredient\", typeName: \"RecipeIngredient\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Tag",comment="name: \"Tag\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="string",comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;8;10;12;14;16}

}

```

## 字段

```title='SmithingTrimRecipe'
[recipe_id][template_ingredient][base_ingredient][addition_ingredient][tag]
```

/// html | div.result
//// define
Recipe Id：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////
//// define
Template Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- <!-- md:samp RecipeIngredient -->类型。


////
//// define
Base Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- <!-- md:samp RecipeIngredient -->类型。


////
//// define
Addition Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- <!-- md:samp RecipeIngredient -->类型。


////
//// define
Tag：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////

///

