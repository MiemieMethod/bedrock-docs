# <!-- md:samp MapDecoration -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp MapDecoration -->类型。该类型用于protocol.type.mapdecoration.description

## 结构

```viz
digraph "MapDecoration" {
rankdir = LR
60
60 -> 61
61 -> 62
60 -> 63
63 -> 64
60 -> 65
65 -> 66
60 -> 67
67 -> 68
60 -> 69
69 -> 70
60 -> 71
71 -> 72

60 [label="MapDecoration",comment="name: \"MapDecoration\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
61 [label="Map Decoration Type",comment="name: \"Map Decoration Type\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
62 [label="byte",comment="name: \"byte\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
63 [label="Rotation",comment="name: \"Rotation\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
64 [label="byte",comment="name: \"byte\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
65 [label="X",comment="name: \"X\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
66 [label="byte",comment="name: \"byte\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
67 [label="Y",comment="name: \"Y\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
68 [label="byte",comment="name: \"byte\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
69 [label="Label",comment="name: \"Label\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
70 [label="string",comment="name: \"string\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
71 [label="Color - ARGB",comment="name: \"Color - ARGB\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
72 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;62;64;66;68;70;72}

}

```

## 字段

```title='MapDecoration'
[map_decoration_type][rotation][x][y][label][color_argb]
```

/// html | div.result
//// define
Map Decoration Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.mapdecoration.map_decoration_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`MarkerWhite`|`0`|protocol.enum.markerwhite|
  |`MarkerGreen`|`1`|protocol.enum.markergreen|
  |`MarkerRed`|`2`|protocol.enum.markerred|
  |`MarkerBlue`|`3`|protocol.enum.markerblue|
  |`XWhite`|`4`|protocol.enum.xwhite|
  |`TriangleRed`|`5`|protocol.enum.trianglered|
  |`SquareWhite`|`6`|protocol.enum.squarewhite|
  |`MarkerSign`|`7`|protocol.enum.markersign|
  |`MarkerPink`|`8`|protocol.enum.markerpink|
  |`MarkerOrange`|`9`|protocol.enum.markerorange|
  |`MarkerYellow`|`10`|protocol.enum.markeryellow|
  |`MarkerTeal`|`11`|protocol.enum.markerteal|
  |`TriangleGreen`|`12`|protocol.enum.trianglegreen|
  |`SmallSquareWhite`|`13`|protocol.enum.smallsquarewhite|
  |`Mansion`|`14`|protocol.enum.mansion|
  |`Monument`|`15`|protocol.enum.monument|
  |`NoDraw`|`16`|protocol.enum.nodraw|
  |`VillageDesert`|`17`|protocol.enum.villagedesert|
  |`VillagePlains`|`18`|protocol.enum.villageplains|
  |`VillageSavanna`|`19`|protocol.enum.villagesavanna|
  |`VillageSnowy`|`20`|protocol.enum.villagesnowy|
  |`VillageTaiga`|`21`|protocol.enum.villagetaiga|
  |`JungleTemple`|`22`|protocol.enum.jungletemple|
  |`WitchHut`|`23`|protocol.enum.witchhut|
  |`TrialChambers`|`24`|protocol.enum.trialchambers|
  |`Count`|`25`|protocol.enum.count|
  |`Player`|`MarkerWhite`|protocol.enum.player|
  |`PlayerOffMap`|`SquareWhite`|protocol.enum.playeroffmap|
  |`PlayerOffLimits`|`SmallSquareWhite`|protocol.enum.playerofflimits|
  |`PlayerHidden`|`NoDraw`|protocol.enum.playerhidden|
  |`ItemFrame`|`MarkerGreen`|protocol.enum.itemframe|



////
//// define
Rotation：<!-- md:samp byte -->

- 基本类型。protocol.type.mapdecoration.rotation.description


////
//// define
X：<!-- md:samp byte -->

- 基本类型。protocol.type.mapdecoration.x.description


////
//// define
Y：<!-- md:samp byte -->

- 基本类型。protocol.type.mapdecoration.y.description


////
//// define
Label：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.mapdecoration.label.description


////
//// define
Color - ARGB：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.mapdecoration.color_argb.description


////

///

