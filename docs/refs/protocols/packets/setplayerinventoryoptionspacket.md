# <!-- md:samp SetPlayerInventoryOptionsPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp SetPlayerInventoryOptionsPacket -->数据包，数字ID是`307`。该数据包用于protocol.packet.setplayerinventoryoptionspacket.description

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
1 [label="Left Inventory Tab",comment="name: \"Left Inventory Tab\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Right Inventory Tab",comment="name: \"Right Inventory Tab\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Filtering",comment="name: \"Filtering\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Layout Inv",comment="name: \"Layout Inv\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="varint",comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Layout Craft",comment="name: \"Layout Craft\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 基本类型枚举。protocol.packet.setplayerinventoryoptionspacket.left_inventory_tab.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`RecipeConstruction`|`1`|protocol.enum.recipeconstruction|
  |`RecipeEquipment`|`2`|protocol.enum.recipeequipment|
  |`RecipeItems`|`3`|protocol.enum.recipeitems|
  |`RecipeNature`|`4`|protocol.enum.recipenature|
  |`RecipeSearch`|`5`|protocol.enum.recipesearch|
  |`Survival`|`6`|protocol.enum.survival|
  |`Count`|`7`|protocol.enum.count|



////
//// define
Right Inventory Tab：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.setplayerinventoryoptionspacket.right_inventory_tab.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`FullScreen`|`1`|protocol.enum.fullscreen|
  |`Crafting`|`2`|protocol.enum.crafting|
  |`Armor`|`3`|protocol.enum.armor|
  |`Count`|`4`|protocol.enum.count|



////
//// define
Filtering：<!-- md:samp bool -->

- 基本类型。protocol.packet.setplayerinventoryoptionspacket.filtering.description


////
//// define
Layout Inv：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.setplayerinventoryoptionspacket.layout_inv.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Survival`|`1`|protocol.enum.survival|
  |`RecipeBook`|`2`|protocol.enum.recipebook|
  |`Creative`|`3`|protocol.enum.creative|
  |`Count`|`4`|protocol.enum.count|



////
//// define
Layout Craft：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.setplayerinventoryoptionspacket.layout_craft.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Survival`|`1`|protocol.enum.survival|
  |`RecipeBook`|`2`|protocol.enum.recipebook|
  |`Creative`|`3`|protocol.enum.creative|
  |`Count`|`4`|protocol.enum.count|



////

///

