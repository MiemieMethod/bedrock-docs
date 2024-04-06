# <!-- md:samp ItemEnchants -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemEnchants -->类型。

## 结构

```viz
digraph "ItemEnchants" {
rankdir = LR
8
8 -> 9
9 -> 10
8 -> 11
11 -> 12
12 -> 13
11 -> 14
14 -> 15
15 -> 16
14 -> 17
17 -> 18
8 -> 19
19 -> 20
20 -> 21
19 -> 22
22 -> 23
23 -> 24
22 -> 25
25 -> 26
8 -> 27
27 -> 28
28 -> 29
27 -> 30
30 -> 31
31 -> 32
30 -> 33
33 -> 34

8 [label="ItemEnchants",comment="name: \"ItemEnchants\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="int",comment="name: \"int\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Item Enchants For Given Activation",comment="name: \"Item Enchants For Given Activation\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
12 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
13 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
15 [label="Enchant Type",comment="name: \"Enchant Type\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Enchant::Type\""];
16 [label="byte",comment="name: \"byte\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Enchant Level",comment="name: \"Enchant Level\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="byte",comment="name: \"byte\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Item Enchants For Given Activation",comment="name: \"Item Enchants For Given Activation\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
20 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
23 [label="Enchant Type",comment="name: \"Enchant Type\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Enchant::Type\""];
24 [label="byte",comment="name: \"byte\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Enchant Level",comment="name: \"Enchant Level\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="byte",comment="name: \"byte\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="Item Enchants For Given Activation",comment="name: \"Item Enchants For Given Activation\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
28 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
31 [label="Enchant Type",comment="name: \"Enchant Type\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Enchant::Type\""];
32 [label="byte",comment="name: \"byte\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Enchant Level",comment="name: \"Enchant Level\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="byte",comment="name: \"byte\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;10;13;16;18;21;24;26;29;32;34}

}

```

## 字段

```title='ItemEnchants'
[slot][item_enchants_for_given_activation][item_enchants_for_given_activation][item_enchants_for_given_activation]
```

/// html | div.result
//// define
Slot：<!-- md:samp int -->

- 基本类型。


////
```title='Item Enchants For Given Activation'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。


/////
```title='示例元素'
[enchant_type][enchant_level]
```

///// html | div.result
////// define
Enchant Type：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ArmorAll`|`0`||
  |`ArmorFire`|`1`||
  |`ArmorFall`|`2`||
  |`ArmorExplosive`|`3`||
  |`ArmorProjectile`|`4`||
  |`ArmorThorns`|`5`||
  |`WaterBreath`|`6`||
  |`WaterSpeed`|`7`||
  |`WaterAffinity`|`8`||
  |`WeaponDamage`|`9`||
  |`WeaponUndead`|`10`||
  |`WeaponArthropod`|`11`||
  |`WeaponKnockback`|`12`||
  |`WeaponFire`|`13`||
  |`WeaponLoot`|`14`||
  |`MiningEfficiency`|`15`||
  |`MiningSilkTouch`|`16`||
  |`MiningDurability`|`17`||
  |`MiningLoot`|`18`||
  |`BowDamage`|`19`||
  |`BowKnockback`|`20`||
  |`BowFire`|`21`||
  |`BowInfinity`|`22`||
  |`FishingLoot`|`23`||
  |`FishingLure`|`24`||
  |`FrostWalker`|`25`||
  |`Mending`|`26`||
  |`CurseBinding`|`27`||
  |`CurseVanishing`|`28`||
  |`TridentImpaling`|`29`||
  |`TridentRiptide`|`30`||
  |`TridentLoyalty`|`31`||
  |`TridentChanneling`|`32`||
  |`CrossbowMultishot`|`33`||
  |`CrossbowPiercing`|`34`||
  |`CrossbowQuickCharge`|`35`||
  |`SoulSpeed`|`36`||
  |`SwiftSneak`|`37`||
  |`NumEnchantments`|`38`||
  |`InvalidEnchantment`|`39`||



