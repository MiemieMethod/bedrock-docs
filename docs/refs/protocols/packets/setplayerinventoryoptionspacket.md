# <!-- md:samp SetPlayerInventoryOptionsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetPlayerInventoryOptionsPacket -->数据包，数字ID是`307`。

## 结构

```viz
digraph "SetPlayerInventoryOptionsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10

0 [label="SetPlayerInventoryOptionsPacket",comment="name: \"SetPlayerInventoryOptionsPacket\", typeName: \"\", id: 0, branchId: 307, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Left Inventory Tab",comment="name: \"Left Inventory Tab\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventoryLeftTabIndex\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Right Inventory Tab",comment="name: \"Right Inventory Tab\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventoryRightTabIndex\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Filtering",comment="name: \"Filtering\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Layout Inv",comment="name: \"Layout Inv\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventoryLayout\""];
8 [label="varint",comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Layout Craft",comment="name: \"Layout Craft\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventoryLayout\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='SetPlayerInventoryOptionsPacket'
[left_inventory_tab][right_inventory_tab][filtering][layout_inv][layout_craft]
```

/// html | div.result
//// define
Left Inventory Tab：<!-- md:samp varint -->

- <!-- md:samp varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`RecipeConstruction`|`1`||
  |`RecipeEquipment`|`2`||
  |`RecipeItems`|`3`||
  |`RecipeNature`|`4`||
  |`RecipeSearch`|`5`||
  |`Survival`|`6`||
  |`Count`|`7`||



////
//// define
Right Inventory Tab：<!-- md:samp varint -->

- <!-- md:samp varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`FullScreen`|`1`||
  |`Crafting`|`2`||
  |`Armor`|`3`||
  |`Count`|`4`||



////
//// define
Filtering：<!-- md:samp bool -->

- <!-- md:samp bool -->类型。


////
//// define
Layout Inv：<!-- md:samp varint -->

- <!-- md:samp varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`Survival`|`1`||
  |`RecipeBook`|`2`||
  |`Creative`|`3`||
  |`Count`|`4`||



////
//// define
Layout Craft：<!-- md:samp varint -->

- <!-- md:samp varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`Survival`|`1`||
  |`RecipeBook`|`2`||
  |`Creative`|`3`||
  |`Count`|`4`||



////

///

