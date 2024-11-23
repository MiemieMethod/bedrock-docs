# <!-- md:samp SmithingTrimRecipe -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp SmithingTrimRecipe -->类型。该类型用于protocol.type.smithingtrimrecipe.description

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

- 特殊类型。protocol.type.smithingtrimrecipe.recipe_id.description


////
//// define
Template Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 特殊类型。protocol.type.smithingtrimrecipe.template_ingredient.description


////
//// define
Base Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 特殊类型。protocol.type.smithingtrimrecipe.base_ingredient.description


////
//// define
Addition Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 特殊类型。protocol.type.smithingtrimrecipe.addition_ingredient.description


////
//// define
Tag：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.smithingtrimrecipe.tag.description


////

///

