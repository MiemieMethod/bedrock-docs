# <!-- md:samp BaseDescription -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BaseDescription -->类型。

## 结构

```viz
digraph "BaseDescription" {
rankdir = LR
1
1 -> 2
2 -> 3
3 -> 4
2 -> 5
5 -> 6
1 -> 7
7 -> 8
8 -> 9
7 -> 10
10 -> 11
1 -> 12
12 -> 13
13 -> 14
1 -> 15
15 -> 16
16 -> 17
15 -> 18
18 -> 19

1 [label="BaseDescription",comment="name: \"BaseDescription\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="Internal ItemDescriptor",comment="name: \"Internal ItemDescriptor\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="Full Name",comment="name: \"Full Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Aux Value",comment="name: \"Aux Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Molang Descriptor",comment="name: \"Molang Descriptor\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="Full Name",comment="name: \"Full Name\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="string",comment="name: \"string\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="Molang Version",comment="name: \"Molang Version\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MolangVersion\""];
11 [label="byte",comment="name: \"byte\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="ItemTag Descriptor",comment="name: \"ItemTag Descriptor\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
13 [label="Item Tag",comment="name: \"Item Tag\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Deferred Descriptor",comment="name: \"Deferred Descriptor\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="Full Name",comment="name: \"Full Name\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="string",comment="name: \"string\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="Aux Value",comment="name: \"Aux Value\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
19 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4;6;9;11;14;17;19}

}

```

## 字段

```title='BaseDescription'
[internal_itemdescriptor][molang_descriptor][itemtag_descriptor][deferred_descriptor]
```

/// html | div.result
```title='Internal ItemDescriptor'
[full_name][aux_value]
```

//// html | div.result
///// define
Full Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


/////
///// define
Aux Value：<!-- md:samp unsigned short -->

- 基本类型。


/////

////
```title='Molang Descriptor'
[full_name][molang_version]
```

//// html | div.result
///// define
Full Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


/////
///// define
Molang Version：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`-1`||
  |`BeforeVersioning`|`0`||
  |`Initial`|`1`||
  |`FixedItemRemainingUseDurationQuery`|`2`||
  |`ExpressionErrorMessages`|`3`||
  |`UnexpectedOperatorErrors`|`4`||
  |`ConditionalOperatorAssociativity`|`5`||
  |`ComparisonAndLogicalOperatorPrecedence`|`6`||
  |`DivideByNegativeValue`|`7`||
  |`FixedCapeFlapAmountQuery`|`8`||
  |`QueryBlockPropertyRenamedToState`|`9`||
  |`DeprecateOldBlockQueryNames`|`10`||
  |`DeprecatedSnifferAndCamelQueries`|`11`||
  |`LeafSupportingInFirstSolidBlockBelow`|`12`||
  |`NumValidVersions`|`13`||
  |`Latest`|`NumValidVersions - 1`||
  |`HardcodedMolang`|`Latest`||



/////

////
```title='ItemTag Descriptor'
[item_tag]
```

//// html | div.result
///// define
Item Tag：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


/////

////
```title='Deferred Descriptor'
[full_name][aux_value]
```

//// html | div.result
///// define
Full Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


/////
///// define
Aux Value：<!-- md:samp unsigned short -->

- 基本类型。


/////

////

///
