# <!-- md:samp SetHudPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp SetHudPacket -->数据包，数字ID是`308`。该数据包用于protocol.packet.sethudpacket.description

## 结构

```viz
digraph "SetHudPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6
0 -> 7
7 -> 8

0 [label="SetHudPacket",comment="name: \"SetHudPacket\", typeName: \"\", id: 0, branchId: 308, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Hud Element List",comment="name: \"Hud Element List\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Hud Element",comment="name: \"Hud Element\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="isHudVisible",comment="name: \"isHudVisible\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="varint",comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6;8}

}

```

## 字段

```title='SetHudPacket'
[hud_element_list][ishudvisible]
```

/// html | div.result
```title='Hud Element List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.sethudpacket.hud_element_list.array_size.description


/////
```title='示例元素'
[hud_element]
```

///// html | div.result
////// define
Hud Element：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.sethudpacket.hud_element_list.example_element.hud_element.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`PaperDoll`|`0`|protocol.enum.paperdoll|
  |`Armor`|`1`|protocol.enum.armor|
  |`ToolTips`|`2`|protocol.enum.tooltips|
  |`TouchControls`|`3`|protocol.enum.touchcontrols|
  |`Crosshair`|`4`|protocol.enum.crosshair|
  |`HotBar`|`5`|protocol.enum.hotbar|
  |`Health`|`6`|protocol.enum.health|
  |`ProgressBar`|`7`|protocol.enum.progressbar|
  |`Hunger`|`8`|protocol.enum.hunger|
  |`AirBubbles`|`9`|protocol.enum.airbubbles|
  |`HorseHealth`|`10`|protocol.enum.horsehealth|
  |`StatusEffects`|`11`|protocol.enum.statuseffects|
  |`ItemText`|`12`|protocol.enum.itemtext|
  |`Count`|`13`|protocol.enum.count|



//////

/////

////
//// define
isHudVisible：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.sethudpacket.ishudvisible.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Hide`|`0`|protocol.enum.hide|
  |`Reset`|`1`|protocol.enum.reset|
  |`Count`|`2`|protocol.enum.count|



////

///

