# <!-- md:samp StructureSettings -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp StructureSettings -->类型。该类型用于protocol.type.structuresettings.description

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
31 [label="Rotation",comment="name: \"Rotation\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="byte",comment="name: \"byte\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Mirror",comment="name: \"Mirror\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="byte",comment="name: \"byte\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Animation Mode",comment="name: \"Animation Mode\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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
[structure_palette_name][should_ignore_entities][should_ignore_blocks][should_allow_non_ticking_player_and_ticking_area_chunks][structure_size][structure_offset][last_edit_player][rotation][mirror][animation_mode][animation_seconds][integrity_value][integrity_seed][rotation_pivot]
```

/// html | div.result
//// define
Structure Palette Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.structuresettings.structure_palette_name.description


////
//// define
Should ignore entities?：<!-- md:samp bool -->

- 基本类型。protocol.type.structuresettings.should_ignore_entities.description


////
//// define
Should ignore blocks?：<!-- md:samp bool -->

- 基本类型。protocol.type.structuresettings.should_ignore_blocks.description


////
//// define
Should Allow Non Ticking Player and Ticking Area Chunks：<!-- md:samp bool -->

- 基本类型。protocol.type.structuresettings.should_allow_non_ticking_player_and_ticking_area_chunks.description


////
//// define
Structure Size：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.type.structuresettings.structure_size.description


////
//// define
Structure Offset：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.type.structuresettings.structure_offset.description


////
//// define
Last Edit Player：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.type.structuresettings.last_edit_player.descriptionPlayer who last edited the structure block.


////
//// define
Rotation：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.structuresettings.rotation.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Rotate90`|`1`|protocol.enum.rotate90|
  |`Rotate180`|`2`|protocol.enum.rotate180|
  |`Rotate270`|`3`|protocol.enum.rotate270|
  |`Total`|`4`|protocol.enum.total|



////
//// define
Mirror：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.structuresettings.mirror.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`X`|`1`|protocol.enum.x|
  |`Z`|`2`|protocol.enum.z|
  |`XZ`|`3`|protocol.enum.xz|



////
//// define
Animation Mode：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.structuresettings.animation_mode.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Layers`|`1`|protocol.enum.layers|
  |`Blocks`|`2`|protocol.enum.blocks|



////
//// define
Animation Seconds：<!-- md:samp float -->

- 基本类型。protocol.type.structuresettings.animation_seconds.description


////
//// define
Integrity Value：<!-- md:samp float -->

- 基本类型。protocol.type.structuresettings.integrity_value.description


////
//// define
Integrity Seed：<!-- md:samp unsigned int -->

- 基本类型。protocol.type.structuresettings.integrity_seed.description


////
//// define
Rotation Pivot：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.type.structuresettings.rotation_pivot.descriptionPivot used to rotate a structure around.


////

///

