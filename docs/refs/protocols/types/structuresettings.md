# <!-- md:samp StructureSettings -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureSettings -->类型。

## 结构

```viz
digraph "StructureSettings" {
rankdir = LR
16
16 -> 17
17 -> 18
16 -> 19
19 -> 20
16 -> 21
21 -> 22
16 -> 23
23 -> 24
16 -> 25
25 -> 26
16 -> 27
27 -> 28
16 -> 29
29 -> 30
16 -> 31
31 -> 32
16 -> 33
33 -> 34
16 -> 35
35 -> 36
16 -> 37
37 -> 38
16 -> 39
39 -> 40
16 -> 41
41 -> 42
16 -> 43
43 -> 44

16 [label="StructureSettings",comment="name: \"StructureSettings\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="Structure Palette Name",comment="name: \"Structure Palette Name\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="string",comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Should ignore entities?",comment="name: \"Should ignore entities?\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="bool",comment="name: \"bool\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Should ignore blocks?",comment="name: \"Should ignore blocks?\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="bool",comment="name: \"bool\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Should Allow Non Ticking Player and Ticking Area Chunks",comment="name: \"Should Allow Non Ticking Player and Ticking Area Chunks\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="bool",comment="name: \"bool\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Structure Size",comment="name: \"Structure Size\", typeName: \"NetworkBlockPosition\", id: 25, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
26 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="Structure Offset",comment="name: \"Structure Offset\", typeName: \"NetworkBlockPosition\", id: 27, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
28 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
29 [label="Last Edit Player",comment="name: \"Last Edit Player\", typeName: \"ActorUniqueID\", id: 29, branchId: 0, recurseId: -1, attributes: 256, notes: \"Player who last edited the structure block.\""];
30 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="Rotation",comment="name: \"Rotation\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Rotation\""];
32 [label="byte",comment="name: \"byte\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Mirror",comment="name: \"Mirror\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Mirror\""];
34 [label="byte",comment="name: \"byte\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Animation Mode",comment="name: \"Animation Mode\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: AnimationMode\""];
36 [label="byte",comment="name: \"byte\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="Animation Seconds",comment="name: \"Animation Seconds\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
38 [label="float",comment="name: \"float\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
39 [label="Integrity Value",comment="name: \"Integrity Value\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
40 [label="float",comment="name: \"float\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="Integrity Seed",comment="name: \"Integrity Seed\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
42 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
43 [label="Rotation Pivot",comment="name: \"Rotation Pivot\", typeName: \"Vec3\", id: 43, branchId: 0, recurseId: -1, attributes: 256, notes: \"Pivot used to rotate a structure around.\""];
44 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;18;20;22;24;26;28;30;32;34;36;38;40;42;44}

}

```

## 字段

```title='StructureSettings'
[structure_palette_name][should_ignore_entities?][should_ignore_blocks?][should_allow_non_ticking_player_and_ticking_area_chunks][structure_size][structure_offset][last_edit_player][rotation][mirror][animation_mode][animation_seconds][integrity_value][integrity_seed][rotation_pivot]
```

/// html | div.result
//// define
Structure Palette Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////
//// define
Should ignore entities?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Should ignore blocks?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Should Allow Non Ticking Player and Ticking Area Chunks：<!-- md:samp bool -->

- 基本类型。


////
//// define
Structure Size：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。


////
//// define
Structure Offset：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。


////
//// define
Last Edit Player：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。Player who last edited the structure block.


////
//// define
Rotation：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`Rotate90`|`1`||
  |`Rotate180`|`2`||
  |`Rotate270`|`3`||
  |`Total`|`4`||



////
//// define
Mirror：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`X`|`1`||
  |`Z`|`2`||
  |`XZ`|`3`||



////
//// define
Animation Mode：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`Layers`|`1`||
  |`Blocks`|`2`||



////
//// define
Animation Seconds：<!-- md:samp float -->

- 基本类型。


////
//// define
Integrity Value：<!-- md:samp float -->

- 基本类型。


////
//// define
Integrity Seed：<!-- md:samp unsigned int -->

- 基本类型。


////
//// define
Rotation Pivot：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。Pivot used to rotate a structure around.


////

///

