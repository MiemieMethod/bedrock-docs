# <!-- md:samp RecipeIngredient -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp RecipeIngredient -->类型。该类型用于protocol.type.recipeingredient.description

## 结构

```viz
digraph "RecipeIngredient" {
rankdir = LR
14
14 -> 15
15 -> 16
14 -> 17
17 -> 18

14 [label="RecipeIngredient",comment="name: \"RecipeIngredient\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="InternalType",comment="name: \"InternalType\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="byte",comment="name: \"byte\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="StackSize",comment="name: \"StackSize\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="varint",comment="name: \"varint\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;16;18}

}

```

## 字段

```title='RecipeIngredient'
[internaltype][stacksize]
```

/// html | div.result
//// define
InternalType：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.recipeingredient.internaltype.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`0`|protocol.enum.invalid|
  |`Default`|`1`|protocol.enum.default|
  |`Molang`|`2`|protocol.enum.molang|
  |`ItemTag`|`3`|protocol.enum.itemtag|
  |`Deferred`|`4`|protocol.enum.deferred|
  |`ComplexAlias`|`5`|protocol.enum.complexalias|



////
//// define
StackSize：<!-- md:samp varint -->

- 基本类型。protocol.type.recipeingredient.stacksize.description


////

///

