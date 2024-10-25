# <!-- md:samp ItemEnchants -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ItemEnchants -->类型。该类型用于protocol.type.itemenchants.description

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
15 [label="Enchant Type",comment="name: \"Enchant Type\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="byte",comment="name: \"byte\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Enchant Level",comment="name: \"Enchant Level\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="byte",comment="name: \"byte\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Item Enchants For Given Activation",comment="name: \"Item Enchants For Given Activation\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
20 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
23 [label="Enchant Type",comment="name: \"Enchant Type\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="byte",comment="name: \"byte\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Enchant Level",comment="name: \"Enchant Level\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="byte",comment="name: \"byte\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="Item Enchants For Given Activation",comment="name: \"Item Enchants For Given Activation\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
28 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
31 [label="Enchant Type",comment="name: \"Enchant Type\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 基本类型。protocol.type.itemenchants.slot.description


////
```title='Item Enchants For Given Activation'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.itemenchants.item_enchants_for_given_activation.array_size.description


/////
```title='示例元素'
[enchant_type][enchant_level]
```

///// html | div.result
////// define
Enchant Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.itemenchants.item_enchants_for_given_activation.example_element.enchant_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Protection`|`0`|protocol.enum.protection|
  |`FireProtection`|`1`|protocol.enum.fireprotection|
  |`FeatherFalling`|`2`|protocol.enum.featherfalling|
  |`BlastProtection`|`3`|protocol.enum.blastprotection|
  |`ProjectileProtection`|`4`|protocol.enum.projectileprotection|
  |`Thorns`|`5`|protocol.enum.thorns|
  |`Respiration`|`6`|protocol.enum.respiration|
  |`DepthStrider`|`7`|protocol.enum.depthstrider|
  |`AquaAffinity`|`8`|protocol.enum.aquaaffinity|
  |`Sharpness`|`9`|protocol.enum.sharpness|
  |`Smite`|`10`|protocol.enum.smite|
  |`BaneOfArthropods`|`11`|protocol.enum.baneofarthropods|
  |`Knockback`|`12`|protocol.enum.knockback|
  |`FireAspect`|`13`|protocol.enum.fireaspect|
  |`Looting`|`14`|protocol.enum.looting|
  |`Efficiency`|`15`|protocol.enum.efficiency|
  |`SilkTouch`|`16`|protocol.enum.silktouch|
  |`Unbreaking`|`17`|protocol.enum.unbreaking|
  |`Fortune`|`18`|protocol.enum.fortune|
  |`Power`|`19`|protocol.enum.power|
  |`Punch`|`20`|protocol.enum.punch|
  |`Flame`|`21`|protocol.enum.flame|
  |`Infinity`|`22`|protocol.enum.infinity|
  |`LuckOfTheSea`|`23`|protocol.enum.luckofthesea|
  |`Lure`|`24`|protocol.enum.lure|
  |`FrostWalker`|`25`|protocol.enum.frostwalker|
  |`Mending`|`26`|protocol.enum.mending|
  |`CurseOfBinding`|`27`|protocol.enum.curseofbinding|
  |`CurseOfVanishing`|`28`|protocol.enum.curseofvanishing|
  |`Impaling`|`29`|protocol.enum.impaling|
  |`Riptide`|`30`|protocol.enum.riptide|
  |`Loyalty`|`31`|protocol.enum.loyalty|
  |`Channeling`|`32`|protocol.enum.channeling|
  |`Multishot`|`33`|protocol.enum.multishot|
  |`Piercing`|`34`|protocol.enum.piercing|
  |`QuickCharge`|`35`|protocol.enum.quickcharge|
  |`SoulSpeed`|`36`|protocol.enum.soulspeed|
  |`SwiftSneak`|`37`|protocol.enum.swiftsneak|
  |`WindBurst`|`38`|protocol.enum.windburst|
  |`Density`|`39`|protocol.enum.density|
  |`Breach`|`40`|protocol.enum.breach|
  |`NumEnchantments`|`41`|protocol.enum.numenchantments|
  |`InvalidEnchantment`|`42`|protocol.enum.invalidenchantment|



//////
////// define
Enchant Level：<!-- md:samp byte -->

- 基本类型。protocol.type.itemenchants.item_enchants_for_given_activation.example_element.enchant_level.description


//////

/////

////
```title='Item Enchants For Given Activation'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.itemenchants.item_enchants_for_given_activation.array_size.description


/////
```title='示例元素'
[enchant_type][enchant_level]
```

///// html | div.result
////// define
Enchant Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.itemenchants.item_enchants_for_given_activation.example_element.enchant_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Protection`|`0`|protocol.enum.protection|
  |`FireProtection`|`1`|protocol.enum.fireprotection|
  |`FeatherFalling`|`2`|protocol.enum.featherfalling|
  |`BlastProtection`|`3`|protocol.enum.blastprotection|
  |`ProjectileProtection`|`4`|protocol.enum.projectileprotection|
  |`Thorns`|`5`|protocol.enum.thorns|
  |`Respiration`|`6`|protocol.enum.respiration|
  |`DepthStrider`|`7`|protocol.enum.depthstrider|
  |`AquaAffinity`|`8`|protocol.enum.aquaaffinity|
  |`Sharpness`|`9`|protocol.enum.sharpness|
  |`Smite`|`10`|protocol.enum.smite|
  |`BaneOfArthropods`|`11`|protocol.enum.baneofarthropods|
  |`Knockback`|`12`|protocol.enum.knockback|
  |`FireAspect`|`13`|protocol.enum.fireaspect|
  |`Looting`|`14`|protocol.enum.looting|
  |`Efficiency`|`15`|protocol.enum.efficiency|
  |`SilkTouch`|`16`|protocol.enum.silktouch|
  |`Unbreaking`|`17`|protocol.enum.unbreaking|
  |`Fortune`|`18`|protocol.enum.fortune|
  |`Power`|`19`|protocol.enum.power|
  |`Punch`|`20`|protocol.enum.punch|
  |`Flame`|`21`|protocol.enum.flame|
  |`Infinity`|`22`|protocol.enum.infinity|
  |`LuckOfTheSea`|`23`|protocol.enum.luckofthesea|
  |`Lure`|`24`|protocol.enum.lure|
  |`FrostWalker`|`25`|protocol.enum.frostwalker|
  |`Mending`|`26`|protocol.enum.mending|
  |`CurseOfBinding`|`27`|protocol.enum.curseofbinding|
  |`CurseOfVanishing`|`28`|protocol.enum.curseofvanishing|
  |`Impaling`|`29`|protocol.enum.impaling|
  |`Riptide`|`30`|protocol.enum.riptide|
  |`Loyalty`|`31`|protocol.enum.loyalty|
  |`Channeling`|`32`|protocol.enum.channeling|
  |`Multishot`|`33`|protocol.enum.multishot|
  |`Piercing`|`34`|protocol.enum.piercing|
  |`QuickCharge`|`35`|protocol.enum.quickcharge|
  |`SoulSpeed`|`36`|protocol.enum.soulspeed|
  |`SwiftSneak`|`37`|protocol.enum.swiftsneak|
  |`WindBurst`|`38`|protocol.enum.windburst|
  |`Density`|`39`|protocol.enum.density|
  |`Breach`|`40`|protocol.enum.breach|
  |`NumEnchantments`|`41`|protocol.enum.numenchantments|
  |`InvalidEnchantment`|`42`|protocol.enum.invalidenchantment|



//////
////// define
Enchant Level：<!-- md:samp byte -->

- 基本类型。protocol.type.itemenchants.item_enchants_for_given_activation.example_element.enchant_level.description


//////

/////

////
```title='Item Enchants For Given Activation'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.itemenchants.item_enchants_for_given_activation.array_size.description


/////
```title='示例元素'
[enchant_type][enchant_level]
```

///// html | div.result
////// define
Enchant Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.itemenchants.item_enchants_for_given_activation.example_element.enchant_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Protection`|`0`|protocol.enum.protection|
  |`FireProtection`|`1`|protocol.enum.fireprotection|
  |`FeatherFalling`|`2`|protocol.enum.featherfalling|
  |`BlastProtection`|`3`|protocol.enum.blastprotection|
  |`ProjectileProtection`|`4`|protocol.enum.projectileprotection|
  |`Thorns`|`5`|protocol.enum.thorns|
  |`Respiration`|`6`|protocol.enum.respiration|
  |`DepthStrider`|`7`|protocol.enum.depthstrider|
  |`AquaAffinity`|`8`|protocol.enum.aquaaffinity|
  |`Sharpness`|`9`|protocol.enum.sharpness|
  |`Smite`|`10`|protocol.enum.smite|
  |`BaneOfArthropods`|`11`|protocol.enum.baneofarthropods|
  |`Knockback`|`12`|protocol.enum.knockback|
  |`FireAspect`|`13`|protocol.enum.fireaspect|
  |`Looting`|`14`|protocol.enum.looting|
  |`Efficiency`|`15`|protocol.enum.efficiency|
  |`SilkTouch`|`16`|protocol.enum.silktouch|
  |`Unbreaking`|`17`|protocol.enum.unbreaking|
  |`Fortune`|`18`|protocol.enum.fortune|
  |`Power`|`19`|protocol.enum.power|
  |`Punch`|`20`|protocol.enum.punch|
  |`Flame`|`21`|protocol.enum.flame|
  |`Infinity`|`22`|protocol.enum.infinity|
  |`LuckOfTheSea`|`23`|protocol.enum.luckofthesea|
  |`Lure`|`24`|protocol.enum.lure|
  |`FrostWalker`|`25`|protocol.enum.frostwalker|
  |`Mending`|`26`|protocol.enum.mending|
  |`CurseOfBinding`|`27`|protocol.enum.curseofbinding|
  |`CurseOfVanishing`|`28`|protocol.enum.curseofvanishing|
  |`Impaling`|`29`|protocol.enum.impaling|
  |`Riptide`|`30`|protocol.enum.riptide|
  |`Loyalty`|`31`|protocol.enum.loyalty|
  |`Channeling`|`32`|protocol.enum.channeling|
  |`Multishot`|`33`|protocol.enum.multishot|
  |`Piercing`|`34`|protocol.enum.piercing|
  |`QuickCharge`|`35`|protocol.enum.quickcharge|
  |`SoulSpeed`|`36`|protocol.enum.soulspeed|
  |`SwiftSneak`|`37`|protocol.enum.swiftsneak|
  |`WindBurst`|`38`|protocol.enum.windburst|
  |`Density`|`39`|protocol.enum.density|
  |`Breach`|`40`|protocol.enum.breach|
  |`NumEnchantments`|`41`|protocol.enum.numenchantments|
  |`InvalidEnchantment`|`42`|protocol.enum.invalidenchantment|



//////
////// define
Enchant Level：<!-- md:samp byte -->

- 基本类型。protocol.type.itemenchants.item_enchants_for_given_activation.example_element.enchant_level.description


//////

/////

////

///

