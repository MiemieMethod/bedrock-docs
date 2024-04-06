# <!-- md:samp SetHudPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetHudPacket -->数据包，数字ID是`308`。

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
5 [label="Hud Element",comment="name: \"Hud Element\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: HudElement\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="isHudVisible",comment="name: \"isHudVisible\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: HudVisibility\""];
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

- 类型：<!-- md:samp unsigned varint -->。


/////
```title='示例元素'
[hud_element]
```

///// html | div.result
////// define
Hud Element：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`PaperDoll`|`0`||
  |`Armor`|`1`||
  |`ToolTips`|`2`||
  |`TouchControls`|`3`||
  |`Crosshair`|`4`||
  |`HotBar`|`5`||
  |`Health`|`6`||
  |`ProgressBar`|`7`||
  |`Hunger`|`8`||
  |`AirBubbles`|`9`||
  |`HorseHealth`|`10`||
  |`Count`|`11`||



//////

/////

////
//// define
isHudVisible：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Hide`|`0`||
  |`Reset`|`1`||
  |`Count`|`2`||



////

///

