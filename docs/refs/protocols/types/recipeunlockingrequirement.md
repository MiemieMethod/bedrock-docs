# <!-- md:samp RecipeUnlockingRequirement -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp RecipeUnlockingRequirement -->类型。该类型用于protocol.type.recipeunlockingrequirement.description

## 结构

```viz
digraph "RecipeUnlockingRequirement" {
rankdir = LR
54
54 -> 55
55 -> 56
54 -> 57
57 -> 58
58 -> 59
57 -> 60
60 -> 61
61 -> 62
62 -> 63
61 -> 64
64 -> 65
65 -> 66

54 [label="RecipeUnlockingRequirement",comment="name: \"RecipeUnlockingRequirement\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
55 [label="Unlocking Context",comment="name: \"Unlocking Context\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
56 [label="byte",comment="name: \"byte\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
57 [label="Dependency on 'Unlocking context is None?'",shape=note,comment="name: \"Dependency on 'Unlocking context is None?'\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
58 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
59 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
60 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 60, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
61 [label="Unlocking Ingredients",comment="name: \"Unlocking Ingredients\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
62 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
63 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
64 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
65 [label="Ingredient",comment="name: \"Ingredient\", typeName: \"RecipeIngredient\", id: 65, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
66 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;56;59;63;66}

}

```

## 字段

```title='RecipeUnlockingRequirement'
[unlocking_context][dependency_on_unlocking_context_is_none]
```

/// html | div.result
//// define
Unlocking Context：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.recipeunlockingrequirement.unlocking_context.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`AlwaysUnlocked`|`1`|protocol.enum.alwaysunlocked|
  |`PlayerInWater`|`2`|protocol.enum.playerinwater|
  |`PlayerHasManyItems`|`3`|protocol.enum.playerhasmanyitems|



////
> 依赖于`Unlocking context is None?`

///// tab | `Unlocking context is None?`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Unlocking context is None?`如果为`1`
```title='if (1)'
[unlocking_ingredients]
```

////// html | div.result
```title='Unlocking Ingredients'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.recipeunlockingrequirement.dependency_on_unlocking_context_is_none.if_1.unlocking_ingredients.array_size.description


////////
```title='示例元素'
[ingredient]
```

//////// html | div.result
///////// define
Ingredient：[<!-- md:samp RecipeIngredient -->](../types/recipeingredient.md)

- 特殊类型。protocol.type.recipeunlockingrequirement.dependency_on_unlocking_context_is_none.if_1.unlocking_ingredients.example_element.ingredient.description


/////////

////////

///////

//////

/////

///