//////
////// define
Enchant Level：<!-- md:samp byte -->

- 基本类型。


//////

/////

////
```title='Item Enchants For Given Activation'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。


/////
```title='示例元素'
[enchant_type][enchant_level]
```

///// html | div.result
////// define
Enchant Type：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ArmorAll`|`0`||
  |`ArmorFire`|`1`||
  |`ArmorFall`|`2`||
  |`ArmorExplosive`|`3`||
  |`ArmorProjectile`|`4`||
  |`ArmorThorns`|`5`||
  |`WaterBreath`|`6`||
  |`WaterSpeed`|`7`||
  |`WaterAffinity`|`8`||
  |`WeaponDamage`|`9`||
  |`WeaponUndead`|`10`||
  |`WeaponArthropod`|`11`||
  |`WeaponKnockback`|`12`||
  |`WeaponFire`|`13`||
  |`WeaponLoot`|`14`||
  |`MiningEfficiency`|`15`||
  |`MiningSilkTouch`|`16`||
  |`MiningDurability`|`17`||
  |`MiningLoot`|`18`||
  |`BowDamage`|`19`||
  |`BowKnockback`|`20`||
  |`BowFire`|`21`||
  |`BowInfinity`|`22`||
  |`FishingLoot`|`23`||
  |`FishingLure`|`24`||
  |`FrostWalker`|`25`||
  |`Mending`|`26`||
  |`CurseBinding`|`27`||
  |`CurseVanishing`|`28`||
  |`TridentImpaling`|`29`||
  |`TridentRiptide`|`30`||
  |`TridentLoyalty`|`31`||
  |`TridentChanneling`|`32`||
  |`CrossbowMultishot`|`33`||
  |`CrossbowPiercing`|`34`||
  |`CrossbowQuickCharge`|`35`||
  |`SoulSpeed`|`36`||
  |`SwiftSneak`|`37`||
  |`NumEnchantments`|`38`||
  |`InvalidEnchantment`|`39`||



//////
////// define
Enchant Level：<!-- md:samp byte -->

- 基本类型。


//////

/////

////
```title='Item Enchants For Given Activation'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。


/////
```title='示例元素'
[enchant_type][enchant_level]
```

///// html | div.result
////// define
Enchant Type：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ArmorAll`|`0`||
  |`ArmorFire`|`1`||
  |`ArmorFall`|`2`||
  |`ArmorExplosive`|`3`||
  |`ArmorProjectile`|`4`||
  |`ArmorThorns`|`5`||
  |`WaterBreath`|`6`||
  |`WaterSpeed`|`7`||
  |`WaterAffinity`|`8`||
  |`WeaponDamage`|`9`||
  |`WeaponUndead`|`10`||
  |`WeaponArthropod`|`11`||
  |`WeaponKnockback`|`12`||
  |`WeaponFire`|`13`||
  |`WeaponLoot`|`14`||
  |`MiningEfficiency`|`15`||
  |`MiningSilkTouch`|`16`||
  |`MiningDurability`|`17`||
  |`MiningLoot`|`18`||
  |`BowDamage`|`19`||
  |`BowKnockback`|`20`||
  |`BowFire`|`21`||
  |`BowInfinity`|`22`||
  |`FishingLoot`|`23`||
  |`FishingLure`|`24`||
  |`FrostWalker`|`25`||
  |`Mending`|`26`||
  |`CurseBinding`|`27`||
  |`CurseVanishing`|`28`||
  |`TridentImpaling`|`29`||
  |`TridentRiptide`|`30`||
  |`TridentLoyalty`|`31`||
  |`TridentChanneling`|`32`||
  |`CrossbowMultishot`|`33`||
  |`CrossbowPiercing`|`34`||
  |`CrossbowQuickCharge`|`35`||
  |`SoulSpeed`|`36`||
  |`SwiftSneak`|`37`||
  |`NumEnchantments`|`38`||
  |`InvalidEnchantment`|`39`||



//////
////// define
Enchant Level：<!-- md:samp byte -->

- 基本类型。


//////

/////

////

///

